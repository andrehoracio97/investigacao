/* -*- c++ -*- */

#define TESTING_SINGLE_SCRAMBLE_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "testing_single_scramble_swig_doc.i"

%{
#include "testing_single_scramble/sc.h"
#include "testing_single_scramble/dsc.h"
%}


%include "testing_single_scramble/sc.h"
GR_SWIG_BLOCK_MAGIC2(testing_single_scramble, sc);
%include "testing_single_scramble/dsc.h"
GR_SWIG_BLOCK_MAGIC2(testing_single_scramble, dsc);
