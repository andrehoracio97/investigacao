#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/it/investigacao/OOT/gr-insert_vec_cpp/lib
export PATH=/home/it/investigacao/OOT/gr-insert_vec_cpp/b/lib:$PATH
export LD_LIBRARY_PATH=/home/it/investigacao/OOT/gr-insert_vec_cpp/b/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-insert_vec_cpp 
