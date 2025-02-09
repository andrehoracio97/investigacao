/* -*- c++ -*- */
/* 
 * Copyright 2019 andre.
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

#ifndef INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_IMPL_H
#define INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_IMPL_H

#include <testing_single_scramble/dsc.h>
#include <gnuradio/digital/lfsr.h>

namespace gr {
  namespace testing_single_scramble {

    class dsc_impl : public dsc
    {
     private:
      digital::lfsr d_lfsr;
      int trash;

     public:
      dsc_impl(int mask, int seed, int len);
      ~dsc_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace testing_single_scramble
} // namespace gr

#endif /* INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_IMPL_H */

