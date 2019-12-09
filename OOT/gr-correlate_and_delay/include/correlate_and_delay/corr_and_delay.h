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


#ifndef INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_H
#define INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_H

#include <correlate_and_delay/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace correlate_and_delay {

    /*!
     * \brief <+description of block+>
     * \ingroup correlate_and_delay
     *
     */
    class CORRELATE_AND_DELAY_API corr_and_delay : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<corr_and_delay> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of correlate_and_delay::corr_and_delay.
       *
       * To avoid accidental use of raw pointers, correlate_and_delay::corr_and_delay's
       * constructor is in a private implementation
       * class. correlate_and_delay::corr_and_delay::make is the public interface for
       * creating new instances.
       */
      static sptr make(int number_bits, int interval, float threshold, float sps);
    };

  } // namespace correlate_and_delay
} // namespace gr

#endif /* INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_H */

