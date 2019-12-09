#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/OOT/gr-insert_vec_cpp/lib
export PATH=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/lib:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/OOT/gr-insert_vec_cpp/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-insert_vec_cpp 
