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
      max_n_produce(0),
      index_seed(0),
      flag_first(1),
      flag_ultimo(0),
      track_n_bits_added(8)
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
      if(flag_ultimo==1){
        max_n_produce=(std::min(noutput_items,track_n_bits_added));
        for(int i=0; i<max_n_produce; i++){
          out[i]=d_lfsr.next_bit_scramble(0);
          oo++;
        }
        if(max_n_produce==noutput_items){
          flag_ultimo=1;
          track_n_bits_added=track_n_bits_added-max_n_produce;
        }else{
          flag_ultimo=0;
          time_to_create=1;
          track_n_bits_added=8;
        }

      }
      else if(time_to_create==1){      
        if(track_n_bits_seed==32){
          new_seed = rand()%255;
          //new_seed=163;
          binary = std::bitset<32>(new_seed).to_string();
        }
        max_n_produce=(std::min(noutput_items,track_n_bits_seed));
        for(int i=0; i<max_n_produce; i++){ //Normalmente track_n_bits_seed menor a 32
          out[i]=(int(binary[index_seed])-48);
          track_n_bits_seed--;
          index_seed++;
          oo++;//do not consume, only produce
        }
        if(track_n_bits_seed==0){ //Ultima parte quando sai do ssed value.
          track_n_bits_seed=32;
          time_to_create=0;
          index_seed=0;
          //std::cout << "SCRAMBLER new seed: " << new_seed <<"\n";
          d_lfsr.reset_to_value(new_seed);

          flag_first=1;
        }
      }else{
        if (flag_first==1){ //Se for a primeira vez que vimos a esta frame, então dropa os primeiros 8 bits
          added_bits=0;
          while(added_bits<8){
            d_lfsr.next_bit_scramble(in[added_bits]);
            ii++;
            remaining_bits--;
            added_bits++;
          }
          added_bits=0;
          flag_first=0;
          time_to_create=0;
        }else{
          max_n_produce=(std::min(noutput_items,remaining_bits));

          for(int i=0; i<max_n_produce; i++){ //Para todos os 
            out[i]=d_lfsr.next_bit_scramble(in[i]);
            //remaining_bits--;
            ii++;
            oo++;
          }
          if(max_n_produce==remaining_bits){
            flag_ultimo=1;
            remaining_bits=n_frame;

          }else{
          	remaining_bits=remaining_bits-max_n_produce;
          }
        }
      }
      consume_each (ii);
      // Tell runtime system how many output items we produced.
      return oo;
    }
  } /* namespace scrambler_cpp */
} /* namespace gr */

