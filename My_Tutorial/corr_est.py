#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tutorial
# Author: Andre Silva
# GNU Radio version: 3.7.13.5
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import insert_vec_cpp
import pmt
import scrambler_packets_same_seed
import time


class corr_est(gr.top_block):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Tutorial")

        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.eb = eb = 0.22
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.rxmod = rxmod = digital.generic_mod(pld_const, False, sps, True, eb, False, False)

        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(sps, sps, 1.0, eb, 11*sps)

        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.nfilts = nfilts = 32
        self.mark_delays = mark_delays = [0, 0, 34, 56, 87, 119]
        self.k = k = 7
        self.ac_hex = ac_hex = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 38
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 50

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.samp_rate = samp_rate = samp_rate_array_MCR[3]

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)


        self.rx_psf_taps = rx_psf_taps = firdes.root_raised_cosine(nfilts, sps*nfilts, 1.0, eb, 11*sps*nfilts)



        self.pld_enc = pld_enc = map( (lambda a: fec.cc_encoder_make(440, k, rate, (polys), 0, fec.CC_TERMINATED, False)), range(0,4) );


        self.pld_dec = pld_dec = map( (lambda a: fec.cc_decoder.make(440, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)), range(0,8) );
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), (ac_hex), ([1]))
        self.mark_delay = mark_delay = mark_delays[sps]
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.filt_delay = filt_delay = 1+(len(rrc_taps)-1)/2
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("serial=F5EAC0", MCR)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(frequencia_usrp, 0)
        self.uhd_usrp_source_0.set_gain(variable_qtgui_range_0_1, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 0)
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
        self.scrambler_packets_same_seed_scramble_packetize_0 = scrambler_packets_same_seed.scramble_packetize(0x8A, 0x7F, 7, 440)
        self.scrambler_packets_same_seed_descramble_packetize_0 = scrambler_packets_same_seed.descramble_packetize(0x8A, 0x7F, 7, 440)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, (rrc_taps))
        self.interp_fir_filter_xxx_0.declare_sample_delay(filt_delay)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.fec_extended_decoder_0_0_1_0_1_0 = fec.extended_decoder(decoder_obj_list=pld_dec, threading='capillary', ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, 6.28/400.0, (rx_psf_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_map_bb_0_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(6.28/100.0, pld_const.arity(), False)
        self.digital_correlate_access_code_xx_ts_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          1, 'packet_len')
        self.digital_corr_est_cc_0 = digital.corr_est_cc((modulated_sync_word), sps, mark_delay, 0.90)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(pld_const)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, 0.01, 2)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'TAG DEBUG', ""); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_mux_0_1_0 = blocks.stream_mux(gr.sizeof_char*1, (96, 896))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (892, 4))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(1, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(pld_const.bits_per_symbol(), 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_keep_m_in_n_0_0_2_0 = blocks.keep_m_in_n(gr.sizeof_char, 892, 896, 0)
        self.blocks_file_source_0_0_1_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/videofhd.mpg', False)
        self.blocks_file_source_0_0_1_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.mpeg', False)
        self.blocks_file_sink_0_0_0_2.set_unbuffered(False)
        self.blocks_char_to_float_0_2_0_0 = blocks.char_to_float(1, 1)
        self.acode_1104 = blocks.vector_source_b([0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0], True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.acode_1104, 0), (self.blocks_stream_mux_0_1_0, 0))
        self.connect((self.blocks_char_to_float_0_2_0_0, 0), (self.fec_extended_decoder_0_0_1_0_1_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_2_0, 0), (self.digital_map_bb_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0_0_0_2, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.scrambler_packets_same_seed_scramble_packetize_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_stream_mux_0_1_0, 1))
        self.connect((self.blocks_stream_mux_0_1_0, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0, 0), (self.blocks_keep_m_in_n_0_0_2_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.fec_extended_decoder_0_0_1_0_1_0, 0), (self.scrambler_packets_same_seed_descramble_packetize_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.scrambler_packets_same_seed_descramble_packetize_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.scrambler_packets_same_seed_scramble_packetize_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_corr_est_cc_0, 0))

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_mark_delay(self.mark_delays[self.sps])
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))

    def get_samp_rate_array_MCR(self):
        return self.samp_rate_array_MCR

    def set_samp_rate_array_MCR(self, samp_rate_array_MCR):
        self.samp_rate_array_MCR = samp_rate_array_MCR
        self.set_samp_rate(self.samp_rate_array_MCR[3])

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.set_filt_delay(1+(len(self.rrc_taps)-1)/2)
        self.interp_fir_filter_xxx_0.set_taps((self.rrc_taps))

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

    def get_mark_delays(self):
        return self.mark_delays

    def set_mark_delays(self, mark_delays):
        self.mark_delays = mark_delays
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_ac_hex(self):
        return self.ac_hex

    def set_ac_hex(self, ac_hex):
        self.ac_hex = ac_hex

    def get_variable_qtgui_range_0_1(self):
        return self.variable_qtgui_range_0_1

    def set_variable_qtgui_range_0_1(self, variable_qtgui_range_0_1):
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1
        self.uhd_usrp_source_0.set_gain(self.variable_qtgui_range_0_1, 0)


    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.uhd_usrp_sink_0_0.set_gain(self.variable_qtgui_range_0, 0)


    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_rx_psf_taps(self):
        return self.rx_psf_taps

    def set_rx_psf_taps(self, rx_psf_taps):
        self.rx_psf_taps = rx_psf_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rx_psf_taps))

    def get_pld_enc(self):
        return self.pld_enc

    def set_pld_enc(self, pld_enc):
        self.pld_enc = pld_enc

    def get_pld_dec(self):
        return self.pld_dec

    def set_pld_dec(self, pld_dec):
        self.pld_dec = pld_dec

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_mark_delay(self):
        return self.mark_delay

    def set_mark_delay(self, mark_delay):
        self.mark_delay = mark_delay
        self.digital_corr_est_cc_0.set_mark_delay(self.mark_delay)

    def get_frequencia_usrp(self):
        return self.frequencia_usrp

    def set_frequencia_usrp(self, frequencia_usrp):
        self.frequencia_usrp = frequencia_usrp
        self.uhd_usrp_source_0.set_center_freq(self.frequencia_usrp, 0)
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


def main(top_block_cls=corr_est, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
