/* -*- c++ -*- */

#define ADD_VECTOR_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "add_vector_swig_doc.i"

%{
#include "add_vector/add_vector_2_cpp.h"
%}
GR_SWIG_BLOCK_MAGIC2(add_vector, add_vector_cpp);
GR_SWIG_BLOCK_MAGIC2(add_vector, add_vector_2_cpp);
%include "add_vector/add_vector_2_cpp.h"
GR_SWIG_BLOCK_MAGIC2(add_vector, add_vector_2_cpp);
