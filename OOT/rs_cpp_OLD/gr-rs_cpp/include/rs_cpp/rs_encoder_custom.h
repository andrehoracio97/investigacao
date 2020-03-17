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


#ifndef INCLUDED_RS_CPP_RS_ENCODER_CUSTOM_H
#define INCLUDED_RS_CPP_RS_ENCODER_CUSTOM_H

#include <rs_cpp/api.h>
#include <gnuradio/block.h>



namespace gr {
  namespace rs_cpp {

    /*!
     * \brief <+description of block+>
     * \ingroup rs_cpp
     *
     */
    class RS_CPP_API rs_encoder_custom : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<rs_encoder_custom> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of rs_cpp::rs_encoder_custom.
       *
       * To avoid accidental use of raw pointers, rs_cpp::rs_encoder_custom's
       * constructor is in a private implementation
       * class. rs_cpp::rs_encoder_custom::make is the public interface for
       * creating new instances.
       */
      static sptr make(int test);
    };

  } // namespace rs_cpp
} // namespace gr

#endif /* INCLUDED_RS_CPP_RS_ENCODER_CUSTOM_H */

