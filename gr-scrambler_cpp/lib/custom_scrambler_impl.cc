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
#include "custom_scrambler_impl.h"
#include <stdlib.h>     /* srand, rand */
#include <bitset> /*para converter*/

namespace gr {
  namespace scrambler_cpp {

    custom_scrambler::sptr
    custom_scrambler::make(int mask, int seed, int len, int frame_bits)
    {
      return gnuradio::get_initial_sptr
        (new custom_scrambler_impl(mask, seed, len, frame_bits));
    }

    /*
     * The private constructor
     */
    custom_scrambler_impl::custom_scrambler_impl(int mask, int seed, int len, int frame_bits)
      : gr::block("custom_scrambler",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
      d_lfsr(mask,seed,len),
      n_frame(frame_bits),
      n_bits_scrambled(99999999),
      track_n_bits_seed(32),
      new_seed(0),
      binary(),
      added_bits(0),
      create_block_seed(0),
      time_to_create(1),
      remaining_bits(frame_bits),
      max_n_produce(0)
    {}

    /*
     * Our virtual destructor.
     */
    custom_scrambler_impl::~custom_scrambler_impl()
    {
    }

    void
    custom_scrambler_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }

    int
    custom_scrambler_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];
      int ii=0;
      int oo=0;
      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      if(time_to_create==1){
       
        if(track_n_bits_seed==32){
          new_seed = rand()%255;
          std::cout << "NEW SEED\n";
          //new_seed=163;
          binary = std::bitset<32>(new_seed).to_string();
        }
        max_n_produce=(std::min(noutput_items,track_n_bits_seed));
        for(int i=0; i<max_n_produce; i++){ //Normalmente track_n_bits_seed menor a 32
          out[i]=(int(binary[32-track_n_bits_seed])-48);
          track_n_bits_seed=track_n_bits_seed-1;
          oo=oo+1;//do not consume, only produce
        }
        if(max_n_produce<=noutput_items){ //Ultima parte quando sai do ssed value.
          track_n_bits_seed=32;
          time_to_create=0;
          d_lfsr.reset_to_value(new_seed);
        }
      }else{
        max_n_produce=(std::min(noutput_items,remaining_bits));
        for(int i=0; i<max_n_produce; i++){ //Para todos os 
          out[i]=d_lfsr.next_bit_scramble(in[i]);
          remaining_bits--;
          ii++;
          oo++;
          if(remaining_bits==0){ //COLOCAR <=0 caso de algum erro
            //CREATE SEED BLOCK
            time_to_create=1;
            remaining_bits=n_frame;
          }
          //IF remaining bits poder ser fora acho....testar
        }
      }
      consume_each (ii);
      // Tell runtime system how many output items we produced.
      return oo;
    }
  } /* namespace scrambler_cpp */
} /* namespace gr */

