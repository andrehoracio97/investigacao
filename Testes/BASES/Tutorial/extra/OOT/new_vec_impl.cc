/* -*- c++ -*- */
/* 
 * Copyright 2019 gr-insert_vec_cpp author.
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
#include "new_vec_impl.h"

namespace gr {
  namespace insert_vec_cpp {

    new_vec::sptr
    new_vec::make(const std::vector<unsigned char> &vec)
    {
      return gnuradio::get_initial_sptr
        (new new_vec_impl(vec));
    }

    /*
     * The private constructor
     */
    new_vec_impl::new_vec_impl(const std::vector<unsigned char> &vec)
      : gr::block("new_vec",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),
      d_data(vec),
      flag(0),
      track_oo(0)
    {}

    /*
     * Our virtual destructor.
     */
    new_vec_impl::~new_vec_impl()
    {
    }

    void
    new_vec_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      /*ninput_items_required[0] = noutput_items;*/
      /*DEFAULT 1:1*/
      unsigned ninputs = ninput_items_required.size ();
      for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }

    int
    new_vec_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      unsigned char *out = (unsigned char *) output_items[0];
      const unsigned char *in = (const unsigned char *) input_items[0];




      // Tell runtime system how many input items we consumed on
      // each input stream.

      //SEE VEC LEN AND DATA
      /*
      printf("%s %d\n","Tam VEC:", (int) d_data.size());
      for(int i=0; i<(int)d_data.size();i++){
        printf("%u ", d_data[i]);
      }
      printf("\n");
      */

      //Do NOTHING, only passes items
      /*for(int i=0; i<noutput_items; i++){
        printf("%d\n",in[i]);
      }
      */

    
      int ii=0;
      int oo=0;



      if(get_flag()==1){ //Vector already inserted.
        //printf("FLAG 1\n");
        ii=noutput_items;
        oo=noutput_items;
        memcpy(&out[0], &in[0], sizeof(unsigned char)*noutput_items);


      }
      else{ //First time, So I need to insert the vector
        //printf("FLAG 0\n" );

        //int max_copy =(int)d_data.size();
        int max_copy = std::min (noutput_items, (((int) d_data.size()) - get_track()) ); //Check for space in buffers to use the restant vector (len(vec) - used)
        oo=max_copy; //That's what I will output (produce, it can be all vector or all buffer)
        ii=0; //(I don't want consume anything)
        memcpy(&out[0],&d_data[get_track()],sizeof(unsigned char)*max_copy); //Output beguining where I stopped the last time (Starting with 0)

        if(max_copy == (((int) d_data.size()) - get_track()) ){ //If I will use last piece of the vector (len(vec)-used) then I can set the flag to get out. 
          set_flag();
        }
        set_track(get_track()+oo); //Increment the track to know where to start copying the vector the next time (Where I wase plus what I will produce now) 
        //printf("%d\n",get_track());
      }

      consume_each (ii);
      // Tell runtime system how many output items we produced.
      return oo;
    }

  } /* namespace insert_vec_cpp */
} /* namespace gr */

