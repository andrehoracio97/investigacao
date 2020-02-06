#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Data Timing Offset
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
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class data_timing_offset(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Data Timing Offset")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Data Timing Offset")
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

        self.settings = Qt.QSettings("GNU Radio", "data_timing_offset")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.ntaps = ntaps = 32
        self.eb = eb = 0.22
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 1
        self.samp_rate = samp_rate = 10000
        self.rrc_tx = rrc_tx = firdes.root_raised_cosine(sps, sps, 1, eb, sps*ntaps)
        self.rrc_rx = rrc_rx = firdes.root_raised_cosine(1, sps, 1, eb, ntaps)
        self.rate = rate = 0.973
        self.pld_const = pld_const = digital.constellation_rect(([1+0j, -1+0j]), ([0, 1]), 4, 2, 2, 1, 1).base()
        self.pld_const.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_range = Range(0, 2, .0001, 1, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'Change timing offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_c(
        	50, #size
        	samp_rate, #samp_rate
        	'QT GUI Plot', #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.001)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.9, 0.0002, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()

        labels = ['NONE', 'TX Data', 'Rx Data', 'NONE', '',
                  '', '', '', '', '']
        widths = [0, 2, 2, 0, 1,
                  1, 1, 1, 1, 1]
        colors = ["cyan", "green", "red", "cyan", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 0, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(sps, (rrc_tx))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_map_bb_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.0,
        	frequency_offset=0.0,
        	epsilon=variable_qtgui_range_0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b((0,1), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0_1, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "data_timing_offset")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_tx(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, self.sps*self.ntaps))
        self.set_rrc_rx(firdes.root_raised_cosine(1, self.sps, 1, self.eb, self.ntaps))

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.channels_channel_model_0.set_timing_offset(self.variable_qtgui_range_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_tx(self):
        return self.rrc_tx

    def set_rrc_tx(self, rrc_tx):
        self.rrc_tx = rrc_tx
        self.interp_fir_filter_xxx_0.set_taps((self.rrc_tx))

    def get_rrc_rx(self):
        return self.rrc_rx

    def set_rrc_rx(self, rrc_rx):
        self.rrc_rx = rrc_rx

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const


def main(top_block_cls=data_timing_offset, options=None):

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
