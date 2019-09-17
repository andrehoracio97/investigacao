#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/gr-testing_single_scramble/lib
export PATH=/home/andre/investigacao/gr-testing_single_scramble/build/lib:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/gr-testing_single_scramble/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-testing_single_scramble 
