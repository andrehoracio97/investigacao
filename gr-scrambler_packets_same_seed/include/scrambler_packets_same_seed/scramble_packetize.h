/* -*- c++ -*- */
/* 
 * Copyright 2019 Andre.
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


#ifndef INCLUDED_SCRAMBLER_PACKETS_SAME_SEED_SCRAMBLE_PACKETIZE_H
#define INCLUDED_SCRAMBLER_PACKETS_SAME_SEED_SCRAMBLE_PACKETIZE_H

#include <scrambler_packets_same_seed/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace scrambler_packets_same_seed {

    /*!
     * \brief <+description of block+>
     * \ingroup scrambler_packets_same_seed
     *
     */
    class SCRAMBLER_PACKETS_SAME_SEED_API scramble_packetize : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<scramble_packetize> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of scrambler_packets_same_seed::scramble_packetize.
       *
       * To avoid accidental use of raw pointers, scrambler_packets_same_seed::scramble_packetize's
       * constructor is in a private implementation
       * class. scrambler_packets_same_seed::scramble_packetize::make is the public interface for
       * creating new instances.
       */
      static sptr make(int mask, int seed, int len, int frame_bit);
    };

  } // namespace scrambler_packets_same_seed
} // namespace gr

#endif /* INCLUDED_SCRAMBLER_PACKETS_SAME_SEED_SCRAMBLE_PACKETIZE_H */

