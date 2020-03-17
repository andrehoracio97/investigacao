/* -*- c++ -*- */

#define RS_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "rs_cpp_swig_doc.i"

%{
#include "rs_cpp/rs_encoder_custom.h"
#include "rs_cpp/rs_decoder_custom.h"
%}


%include "rs_cpp/rs_encoder_custom.h"
GR_SWIG_BLOCK_MAGIC2(rs_cpp, rs_encoder_custom);
%include "rs_cpp/rs_decoder_custom.h"
GR_SWIG_BLOCK_MAGIC2(rs_cpp, rs_decoder_custom);
