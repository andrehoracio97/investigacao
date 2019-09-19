/* -*- c++ -*- */
/* 
 * Copyright 2019 Andre Silva.
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

#ifndef INCLUDED_SCRAMBLER_CPP_CUSTOM_DESCRAMBLER_IMPL_H
#define INCLUDED_SCRAMBLER_CPP_CUSTOM_DESCRAMBLER_IMPL_H

#include <scrambler_cpp/custom_descrambler.h>
#include <gnuradio/digital/lfsr.h>

namespace gr {
  namespace scrambler_cpp {

    class custom_descrambler_impl : public custom_descrambler
    {
     private:
      digital::lfsr d_lfsr;
      int n_frame;
      int track_n_bits_seed;
      int new_seed;
      int remaining_bits;
      int max_n_produce;
      int time_to_get;

     public:
      custom_descrambler_impl(int mask, int seed, int len, int frame_bits);
      ~custom_descrambler_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace scrambler_cpp
} // namespace gr

#endif /* INCLUDED_SCRAMBLER_CPP_CUSTOM_DESCRAMBLER_IMPL_H */

