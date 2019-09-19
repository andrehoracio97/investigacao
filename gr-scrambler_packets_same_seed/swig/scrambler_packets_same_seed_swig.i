/* -*- c++ -*- */

#define SCRAMBLER_PACKETS_SAME_SEED_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "scrambler_packets_same_seed_swig_doc.i"

%{
#include "scrambler_packets_same_seed/scramble_packetize.h"
#include "scrambler_packets_same_seed/descramble_packetize.h"
%}


%include "scrambler_packets_same_seed/scramble_packetize.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_packets_same_seed, scramble_packetize);
%include "scrambler_packets_same_seed/descramble_packetize.h"
GR_SWIG_BLOCK_MAGIC2(scrambler_packets_same_seed, descramble_packetize);
