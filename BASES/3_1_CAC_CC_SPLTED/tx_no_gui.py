#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx No Gui
# Author: andresilva
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import insert_vec_cpp
import pmt
import random
import time


class tx_no_gui(gr.top_block):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Tx No Gui")

        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.vector = vector = [int(random.random()*4) for i in range(49600)]
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 50
        self.samp_rate = samp_rate = samp_rate_array_MCR[1]


        self.pld_enc = pld_enc = map( (lambda a: fec.cc_encoder_make(440, k, rate, (polys), 0, fec.CC_TERMINATED, False)), range(0,8) );
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("serial=F5EAE1", MCR)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_center_freq(frequencia_usrp, 0)
        self.uhd_usrp_sink_0_0.set_gain(variable_qtgui_range_0, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self.insert_vec_cpp_new_vec_0 = insert_vec_cpp.new_vec((vector))
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.digital_map_bb_1_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(4)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_stream_to_tagged_stream_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 992, "packet_len")
        self.blocks_stream_mux_0_1_0 = blocks.stream_mux(gr.sizeof_char*1, (96, 896))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (892, 4))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_0 = blocks.repack_bits_bb(1, 2, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_file_source_0_0_1_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/video_lion.mpeg', False)
        self.blocks_file_source_0_0_1_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.acode_1104 = blocks.vector_source_b([0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0], True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.acode_1104, 0), (self.blocks_stream_mux_0_1_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0, 0), (self.insert_vec_cpp_new_vec_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_stream_mux_0_1_0, 1))
        self.connect((self.blocks_stream_mux_0_1_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_map_bb_1_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.insert_vec_cpp_new_vec_0, 0), (self.digital_map_bb_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_rrc_taps))

    def get_taps_per_filt(self):
        return self.taps_per_filt

    def set_taps_per_filt(self, taps_per_filt):
        self.taps_per_filt = taps_per_filt
        self.set_filt_delay(1+(self.taps_per_filt-1)/2)

    def get_samp_rate_array_MCR(self):
        return self.samp_rate_array_MCR

    def set_samp_rate_array_MCR(self, samp_rate_array_MCR):
        self.samp_rate_array_MCR = samp_rate_array_MCR
        self.set_samp_rate(self.samp_rate_array_MCR[1])

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

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.uhd_usrp_sink_0_0.set_gain(self.variable_qtgui_range_0, 0)


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

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
        self.uhd_usrp_sink_0_0.set_center_freq(self.frequencia_usrp, 0)

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay

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


def main(top_block_cls=tx_no_gui, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
