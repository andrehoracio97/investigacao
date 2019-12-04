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


#include <gnuradio/io_signature.h>
#include <gnuradio/math.h>
#include <volk/volk.h>
#include <boost/format.hpp>
#include <boost/math/special_functions/round.hpp>

#include <iostream>
#include <deque>



namespace gr {
  namespace correlate_and_delay {

    corr_and_delay::sptr
    corr_and_delay::make(int number_bits, int interval, float threshold, float sps)
    {
      return gnuradio::get_initial_sptr
        (new corr_and_delay_impl(number_bits, interval, threshold, sps));
    }

    corr_and_delay_impl::corr_and_delay_impl(int number_bits, int interval, float threshold, float sps)
      : gr::block("corr_and_delay",
              gr::io_signature::make(2, 2, sizeof(gr_complex)),
              gr::io_signature::make(2, 3, sizeof(gr_complex))),
      lenght_access_code(number_bits),
      access_code(),
      detection(0),
      have_corr(false),
      d_sps(sps),
      d_src_id(pmt::intern(alias())),
      delay_needed(0),
      print_once(false),
      have_access_code(false)
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
      /*gr_complex *corr;
         corr=d_corr;*/


      if(have_access_code==false){ //If access code still not catched
        if(noutput_items>=lenght_access_code){ //Make sure we have number of samples enough to create fft filte of nois
          //BEFORE
          /*for (int i = access_code.size(); i < lenght_access_code; i++){
              access_code.push_back(ii_noise[i]);
              fifo.push_back(ii_noise[i]);

              if (i==(lenght_access_code-1)){ //All the access code catched
                printf("Access Code Caught\n");
                have_access_code=true;

                //conjugate and reverse
                for (int j = 0; j < access_code.size(); j++) { //doing the conjugate
                  access_code[j] = conj(access_code[j]);
                }
                std::reverse(access_code.begin(), access_code.end()); //doing the reverse

                correlation_filter = new kernel::fft_filter_ccc(1, access_code); //create correlation filter from the access code --1=decimation then the taps
                int nsamples;
                nsamples = correlation_filter->set_taps(access_code); //The filter function expects that the input signal is a multiple of d_nsamples in the class that's computed internally to be as fast as possible. The function set_taps will return the value of nsamples that can be used externally to check this boundary
                set_output_multiple(nsamples); //Ensures the scheduler always passes this block the right number of samples
                
                set_history(lenght_access_code+1);
                
                consume (0,lenght_access_code); //consume the samples we set to correlate with
                //produce(0,lenght_access_code); //Not producing because it will be delayed
              }
          }*/
          //NOW
          access_code.resize(lenght_access_code);
          memcpy(&access_code[0],&ii_noise[0],lenght_access_code*sizeof(gr_complex));
          
          fifo.resize(lenght_access_code);
          memcpy(&fifo[0],&ii_noise[0],lenght_access_code*sizeof(gr_complex));

          for (int j = 0; j < access_code.size(); j++) { //doing the conjugate
            access_code[j] = conj(access_code[j]);
          }
          std::reverse(access_code.begin(), access_code.end()); //doing the reverse
          
          correlation_filter = new kernel::fft_filter_ccc(1, access_code); //create correlation filter from the access code --1=decimation then the taps
          
          int nsamples;
          nsamples = correlation_filter->set_taps(access_code); //The filter function expects that the input signal is a multiple of d_nsamples in the class that's computed internally to be as fast as possible. The function set_taps will return the value of nsamples that can be used externally to check this boundary
          set_output_multiple(nsamples); //Ensures the scheduler always passes this block the right number of samples
          
          set_history(lenght_access_code+1);

          printf("Access Code Caught\n");
          have_access_code=true;

          consume (0,lenght_access_code); //consume the samples we set to correlate with - TO TAKE OUT THIS CONSUME I NEED TO NOT INTRODUCE THE ACESSCODE ON FIFO.
        }
        return 0;
      }else if(have_corr==false){ //If we have access code
          unsigned int hist_len = history() - 1;
          correlation_filter->filter(noutput_items, &ii_signal[hist_len], corr); //Calculate the correlation of input with the noise. 1ºItems to produce. 2ºInpuct vector to be filtered. 3ºresult of filter opertation.  The 2º starts in the "window" that I am.
          volk_32fc_magnitude_squared_32f(&d_corr_mag[0], corr, noutput_items); //magnitude squared of the correlation

          float detection = 0; 
          for (int j = 0; j < noutput_items; j++) { //Sum of all magnitude squared values
            detection += d_corr_mag[j];
          }
          detection /= static_cast<float>(noutput_items);
          detection *= d_pfa;

          //printf("DET: %f\n", detection);
          int isps = (int)(d_sps + 0.5f);
          int i = 0;
          while (i < noutput_items) {
            // Look for the correlator output to cross the threshold.
            // Sum power over two consecutive symbols in case we're offset
            // in time. If off by 1/2 a symbol, the peak of any one point
            // is much lower.
            float corr_mag = d_corr_mag[i] + d_corr_mag[i + 1];
            if (corr_mag <= 4 * detection) {
                i++;
                continue;
            }

            // Go to (just past) the current correlator output peak
            while ((i < (noutput_items - 1)) && (d_corr_mag[i] < d_corr_mag[i + 1])) {
                i++;
            }
            add_item_tag(1,
                           nitems_written(1) + i,
                           pmt::intern("correlation"),
                           pmt::from_double(d_corr_mag[i]),
                           d_src_id);
            add_item_tag(2,
                         nitems_written(2) + i,
                         pmt::intern("correlation"),
                         pmt::from_double(d_corr_mag[i]),
                         d_src_id);
              
            printf("CORR SAMPLE FOUND -SAMPLE %d\n",nitems_written(1) + i);

            have_corr=true;
            delay_needed=i;
            printf("DELAY in this STREAM in sample: %d\n",delay_needed);
            break;
            i += isps;
          }

          if(have_corr==true){//if occur correlation than sync: -save all noise, and starting from i producet the beguining of the noise       
            //delay_needed=i;

            printf("FOUNF CORR, SO DELAY NOISE with %d\n",delay_needed);  


            //BEFORE
          /*  for (int o = 0; o < delay_needed; o++){
              fifo.push_back(ii_noise[o]);
              oo_noise[o]=0;
            }

            for (int i = delay_needed; i <noutput_items ; i++){
              fifo.push_back(ii_noise[i]);
              oo_noise[i]=fifo.front();
              fifo.pop_front();
            }*/



            //NOW
            /*for (int o = 0; o < noutput_items; o++){
              fifo.push_back(ii_noise[o]);
            }*/
            int tam_temp=fifo.size();
            fifo.resize(fifo.size()+noutput_items);
            memcpy(&fifo[tam_temp],&ii_noise[0],noutput_items*sizeof(gr_complex));


            /*for (int o = 0; o < delay_needed; o++){
              oo_noise[o]=0;
            }*/
            memset(&oo_noise[0],0,delay_needed*sizeof(gr_complex));

            //HERE I have the FIFO VECTOR complete, so iniciate the CURCULAR BUFFER.
            d_writer = gr::make_buffer(3*fifo.size(), sizeof(gr_complex)); //create writter pointer 3 just to make sure, but 2 is maybe enough
            d_reader = gr::buffer_add_reader(d_writer, 0); //create reader pointer

            //Write everithing from fifo to buffer
            gr_complex* a = (gr_complex*)d_writer->write_pointer(); 
            memcpy(a,&fifo[0],fifo.size()*sizeof(gr_complex));
            d_writer->update_write_pointer(fifo.size()); //update writter pointer

            //First take out from the buffer to increase the space available
            memcpy(&oo_noise[delay_needed],d_reader->read_pointer(),(noutput_items-delay_needed) * sizeof(gr_complex));
            d_reader->update_read_pointer((noutput_items-delay_needed));
            
            //in noise
            consume(0,noutput_items);
            produce(0,noutput_items);

            //in signal
            memcpy(oo_signal, &ii_signal[0], sizeof(gr_complex)*noutput_items);
            consume(1,noutput_items);
            produce(1,noutput_items);

            //in corr
            produce(2,noutput_items);

          }else{//if not encontered correlation store the noise and try again.
            //In noise we store and consume and produce

            /*for (int o = 0; o < noutput_items; o++){  //AFTER CHANGE TO RESIZE AND MEMCPY
              fifo.push_back(ii_noise[o]);
            }*/
            int tam_temp=fifo.size();
            fifo.resize(fifo.size()+noutput_items);
            memcpy(&fifo[tam_temp],&ii_noise[0],noutput_items*sizeof(gr_complex));

            //In noise
            memcpy(oo_noise, &ii_noise[0], sizeof(gr_complex)*noutput_items);
            consume(0,noutput_items);
            produce(0,noutput_items);

            //In signal
            memcpy(oo_signal, &ii_signal[0], sizeof(gr_complex)*noutput_items);
            consume(1,noutput_items);
            produce(1,noutput_items);

            //in corr
            produce(2,noutput_items);
          }
        return 0;
      }else{ //Correlation found, just pass the streams
        /*for (int i = 0; i < noutput_items; i++){
          fifo.push_back(ii_noise[i]);
        }

        for (int i = 0; i < noutput_items; i++){
          oo_noise[i]=fifo.front();
          fifo.pop_front();
        }*/


        //WRITE on the free space
        gr_complex* p = (gr_complex*)d_writer->write_pointer(); 
        memcpy(p,&ii_noise[0],(noutput_items)*sizeof(gr_complex));
        d_writer->update_write_pointer(noutput_items); //update writter pointer
        
        //READ to free space
        memcpy(&oo_noise[0],d_reader->read_pointer(),noutput_items * sizeof(gr_complex));
        d_reader->update_read_pointer(noutput_items);






        consume(0,noutput_items);
        produce(0,noutput_items);


        memcpy(oo_signal, &ii_signal[0], sizeof(gr_complex)*noutput_items);
        consume(1,noutput_items);
        produce(1,noutput_items);

        for (int o = 0; o < noutput_items; ++o){
              corr[o]=0;
        }
        produce(2,noutput_items);
        return 0;
      }
    }
  } /* namespace correlate_and_delay */
} /* namespace gr */

