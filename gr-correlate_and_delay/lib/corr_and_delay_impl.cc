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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "corr_and_delay_impl.h"

namespace gr {
  namespace correlate_and_delay {

    corr_and_delay::sptr
    corr_and_delay::make(int number_bits, int interval, int threshold)
    {
      return gnuradio::get_initial_sptr
        (new corr_and_delay_impl(number_bits, interval, threshold));
    }

    /*
     * The private constructor
     */
    corr_and_delay_impl::corr_and_delay_impl(int number_bits, int interval, int threshold)
      : gr::block("corr_and_delay",
              gr::io_signature::make(2, 2, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, sizeof(gr_complex))),
      time_to_catch(1),
      lenght_access_code(100),
      access_code()
    {}

    /*
     * Our virtual destructor.
     */
    corr_and_delay_impl::~corr_and_delay_impl()
    {
    }

    void
    corr_and_delay_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
    unsigned ninputs = ninput_items_required.size ();
    for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = noutput_items;
    }

    int
    corr_and_delay_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
    const gr_complex *ii_noise = (const gr_complex*)input_items[0];
    gr_complex *oo_noise = (gr_complex *) output_items[0];

    const gr_complex *ii_signal = (const gr_complex*)input_items[1];
    gr_complex *oo_signal = (gr_complex *) output_items[1];

    if (time_to_catch==1){
      for (int i = 0; i < lenght_access_code; i++){
        access_code[i]=ii_noise[i];
        printf("access_code[%d]=%f\n",i,access_code[i]);
      }
      time_to_catch=0;
    }


   /*   printf("ii_noise[0]=%f\n",ii_noise[0]);
      printf("ii_noise[1]=%f\n",ii_noise[1]);
*/

    memcpy(oo_noise, ii_noise, sizeof(gr_complex)*noutput_items);
    memcpy(oo_signal, ii_signal, sizeof(gr_complex)*noutput_items);

    


      // Tell runtime system how many input items we consumed on each input stream.
      //consume_each (noutput_items);
      consume (0,noutput_items);
      consume (1,noutput_items);

      // Tell runtime system how many output items we produced.
      produce(0,noutput_items);
      produce(1,noutput_items);
      return 0;

    }

  } /* namespace correlate_and_delay */
} /* namespace gr */

