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


#ifndef INCLUDED_PUNCTURE64_CPP_DEPUNCTURE64_H
#define INCLUDED_PUNCTURE64_CPP_DEPUNCTURE64_H

#include <puncture64_cpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace puncture64_cpp {

    /*!
     * \brief <+description of block+>
     * \ingroup puncture64_cpp
     *
     */
    class PUNCTURE64_CPP_API depuncture64 : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<depuncture64> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of puncture64_cpp::depuncture64.
       *
       * To avoid accidental use of raw pointers, puncture64_cpp::depuncture64's
       * constructor is in a private implementation
       * class. puncture64_cpp::depuncture64::make is the public interface for
       * creating new instances.
       */
      static sptr make(int puncsize, uint64_t puncpat, char sym);
    };

  } // namespace puncture64_cpp
} // namespace gr

#endif /* INCLUDED_PUNCTURE64_CPP_DEPUNCTURE64_H */

