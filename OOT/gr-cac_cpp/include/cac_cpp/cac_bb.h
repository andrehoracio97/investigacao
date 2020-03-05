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


#ifndef INCLUDED_CAC_CPP_CAC_BB_H
#define INCLUDED_CAC_CPP_CAC_BB_H

#include <cac_cpp/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace cac_cpp {

    /*!
     * \brief <+description of block+>
     * \ingroup cac_cpp
     *
     */
    class CAC_CPP_API cac_bb : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<cac_bb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of cac_cpp::cac_bb.
       *
       * To avoid accidental use of raw pointers, cac_cpp::cac_bb's
       * constructor is in a private implementation
       * class. cac_cpp::cac_bb::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string& access_code, int threshold);
      virtual bool set_access_code(const std::string& access_code) = 0;
      virtual unsigned long long access_code() const = 0;
    };

  } // namespace cac_cpp
} // namespace gr

#endif /* INCLUDED_CAC_CPP_CAC_BB_H */

