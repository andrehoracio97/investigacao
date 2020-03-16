/* -*- c++ -*- */

#define PUNCTURE64_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "puncture64_cpp_swig_doc.i"

%{
#include "puncture64_cpp/puncture64.h"
#include "puncture64_cpp/depuncture64.h"
%}


%include "puncture64_cpp/puncture64.h"
GR_SWIG_BLOCK_MAGIC2(puncture64_cpp, puncture64);
%include "puncture64_cpp/depuncture64.h"
GR_SWIG_BLOCK_MAGIC2(puncture64_cpp, depuncture64);
