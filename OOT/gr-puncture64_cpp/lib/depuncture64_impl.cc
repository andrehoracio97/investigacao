/* -*- c++ -*- */
/* 
 * Copyright 2020 andre silva.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "depuncture64_impl.h"

#include <pmt/pmt.h>
#include <stdio.h>
#include <volk/volk.h>
#include <boost/bind.hpp>
#include <string>

namespace gr {
  namespace puncture64_cpp {

    depuncture64::sptr
    depuncture64::make(int puncsize, uint64_t puncpat, char sym)
    {
      return gnuradio::get_initial_sptr
        (new depuncture64_impl(puncsize, puncpat, sym));
    }

    /*
     * The private constructor
     */
    depuncture64_impl::depuncture64_impl(int puncsize, uint64_t puncpat, char sym)
      : gr::block("depuncture64",
            io_signature::make(1, 1, sizeof(unsigned char)),
            io_signature::make(1, 1, sizeof(unsigned char))),
      d_puncsize(puncsize),
      d_sym(sym)
    {
      // Create a mask of all 1's of puncsize length
      uint64_t mask = 0x0;
      uint64_t bit= 0x1;
      for (int i = 0; i < d_puncsize; i++){
        bit=bit<<1;
        mask=mask|bit;
        //printf("mask: %d:  ----> %llu \n",i, mask);
      }

      // Rotate the pattern for the delay value; then mask it if there
      // are any excess 1's in the pattern.
      /*for (int i = 0; i < d_delay; ++i) {
          puncpat = ((puncpat & 1) << (d_puncsize - 1)) + (puncpat >> 1);
      }*/
      d_puncpat = puncpat & mask;

      // Calculate the number of holes in the pattern. The mask is all
      // 1's given puncsize and puncpat is a pattern with >= puncsize
      // 0's (masked to ensure this). The difference between the
      // number of 1's in the mask and the puncpat is the number of
      // holes.
      uint64_t count_mask = 0, count_pat = 0;
      volk_64u_popcnt(&count_mask, static_cast<uint64_t>(mask));
      volk_64u_popcnt(&count_pat, static_cast<uint64_t>(d_puncpat));
      d_puncholes = count_mask - count_pat;

      set_fixed_rate(true);
      set_relative_rate((double)d_puncsize / (d_puncsize - d_puncholes));
      set_output_multiple(d_puncsize);
      // set_msg_handler(boost::bind(&depuncture_bb_impl::catch_msg, this, _1));

    }

    /*
     * Our virtual destructor.
     */
    depuncture64_impl::~depuncture64_impl()
    {
    }

    void
    depuncture64_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = (int)((((d_puncsize - d_puncholes) / (double)(d_puncsize)) * noutput_items) + .5);
    }

    int depuncture64_impl::fixed_rate_ninput_to_noutput(int ninput)
    {
        return (int)(((d_puncsize / (double)(d_puncsize - d_puncholes)) * ninput) + .5);
    }

    int depuncture64_impl::fixed_rate_noutput_to_ninput(int noutput)
    {
        return (int)((((d_puncsize - d_puncholes) / (double)(d_puncsize)) * noutput) + .5);
    }

    int
    depuncture64_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const uint8_t* in = (const uint8_t*)input_items[0];
      uint8_t* out = (uint8_t*)output_items[0];

      for (int i = 0, k = 0; i < noutput_items / output_multiple(); ++i) {
          for (int j = 0; j < output_multiple(); ++j) {
              out[i * output_multiple() + j] =
                  ((d_puncpat >> (d_puncsize - 1 - j)) & 1) ? in[k++] : d_sym;
          }
      }

      /*
      GR_LOG_DEBUG(d_debug_logger, ">>>>>> start");
      for(int i = 0, k=0; i < noutput_items; ++i) {
        if((d_puncpat >> (d_puncsize - 1 - (i % d_puncsize))) & 1) {
          GR_LOG_DEBUG(d_debug_logger, boost::format("%1%...%2%") \
                       % out[i] % in[k++]);
        }
        else {
          GR_LOG_DEBUG(d_debug_logger, boost::format("snit %1%") % out[i]);
        }
      }

      GR_LOG_DEBUG(d_debug_logger, boost::format("comp: %1%, %2%\n") \
                   % noutput_items % ninput_items[0]);
      GR_LOG_DEBUG(d_debug_logger, boost::format("consuming %1%") \
                   % ((int)(((1.0/relative_rate()) * noutput_items) + .5)));
      */

      consume_each((int)(((1.0 / relative_rate()) * noutput_items) + .5));
      return noutput_items;
    }

  } /* namespace puncture64_cpp */
} /* namespace gr */

