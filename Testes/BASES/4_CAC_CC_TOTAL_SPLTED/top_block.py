#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
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


class top_block(gr.top_block):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.nfilts = nfilts = 32
        self.k = k = 7
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.samp_rate = samp_rate = samp_rate_array_MCR[0]


        self.pld_enc = pld_enc = map( (lambda a: fec.cc_encoder_make(440, k, rate, (polys), 0, fec.CC_TERMINATED, True)), range(0,8) );
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (892, 4))
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (440, 2))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0_0_1_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/video_lion.mpeg', False)
        self.blocks_file_source_0_0_1_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/TX_TEMP.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0_0_1_0_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0, 0))

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate_array_MCR(self):
        return self.samp_rate_array_MCR

    def set_samp_rate_array_MCR(self, samp_rate_array_MCR):
        self.samp_rate_array_MCR = samp_rate_array_MCR
        self.set_samp_rate(self.samp_rate_array_MCR[0])

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pld_enc(self):
        return self.pld_enc

    def set_pld_enc(self, pld_enc):
        self.pld_enc = pld_enc

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_frequencia_usrp(self):
        return self.frequencia_usrp

    def set_frequencia_usrp(self, frequencia_usrp):
        self.frequencia_usrp = frequencia_usrp

    def get_MCR(self):
        return self.MCR

    def set_MCR(self, MCR):
        self.MCR = MCR


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
