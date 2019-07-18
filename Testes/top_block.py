#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jul 18 17:34:26 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt, QtCore
from extremly_simple_packet_encoder_and_soft_modulation import extremly_simple_packet_encoder_and_soft_modulation  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, frame_size=30, puncpat='11'):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.frame_size = frame_size
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.H = H = fec.ldpc_H_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 2)
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 50
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 34
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps_channel_model = taps_channel_model = [1.0]
        self.samp_rate = samp_rate = 250000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.rate = rate = 2
        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.preambulo_documentacao = preambulo_documentacao = "1010010011110010"
        self.polys = polys = [109, 79]
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise_volt = noise_volt = 0.0000
        self.k = k = 7
        self.frequencia_usrp = frequencia_usrp = 435000000
        self.freq_offset = freq_offset = 0
        self.excess_bw = excess_bw = 0.35
        self.eq_gain = eq_gain = 0.01


        self.encoder = encoder = fec.ldpc_par_mtrx_encoder_make_H(H)
        self.documentacao = documentacao = "1010010011110010"


        self.decoder = decoder = fec.ldpc_bit_flip_decoder.make(H.get_base_sptr(), 100)
        self.barker_code_13_2vezes = barker_code_13_2vezes = "11111001101011111100110101"
        self.barker_code_13 = barker_code_13 = "1111100110101"
        self.arity = arity = 4
        self.ac_site = ac_site = "010110011011101100010101011111101001001110001011010001101010001"
        self.ac = ac = "1010110011011101101001001110001011110010100011000010000011111100"
        self.G = G = fec.ldpc_G_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0058_gen_matrix.alist")
        self.AC_documentacao_2_DEFAULT = AC_documentacao_2_DEFAULT = "1010110011011101101001001110001011110010100011000010000011111100"
        self.AC_documentacao = AC_documentacao = "010101010111000100"

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, 'Time: BW', "slider", float)
        self.top_grid_layout.addWidget(self._timing_loop_bw_win, 6, 3, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_range = Range(0, 10000000, 1, 250000, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, 'samp_rate', "counter_slider", int)
        self.top_grid_layout.addWidget(self._samp_rate_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.28/100.0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Phase: Bandwidth', "dial", float)
        self.top_grid_layout.addWidget(self._phase_bw_win, 6, 1, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._noise_volt_range = Range(0, 1, 0.01, 0.0000, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, 'Noise Voltage', "slider", float)
        self.top_grid_layout.addWidget(self._noise_volt_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_offset_range = Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 3, 2, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._eq_gain_range = Range(0.0, 0.1, 0.001, 0.01, 200)
        self._eq_gain_win = RangeWidget(self._eq_gain_range, self.set_eq_gain, 'Equalizer: rate (Gain)', "slider", float)
        self.top_grid_layout.addWidget(self._eq_gain_win, 6, 2, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_range_0_1_range = Range(0, 73, 1, 50, 200)
        self._variable_qtgui_range_0_1_win = RangeWidget(self._variable_qtgui_range_0_1_range, self.set_variable_qtgui_range_0_1, 'Gain_RX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_1_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_range_0_range = Range(0, 90, 1, 34, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Gain_TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._time_offset_range = Range(0.999, 1.001, 0.0001, 1.00, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 3, 3, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fec_extended_encoder_1 = fec.extended_encoder(encoder_obj_list=encoder, threading='capillary', puncpat=puncpat)
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=decoder, threading= None, ann=None, puncpat=puncpat, integration_period=10000)
        self.extremly_simple_packet_encoder_and_soft_modulation_0 = extremly_simple_packet_encoder_and_soft_modulation(
            access_code=AC_documentacao_2_DEFAULT,
            eq_gain=0.01,
            freq_offset=0,
            noise_volt=0.0000,
            payload_length=0,
            phase_bw=6.28/100.0,
            preambulo="",
            samp_rate=samp_rate,
            threshold=-1,
            timing_loop_bw=6.28/100.0,
        )
        self.top_grid_layout.addWidget(self.extremly_simple_packet_encoder_and_soft_modulation_0)
        self.digital_map_bb_0 = digital.map_bb((-1, 1))
        self.blocks_throttle_0_1_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, '', True, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, "", True, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0_0_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/video.mpg', False)
        self.blocks_file_source_0_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_1_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/transmitido/depois.mpg', False)
        self.blocks_file_sink_0_0_1_0.set_unbuffered(False)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.blocks_file_source_0_0_0_0, 0), (self.blocks_throttle_0_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0_0_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.fec_extended_encoder_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.extremly_simple_packet_encoder_and_soft_modulation_0, 0))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.extremly_simple_packet_encoder_and_soft_modulation_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.fec_extended_encoder_1, 0), (self.blocks_repack_bits_bb_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_size(self, frame_size):
        self.frame_size = frame_size

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_H(self):
        return self.H

    def set_H(self, H):
        self.H = H

    def get_variable_qtgui_range_0_1(self):
        return self.variable_qtgui_range_0_1

    def set_variable_qtgui_range_0_1(self, variable_qtgui_range_0_1):
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps_channel_model(self):
        return self.taps_channel_model

    def set_taps_channel_model(self, taps_channel_model):
        self.taps_channel_model = taps_channel_model

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.extremly_simple_packet_encoder_and_soft_modulation_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_preambulo_documentacao(self):
        return self.preambulo_documentacao

    def set_preambulo_documentacao(self, preambulo_documentacao):
        self.preambulo_documentacao = preambulo_documentacao

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_frequencia_usrp(self):
        return self.frequencia_usrp

    def set_frequencia_usrp(self, frequencia_usrp):
        self.frequencia_usrp = frequencia_usrp

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain

    def get_encoder(self):
        return self.encoder

    def set_encoder(self, encoder):
        self.encoder = encoder

    def get_documentacao(self):
        return self.documentacao

    def set_documentacao(self, documentacao):
        self.documentacao = documentacao

    def get_decoder(self):
        return self.decoder

    def set_decoder(self, decoder):
        self.decoder = decoder

    def get_barker_code_13_2vezes(self):
        return self.barker_code_13_2vezes

    def set_barker_code_13_2vezes(self, barker_code_13_2vezes):
        self.barker_code_13_2vezes = barker_code_13_2vezes

    def get_barker_code_13(self):
        return self.barker_code_13

    def set_barker_code_13(self, barker_code_13):
        self.barker_code_13 = barker_code_13

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity

    def get_ac_site(self):
        return self.ac_site

    def set_ac_site(self, ac_site):
        self.ac_site = ac_site

    def get_ac(self):
        return self.ac

    def set_ac(self, ac):
        self.ac = ac

    def get_G(self):
        return self.G

    def set_G(self, G):
        self.G = G

    def get_AC_documentacao_2_DEFAULT(self):
        return self.AC_documentacao_2_DEFAULT

    def set_AC_documentacao_2_DEFAULT(self, AC_documentacao_2_DEFAULT):
        self.AC_documentacao_2_DEFAULT = AC_documentacao_2_DEFAULT
        self.extremly_simple_packet_encoder_and_soft_modulation_0.set_access_code(self.AC_documentacao_2_DEFAULT)

    def get_AC_documentacao(self):
        return self.AC_documentacao

    def set_AC_documentacao(self, AC_documentacao):
        self.AC_documentacao = AC_documentacao


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--frame-size", dest="frame_size", type="intx", default=30,
        help="Set Frame Size [default=%default]")
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(frame_size=options.frame_size, puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
