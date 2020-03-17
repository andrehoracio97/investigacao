/* -*- c++ -*- */
/* 
 * Copyright 2020 andre.
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
#include "rs_encoder_custom_impl.h"

namespace gr {
  namespace rs_cpp {
    rs_encoder_custom::sptr
    rs_encoder_custom::make(int test)
    {
      return gnuradio::get_initial_sptr
        (new rs_encoder_custom_impl(test));
    }

    /*
     * The private constructor
     */
    rs_encoder_custom_impl::rs_encoder_custom_impl(int test)
      : gr::block("rs_encoder_custom",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {
      init_rs();
    }

    /*
     * Our virtual destructor.
     */
    rs_encoder_custom_impl::~rs_encoder_custom_impl()
    {
    }

    void
    rs_encoder_custom_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
        ninput_items_required[i] = noutput_items;
    }


    void rs_encoder_custom_impl::init_rs (void)
    {
      printf("faz\n");
      generate_gf();
      gen_poly();
    }

    int
    rs_encoder_custom_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];

      //insert_data_to_ecode
      for (int i = 0; i < 21; ++i)
      {
        printf("data: %d\n",in[i]);
      }


      //insert_data_to_decode
      for (int i = 0; i < 21; ++i)
      {
        insert_data(in[i],i);
      }
      encode_rs();
      int* code= get_codeword();
      for(int i=0;i<31;i++){
        printf("CODED on BLOCK=%d\n",code[i]);
      }
      //get_codeword();




      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace rs_cpp */
} /* namespace gr */

