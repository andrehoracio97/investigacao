#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/gr-correlate_and_delay/lib
export PATH=/home/andre/investigacao/gr-correlate_and_delay/build/lib:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/gr-correlate_and_delay/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-correlate_and_delay 
