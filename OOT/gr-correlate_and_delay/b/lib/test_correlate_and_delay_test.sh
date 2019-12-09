#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/it/investigacao/gr-correlate_and_delay/lib
export PATH=/home/it/investigacao/gr-correlate_and_delay/b/lib:$PATH
export LD_LIBRARY_PATH=/home/it/investigacao/gr-correlate_and_delay/b/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-correlate_and_delay 
