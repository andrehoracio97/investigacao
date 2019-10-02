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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import insert_vec_cpp
import pmt
import random
import scrambler_packets_same_seed
import sip
import sys
import time
from gnuradio import qtgui


class tutorial_11(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "tutorial_11")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 3, 2]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.samp_rate_array_MCR = samp_rate_array_MCR = [7500000,5000000,3750000,3000000,2500000,2000000,1500000,1000000,937500,882352,833333,714285,533333,500000,421052,400000,380952]
        self.rxmod = rxmod = digital.generic_mod(pld_const, False, sps, True, eb, False, False)

        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(sps, sps, 1.0, eb, 11*sps)

        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.mark_delays = mark_delays = [0, 0, 34, 56, 87, 119]
        self.k = k = 7
        self.header = header = [0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
        self.ac_hex = ac_hex = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.vector = vector = header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)] +header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]+header + [int(random.random()*2) for i in range(896)]
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 35
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 50
        self.samp_rate = samp_rate = samp_rate_array_MCR[3]

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)


        self.rx_psf_taps = rx_psf_taps = firdes.root_raised_cosine(nfilts, sps*nfilts, 1.0, eb, 11*sps*nfilts)



        self.pld_enc = pld_enc = map( (lambda a: fec.cc_encoder_make(440, k, rate, (polys), 0, fec.CC_TERMINATED, False)), range(0,4) );


        self.pld_dec = pld_dec = map( (lambda a: fec.cc_decoder.make(440, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)), range(0,8) );
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), (ac_hex), ([1]))
        self.mark_delay = mark_delay = mark_delays[sps]
        self.mark = mark = 57
        self.header_main = header_main = [0x1, 0x0, 0x1, 0x0, 0x1, 0x1, 0x0, 0x0, 0x1, 0x1, 0x0, 0x1, 0x1, 0x1, 0x0, 0x1, 0x1, 0x0, 0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0]
        self.frequencia_usrp = frequencia_usrp = 484e6
        self.filt_delay2 = filt_delay2 = 1+(len(rrc_taps)-1)/2
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2
        self.copy = copy = True
        self.ac = ac = map(lambda x: int(x), list(digital.packet_utils.default_access_code))
        self.MCR = MCR = "master_clock_rate=60e6"

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_1_range = Range(0, 73, 1, 35, 200)
        self._variable_qtgui_range_0_1_win = RangeWidget(self._variable_qtgui_range_0_1_range, self.set_variable_qtgui_range_0_1, 'Gain_RX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_1_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_range_0_range = Range(0, 90, 1, 50, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Gain_TX', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _copy_check_box = Qt.QCheckBox("copy")
        self._copy_choices = {True: True, False: False}
        self._copy_choices_inv = dict((v,k) for k,v in self._copy_choices.iteritems())
        self._copy_callback = lambda i: Qt.QMetaObject.invokeMethod(_copy_check_box, "setChecked", Qt.Q_ARG("bool", self._copy_choices_inv[i]))
        self._copy_callback(self.copy)
        _copy_check_box.stateChanged.connect(lambda i: self.set_copy(self._copy_choices[bool(i)]))
        self.top_grid_layout.addWidget(_copy_check_box, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 1, 4, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"TX USRP", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

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
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 1, 3, 1, 1)
        for r in range(1, 2):
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
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_c(
        	512, #size
        	10, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-15, 15)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 15, 0, 'corr_est')
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_1.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	512, #size
        	1, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-100, 4000)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 15, 0, 'corr_est')
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 3, 2, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	100*2, #size
        	samp_rate, #samp_rate
        	'Tx Data', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 256)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'packet_length_tag_key')
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
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
        self.qtgui_const_sink_x_0_0_0_1 = qtgui.const_sink_c(
        	1024, #size
        	"RX Constellation", #name
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_1_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self._mark_range = Range(50, 120, 1, 57, 200)
        self._mark_win = RangeWidget(self._mark_range, self.set_mark, 'mark', "counter_slider", float)
        self.top_grid_layout.addWidget(self._mark_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.insert_vec_cpp_new_vec_0 = insert_vec_cpp.new_vec((vector))
        self.fec_extended_encoder_0 = fec.extended_encoder(encoder_obj_list=pld_enc, threading='capillary', puncpat=puncpat)
        self.fec_extended_decoder_0_0_1_0_1_0 = fec.extended_decoder(decoder_obj_list=pld_dec, threading='capillary', ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28/400.0, (rx_rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_map_bb_0_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(6.28/100.0, pld_const.arity(), False)
        self.digital_correlate_access_code_xx_ts_0_0 = digital.correlate_access_code_bb_ts(digital.packet_utils.default_access_code,
          1, 'packet_len')
        self.digital_corr_est_cc_0 = digital.corr_est_cc((modulated_sync_word), sps, mark_delay, 0.999)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(pld_const)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_b([0], True, 1, [])
        self.blocks_stream_mux_0_1_0 = blocks.stream_mux(gr.sizeof_char*1, (96, 896))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_char*1, (892, 4))
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1_0 = blocks.repack_bits_bb(1, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(pld_const.bits_per_symbol(), 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_keep_m_in_n_0_0_2_0 = blocks.keep_m_in_n(gr.sizeof_char, 892, 896, 0)
        self.blocks_file_source_0_0_1_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/trasmit_10_mb.txt', False)
        self.blocks_file_source_0_0_1_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0_2 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0_0_0_2.set_unbuffered(False)
        self.blocks_copy_0 = blocks.copy(gr.sizeof_gr_complex*1)
        self.blocks_copy_0.set_enabled(copy)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_2_0_0 = blocks.char_to_float(1, 1)
        self.acode_1104 = blocks.vector_source_b(header_main, True, 1, [])



        ##################################################
        # Connections
        ##################################################
        self.connect((self.acode_1104, 0), (self.blocks_stream_mux_0_1_0, 0))
        self.connect((self.blocks_char_to_float_0_2_0_0, 0), (self.fec_extended_decoder_0_0_1_0_1_0, 0))
        self.connect((self.blocks_char_to_float_1_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_copy_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_char_to_float_1_0_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_2_0, 0), (self.digital_map_bb_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0_0_0_2, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.scrambler_packets_same_seed_scramble_packetize_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_stream_mux_0_1_0, 1))
        self.connect((self.blocks_stream_mux_0_1_0, 0), (self.insert_vec_cpp_new_vec_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_corr_est_cc_0, 1), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_corr_est_cc_0, 1), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0, 0), (self.blocks_keep_m_in_n_0_0_2_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_0_0_0_1_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.fec_extended_decoder_0_0_1_0_1_0, 0), (self.scrambler_packets_same_seed_descramble_packetize_0, 0))
        self.connect((self.fec_extended_encoder_0, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.insert_vec_cpp_new_vec_0, 0), (self.blocks_repack_bits_bb_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_copy_0, 0))
        self.connect((self.scrambler_packets_same_seed_descramble_packetize_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.scrambler_packets_same_seed_scramble_packetize_0, 0), (self.fec_extended_encoder_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_corr_est_cc_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_const_sink_x_0_0_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_time_sink_x_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tutorial_11")
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
        self.set_mark_delay(self.mark_delays[self.sps])
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))
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
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_rrc_taps))

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const
        self.set_rxmod(digital.generic_mod(self.pld_const, False, self.sps, True, self.eb, False, False))

    def get_taps_per_filt(self):
        return self.taps_per_filt

    def set_taps_per_filt(self, taps_per_filt):
        self.taps_per_filt = taps_per_filt
        self.set_filt_delay(1+(self.taps_per_filt-1)/2)

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
        self.set_filt_delay2(1+(len(self.rrc_taps)-1)/2)

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_mark_delays(self):
        return self.mark_delays

    def set_mark_delays(self, mark_delays):
        self.mark_delays = mark_delays
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_header(self):
        return self.header

    def set_header(self, header):
        self.header = header
        self.set_vector(self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)] +self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)]+self.header + [int(random.random()*2) for i in range(896)])

    def get_ac_hex(self):
        return self.ac_hex

    def set_ac_hex(self, ac_hex):
        self.ac_hex = ac_hex

    def get_vector(self):
        return self.vector

    def set_vector(self, vector):
        self.vector = vector

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


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_rx_psf_taps(self):
        return self.rx_psf_taps

    def set_rx_psf_taps(self, rx_psf_taps):
        self.rx_psf_taps = rx_psf_taps

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

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_header_main(self):
        return self.header_main

    def set_header_main(self, header_main):
        self.header_main = header_main
        self.acode_1104.set_data(self.header_main, [])

    def get_frequencia_usrp(self):
        return self.frequencia_usrp

    def set_frequencia_usrp(self, frequencia_usrp):
        self.frequencia_usrp = frequencia_usrp
        self.uhd_usrp_source_0.set_center_freq(self.frequencia_usrp, 0)
        self.uhd_usrp_sink_0_0.set_center_freq(self.frequencia_usrp, 0)

    def get_filt_delay2(self):
        return self.filt_delay2

    def set_filt_delay2(self, filt_delay2):
        self.filt_delay2 = filt_delay2

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay

    def get_copy(self):
        return self.copy

    def set_copy(self, copy):
        self.copy = copy
        self._copy_callback(self.copy)
        self.blocks_copy_0.set_enabled(self.copy)

    def get_ac(self):
        return self.ac

    def set_ac(self, ac):
        self.ac = ac

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


def main(top_block_cls=tutorial_11, options=None):
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
