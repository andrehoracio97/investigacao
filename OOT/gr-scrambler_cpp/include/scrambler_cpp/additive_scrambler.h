/* -*- c++ -*- */
/* 
 * Copyright 2019 andre silva.
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


#ifndef INCLUDED_SCRAMBLER_CPP_ADDITIVE_SCRAMBLER_H
#define INCLUDED_SCRAMBLER_CPP_ADDITIVE_SCRAMBLER_H

#include <scrambler_cpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace scrambler_cpp {

    /*!
     * \brief <+description of block+>
     * \ingroup scrambler_cpp
     *
     */
    class SCRAMBLER_CPP_API additive_scrambler : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<additive_scrambler> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of scrambler_cpp::additive_scrambler.
       *
       * To avoid accidental use of raw pointers, scrambler_cpp::additive_scrambler's
       * constructor is in a private implementation
       * class. scrambler_cpp::additive_scrambler::make is the public interface for
       * creating new instances.
       */
      static sptr make(int mask, int seed, int len, int frame_bits);
    };

  } // namespace scrambler_cpp
} // namespace gr

#endif /* INCLUDED_SCRAMBLER_CPP_ADDITIVE_SCRAMBLER_H */

