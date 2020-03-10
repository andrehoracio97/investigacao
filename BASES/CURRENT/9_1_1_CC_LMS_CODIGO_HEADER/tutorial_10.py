#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tutorial
# Author: Andre Silva
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import adapt
import insert_vec_cpp
import pmt
import random
import scrambler_cpp
import sip
import sys
from gnuradio import qtgui


class tutorial_10(gr.top_block, Qt.QWidget):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Tutorial")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Tutorial")
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

        self.settings = Qt.QSettings("GNU Radio", "tutorial_10")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


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
        self.H_dec = H_dec = fec.ldpc_H_matrix('/usr/local/share/gnuradio/fec/ldpc/n_1100_k_0442_gap_24.alist', 24)
        self.H = H = fec.ldpc_H_matrix('/usr/local/share/gnuradio/fec/ldpc/n_1100_k_0442_gap_24.alist', 24)
        self.vector = vector = [int(random.random()*4) for i in range(49600)]

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)

        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.samp_rate = samp_rate = 100000000

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)



        self.pld_enc = pld_enc = map((lambda a: fec.ldpc_par_mtrx_encoder_make_H(H)), range(0,4))


        self.pld_dec = pld_dec = map((lambda a: fec.ldpc_bit_flip_decoder.make(H_dec.get_base_sptr(), 100)), range(0,8))
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.gui_lambda = gui_lambda = 1
        self.gui_delta = gui_delta = 1

        ##################################################
        # Blocks
        ##################################################
        self._gui_lambda_range = Range(0.01, 1, 0.01, 1, 100)
        self._gui_lambda_win = RangeWidget(self._gui_lambda_range, self.set_gui_lambda, 'Lambda', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_lambda_win, 0, 3, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gui_delta_range = Range(0, 300, 1, 1, 300)
        self._gui_delta_win = RangeWidget(self._gui_delta_range, self.set_gui_delta, 'Delta', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_delta_win, 0, 1, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.scrambler_cpp_additive_scrambler_0 = scrambler_cpp.additive_scrambler(0x8A, 0x7F, 7, 440-32)
        self.scrambler_cpp_additive_descrambler_0 = scrambler_cpp.additive_descrambler(0x8A, 0x7F, 7, 440-32)
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
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"LMS IN/OUT", #name
        	3 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)

        labels = ['Signal MIXED', 'ERROR', 'OUT', 'Error', 'MIX',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["black", "red", "green", "cyan", "magenta",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 5, 1, 1, 3)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_1_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"ORIGINAL/RECOVERED", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0_0.set_plot_pos_half(not True)

        labels = ['After Chunks to symbols', 'After Treated', 'Error LMS', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_0_win, 7, 1, 1, 3)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"TX/OUT LMS", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_1_0.set_plot_pos_half(not True)

        labels = ['After TX RRC', 'ERROR LMS', 'Error LMS', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_1_0_win, 6, 1, 1, 3)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RX Frequency", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Jamming", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"TX Frequency", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"RX Treated Constellation", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_1_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_1_0.disable_legend()

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
                self.qtgui_const_sink_x_0_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_1_0_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"TX Constellation", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_0_0.disable_legend()

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
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)

        self.interp_fir_filter_xxx_1_0 = filter.interp_fir_filter_ccc(4, ([1,0,0,0]))
        self.interp_fir_filter_xxx_1_0.declare_sample_delay(0)
        self.insert_vec_cpp_new_vec_0_0 = insert_vec_cpp.new_vec((vector))
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.fec_extended_decoder_0_0_1_0_1_0_0 = fec.extended_decoder(decoder_obj_list=pld_dec, threading='capillary', ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28/100.0, (rx_rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_map_bb_0_0_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_diff_encoder_bb_0_0 = digital.diff_encoder_bb(pld_const.arity())
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(pld_const.arity())
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(6.28/100.0, pld_const.arity(), False)
        self.digital_correlate_access_code_xx_ts_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          4, 'packet_len')
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(pld_const)
        self.digital_cma_equalizer_cc_0_0 = digital.cma_equalizer_cc(15, 1, 0.01, 2)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_mux_0_1_0_0_0 = blocks.stream_mux(gr.sizeof_char*1, (96, 1104))
        self.blocks_stream_mux_0_0_0 = blocks.stream_mux(gr.sizeof_char*1, (1100, 4))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (440, 2))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_0_0 = blocks.repack_bits_bb(1, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_1_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(pld_const.bits_per_symbol(), 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_keep_m_in_n_0_1_1_0 = blocks.keep_m_in_n(gr.sizeof_char, 440, 442, 0)
        self.blocks_keep_m_in_n_0_0_2_0_0 = blocks.keep_m_in_n(gr.sizeof_char, 1100, 1104, 0)
        self.blocks_file_source_0_0_1_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/trasmit_10_mb.txt', False)
        self.blocks_file_source_0_0_1_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0_0_0_2.set_unbuffered(False)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_2_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, -5)
        self.adapt_qrd_rls_filter_xx_0 = adapt.qrd_rls_filter_cc(32, gui_delta, gui_lambda, 0, 1, True, False)
        self.acode_1104_0_0 = blocks.vector_source_b([0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0], True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.acode_1104_0_0, 0), (self.blocks_stream_mux_0_1_0_0_0, 0))
        self.connect((self.adapt_qrd_rls_filter_xx_0, 1), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.adapt_qrd_rls_filter_xx_0, 1), (self.qtgui_freq_sink_x_0_0_1_0, 1))
        self.connect((self.adapt_qrd_rls_filter_xx_0, 1), (self.qtgui_freq_sink_x_1_0, 1))
        self.connect((self.adapt_qrd_rls_filter_xx_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.interp_fir_filter_xxx_1_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.adapt_qrd_rls_filter_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_1_0, 2))
        self.connect((self.blocks_char_to_float_0_2_0_0_0, 0), (self.fec_extended_decoder_0_0_1_0_1_0_0, 0))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_2_0_0, 0), (self.digital_map_bb_0_0_0_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_1_1_0, 0), (self.scrambler_cpp_additive_descrambler_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.adapt_qrd_rls_filter_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0, 0), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_1_0, 0), (self.blocks_file_sink_0_0_0_2, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0_0, 0), (self.insert_vec_cpp_new_vec_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.scrambler_cpp_additive_scrambler_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.blocks_stream_mux_0_1_0_0_0, 1))
        self.connect((self.blocks_stream_mux_0_1_0_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0, 0), (self.blocks_keep_m_in_n_0_0_2_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_0_0_1_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0_0, 1))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_diff_encoder_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0_0, 0))
        self.connect((self.fec_extended_decoder_0_0_1_0_1_0_0, 0), (self.blocks_keep_m_in_n_0_1_1_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0_0, 0))
        self.connect((self.insert_vec_cpp_new_vec_0_0, 0), (self.digital_diff_encoder_bb_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_1_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0_1_0, 0))
        self.connect((self.scrambler_cpp_additive_descrambler_0, 0), (self.blocks_repack_bits_bb_0_0_0_1_0, 0))
        self.connect((self.scrambler_cpp_additive_scrambler_0, 0), (self.blocks_stream_mux_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tutorial_10")
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
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.sps)

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
        self.pfb_arb_resampler_xxx_0_0.set_taps((self.tx_rrc_taps))

    def get_samp_rate_array_MCR(self):
        return self.samp_rate_array_MCR

    def set_samp_rate_array_MCR(self, samp_rate_array_MCR):
        self.samp_rate_array_MCR = samp_rate_array_MCR

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_pld_enc(self):
        return self.pld_enc

    def set_pld_enc(self, pld_enc):
        self.pld_enc = pld_enc

    def get_pld_dec(self):
        return self.pld_dec

    def set_pld_dec(self, pld_dec):
        self.pld_dec = pld_dec

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_gui_lambda(self):
        return self.gui_lambda

    def set_gui_lambda(self, gui_lambda):
        self.gui_lambda = gui_lambda
        self.adapt_qrd_rls_filter_xx_0.set_lambda(self.gui_lambda)

    def get_gui_delta(self):
        return self.gui_delta

    def set_gui_delta(self, gui_delta):
        self.gui_delta = gui_delta
        self.adapt_qrd_rls_filter_xx_0.set_delta(self.gui_delta)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=tutorial_10, options=None):
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
