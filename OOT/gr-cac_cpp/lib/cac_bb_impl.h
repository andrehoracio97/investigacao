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

#ifndef INCLUDED_CAC_CPP_CAC_BB_IMPL_H
#define INCLUDED_CAC_CPP_CAC_BB_IMPL_H

#include <cac_cpp/cac_bb.h>
 

extern "C" {
#include <rs_changed.c>
}
/*
extern "C" {
#include <gnuradio/fec/rs.h>
}*/

namespace gr {
  namespace cac_cpp {

    class cac_bb_impl : public cac_bb
    {
     private:
      enum state_t { STATE_SYNC_SEARCH, STATE_HAVE_SYNC, STATE_HAVE_HEADER };

      state_t d_state;

      unsigned long long d_access_code; // access code to locate start of packet
                                      //   access code is left justified in the word
      unsigned long long d_data_reg;    // used to look for access_code
      unsigned long long d_mask;        // masks access_code bits (top N bits are set where
                                      //   N is the number of bits in the access code)
      unsigned int d_threshold;         // how many bits may be wrong in sync vector
      unsigned int d_len;               // the length of the access code

      unsigned long long d_hdr_reg; // used to look for header
      int d_hdr_count;

      pmt::pmt_t d_key, d_me; // d_key is the tag name, d_me is the block name + unique ID
      int d_pkt_len, d_pkt_count;

      //NOVO
      int count_bits_read;
      unsigned char byte_to_be_inputed;


      void enter_search();
      void enter_have_sync();
      void enter_have_header(int payload_len);

      bool header_ok();
      int header_payload();
     public:
      cac_bb_impl(const std::string& access_code, int threshold);
      ~cac_bb_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
      
        bool set_access_code(const std::string& access_code);
        unsigned long long access_code() const;
        void init_rs(void);
    };

  } // namespace cac_cpp
} // namespace gr

#endif /* INCLUDED_CAC_CPP_CAC_BB_IMPL_H */

