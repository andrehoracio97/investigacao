/* -*- c++ -*- */

#define INSERT_VEC_CPP_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "insert_vec_cpp_swig_doc.i"

%{
#include "insert_vec_cpp/new_vec.h"
%}


%include "insert_vec_cpp/new_vec.h"
GR_SWIG_BLOCK_MAGIC2(insert_vec_cpp, new_vec);
