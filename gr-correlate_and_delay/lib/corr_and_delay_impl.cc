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

#include <gnuradio/filter/firdes.h>
#include <volk/volk.h>

#include <gnuradio/filter/pfb_arb_resampler.h>

namespace gr {
  namespace correlate_and_delay {

    corr_and_delay::sptr
    corr_and_delay::make(int number_bits, int interval, float threshold)
    {
      return gnuradio::get_initial_sptr
        (new corr_and_delay_impl(number_bits, interval, threshold));
    }

    corr_and_delay_impl::corr_and_delay_impl(int number_bits, int interval, float threshold)
      : gr::block("corr_and_delay",
              gr::io_signature::make(2, 2, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, sizeof(gr_complex))),
      time_to_catch(1),
      lenght_access_code(100),
      access_code()
    {
    
    const size_t nitems = 24 * 1024;
    set_max_noutput_items(nitems);
    d_corr = (gr_complex*)volk_malloc(sizeof(gr_complex) * nitems, volk_get_alignment());
    d_corr_mag = (float*)volk_malloc(sizeof(float) * nitems, volk_get_alignment());
    
    d_pfa = -logf(1.0f - threshold);
    d_scale = 1.0f;
    }

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


    void corr_and_delay_impl::conjugate_and_reverse(std::vector<gr_complex> access_code){
      for (size_t i = 0; i < access_code.size(); i++) {
        access_code[i] = conj(access_code[i]);
      }
      std::reverse(access_code.begin(), access_code.end());
    }


    int corr_and_delay_impl::correlate_it(){


      return 0;
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

    if(noutput_items>=lenght_access_code){ //I need to have 100 samples to start
      if (time_to_catch==1){  //ii_noise has to have lenght_access_code items already
        for (int i = access_code.size(); i < lenght_access_code; i++){
          //access_code[i]=ii_noise[i];
          access_code.push_back(ii_noise[i]);
          if (i==99){ //All the access code catched
            printf("Access_code Catched");
            time_to_catch=0;
            conjugate_and_reverse(access_code); //conjugate and reverse
            correlation_filter = new kernel::fft_filter_ccc(1, access_code); //create correlation filter from the access code --1=decimation then the taps
            int nsamples;
            nsamples = correlation_filter->set_taps(access_code); //The filter function expects that the input signal is a multiple of d_nsamples in the class that's computed internally to be as fast as possible. The function set_taps will return the value of nsamples that can be used externally to check this boundary
            set_output_multiple(nsamples); //Ensures the scheduler always passes this block the right number of samples
          }
        }
      }else{ //I already have the access code so I need to correlate it against the received symbols
        for(int i=0; i<(noutput_items-lenght_access_code+1); i++){ //Got o each "Window" in output items -> For 5 window, and 10 items, I can do 10-5+1 times. 
          correlation_filter->filter(lenght_access_code, &ii_signal[i], d_corr); //Calculate the correlation of input with the noise. 1ºItems to produce. 2ºInpuct vector to be filtered. 3ºresult of filter opertation.  The 2º starts in the "window" that I am.
          volk_32fc_magnitude_squared_32f(&d_corr_mag[0], d_corr, lenght_access_code); //magnitude squared of the correlation

          float detection = 0;
          for (int j = 0; j < lenght_access_code; j++) {
            detection += d_corr_mag[j];
          }
          detection /= static_cast<float>(lenght_access_code);
          detection *= d_pfa;
          //printf("DeT %f\n",detection);

          int isps = (int)(4 + 0.5f);
          int k=0;
          while (k<lenght_access_code){
            // Look for the correlator output to cross the threshold.
        // Sum power over two consecutive symbols in case we're offset
        // in time. If off by 1/2 a symbol, the peak of any one point
        // is much lower.
            float corr_mag = d_corr_mag[k] + d_corr_mag[k + 1];
            if (corr_mag <= 4 * detection) {
                k++;
                continue;
            }

            // Go to (just past) the current correlator output peak
            while ((k < (lenght_access_code - 1)) && (d_corr_mag[k] < d_corr_mag[k + 1])) {
                k++;
            }
            double nom = 0, den = 0;
            nom = d_corr_mag[k - 1] + 2 * d_corr_mag[k] + 3 * d_corr_mag[k + 1];
            den = d_corr_mag[k - 1] + d_corr_mag[k] + d_corr_mag[k + 1];
            double center = nom / den;
            center = (center - 2.0); // adjust for bias in center of mass calculation

            uint32_t maxi;
            volk_32fc_index_max_32u_manual(&maxi, (gr_complex*)ii_signal, lenght_access_code, "generic");
            d_scale = 1 / std::abs(ii_signal[maxi]);
            //printf("DETECTED CORRELATION\n");

            k += isps;
          }


          /*if (detection>=threshold){
            printf("DETECTED CORRELATION\n");
          }*/
        }
      }
    }

   /*   printf("ii_noise[0]=%f\n",ii_noise[0]);
      printf("ii_noise[1]=%f\n",ii_noise[1]);
*/


    memcpy(oo_noise, ii_noise, sizeof(gr_complex)*noutput_items);
    memcpy(oo_signal, ii_signal, sizeof(gr_complex)*noutput_items);

    


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

