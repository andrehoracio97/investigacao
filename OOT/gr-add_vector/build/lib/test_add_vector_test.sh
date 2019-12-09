#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/gr-add_vector/lib
export PATH=/home/andre/investigacao/gr-add_vector/build/lib:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/gr-add_vector/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-add_vector 
