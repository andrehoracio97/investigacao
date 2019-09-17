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
      n_bits_scrambled(0),
      track_n_bits_seed(0),
      new_seed(0),
      binary()
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

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      for(int i=0;i<noutput_items;i++){  //in[i] has the unpacked bytes, so we bo byte at byte (in our case bit - unpacked)

        //If we still has bits to scramble, go ahead
        if(n_bits_scrambled<n_frame){
          out[i]=d_lfsr.next_bit_scramble(in[i]);
          n_bits_scrambled=n_bits_scrambled+1;
        }
        else{ //end of frame bits, new stuff to do


          if(track_n_bits_seed==0){
            //NEW SEED - if we have left bits at 0 (we don't begin yet)
            new_seed = rand()%255; //Betwen 0 an max value. 2147483647
            //Convert SEED to binary of 32 bits
            binary = std::bitset<32>(new_seed).to_string();
          }
          

          //Now we need to add the new 32 bits of the new seet to our stream (BIT per BIT), taking into account the space available on output buffer, we can do this by only tracking the left bits because we come here again (bacause the for cycle).
          //--if we still has bits, then we keep adding and tracking how many left bits and don't and reset n_bits_scrambled).
          if(track_n_bits_seed<32){
            out[i]=binary[track_n_bits_seed];
            track_n_bits_seed=track_n_bits_seed+1;
          }
          else{
          //--if there is no left bits we reset reset seed to lfsr and reset n_bits_scrambled
            track_n_bits_seed=0; //Reset track
            d_lfsr.reset_to_value(new_seed); //Scramble with new seed
            n_bits_scrambled=0; //Scramble a new packet

          }
        }
      }


      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace scrambler_cpp */
} /* namespace gr */

