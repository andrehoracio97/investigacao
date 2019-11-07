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

#ifndef INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_IMPL_H
#define INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_IMPL_H

#include <correlate_and_delay/corr_and_delay.h>
#include <gnuradio/filter/fft_filter.h>

using namespace gr::filter;

namespace gr {
  namespace correlate_and_delay {

    class corr_and_delay_impl : public corr_and_delay
    {
     private:
    std::vector<gr_complex> access_code;
    std::vector<gr_complex> d_access_code;

    int lenght_access_code;

    kernel::fft_filter_ccc* correlation_filter;

    gr_complex* d_corr;
    float* d_corr_mag;
    float d_pfa; // probability of false alarm
    float d_scale;
    float detection;
    bool have_access_code;
    bool have_corr;
    float d_sps;

    pmt::pmt_t d_src_id;

     public:
      corr_and_delay_impl(int number_bits, int interval, float threshold);
      ~corr_and_delay_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

    };

  } // namespace correlate_and_delay
} // namespace gr

#endif /* INCLUDED_CORRELATE_AND_DELAY_CORR_AND_DELAY_IMPL_H */

