/* -*- c++ -*- */
/* 
 * Copyright 2019 Andre.
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
#include "descramble_packetize_impl.h"

namespace gr {
  namespace scrambler_packets_same_seed {

    descramble_packetize::sptr
    descramble_packetize::make(int mask, int seed, int len, int frame_bit)
    {
      return gnuradio::get_initial_sptr
        (new descramble_packetize_impl(mask, seed, len, frame_bit));
    }

    /*
     * The private constructor
     */
    descramble_packetize_impl::descramble_packetize_impl(int mask, int seed, int len, int frame_bit)
      : gr::block("descramble_packetize",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
      d_lfsr(mask, seed, len),
      n_frame(frame_bit),
      remaining_bits(frame_bit),
      max_n_produce(0)
    {}

    /*
     * Our virtual destructor.
     */
    descramble_packetize_impl::~descramble_packetize_impl()
    {
    }

    void
    descramble_packetize_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
    unsigned ninputs = ninput_items_required.size ();
    for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }

    int
    descramble_packetize_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
    const unsigned char *in = (const unsigned char *) input_items[0];
    unsigned char *out = (unsigned char *) output_items[0];
    int ii=0; //Track how many input bits we consume
    int oo=0; //Track how many output bits we produce
    max_n_produce=(std::min(noutput_items,remaining_bits)); //Check buffer to the amount of bits that we can descramble
    for(int i=0; i<max_n_produce; i++){
      out[i]=d_lfsr.next_bit_descramble(in[i]);
      ii++;
      oo++;
    }
    if(max_n_produce==remaining_bits){ //All bits of the frame was sent: ->Reset registers with seed ->Reset variables
      d_lfsr.reset();
      remaining_bits=n_frame;
    }else{ //If we didn't sent all bits, then go again to send what is possible. 
      remaining_bits=remaining_bits-max_n_produce;
    }    
    consume_each (ii);
    return oo;
    }
  } /* namespace scrambler_packets_same_seed */
} /* namespace gr */

