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

#ifndef INCLUDED_INSERT_VEC_CPP_NEW_VEC_IMPL_H
#define INCLUDED_INSERT_VEC_CPP_NEW_VEC_IMPL_H

#include <insert_vec_cpp/new_vec.h>

namespace gr {
  namespace insert_vec_cpp {

    class new_vec_impl : public new_vec
    {
     private:
      std::vector<unsigned char> d_data;
      int flag;
      int track_oo;
      // Nothing to declare in this block.

     public:
      new_vec_impl(const std::vector<unsigned char> &vec);
      ~new_vec_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);
      void set_data(const std::vector<unsigned char> &vec){
        d_data=vec;
      }
      int get_flag(){
        return flag;
      }
      void set_flag(){
        flag=1;
      }
      void set_track(int a){
        track_oo=a;
      }
      int get_track(){
        return track_oo;
      }

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace insert_vec_cpp
} // namespace gr

#endif /* INCLUDED_INSERT_VEC_CPP_NEW_VEC_IMPL_H */

