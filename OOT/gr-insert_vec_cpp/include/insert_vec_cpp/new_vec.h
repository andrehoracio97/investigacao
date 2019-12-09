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


#ifndef INCLUDED_INSERT_VEC_CPP_NEW_VEC_H
#define INCLUDED_INSERT_VEC_CPP_NEW_VEC_H

#include <insert_vec_cpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace insert_vec_cpp {

    /*!
     * \brief <+description of block+>
     * \ingroup insert_vec_cpp
     *
     */
    class INSERT_VEC_CPP_API new_vec : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<new_vec> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of insert_vec_cpp::new_vec.
       *
       * To avoid accidental use of raw pointers, insert_vec_cpp::new_vec's
       * constructor is in a private implementation
       * class. insert_vec_cpp::new_vec::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<unsigned char> &vec);

      virtual void set_data(const std::vector<unsigned char> &vec) = 0;
    };

  } // namespace insert_vec_cpp
} // namespace gr

#endif /* INCLUDED_INSERT_VEC_CPP_NEW_VEC_H */

