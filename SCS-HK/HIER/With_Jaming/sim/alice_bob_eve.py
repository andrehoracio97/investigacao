#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Alice Bob Eve
# Author: andresilva
# GNU Radio version: 3.7.13.5
##################################################

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

from PyQt4 import Qt
from bob_hier_sim import bob_hier_sim  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import adapt
import pmt
import random
import scrambler_cpp
import sip
from gnuradio import qtgui


class alice_bob_eve(gr.top_block, Qt.QWidget):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Alice Bob Eve")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Alice Bob Eve")
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

        self.settings = Qt.QSettings("GNU Radio", "alice_bob_eve")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22
        self.H = H = fec.ldpc_H_matrix('/usr/local/share/gnuradio/fec/ldpc/n_1100_k_0442_gap_24.alist', 24)
        self.vector = vector = [int(random.random()*4) for i in range(49600)]

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)

        self.samp_rate = samp_rate = samp_rate_array_MCR[15]


        self.pld_enc = pld_enc = map((lambda a: fec.ldpc_par_mtrx_encoder_make_H(H)), range(0,4))
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self.scrambler_cpp_additive_scrambler_0 = scrambler_cpp.additive_scrambler(0x8A, 0x7F, 7, 440-32)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	100*2, #size
        	samp_rate, #samp_rate
        	'Rx Data EVE', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1, 256)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'packet_length_tag_key')
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_0_win, 3, 3, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	100*2, #size
        	samp_rate, #samp_rate
        	'Rx Data', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 256)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'packet_length_tag_key')
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 2, 3, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"RX Treated EVE", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_1.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_1_win, 3, 2, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"RX Treated", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.interp_fir_filter_xxx_1 = filter.interp_fir_filter_ccc(4, ([1,0,0,0]))
        self.interp_fir_filter_xxx_1.declare_sample_delay(0)
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.bob_hier_sim_0_0 = bob_hier_sim(
            samp_rate=samp_rate,
        )
        self.bob_hier_sim_0 = bob_hier_sim(
            samp_rate=samp_rate,
        )
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_mux_0_1_0_0 = blocks.stream_mux(gr.sizeof_char*1, (96, 1104))
        self.blocks_stream_mux_0_0_0 = blocks.stream_mux(gr.sizeof_char*1, (1100, 4))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (440, 2))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_0 = blocks.repack_bits_bb(1, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_file_source_0_0_1_0_1 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/book.txt', False)
        self.blocks_file_source_0_0_1_0_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0_0_2_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0_0_0_0_2_0.set_unbuffered(False)
        self.blocks_file_sink_0_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0_0_0_0_2.set_unbuffered(False)
        self.blocks_char_to_float_1_0_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, -5)
        self.adapt_lms_filter_xx_0 = adapt.lms_filter_cc(True, 32, 0.0001, 0, 1, True, False, False)
        self.acode_1104_0 = blocks.vector_source_b([0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0], True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.acode_1104_0, 0), (self.blocks_stream_mux_0_1_0_0, 0))
        self.connect((self.adapt_lms_filter_xx_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.adapt_lms_filter_xx_0, 1), (self.bob_hier_sim_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.interp_fir_filter_xxx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.adapt_lms_filter_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.bob_hier_sim_0_0, 0))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_char_to_float_1_0_1_0, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0_1, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.scrambler_cpp_additive_scrambler_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.blocks_stream_mux_0_1_0_0, 1))
        self.connect((self.blocks_stream_mux_0_1_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0_0, 1))
        self.connect((self.bob_hier_sim_0, 1), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.bob_hier_sim_0, 1), (self.blocks_file_sink_0_0_0_0_2, 0))
        self.connect((self.bob_hier_sim_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))
        self.connect((self.bob_hier_sim_0_0, 1), (self.blocks_char_to_float_1_0_1_0, 0))
        self.connect((self.bob_hier_sim_0_0, 1), (self.blocks_file_sink_0_0_0_0_2_0, 0))
        self.connect((self.bob_hier_sim_0_0, 0), (self.qtgui_const_sink_x_0_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.adapt_lms_filter_xx_0, 1))
        self.connect((self.interp_fir_filter_xxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.scrambler_cpp_additive_scrambler_0, 0), (self.blocks_stream_mux_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "alice_bob_eve")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_samp_rate_array_MCR(self):
        return self.samp_rate_array_MCR

    def set_samp_rate_array_MCR(self, samp_rate_array_MCR):
        self.samp_rate_array_MCR = samp_rate_array_MCR
        self.set_samp_rate(self.samp_rate_array_MCR[15])

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_H(self):
        return self.H

    def set_H(self, H):
        self.H = H

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_rrc_taps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.bob_hier_sim_0_0.set_samp_rate(self.samp_rate)
        self.bob_hier_sim_0.set_samp_rate(self.samp_rate)
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


def main(top_block_cls=alice_bob_eve, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
