#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Eve Dec
# Author: andresilva
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class eve_dec(gr.top_block):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Eve Dec")

        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.samp_rate = samp_rate = 10000000


        self.pld_dec = pld_dec = map( (lambda a: fec.cc_decoder.make(896, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)), range(0,4) );

        ##################################################
        # Blocks
        ##################################################
        self.fec_extended_decoder_0_0_1_0_1_0_0 = fec.extended_decoder(decoder_obj_list=pld_dec, threading='capillary', ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_map_bb_0_0_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_repack_bits_bb_0_0_0_1_0_0 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_1_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/ELI/1/EVE_55_8000_BRUTO.txt', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/ELI/1/EVE_55_8000.txt', False)
        self.blocks_file_sink_0_0_0_0_2.set_unbuffered(True)
        self.blocks_char_to_float_0_2_0_0_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_2_0_0_0, 0), (self.fec_extended_decoder_0_0_1_0_1_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_repack_bits_bb_0_0_0_1_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0, 0), (self.blocks_file_sink_0_0_0_0_2, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_map_bb_0_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0_0_0, 0))
        self.connect((self.fec_extended_decoder_0_0_1_0_1_0_0, 0), (self.blocks_repack_bits_bb_0_0_0_1_0, 0))

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pld_dec(self):
        return self.pld_dec

    def set_pld_dec(self, pld_dec):
        self.pld_dec = pld_dec


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=eve_dec, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
