/* -*- c++ -*- */
/* 
 * Copyright 2019 andre.
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
#include "dsc_impl.h"

namespace gr {
  namespace testing_single_scramble {

    dsc::sptr
    dsc::make(int mask, int seed, int len)
    {
      return gnuradio::get_initial_sptr
        (new dsc_impl(mask, seed, len));
    }

    /*
     * The private constructor
     */
    dsc_impl::dsc_impl(int mask, int seed, int len)
      : gr::block("dsc",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
            d_lfsr(mask,seed,len),
        trash(8)
    {}

    /*
     * Our virtual destructor.
     */
    dsc_impl::~dsc_impl()
    {
    }

    void
    dsc_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
        unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }
    
    int
    dsc_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      int ii=0;
      int oo=0;

      if(trash!=0){
        d_lfsr.next_bit_descramble(in[0]);
        ii=ii+1;
        trash=trash-1;

      }else{
        out[0]=d_lfsr.next_bit_descramble(in[0]);
        ii++;
        oo++;        
      }


      consume_each (ii);

      // Tell runtime system how many output items we produced.
      return oo;
    }

  } /* namespace testing_single_scramble */
} /* namespace gr */

