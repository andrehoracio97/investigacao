/* -*- c++ -*- */
/* 
 * Copyright 2019 gr-add_vector author.
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
#include "add_vector_2_cpp_impl.h"

namespace gr {
  namespace add_vector {

    add_vector_2_cpp::sptr
    add_vector_2_cpp::make(const std::vector<int> &vec)
    {
      return gnuradio::get_initial_sptr
        (new add_vector_2_cpp_impl(vec));
    }

    /*
     * The private constructor
     */
    add_vector_2_cpp_impl::add_vector_2_cpp_impl(const std::vector<int> &vec)
      : gr::block("add_vector_2_cpp",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int)))
    {}

    /*
     * Our virtual destructor.
     */
    add_vector_2_cpp_impl::~add_vector_2_cpp_impl()
    {
    }

    void
    add_vector_2_cpp_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }

    int
    add_vector_2_cpp_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const int *in = (const int *) input_items[0];
      int *out = (int *) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace add_vector */
} /* namespace gr */

