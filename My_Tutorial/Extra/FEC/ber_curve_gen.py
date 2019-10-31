#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ber Curve Gen
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
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class ber_curve_gen(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ber Curve Gen")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ber Curve Gen")
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

        self.settings = Qt.QSettings("GNU Radio", "ber_curve_gen")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [79, 109]
        self.k = k = 7
        self.framebits = framebits = 4096
        self.esno_0 = esno_0 = numpy.arange(0, 8, .5)
        self.samp_rate_0 = samp_rate_0 = 35000000

        self.enc_tpc = enc_tpc = map( (lambda b: map( ( lambda a: fec.tpc_encoder_make(([3]), ([43]), 26, 6, 9, 3)), range(0,1) ) ), range(0,len(esno_0)));

        self.enc_rep = enc_rep = map((lambda b: map((lambda a: fec.repetition_encoder_make(framebits, 3)), range(0,1))), range(0,len(esno_0)))

        self.enc_ldpc = enc_ldpc = map( (lambda b: map( ( lambda a: fec.ldpc_encoder_make('/usr/local/share/gnuradio/fec/ldpc/271.127.3.112')), range(0,1) ) ), range(0,len(esno_0)));

        self.enc_dummy = enc_dummy = map((lambda b: map((lambda a: fec.dummy_encoder_make(framebits)), range(0,1))), range(0,len(esno_0)))

        self.enc_cc = enc_cc = map( (lambda b: map( ( lambda a: fec.cc_encoder_make(framebits, k, rate, (polys), 0, fec.CC_STREAMING, False)), range(0,1) ) ), range(0,len(esno_0)));

        self.dec_tpc = dec_tpc = map( (lambda b: map( ( lambda a: fec.tpc_decoder_make(([3]), ([43]), 26, 6, 9, 3, 6, 1)), range(0,1) ) ), range(0,len(esno_0)));

        self.dec_rep = dec_rep = map( (lambda b: map( ( lambda a: fec.repetition_decoder.make(framebits, 3, 0.5)), range(0,1) ) ), range(0,len(esno_0)))

        self.dec_ldpc = dec_ldpc = map( (lambda b: map( ( lambda a: fec.ldpc_decoder.make('/usr/local/share/gnuradio/fec/ldpc/271.127.3.112', 0.5, 50)), range(0,1) ) ), range(0,len(esno_0)));

        self.dec_dummy = dec_dummy = map((lambda b: map((lambda a: fec.dummy_decoder.make(framebits)), range(0,1))), range(0,len(esno_0)))

        self.dec_cc = dec_cc = map( (lambda b: map( ( lambda a: fec.cc_decoder.make(framebits, k, rate, (polys), 0, -1, fec.CC_STREAMING, False)), range(0,1) ) ), range(0,len(esno_0)));

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_bercurve_sink_0 =   qtgui.ber_sink_b(
            esno_0, #range of esnos
            5, #number of curves
            1000, #ensure at least
            -10, #cutoff
            [], #indiv. curve names
          )
        self.qtgui_bercurve_sink_0.set_update_time(0.10)
        self.qtgui_bercurve_sink_0.set_y_axis(-10, 0)
        self.qtgui_bercurve_sink_0.set_x_axis(esno_0[0], esno_0[-1])

        labels = ['None', 'Rep. (Rate=3)', 'CC (K=7, Rate=2)', 'LDPC', 'TPC',
                  '', '', '', '', '']
        widths = [2, 2, 2, 2, 2,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "magenta", "dark red", "Dark Blue",
                  "red", "red", "red", "red", "red"]
        styles = [1, 2, 5, 5, 4,
                  0, 0, 0, 0, 0]
        markers = [0, 1, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1, 1, 1, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_bercurve_sink_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_bercurve_sink_0.set_line_label(i, labels[i])
            self.qtgui_bercurve_sink_0.set_line_width(i, widths[i])
            self.qtgui_bercurve_sink_0.set_line_color(i, colors[i])
            self.qtgui_bercurve_sink_0.set_line_style(i, styles[i])
            self.qtgui_bercurve_sink_0.set_line_marker(i, markers[i])
            self.qtgui_bercurve_sink_0.set_line_alpha(i, alphas[i])

        self._qtgui_bercurve_sink_0_win = sip.wrapinstance(self.qtgui_bercurve_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_bercurve_sink_0_win)
        self.fec_bercurve_generator_0_1_0 = fec.bercurve_generator(
        	enc_tpc, #size
        	dec_tpc, #name
        	esno_0, #range of esnos
        	samp_rate_0, #throttle
                "capillary", #threading mode
        	'11', #puncture pattern
                -100 # noise gen. seed
        )

        self.fec_bercurve_generator_0_1 = fec.bercurve_generator(
        	enc_ldpc, #size
        	dec_ldpc, #name
        	esno_0, #range of esnos
        	samp_rate_0, #throttle
                "capillary", #threading mode
        	'11', #puncture pattern
                -100 # noise gen. seed
        )

        self.fec_bercurve_generator_0_0_0 = fec.bercurve_generator(
        	enc_dummy, #size
        	dec_dummy, #name
        	esno_0, #range of esnos
        	samp_rate_0, #throttle
                "capillary", #threading mode
        	'11', #puncture pattern
                -100 # noise gen. seed
        )

        self.fec_bercurve_generator_0_0 = fec.bercurve_generator(
        	enc_rep, #size
        	dec_rep, #name
        	esno_0, #range of esnos
        	samp_rate_0, #throttle
                "capillary", #threading mode
        	'11', #puncture pattern
                -100 # noise gen. seed
        )

        self.fec_bercurve_generator_0 = fec.bercurve_generator(
        	enc_cc, #size
        	dec_cc, #name
        	esno_0, #range of esnos
        	samp_rate_0, #throttle
                "capillary", #threading mode
        	'11', #puncture pattern
                -100 # noise gen. seed
        )




        ##################################################
        # Connections
        ##################################################
        self.connect((self.fec_bercurve_generator_0, 0), (self.qtgui_bercurve_sink_0, 64))
        self.connect((self.fec_bercurve_generator_0, 1), (self.qtgui_bercurve_sink_0, 65))
        self.connect((self.fec_bercurve_generator_0, 2), (self.qtgui_bercurve_sink_0, 66))
        self.connect((self.fec_bercurve_generator_0, 3), (self.qtgui_bercurve_sink_0, 67))
        self.connect((self.fec_bercurve_generator_0, 4), (self.qtgui_bercurve_sink_0, 68))
        self.connect((self.fec_bercurve_generator_0, 5), (self.qtgui_bercurve_sink_0, 69))
        self.connect((self.fec_bercurve_generator_0, 6), (self.qtgui_bercurve_sink_0, 70))
        self.connect((self.fec_bercurve_generator_0, 7), (self.qtgui_bercurve_sink_0, 71))
        self.connect((self.fec_bercurve_generator_0, 8), (self.qtgui_bercurve_sink_0, 72))
        self.connect((self.fec_bercurve_generator_0, 9), (self.qtgui_bercurve_sink_0, 73))
        self.connect((self.fec_bercurve_generator_0, 10), (self.qtgui_bercurve_sink_0, 74))
        self.connect((self.fec_bercurve_generator_0, 11), (self.qtgui_bercurve_sink_0, 75))
        self.connect((self.fec_bercurve_generator_0, 12), (self.qtgui_bercurve_sink_0, 76))
        self.connect((self.fec_bercurve_generator_0, 13), (self.qtgui_bercurve_sink_0, 77))
        self.connect((self.fec_bercurve_generator_0, 14), (self.qtgui_bercurve_sink_0, 78))
        self.connect((self.fec_bercurve_generator_0, 15), (self.qtgui_bercurve_sink_0, 79))
        self.connect((self.fec_bercurve_generator_0, 16), (self.qtgui_bercurve_sink_0, 80))
        self.connect((self.fec_bercurve_generator_0, 17), (self.qtgui_bercurve_sink_0, 81))
        self.connect((self.fec_bercurve_generator_0, 18), (self.qtgui_bercurve_sink_0, 82))
        self.connect((self.fec_bercurve_generator_0, 19), (self.qtgui_bercurve_sink_0, 83))
        self.connect((self.fec_bercurve_generator_0, 20), (self.qtgui_bercurve_sink_0, 84))
        self.connect((self.fec_bercurve_generator_0, 21), (self.qtgui_bercurve_sink_0, 85))
        self.connect((self.fec_bercurve_generator_0, 22), (self.qtgui_bercurve_sink_0, 86))
        self.connect((self.fec_bercurve_generator_0, 23), (self.qtgui_bercurve_sink_0, 87))
        self.connect((self.fec_bercurve_generator_0, 24), (self.qtgui_bercurve_sink_0, 88))
        self.connect((self.fec_bercurve_generator_0, 25), (self.qtgui_bercurve_sink_0, 89))
        self.connect((self.fec_bercurve_generator_0, 26), (self.qtgui_bercurve_sink_0, 90))
        self.connect((self.fec_bercurve_generator_0, 27), (self.qtgui_bercurve_sink_0, 91))
        self.connect((self.fec_bercurve_generator_0, 28), (self.qtgui_bercurve_sink_0, 92))
        self.connect((self.fec_bercurve_generator_0, 29), (self.qtgui_bercurve_sink_0, 93))
        self.connect((self.fec_bercurve_generator_0, 30), (self.qtgui_bercurve_sink_0, 94))
        self.connect((self.fec_bercurve_generator_0, 31), (self.qtgui_bercurve_sink_0, 95))
        self.connect((self.fec_bercurve_generator_0_0, 0), (self.qtgui_bercurve_sink_0, 32))
        self.connect((self.fec_bercurve_generator_0_0, 1), (self.qtgui_bercurve_sink_0, 33))
        self.connect((self.fec_bercurve_generator_0_0, 2), (self.qtgui_bercurve_sink_0, 34))
        self.connect((self.fec_bercurve_generator_0_0, 3), (self.qtgui_bercurve_sink_0, 35))
        self.connect((self.fec_bercurve_generator_0_0, 4), (self.qtgui_bercurve_sink_0, 36))
        self.connect((self.fec_bercurve_generator_0_0, 5), (self.qtgui_bercurve_sink_0, 37))
        self.connect((self.fec_bercurve_generator_0_0, 6), (self.qtgui_bercurve_sink_0, 38))
        self.connect((self.fec_bercurve_generator_0_0, 7), (self.qtgui_bercurve_sink_0, 39))
        self.connect((self.fec_bercurve_generator_0_0, 8), (self.qtgui_bercurve_sink_0, 40))
        self.connect((self.fec_bercurve_generator_0_0, 9), (self.qtgui_bercurve_sink_0, 41))
        self.connect((self.fec_bercurve_generator_0_0, 10), (self.qtgui_bercurve_sink_0, 42))
        self.connect((self.fec_bercurve_generator_0_0, 11), (self.qtgui_bercurve_sink_0, 43))
        self.connect((self.fec_bercurve_generator_0_0, 12), (self.qtgui_bercurve_sink_0, 44))
        self.connect((self.fec_bercurve_generator_0_0, 13), (self.qtgui_bercurve_sink_0, 45))
        self.connect((self.fec_bercurve_generator_0_0, 14), (self.qtgui_bercurve_sink_0, 46))
        self.connect((self.fec_bercurve_generator_0_0, 15), (self.qtgui_bercurve_sink_0, 47))
        self.connect((self.fec_bercurve_generator_0_0, 16), (self.qtgui_bercurve_sink_0, 48))
        self.connect((self.fec_bercurve_generator_0_0, 17), (self.qtgui_bercurve_sink_0, 49))
        self.connect((self.fec_bercurve_generator_0_0, 18), (self.qtgui_bercurve_sink_0, 50))
        self.connect((self.fec_bercurve_generator_0_0, 19), (self.qtgui_bercurve_sink_0, 51))
        self.connect((self.fec_bercurve_generator_0_0, 20), (self.qtgui_bercurve_sink_0, 52))
        self.connect((self.fec_bercurve_generator_0_0, 21), (self.qtgui_bercurve_sink_0, 53))
        self.connect((self.fec_bercurve_generator_0_0, 22), (self.qtgui_bercurve_sink_0, 54))
        self.connect((self.fec_bercurve_generator_0_0, 23), (self.qtgui_bercurve_sink_0, 55))
        self.connect((self.fec_bercurve_generator_0_0, 24), (self.qtgui_bercurve_sink_0, 56))
        self.connect((self.fec_bercurve_generator_0_0, 25), (self.qtgui_bercurve_sink_0, 57))
        self.connect((self.fec_bercurve_generator_0_0, 26), (self.qtgui_bercurve_sink_0, 58))
        self.connect((self.fec_bercurve_generator_0_0, 27), (self.qtgui_bercurve_sink_0, 59))
        self.connect((self.fec_bercurve_generator_0_0, 28), (self.qtgui_bercurve_sink_0, 60))
        self.connect((self.fec_bercurve_generator_0_0, 29), (self.qtgui_bercurve_sink_0, 61))
        self.connect((self.fec_bercurve_generator_0_0, 30), (self.qtgui_bercurve_sink_0, 62))
        self.connect((self.fec_bercurve_generator_0_0, 31), (self.qtgui_bercurve_sink_0, 63))
        self.connect((self.fec_bercurve_generator_0_0_0, 0), (self.qtgui_bercurve_sink_0, 0))
        self.connect((self.fec_bercurve_generator_0_0_0, 1), (self.qtgui_bercurve_sink_0, 1))
        self.connect((self.fec_bercurve_generator_0_0_0, 2), (self.qtgui_bercurve_sink_0, 2))
        self.connect((self.fec_bercurve_generator_0_0_0, 3), (self.qtgui_bercurve_sink_0, 3))
        self.connect((self.fec_bercurve_generator_0_0_0, 4), (self.qtgui_bercurve_sink_0, 4))
        self.connect((self.fec_bercurve_generator_0_0_0, 5), (self.qtgui_bercurve_sink_0, 5))
        self.connect((self.fec_bercurve_generator_0_0_0, 6), (self.qtgui_bercurve_sink_0, 6))
        self.connect((self.fec_bercurve_generator_0_0_0, 7), (self.qtgui_bercurve_sink_0, 7))
        self.connect((self.fec_bercurve_generator_0_0_0, 8), (self.qtgui_bercurve_sink_0, 8))
        self.connect((self.fec_bercurve_generator_0_0_0, 9), (self.qtgui_bercurve_sink_0, 9))
        self.connect((self.fec_bercurve_generator_0_0_0, 10), (self.qtgui_bercurve_sink_0, 10))
        self.connect((self.fec_bercurve_generator_0_0_0, 11), (self.qtgui_bercurve_sink_0, 11))
        self.connect((self.fec_bercurve_generator_0_0_0, 12), (self.qtgui_bercurve_sink_0, 12))
        self.connect((self.fec_bercurve_generator_0_0_0, 13), (self.qtgui_bercurve_sink_0, 13))
        self.connect((self.fec_bercurve_generator_0_0_0, 14), (self.qtgui_bercurve_sink_0, 14))
        self.connect((self.fec_bercurve_generator_0_0_0, 15), (self.qtgui_bercurve_sink_0, 15))
        self.connect((self.fec_bercurve_generator_0_0_0, 16), (self.qtgui_bercurve_sink_0, 16))
        self.connect((self.fec_bercurve_generator_0_0_0, 17), (self.qtgui_bercurve_sink_0, 17))
        self.connect((self.fec_bercurve_generator_0_0_0, 18), (self.qtgui_bercurve_sink_0, 18))
        self.connect((self.fec_bercurve_generator_0_0_0, 19), (self.qtgui_bercurve_sink_0, 19))
        self.connect((self.fec_bercurve_generator_0_0_0, 20), (self.qtgui_bercurve_sink_0, 20))
        self.connect((self.fec_bercurve_generator_0_0_0, 21), (self.qtgui_bercurve_sink_0, 21))
        self.connect((self.fec_bercurve_generator_0_0_0, 22), (self.qtgui_bercurve_sink_0, 22))
        self.connect((self.fec_bercurve_generator_0_0_0, 23), (self.qtgui_bercurve_sink_0, 23))
        self.connect((self.fec_bercurve_generator_0_0_0, 24), (self.qtgui_bercurve_sink_0, 24))
        self.connect((self.fec_bercurve_generator_0_0_0, 25), (self.qtgui_bercurve_sink_0, 25))
        self.connect((self.fec_bercurve_generator_0_0_0, 26), (self.qtgui_bercurve_sink_0, 26))
        self.connect((self.fec_bercurve_generator_0_0_0, 27), (self.qtgui_bercurve_sink_0, 27))
        self.connect((self.fec_bercurve_generator_0_0_0, 28), (self.qtgui_bercurve_sink_0, 28))
        self.connect((self.fec_bercurve_generator_0_0_0, 29), (self.qtgui_bercurve_sink_0, 29))
        self.connect((self.fec_bercurve_generator_0_0_0, 30), (self.qtgui_bercurve_sink_0, 30))
        self.connect((self.fec_bercurve_generator_0_0_0, 31), (self.qtgui_bercurve_sink_0, 31))
        self.connect((self.fec_bercurve_generator_0_1, 0), (self.qtgui_bercurve_sink_0, 96))
        self.connect((self.fec_bercurve_generator_0_1, 1), (self.qtgui_bercurve_sink_0, 97))
        self.connect((self.fec_bercurve_generator_0_1, 2), (self.qtgui_bercurve_sink_0, 98))
        self.connect((self.fec_bercurve_generator_0_1, 3), (self.qtgui_bercurve_sink_0, 99))
        self.connect((self.fec_bercurve_generator_0_1, 4), (self.qtgui_bercurve_sink_0, 100))
        self.connect((self.fec_bercurve_generator_0_1, 5), (self.qtgui_bercurve_sink_0, 101))
        self.connect((self.fec_bercurve_generator_0_1, 6), (self.qtgui_bercurve_sink_0, 102))
        self.connect((self.fec_bercurve_generator_0_1, 7), (self.qtgui_bercurve_sink_0, 103))
        self.connect((self.fec_bercurve_generator_0_1, 8), (self.qtgui_bercurve_sink_0, 104))
        self.connect((self.fec_bercurve_generator_0_1, 9), (self.qtgui_bercurve_sink_0, 105))
        self.connect((self.fec_bercurve_generator_0_1, 10), (self.qtgui_bercurve_sink_0, 106))
        self.connect((self.fec_bercurve_generator_0_1, 11), (self.qtgui_bercurve_sink_0, 107))
        self.connect((self.fec_bercurve_generator_0_1, 12), (self.qtgui_bercurve_sink_0, 108))
        self.connect((self.fec_bercurve_generator_0_1, 13), (self.qtgui_bercurve_sink_0, 109))
        self.connect((self.fec_bercurve_generator_0_1, 14), (self.qtgui_bercurve_sink_0, 110))
        self.connect((self.fec_bercurve_generator_0_1, 15), (self.qtgui_bercurve_sink_0, 111))
        self.connect((self.fec_bercurve_generator_0_1, 16), (self.qtgui_bercurve_sink_0, 112))
        self.connect((self.fec_bercurve_generator_0_1, 17), (self.qtgui_bercurve_sink_0, 113))
        self.connect((self.fec_bercurve_generator_0_1, 18), (self.qtgui_bercurve_sink_0, 114))
        self.connect((self.fec_bercurve_generator_0_1, 19), (self.qtgui_bercurve_sink_0, 115))
        self.connect((self.fec_bercurve_generator_0_1, 20), (self.qtgui_bercurve_sink_0, 116))
        self.connect((self.fec_bercurve_generator_0_1, 21), (self.qtgui_bercurve_sink_0, 117))
        self.connect((self.fec_bercurve_generator_0_1, 22), (self.qtgui_bercurve_sink_0, 118))
        self.connect((self.fec_bercurve_generator_0_1, 23), (self.qtgui_bercurve_sink_0, 119))
        self.connect((self.fec_bercurve_generator_0_1, 24), (self.qtgui_bercurve_sink_0, 120))
        self.connect((self.fec_bercurve_generator_0_1, 25), (self.qtgui_bercurve_sink_0, 121))
        self.connect((self.fec_bercurve_generator_0_1, 26), (self.qtgui_bercurve_sink_0, 122))
        self.connect((self.fec_bercurve_generator_0_1, 27), (self.qtgui_bercurve_sink_0, 123))
        self.connect((self.fec_bercurve_generator_0_1, 28), (self.qtgui_bercurve_sink_0, 124))
        self.connect((self.fec_bercurve_generator_0_1, 29), (self.qtgui_bercurve_sink_0, 125))
        self.connect((self.fec_bercurve_generator_0_1, 30), (self.qtgui_bercurve_sink_0, 126))
        self.connect((self.fec_bercurve_generator_0_1, 31), (self.qtgui_bercurve_sink_0, 127))
        self.connect((self.fec_bercurve_generator_0_1_0, 0), (self.qtgui_bercurve_sink_0, 128))
        self.connect((self.fec_bercurve_generator_0_1_0, 1), (self.qtgui_bercurve_sink_0, 129))
        self.connect((self.fec_bercurve_generator_0_1_0, 2), (self.qtgui_bercurve_sink_0, 130))
        self.connect((self.fec_bercurve_generator_0_1_0, 3), (self.qtgui_bercurve_sink_0, 131))
        self.connect((self.fec_bercurve_generator_0_1_0, 4), (self.qtgui_bercurve_sink_0, 132))
        self.connect((self.fec_bercurve_generator_0_1_0, 5), (self.qtgui_bercurve_sink_0, 133))
        self.connect((self.fec_bercurve_generator_0_1_0, 6), (self.qtgui_bercurve_sink_0, 134))
        self.connect((self.fec_bercurve_generator_0_1_0, 7), (self.qtgui_bercurve_sink_0, 135))
        self.connect((self.fec_bercurve_generator_0_1_0, 8), (self.qtgui_bercurve_sink_0, 136))
        self.connect((self.fec_bercurve_generator_0_1_0, 9), (self.qtgui_bercurve_sink_0, 137))
        self.connect((self.fec_bercurve_generator_0_1_0, 10), (self.qtgui_bercurve_sink_0, 138))
        self.connect((self.fec_bercurve_generator_0_1_0, 11), (self.qtgui_bercurve_sink_0, 139))
        self.connect((self.fec_bercurve_generator_0_1_0, 12), (self.qtgui_bercurve_sink_0, 140))
        self.connect((self.fec_bercurve_generator_0_1_0, 13), (self.qtgui_bercurve_sink_0, 141))
        self.connect((self.fec_bercurve_generator_0_1_0, 14), (self.qtgui_bercurve_sink_0, 142))
        self.connect((self.fec_bercurve_generator_0_1_0, 15), (self.qtgui_bercurve_sink_0, 143))
        self.connect((self.fec_bercurve_generator_0_1_0, 16), (self.qtgui_bercurve_sink_0, 144))
        self.connect((self.fec_bercurve_generator_0_1_0, 17), (self.qtgui_bercurve_sink_0, 145))
        self.connect((self.fec_bercurve_generator_0_1_0, 18), (self.qtgui_bercurve_sink_0, 146))
        self.connect((self.fec_bercurve_generator_0_1_0, 19), (self.qtgui_bercurve_sink_0, 147))
        self.connect((self.fec_bercurve_generator_0_1_0, 20), (self.qtgui_bercurve_sink_0, 148))
        self.connect((self.fec_bercurve_generator_0_1_0, 21), (self.qtgui_bercurve_sink_0, 149))
        self.connect((self.fec_bercurve_generator_0_1_0, 22), (self.qtgui_bercurve_sink_0, 150))
        self.connect((self.fec_bercurve_generator_0_1_0, 23), (self.qtgui_bercurve_sink_0, 151))
        self.connect((self.fec_bercurve_generator_0_1_0, 24), (self.qtgui_bercurve_sink_0, 152))
        self.connect((self.fec_bercurve_generator_0_1_0, 25), (self.qtgui_bercurve_sink_0, 153))
        self.connect((self.fec_bercurve_generator_0_1_0, 26), (self.qtgui_bercurve_sink_0, 154))
        self.connect((self.fec_bercurve_generator_0_1_0, 27), (self.qtgui_bercurve_sink_0, 155))
        self.connect((self.fec_bercurve_generator_0_1_0, 28), (self.qtgui_bercurve_sink_0, 156))
        self.connect((self.fec_bercurve_generator_0_1_0, 29), (self.qtgui_bercurve_sink_0, 157))
        self.connect((self.fec_bercurve_generator_0_1_0, 30), (self.qtgui_bercurve_sink_0, 158))
        self.connect((self.fec_bercurve_generator_0_1_0, 31), (self.qtgui_bercurve_sink_0, 159))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_curve_gen")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_framebits(self):
        return self.framebits

    def set_framebits(self, framebits):
        self.framebits = framebits

    def get_esno_0(self):
        return self.esno_0

    def set_esno_0(self, esno_0):
        self.esno_0 = esno_0

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_enc_tpc(self):
        return self.enc_tpc

    def set_enc_tpc(self, enc_tpc):
        self.enc_tpc = enc_tpc

    def get_enc_rep(self):
        return self.enc_rep

    def set_enc_rep(self, enc_rep):
        self.enc_rep = enc_rep

    def get_enc_ldpc(self):
        return self.enc_ldpc

    def set_enc_ldpc(self, enc_ldpc):
        self.enc_ldpc = enc_ldpc

    def get_enc_dummy(self):
        return self.enc_dummy

    def set_enc_dummy(self, enc_dummy):
        self.enc_dummy = enc_dummy

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_tpc(self):
        return self.dec_tpc

    def set_dec_tpc(self, dec_tpc):
        self.dec_tpc = dec_tpc

    def get_dec_rep(self):
        return self.dec_rep

    def set_dec_rep(self, dec_rep):
        self.dec_rep = dec_rep

    def get_dec_ldpc(self):
        return self.dec_ldpc

    def set_dec_ldpc(self, dec_ldpc):
        self.dec_ldpc = dec_ldpc

    def get_dec_dummy(self):
        return self.dec_dummy

    def set_dec_dummy(self, dec_dummy):
        self.dec_dummy = dec_dummy

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc


def main(top_block_cls=ber_curve_gen, options=None):

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
