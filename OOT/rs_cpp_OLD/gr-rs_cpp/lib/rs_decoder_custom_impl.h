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

#ifndef INCLUDED_RS_CPP_RS_DECODER_CUSTOM_IMPL_H
#define INCLUDED_RS_CPP_RS_DECODER_CUSTOM_IMPL_H

#include <rs_cpp/rs_decoder_custom.h>

namespace gr {
  namespace rs_cpp {

    class rs_decoder_custom_impl : public rs_decoder_custom
    {
     private:
      // Nothing to declare in this block.

     public:
      rs_decoder_custom_impl(int teste);
      ~rs_decoder_custom_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace rs_cpp
} // namespace gr

#endif /* INCLUDED_RS_CPP_RS_DECODER_CUSTOM_IMPL_H */

