#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Self-Interference Cancellation with Adaptive Filters
# Author: karel
# Description: This example demonstrates how to adaptively cancel self-interference.
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import adapt
import pmt
import sip
import sys
from gnuradio import qtgui


class self_interference_cancellation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Self-Interference Cancellation with Adaptive Filters")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Self-Interference Cancellation with Adaptive Filters")
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

        self.settings = Qt.QSettings("GNU Radio", "self_interference_cancellation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)


        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(sps, sps, 1.0, eb, 11*sps)

        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.samp_rate = samp_rate = 32000

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)

        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.n_taps = n_taps = 16
        self.gui_reset = gui_reset = False
        self.gui_nlms_mu = gui_nlms_mu = 1
        self.gui_lms_mu = gui_lms_mu = 0.001
        self.gui_lambda = gui_lambda = 1
        self.gui_delta = gui_delta = 1
        self.gui_adapt = gui_adapt = True
        self.frequency = frequency = 2e3
        self.filt_delay = filt_delay = 1+(len(rrc_taps)-1)/2

        ##################################################
        # Blocks
        ##################################################
        _gui_reset_check_box = Qt.QCheckBox('Reset')
        self._gui_reset_choices = {True: True, False: False}
        self._gui_reset_choices_inv = dict((v,k) for k,v in self._gui_reset_choices.iteritems())
        self._gui_reset_callback = lambda i: Qt.QMetaObject.invokeMethod(_gui_reset_check_box, "setChecked", Qt.Q_ARG("bool", self._gui_reset_choices_inv[i]))
        self._gui_reset_callback(self.gui_reset)
        _gui_reset_check_box.stateChanged.connect(lambda i: self.set_gui_reset(self._gui_reset_choices[bool(i)]))
        self.top_grid_layout.addWidget(_gui_reset_check_box, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gui_lms_mu_range = Range(0.001, 1, 0.01, 0.001, 100)
        self._gui_lms_mu_win = RangeWidget(self._gui_lms_mu_range, self.set_gui_lms_mu, 'LMS Mu', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_lms_mu_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _gui_adapt_check_box = Qt.QCheckBox('Adapt')
        self._gui_adapt_choices = {True: True, False: False}
        self._gui_adapt_choices_inv = dict((v,k) for k,v in self._gui_adapt_choices.iteritems())
        self._gui_adapt_callback = lambda i: Qt.QMetaObject.invokeMethod(_gui_adapt_check_box, "setChecked", Qt.Q_ARG("bool", self._gui_adapt_choices_inv[i]))
        self._gui_adapt_callback(self.gui_adapt)
        _gui_adapt_check_box.stateChanged.connect(lambda i: self.set_gui_adapt(self._gui_adapt_choices[bool(i)]))
        self.top_grid_layout.addWidget(_gui_adapt_check_box, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 10, 5, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Depois poly", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_axis_labels(True)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_2.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_2_win, 10, 3, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	6 #number of inputs
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

        labels = ['Input', 'Reference', 'Out', 'Error', 'MIX',
                  'Original', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(6):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 6, 0, 3, 3)
        for r in range(6, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"Depois poly", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

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
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 10, 2, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, (rrc_taps))
        self.interp_fir_filter_xxx_0.declare_sample_delay(filt_delay)
        self._gui_nlms_mu_range = Range(0.001, 2, 0.01, 1, 100)
        self._gui_nlms_mu_win = RangeWidget(self._gui_nlms_mu_range, self.set_gui_nlms_mu, 'NLMS Mu', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_nlms_mu_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gui_lambda_range = Range(0.01, 1, 0.01, 1, 100)
        self._gui_lambda_win = RangeWidget(self._gui_lambda_range, self.set_gui_lambda, 'Lambda', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_lambda_win, 1, 1, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gui_delta_range = Range(0, 300, 1, 1, 300)
        self._gui_delta_win = RangeWidget(self._gui_delta_range, self.set_gui_delta, 'Delta', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gui_delta_win, 0, 1, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._frequency_range = Range(1e3, 1e4, 1e3, 2e3, 10)
        self._frequency_win = RangeWidget(self._frequency_range, self.set_frequency, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4, 6.28/100, (rx_rrc_taps), nfilts, 16, 1.5, 1)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(pld_const)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 2, '', False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0_0_1_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/trasmit_10_mb.txt', False)
        self.blocks_file_source_0_0_1_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.band_pass_filter_0_0_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, 1, 5000, 50, firdes.WIN_HAMMING, 6.76))
        self.analog_noise_source_x_0_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)
        self.adapt_lms_filter_xx_0_0 = adapt.lms_filter_cc(False, n_taps*2, gui_lms_mu, 0, 1, gui_adapt, False, gui_reset)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.adapt_lms_filter_xx_0_0, 1), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.adapt_lms_filter_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 3))
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 2))
        self.connect((self.blocks_add_xx_0_0, 0), (self.adapt_lms_filter_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 4))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.adapt_lms_filter_xx_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_2, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 5))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "self_interference_cancellation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

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

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.set_filt_delay(1+(len(self.rrc_taps)-1)/2)
        self.interp_fir_filter_xxx_0.set_taps((self.rrc_taps))

    def get_taps_per_filt(self):
        return self.taps_per_filt

    def set_taps_per_filt(self, taps_per_filt):
        self.taps_per_filt = taps_per_filt

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 1, 5000, 50, firdes.WIN_HAMMING, 6.76))

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_n_taps(self):
        return self.n_taps

    def set_n_taps(self, n_taps):
        self.n_taps = n_taps

    def get_gui_reset(self):
        return self.gui_reset

    def set_gui_reset(self, gui_reset):
        self.gui_reset = gui_reset
        self._gui_reset_callback(self.gui_reset)
        self.adapt_lms_filter_xx_0_0.set_reset(self.gui_reset)

    def get_gui_nlms_mu(self):
        return self.gui_nlms_mu

    def set_gui_nlms_mu(self, gui_nlms_mu):
        self.gui_nlms_mu = gui_nlms_mu

    def get_gui_lms_mu(self):
        return self.gui_lms_mu

    def set_gui_lms_mu(self, gui_lms_mu):
        self.gui_lms_mu = gui_lms_mu
        self.adapt_lms_filter_xx_0_0.set_mu(self.gui_lms_mu)

    def get_gui_lambda(self):
        return self.gui_lambda

    def set_gui_lambda(self, gui_lambda):
        self.gui_lambda = gui_lambda

    def get_gui_delta(self):
        return self.gui_delta

    def set_gui_delta(self, gui_delta):
        self.gui_delta = gui_delta

    def get_gui_adapt(self):
        return self.gui_adapt

    def set_gui_adapt(self, gui_adapt):
        self.gui_adapt = gui_adapt
        self._gui_adapt_callback(self.gui_adapt)
        self.adapt_lms_filter_xx_0_0.set_adapt(self.gui_adapt)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay


def main(top_block_cls=self_interference_cancellation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
