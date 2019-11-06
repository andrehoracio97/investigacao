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
              gr::io_signature::make(2, 3, sizeof(gr_complex))),
      lenght_access_code(number_bits),
      access_code(),
      detection(0),
      have_corr(false),
      have_access_code(false),
      d_sps(1)
    {
    
    const size_t nitems = 24 * 1024;
    set_max_noutput_items(nitems);
    d_corr = (gr_complex*)volk_malloc(sizeof(gr_complex) * nitems, volk_get_alignment());
    d_corr_mag = (float*)volk_malloc(sizeof(float) * nitems, volk_get_alignment());
    
    d_pfa = -logf(1.0f - threshold);
    d_scale = 1.0f;

    //ADDED
   /* set_history(lenght_access_code + 1);
    declare_sample_delay(1, 0);
    declare_sample_delay(0, lenght_access_code);*/



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

      gr_complex *corr = (gr_complex*)output_items[2];

      /*gr_complex* corr;
      if (output_items.size() > 2)
        corr = (gr_complex*)output_items[2];
      else
        corr = d_corr;
*/


      if(noutput_items>=lenght_access_code){ //Make sure we have number of samples enough to create fft filte of noise
        if(have_access_code==false){ //If access code still not catched
          for (int i = access_code.size(); i < lenght_access_code; i++){
              //access_code[i]=ii_noise[i];
              access_code.push_back(ii_noise[i]);


              if (i==(lenght_access_code-1)){ //All the access code catched
                printf("Access Code Caught\n");
                have_access_code=true;

                //conjugate_and_reverse(access_code); //conjugate and reverse
                //conjugate and reverse
                for (int j = 0; j < access_code.size(); j++) { //doing the conjugate
                  access_code[j] = conj(access_code[j]);
                }
                std::reverse(access_code.begin(), access_code.end()); //doing the reverse

                correlation_filter = new kernel::fft_filter_ccc(1, access_code); //create correlation filter from the access code --1=decimation then the taps
                int nsamples;
                nsamples = correlation_filter->set_taps(access_code); //The filter function expects that the input signal is a multiple of d_nsamples in the class that's computed internally to be as fast as possible. The function set_taps will return the value of nsamples that can be used externally to check this boundary
                set_output_multiple(nsamples); //Ensures the scheduler always passes this block the right number of samples

                //Just catch, don't produce or consume.
                //memcpy(oo_noise, ii_noise, sizeof(gr_complex)*lenght_access_code);
                //consume (0,lenght_access_code); //consume the samples we set to correlate with
                //produce(0,lenght_access_code);
              }
          }
        }else{ //If we have access code
          if(have_corr==false){ //We have access code and we need to find the correlation
              for(int i=0; i<=(noutput_items-lenght_access_code); i++){ //Got o each "Window" in output items -> For 5 window, and 10 items, I can do 10-5+1 times. 
              correlation_filter->filter(lenght_access_code, &ii_signal[i], d_corr); //Calculate the correlation of input with the noise. 1ºItems to produce. 2ºInpuct vector to be filtered. 3ºresult of filter opertation.  The 2º starts in the "window" that I am.
              correlation_filter->filter(lenght_access_code, &ii_signal[i], corr); //Calculate the correlation of input with the noise. 1ºItems to produce. 2ºInpuct vector to be filtered. 3ºresult of filter opertation.  The 2º starts in the "window" that I am.
              
              volk_32fc_magnitude_squared_32f(&d_corr_mag[0], d_corr, lenght_access_code); //magnitude squared of the correlation
              volk_32fc_magnitude_squared_32f(&d_corr_mag[0], corr, lenght_access_code); //magnitude squared of the correlation

              detection = 0;
              for (int j = 0; j < lenght_access_code; j++) { //Sum of all magnitude squared values
                detection += d_corr_mag[j];
              }
              detection /= static_cast<float>(lenght_access_code);
              detection *= d_pfa;

              printf("DET: %f\n",detection);
              //If found the correlation then set have_corr to true
              /*if(detection>2500){ //this is for AUTO_CORR FG
                printf("MAI:%f\n",detection);
              }*/
              /*if(detection>330){ //this is for CORR_AND_DELAY_SIMULATION FG
                printf("MAI:%f\n",detection);
              }*/
            //bypass the signal
            }
            //Didn't find correlation, but, for now only passes to correlate the next samples
            //NOISE
            memcpy(oo_noise, ii_noise, sizeof(gr_complex)*noutput_items);
            consume (0,noutput_items);
            produce(0,noutput_items);

            //SIGNAL
            memcpy(oo_signal, ii_signal, sizeof(gr_complex)*noutput_items);
            consume (1,noutput_items);
            produce(1,noutput_items);
            memcpy(corr, d_corr, sizeof(gr_complex)*noutput_items);
            produce(2,noutput_items);

          }else{ //Correlation found, so passing streams with correct delay synchronize them
          }
        }
        //memcpy(oo_noise, ii_noise, sizeof(gr_complex)*noutput_items);
        //memcpy(oo_signal, ii_signal, sizeof(gr_complex)*noutput_items);
        //consume (0,noutput_items);
        //consume (1,noutput_items);

        //produce(0,noutput_items);
        //produce(1,noutput_items);

     /* consume (0,noutput_items);
        consume (1,noutput_items);
        produce(0,noutput_items);
        produce(1,noutput_items);*/
      }
    }
  } /* namespace correlate_and_delay */
} /* namespace gr */

