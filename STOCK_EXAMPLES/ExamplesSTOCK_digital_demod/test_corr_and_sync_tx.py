#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Test Corr And Sync Tx
# Generated: Wed Jul 24 10:30:32 2019
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

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys
import time
from gnuradio import qtgui


class test_corr_and_sync_tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Corr And Sync Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Corr And Sync Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "test_corr_and_sync_tx")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate = samp_rate = 250000
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.payload_size = payload_size = 992
        self.gap = gap = 20000
        self.gain = gain = 12.5
        self.freq = freq = 450e6
        self.fine_freq = fine_freq = 0
        self.eb = eb = 0.35
        self.digital_gain = digital_gain = 45

        self.constel = constel = digital.constellation_calcdist(([1,- 1]), ([0,1]), 2, 1).base()

        self.addr = addr = "addr=192.168.10.2"

        ##################################################
        # Blocks
        ##################################################
        self._gain_range = Range(0, 31.5, 0.5, 12.5, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, 'Tx Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = Range(400e6, 500e6, 100e3, 450e6, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Tx Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fine_freq_range = Range(-10e3, 10e3, 10, 0, 200)
        self._fine_freq_win = RangeWidget(self._fine_freq_range, self.set_fine_freq, 'Fine Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._fine_freq_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._digital_gain_range = Range(0, 200, 1, 45, 200)
        self._digital_gain_win = RangeWidget(self._digital_gain_range, self.set_digital_gain, 'Digital Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._digital_gain_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join((addr, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq+fine_freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, 20)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=constel,
          differential=False,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=eb,
          verbose=False,
          log=False,
          )
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b(map(lambda x: (-x+1)/2, preamble), True, 1, [])
        self.blocks_stream_mux_0_0_0 = blocks.stream_mux(gr.sizeof_char*1, (len(preamble)/8,payload_size))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_gr_complex*1, ((len(preamble)+8*payload_size)*sps, gap))
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((digital_gain, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 100000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_mux_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_null_source_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_stream_mux_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_stream_mux_0_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_stream_mux_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test_corr_and_sync_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble
        self.blocks_vector_source_x_0_0.set_data(map(lambda x: (-x+1)/2, self.preamble), [])

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_gap(self):
        return self.gap

    def set_gap(self, gap):
        self.gap = gap

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_sink_0.set_gain(self.gain, 0)


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq+self.fine_freq, 0)

    def get_fine_freq(self):
        return self.fine_freq

    def set_fine_freq(self, fine_freq):
        self.fine_freq = fine_freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq+self.fine_freq, 0)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_digital_gain(self):
        return self.digital_gain

    def set_digital_gain(self, digital_gain):
        self.digital_gain = digital_gain
        self.blocks_multiply_const_vxx_0.set_k((self.digital_gain, ))

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr


def main(top_block_cls=test_corr_and_sync_tx, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
