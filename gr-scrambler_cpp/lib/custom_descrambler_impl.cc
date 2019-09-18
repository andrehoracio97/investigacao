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
      n_bits_descrambled(99999999),
      track_n_bits_seed(31),
      new_seed(0),
      remaining_bits(frame_bits),
      max_n_produce(0),
      time_to_get(1),
      index_seed(0)
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

      // Do <+signal processing+>
      int ii=0;
      int oo=0;
      if(time_to_get==1){
        max_n_produce=(std::min(noutput_items,track_n_bits_seed));
        for(int i=max_n_produce; i>=0; i--){ //Normalmente track_n_bits_seed menor a 32
          if(int(in[i])==1){
            new_seed=new_seed+pow(2.0, index_seed);
          }
          std::cout << "BIT:" << int(in[i]) << "\n";
          track_n_bits_seed--;
          index_seed++;
          ii++;
        }
        if(max_n_produce<=noutput_items){ //Ultima parte do bloco seed já foi enviada - reset valores
          track_n_bits_seed=31;
          time_to_get=0;
          remaining_bits=n_frame;
          //new_seed=163;
          std::cout << "DESCRAMBLER: " << new_seed <<"\n";
          d_lfsr.reset_to_value(new_seed);
          new_seed=0;
          index_seed=0;
        }
      }else{
        max_n_produce=(std::min(noutput_items,remaining_bits));
        for(int i=0; i<max_n_produce; i++){ //Para todos os 
          out[i]=d_lfsr.next_bit_descramble(in[i]);
          remaining_bits--;
          ii++;
          oo++;
        }
        if(max_n_produce<=0){ //COLOCAR <=0 caso de algum erro
          //CREATE SEED BLOCK
          time_to_get=1;
          remaining_bits=n_frame;
        }
      }

      
      consume_each (ii);
      // Tell runtime system how many output items we produced.
      return oo;
    }

  } /* namespace scrambler_cpp */
} /* namespace gr */

