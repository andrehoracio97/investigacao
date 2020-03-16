/* -*- c++ -*- */
/* 
 * Copyright 2020 andre silva.
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

#ifndef INCLUDED_PUNCTURE64_CPP_PUNCTURE64_IMPL_H
#define INCLUDED_PUNCTURE64_CPP_PUNCTURE64_IMPL_H

#include <puncture64_cpp/puncture64.h>

namespace gr {
  namespace puncture64_cpp {

    class puncture64_impl : public puncture64
    {
     private:
      int d_puncsize;
      int d_puncholes;
      uint64_t d_puncpat;

     public:
      puncture64_impl(int puncsize, uint64_t puncpat);
      ~puncture64_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
      int fixed_rate_ninput_to_noutput(int ninput);
      int fixed_rate_noutput_to_ninput(int noutput);
    };

  } // namespace puncture64_cpp
} // namespace gr

#endif /* INCLUDED_PUNCTURE64_CPP_PUNCTURE64_IMPL_H */

