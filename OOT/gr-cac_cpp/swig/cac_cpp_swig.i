/* -*- c++ -*- */

#define CAC_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "cac_cpp_swig_doc.i"

%{
#include "cac_cpp/cac_bb.h"
%}


%include "cac_cpp/cac_bb.h"
GR_SWIG_BLOCK_MAGIC2(cac_cpp, cac_bb);
