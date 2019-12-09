/* -*- c++ -*- */

#define SCRAMBLER_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "scrambler_cpp_swig_doc.i"

%{
#include "scrambler_cpp/custom_scrambler.h"
#include "scrambler_cpp/custom_descrambler.h"
#include "scrambler_cpp/additive_scrambler.h"
#include "scrambler_cpp/additive_descrambler.h"
%}


%include "scrambler_cpp/custom_scrambler.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_cpp, custom_scrambler);
%include "scrambler_cpp/custom_descrambler.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_cpp, custom_descrambler);
%include "scrambler_cpp/additive_scrambler.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_cpp, additive_scrambler);
%include "scrambler_cpp/additive_descrambler.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_cpp, additive_descrambler);
