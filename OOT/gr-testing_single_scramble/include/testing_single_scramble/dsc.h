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


#ifndef INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_H
#define INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_H

#include <testing_single_scramble/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace testing_single_scramble {

    /*!
     * \brief <+description of block+>
     * \ingroup testing_single_scramble
     *
     */
    class TESTING_SINGLE_SCRAMBLE_API dsc : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<dsc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of testing_single_scramble::dsc.
       *
       * To avoid accidental use of raw pointers, testing_single_scramble::dsc's
       * constructor is in a private implementation
       * class. testing_single_scramble::dsc::make is the public interface for
       * creating new instances.
       */
      static sptr make(int mask, int seed, int len);
    };

  } // namespace testing_single_scramble
} // namespace gr

#endif /* INCLUDED_TESTING_SINGLE_SCRAMBLE_DSC_H */

