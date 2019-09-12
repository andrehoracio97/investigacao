#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: roll_off _factor
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class roll_off(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "roll_off _factor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("roll_off _factor")
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

        self.settings = Qt.QSettings("GNU Radio", "roll_off")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, 0.1, 5*sps*nfilts)

        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts

        self.tx_rrc_taps_0_0_0_0 = tx_rrc_taps_0_0_0_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0, 1, 5*sps*nfilts)


        self.tx_rrc_taps_0_0_0 = tx_rrc_taps_0_0_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0, 0.500, 5*sps*nfilts)


        self.tx_rrc_taps_0_0 = tx_rrc_taps_0_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0, 0.350, 5*sps*nfilts)


        self.tx_rrc_taps_0 = tx_rrc_taps_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0, 0.22, 5*sps*nfilts)

        self.samp_rate = samp_rate = 32000
        self.pld_const = pld_const = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
        	5 #number of inputs
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

        labels = ['Roll Off: 0.1', 'Roll Off: 0.22', 'Roll Off: 0.35', 'Roll Off: 0.5', 'Roll Off: 1',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0_0_0_0_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps_0_0_0_0),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0_0_0_0_0.declare_sample_delay(filt_delay)

        self.pfb_arb_resampler_xxx_0_0_0_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps_0_0_0),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0_0_0_0.declare_sample_delay(filt_delay)

        self.pfb_arb_resampler_xxx_0_0_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps_0_0),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0_0_0.declare_sample_delay(filt_delay)

        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps_0),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(filt_delay)

        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self.digital_map_bb_0_0_0_0_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_0_0_0_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_0_0_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_0_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_chunks_to_symbols_xx_0_0_0_0_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_throttle_0_0_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_repack_bits_bb_1_0_0_1_0_0_0_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_1_0_0_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_1_0_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_1_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), '', False, gr.GR_MSB_FIRST)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 1000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_1_0_0_1_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_1_0_0_1_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_1_0_0_1_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_1_0_0_1_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1_0_0, 0), (self.digital_map_bb_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1_0_0_0, 0), (self.digital_map_bb_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1_0_0_0_0, 0), (self.digital_map_bb_0_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_throttle_0_0_0_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.blocks_throttle_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0, 4))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0_0, 0), (self.blocks_throttle_0_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "roll_off")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.pfb_arb_resampler_xxx_0_0_0_0_0.set_rate(self.sps)
        self.pfb_arb_resampler_xxx_0_0_0_0.set_rate(self.sps)
        self.pfb_arb_resampler_xxx_0_0_0.set_rate(self.sps)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.sps)
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)

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

    def get_tx_rrc_taps_0_0_0_0(self):
        return self.tx_rrc_taps_0_0_0_0

    def set_tx_rrc_taps_0_0_0_0(self, tx_rrc_taps_0_0_0_0):
        self.tx_rrc_taps_0_0_0_0 = tx_rrc_taps_0_0_0_0
        self.pfb_arb_resampler_xxx_0_0_0_0_0.set_taps((self.tx_rrc_taps_0_0_0_0))

    def get_tx_rrc_taps_0_0_0(self):
        return self.tx_rrc_taps_0_0_0

    def set_tx_rrc_taps_0_0_0(self, tx_rrc_taps_0_0_0):
        self.tx_rrc_taps_0_0_0 = tx_rrc_taps_0_0_0
        self.pfb_arb_resampler_xxx_0_0_0_0.set_taps((self.tx_rrc_taps_0_0_0))

    def get_tx_rrc_taps_0_0(self):
        return self.tx_rrc_taps_0_0

    def set_tx_rrc_taps_0_0(self, tx_rrc_taps_0_0):
        self.tx_rrc_taps_0_0 = tx_rrc_taps_0_0
        self.pfb_arb_resampler_xxx_0_0_0.set_taps((self.tx_rrc_taps_0_0))

    def get_tx_rrc_taps_0(self):
        return self.tx_rrc_taps_0

    def set_tx_rrc_taps_0(self, tx_rrc_taps_0):
        self.tx_rrc_taps_0 = tx_rrc_taps_0
        self.pfb_arb_resampler_xxx_0_0.set_taps((self.tx_rrc_taps_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay


def main(top_block_cls=roll_off, options=None):

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
