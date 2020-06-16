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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "custom_descrambler_impl.h"
#include "math.h"

namespace gr {
  namespace scrambler_cpp {

    custom_descrambler::sptr
    custom_descrambler::make(int mask, int seed, int len, int frame_bits)
    {
      return gnuradio::get_initial_sptr
        (new custom_descrambler_impl(mask, seed, len, frame_bits));
    }

    /*
     * The private constructor
     */
    custom_descrambler_impl::custom_descrambler_impl(int mask, int seed, int len, int frame_bits)
      : gr::block("custom_descrambler",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
      d_lfsr(mask, seed, len),
      n_frame(frame_bits),
      track_n_bits_seed(8),
      n_bits_seed(8),
      new_seed(0),
      remaining_bits(frame_bits),
      max_n_produce(0),
      time_to_get(1)
    {}

    /*
     * Our virtual destructor.
     */
    custom_descrambler_impl::~custom_descrambler_impl()
    {
    }

    void
    custom_descrambler_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
    unsigned ninputs = ninput_items_required.size ();
    for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }

    int
    custom_descrambler_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];
      int ii=0; //Track how many inputbits we consume
      int oo=0; //Track how many output bit we produce
      if(time_to_get==1){ //We are in seed block
        max_n_produce=(std::min(noutput_items,track_n_bits_seed));
        for(int i=0; i<max_n_produce; i++){ 
          new_seed=new_seed<<1;
          //std::cout << "BIT:" << int(in[i]) << "\n";
          new_seed=(new_seed|in[i]);
          ii++;
        }if(max_n_produce==track_n_bits_seed){ //If all bits sent out of seed block ->SAIR
          track_n_bits_seed=n_bits_seed;
          time_to_get=0;
          //new_seed=163;
          //std::cout << "DESCRAMBLER: " << new_seed <<"\n";
          d_lfsr.reset_to_value(new_seed); //Set new seed
          new_seed=0;
        }else{
          track_n_bits_seed=track_n_bits_seed-max_n_produce;
        }
      }else{
        max_n_produce=(std::min(noutput_items,remaining_bits));
        for(int i=0; i<max_n_produce; i++){
          out[i]=d_lfsr.next_bit_descramble(in[i]);
          ii++;
          oo++;
        }
        if(max_n_produce==remaining_bits){ //All bits of the frame was sent - Go to seed block
          time_to_get=1; //Go to get seed from seed block
          remaining_bits=n_frame;
        }else{
          remaining_bits=remaining_bits-max_n_produce;
        }
      }      
      consume_each (ii);
      return oo;
    }
  } /* namespace scrambler_cpp */
} /* namespace gr */

