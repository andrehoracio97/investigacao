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
      n_bits_seed(8),
      track_n_bits_seed(8),
      new_seed(0),
      time_to_create(1),
      remaining_bits(frame_bits),
      max_n_produce(0),
      flag_last(0),
      track_n_bits_added(8),
      mask()
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
    int ii=0; //Track how many inputbits we consume
    int oo=0; //Track how many output bit we produces
    if(flag_last==1){ //It's the last bits of the frame, so we need to flush it
      	max_n_produce=(std::min(noutput_items,track_n_bits_added));
      	for(int i=0; i<max_n_produce; i++){
      		out[i]=d_lfsr.next_bit_scramble(0);
      		oo++;
      	}
      	if(max_n_produce==track_n_bits_added){ //If we sent all bits, we reset variables and we get out of last byte to create a new SEED block
      		flag_last=0; 
      		time_to_create=1; //Create a new Seed block
      		track_n_bits_added=8;
      	}else{ //If we didn't sent all bit's, then go again. 
      		track_n_bits_added=track_n_bits_added-max_n_produce;
      	}
    }
    else if(time_to_create==1){      
      	if(track_n_bits_seed==n_bits_seed){ //If the first time in Seed Block
      		new_seed = rand()%255;	//We generate a new seed.
      		mask= 1 << (n_bits_seed-1); //Reset mask
          //new_seed=163;
      	}
      	max_n_produce=(std::min(noutput_items,track_n_bits_seed));
        for(int i=0; i<max_n_produce; i++){ //Normalmente track_n_bits_seed menor a 32
        	out[i]=((mask & new_seed) != 0);
        	mask >>= 1;
        	oo++;//do not consume, only produce
        }
        if(max_n_produce==track_n_bits_seed){ //All bits sent SO: -Drop first bits and OUT of Seed Block
        	track_n_bits_seed=n_bits_seed;
          //std::cout << "SCRAMBLER new seed: " << new_seed <<"\n";
        	d_lfsr.reset_to_value(new_seed); //Set the new seed
        	
        	for(int i=0;i<8;i++){ //First bits of the frame, so it's trash -->DROP
        		d_lfsr.next_bit_scramble(in[i]);
        		ii++;
        		remaining_bits--;
        	}
        	time_to_create=0; //Get out of seed block 
        }else{
        	track_n_bits_seed=track_n_bits_seed-max_n_produce;
        }
    }else{ //Normal behaviour - Inside the frame
    	max_n_produce=(std::min(noutput_items,remaining_bits));
    	for(int i=0; i<max_n_produce; i++){
      		out[i]=d_lfsr.next_bit_scramble(in[i]);
      		ii++;
      		oo++;
      	}
      	if(max_n_produce==remaining_bits){ //If we sent all bits, go to last to flush.
      		flag_last=1;
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

