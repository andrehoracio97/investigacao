#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/OOT/gr-scrambler_packets_same_seed/lib
export PATH=/home/andre/investigacao/OOT/gr-scrambler_packets_same_seed/build/lib:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/OOT/gr-scrambler_packets_same_seed/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-scrambler_packets_same_seed 
