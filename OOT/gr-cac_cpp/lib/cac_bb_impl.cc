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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "cac_bb_impl.h"

#include <volk/volk.h>
#include <boost/format.hpp>
#include <cstdio>
#include <iostream>
#include <stdexcept>


namespace gr {
  namespace cac_cpp {

    cac_bb::sptr
    cac_bb::make(const std::string& access_code, int threshold)
    {
      return gnuradio::get_initial_sptr
        (new cac_bb_impl(access_code, threshold));
    }

    /*
     * The private constructor
     */
    cac_bb_impl::cac_bb_impl(const std::string& access_code, int threshold)
      : gr::block("cac_bb",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char))),
      d_data_reg(0),
      d_mask(0),
      d_threshold(threshold),
      d_len(0)

    {
    set_tag_propagation_policy(TPP_DONT);

    if (!set_access_code(access_code)) {
        GR_LOG_ERROR(d_logger, "access_code is > 64 bits");
        throw std::out_of_range("access_code is > 64 bits");
    }

    std::stringstream str;
    str << name() << unique_id();
    d_me = pmt::string_to_symbol(str.str());
    d_key = pmt::string_to_symbol("tag_name");

    d_state = STATE_SYNC_SEARCH;
    d_pkt_len = 0;
    d_pkt_count = 0;
    d_hdr_reg = 0;
    d_hdr_count = 0;

    //Added by me
    count_bits_read=0;
    reset_counts_input_bit();
    init_rs();
}

    /*
     * Our virtual destructor.
     */
    cac_bb_impl::~cac_bb_impl()
    {
    }

    void
    cac_bb_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        unsigned ninputs = ninput_items_required.size ();
        for(unsigned i = 0; i < ninputs; i++)
          ninput_items_required[i] = noutput_items;
    }

    void cac_bb_impl::init_rs (void)
    {
      printf("INIT_RS\n");
      generate_gf();
      gen_poly();
    }


    bool cac_bb_impl::set_access_code(const std::string& access_code)
    {
        d_len = access_code.length(); // # of bytes in string
        if (d_len > 64)
            return false;

        // set len least significant bits to 1.
        d_mask = ((~0ULL) >> (64 - d_len));

        d_access_code = 0;
        for (unsigned i = 0; i < d_len; i++) {
            d_access_code = (d_access_code << 1) | (access_code[i] & 1);
        }

        GR_LOG_DEBUG(d_logger, boost::format("Access code: %llx") % d_access_code);
        GR_LOG_DEBUG(d_logger, boost::format("Mask: %llx") % d_mask);

        return true;
    }

    unsigned long long cac_bb_impl::access_code() const
    {
        return d_access_code;
    }

    inline void cac_bb_impl::enter_search()
    {
        d_state = STATE_SYNC_SEARCH;

        //Maybe rest data to decode???
        //Added by me
        count_bits_read=0;
        reset_counts_input_bit();
        printf("RESET CONTS\n");


    }

    inline void cac_bb_impl::enter_have_sync()
    {
        d_state = STATE_HAVE_SYNC;
        d_hdr_reg = 0;
        d_hdr_count = 0;
    }

    inline void cac_bb_impl::enter_have_header(int payload_len)
    {
        d_state = STATE_HAVE_HEADER;
        d_pkt_len = 8 * payload_len;
        d_pkt_count = 0;
    }

    bool cac_bb_impl::header_ok()
    {
        // confirm that two copies of header info are identical
        return ((d_hdr_reg >> 16) ^ (d_hdr_reg & 0xffff)) == 0;
    }

    int cac_bb_impl::header_payload()
    {
        return (d_hdr_reg >> 16) & 0x0fff;
    }



    int
    cac_bb_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];

      uint64_t abs_out_sample_cnt = nitems_written(0);

      int nprod = 0;
      int count = 0;


      while (count < noutput_items) {
          switch (d_state) {
            case STATE_SYNC_SEARCH: // Look for the access code correlation
                while (count < noutput_items) {
                    //printf("Received_Bit=%d\n",in[count_bits_read]);
                    if(count_bits_read<155){ //read 155 bits to fill the data in RS to be decoded
                        input_bit_in_received_data(in[count]);
                    }else{ //all bytes filled
                        printf("All 155 bits readed: SHIFTS\n");
                        decode_costum(); //Decode

                        uint64_t word_decoded=get_64bit_ac_received_word(); //Word in64bit len resulted from RS decode
                        uint64_t wrong_bits = 0;
                        uint64_t nwrong = d_threshold + 1;
                        wrong_bits = (word_decoded ^ d_access_code) & d_mask;
                        volk_64u_popcnt(&nwrong, wrong_bits); //How many 1's - ERRORS
                        if (nwrong <= d_threshold) {
                            //printf("Acces Code Decoded Catched!!");
                            d_hdr_reg=get_64bit_payload_lenght_word(); //Pick the 32bit len of the payload lenght decoded by the RS.
                            if (header_ok()) {
                                //printf("Header is equal\n");
                                int payload_len = header_payload();
                                enter_have_header(payload_len);
                                break; //End, caso contratio irá continuar a fazer o count e andar sempre neste loop
                            } else {
                                printf("POR ENQUANTO NAO PODE AQUI, SERA realizado um shift-----_PAYLOAD DIFF\n");
                                //keep searching----??????????????????
                                //shift_and_input_bit_in_received_data(in[count_bits_read], count_bits_read);
                            }
                        }else{
                            printf("POR ENQUANTO NAO PODE AQUI, SERA realizado um shift -----NWORNG\n");
                            //Muitos erros por isso faz shift e tenta proxmio
                            //shift_and_input_bit_in_received_data(in[count_bits_read], count_bits_read);
                        }
                    }
                    count_bits_read++;
                    count++;
                }
                break; //break because its a CASE
         
            case STATE_HAVE_HEADER:
                if (d_pkt_count == 0) {
                    // MAKE A TAG OUT OF THIS AND UPDATE OFFSET
                    add_item_tag(0,                          // stream ID
                                 abs_out_sample_cnt + nprod, // sample
                                 d_key,                      // length key
                                 pmt::from_long(d_pkt_len),  // length data
                                 d_me);                      // block src id
                }

                while (count < noutput_items) {
                    if (d_pkt_count < d_pkt_len) {
                        out[nprod++] = in[count++];
                        d_pkt_count++;
                    } else {
                        printf("End Payload\n");
                        enter_search();
                        break;
                    }
                }
                break;
            }
      }

      consume_each(noutput_items);
      return nprod;
    }

  } /* namespace cac_cpp */
} /* namespace gr */

