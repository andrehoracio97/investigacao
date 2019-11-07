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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import adapt
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
        self.samp_rate = samp_rate = 32000
        self.n_taps = n_taps = 16
        self.gui_reset = gui_reset = False
        self.gui_nlms_mu = gui_nlms_mu = 1
        self.gui_lms_mu = gui_lms_mu = 0.01
        self.gui_lambda = gui_lambda = 1
        self.gui_delta = gui_delta = 1
        self.gui_adapt = gui_adapt = True
        self.frequency = frequency = 2e3

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
        self._gui_lms_mu_range = Range(0.001, 1, 0.01, 0.01, 100)
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
        self._frequency_range = Range(1e3, 1e4, 1e3, 2e3, 10)
        self._frequency_win = RangeWidget(self._frequency_range, self.set_frequency, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._frequency_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            n_taps,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-1, 1)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

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
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win, 3, 0, 3, 3)
        for r in range(3, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
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

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Input', 'Reference', 'Out', 'Error', 'Original',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 6, 0, 3, 3)
        for r in range(6, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, frequency, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, samp_rate/32, 1, 0)
        self.adapt_lms_filter_xx_0 = adapt.lms_filter_ff(True, n_taps, gui_lms_mu, 0, 1, gui_adapt, False, gui_reset)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.adapt_lms_filter_xx_0, 1), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.adapt_lms_filter_xx_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.adapt_lms_filter_xx_0, 2), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.qtgui_freq_sink_x_0, 4))
        self.connect((self.analog_sig_source_x_1, 0), (self.adapt_lms_filter_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.adapt_lms_filter_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "self_interference_cancellation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.samp_rate/32)

    def get_n_taps(self):
        return self.n_taps

    def set_n_taps(self, n_taps):
        self.n_taps = n_taps

    def get_gui_reset(self):
        return self.gui_reset

    def set_gui_reset(self, gui_reset):
        self.gui_reset = gui_reset
        self._gui_reset_callback(self.gui_reset)
        self.adapt_lms_filter_xx_0.set_reset(self.gui_reset)

    def get_gui_nlms_mu(self):
        return self.gui_nlms_mu

    def set_gui_nlms_mu(self, gui_nlms_mu):
        self.gui_nlms_mu = gui_nlms_mu

    def get_gui_lms_mu(self):
        return self.gui_lms_mu

    def set_gui_lms_mu(self, gui_lms_mu):
        self.gui_lms_mu = gui_lms_mu
        self.adapt_lms_filter_xx_0.set_mu(self.gui_lms_mu)

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
        self.adapt_lms_filter_xx_0.set_adapt(self.gui_adapt)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_1.set_frequency(self.frequency)


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
