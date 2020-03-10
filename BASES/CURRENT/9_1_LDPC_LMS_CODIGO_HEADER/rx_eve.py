#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Rx Eve
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import cac_cpp
import scrambler_cpp
import sip
import sys
import time
from gnuradio import qtgui


class rx_eve(gr.top_block, Qt.QWidget):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Rx Eve")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Rx Eve")
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

        self.settings = Qt.QSettings("GNU Radio", "rx_eve")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952,200000]
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22
        self.H_dec = H_dec = fec.ldpc_H_matrix('/usr/local/share/gnuradio/fec/ldpc/n_1100_k_0442_gap_24.alist', 24)
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 48
        self.samp_rate = samp_rate = samp_rate_array_MCR[15]

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)



        self.pld_dec = pld_dec = map((lambda a: fec.ldpc_bit_flip_decoder.make(H_dec.get_base_sptr(), 50)), range(0,8))
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_1_range = Range(0, 73, 1, 48, 200)
        self._variable_qtgui_range_0_1_win = RangeWidget(self._variable_qtgui_range_0_1_range, self.set_variable_qtgui_range_0_1, 'Gain_RX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_1_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("serial=F5EB09", MCR)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0_0.set_center_freq(frequencia_usrp, 0)
        self.uhd_usrp_source_0_0.set_gain(variable_qtgui_range_0_1, 0)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 0)
        self.scrambler_cpp_additive_descrambler_0 = scrambler_cpp.additive_descrambler(0x8A, 0x7F, 7, 440-32)
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"After CAC", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(0, 1.5)

        self.qtgui_time_sink_x_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0.enable_grid(True)
        self.qtgui_time_sink_x_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)
        self.qtgui_time_sink_x_2_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2_0.disable_legend()

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
                self.qtgui_time_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_0_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX USRP", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
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
        	"RX Const", #name
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_1_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fec_extended_decoder_0_0_1_0_1_0_0 = fec.extended_decoder(decoder_obj_list=pld_dec, threading='capillary', ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28/100.0, (rx_rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_map_bb_0_0_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(pld_const.arity())
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(6.28/100.0, pld_const.arity(), False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(pld_const)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, 0.01, 2)
        self.cac_cpp_cac_bb_0 = cac_cpp.cac_bb(digital.packet_utils.default_access_code, 1)
        self.blocks_repack_bits_bb_0_0_0_1_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(pld_const.bits_per_symbol(), 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_keep_m_in_n_0_1_1_0 = blocks.keep_m_in_n(gr.sizeof_char, 440, 442, 0)
        self.blocks_keep_m_in_n_0_0_2_0_0 = blocks.keep_m_in_n(gr.sizeof_char, 1100, 1104, 0)
        self.blocks_file_sink_0_0_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0_0_0_0_0.set_unbuffered(False)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_2_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_2_0, 0))
        self.connect((self.blocks_char_to_float_0_2_0_0_0, 0), (self.fec_extended_decoder_0_0_1_0_1_0_0, 0))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_2_0_0, 0), (self.digital_map_bb_0_0_0_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_1_1_0, 0), (self.scrambler_cpp_additive_descrambler_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.cac_cpp_cac_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0, 0), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0, 0), (self.blocks_file_sink_0_0_0_0_0, 0))
        self.connect((self.cac_cpp_cac_bb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.cac_cpp_cac_bb_0, 0), (self.blocks_keep_m_in_n_0_0_2_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.fec_extended_decoder_0_0_1_0_1_0_0, 0), (self.blocks_keep_m_in_n_0_1_1_0, 0))
        self.connect((self.scrambler_cpp_additive_descrambler_0, 0), (self.blocks_repack_bits_bb_0_0_0_1_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_const_sink_x_0_0_0_1, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_time_sink_x_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx_eve")
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

    def get_H_dec(self):
        return self.H_dec

    def set_H_dec(self, H_dec):
        self.H_dec = H_dec

    def get_variable_qtgui_range_0_1(self):
        return self.variable_qtgui_range_0_1

    def set_variable_qtgui_range_0_1(self, variable_qtgui_range_0_1):
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1
        self.uhd_usrp_source_0_0.set_gain(self.variable_qtgui_range_0_1, 0)


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_pld_dec(self):
        return self.pld_dec

    def set_pld_dec(self, pld_dec):
        self.pld_dec = pld_dec

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_frequencia_usrp(self):
        return self.frequencia_usrp

    def set_frequencia_usrp(self, frequencia_usrp):
        self.frequencia_usrp = frequencia_usrp
        self.uhd_usrp_source_0_0.set_center_freq(self.frequencia_usrp, 0)

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


def main(top_block_cls=rx_eve, options=None):
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
