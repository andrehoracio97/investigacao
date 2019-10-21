/* -*- c++ -*- */

#define CORRELATE_AND_DELAY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "correlate_and_delay_swig_doc.i"

%{
#include "correlate_and_delay/corr_and_delay.h"
%}


%include "correlate_and_delay/corr_and_delay.h"
GR_SWIG_BLOCK_MAGIC2(correlate_and_delay, corr_and_delay);
