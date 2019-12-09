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


#ifndef INCLUDED_ADD_VECTOR_ADD_VECTOR_2_CPP_H
#define INCLUDED_ADD_VECTOR_ADD_VECTOR_2_CPP_H

#include <add_vector/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace add_vector {

    /*!
     * \brief <+description of block+>
     * \ingroup add_vector
     *
     */
    class ADD_VECTOR_API add_vector_2_cpp : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<add_vector_2_cpp> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of add_vector::add_vector_2_cpp.
       *
       * To avoid accidental use of raw pointers, add_vector::add_vector_2_cpp's
       * constructor is in a private implementation
       * class. add_vector::add_vector_2_cpp::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<int> &vec);
    };

  } // namespace add_vector
} // namespace gr

#endif /* INCLUDED_ADD_VECTOR_ADD_VECTOR_2_CPP_H */

