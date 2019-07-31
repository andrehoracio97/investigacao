#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fecapi Tagged Decoders
# Generated: Thu Jul 25 16:35:52 2019
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
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class fecapi_tagged_decoders(gr.top_block, Qt.QWidget):

    def __init__(self, MTU=1500, frame_size=30, puncpat='11'):
        gr.top_block.__init__(self, "Fecapi Tagged Decoders")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fecapi Tagged Decoders")
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

        self.settings = Qt.QSettings("GNU Radio", "fecapi_tagged_decoders")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.MTU = MTU
        self.frame_size = frame_size
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.rep = rep = 3
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.samp_rate = samp_rate = 50000
        self.length_tag = length_tag = "packet_len"


        self.enc_rep = enc_rep = map((lambda a: fec.repetition_encoder_make(MTU*8, rep)), range(0,1))


        self.enc_dummy = enc_dummy = map((lambda a: fec.repetition_encoder_make(MTU*8, 3)), range(0,1))


        self.enc_cc = enc_cc = fec.cc_encoder_make(MTU*8, k, rate, (polys), 0, fec.CC_TERMINATED, True)



        self.dec_rep = dec_rep = map( (lambda a: fec.repetition_decoder.make(MTU*8, rep, 0.5)), range(0,1) )


        self.dec_dummy = dec_dummy = map((lambda a: fec.dummy_decoder.make(MTU*8)), range(0,1))


        self.dec_cc = dec_cc = map( (lambda a: fec.cc_decoder.make(MTU*8, k, rate, (polys), 0, -1, fec.CC_TERMINATED, True)), range(0,1) );

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	'', #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.01)
        self.qtgui_time_sink_x_1.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['None', 'Rep (Rate=3)', 'CC (K=7, Rate=2)', '', '',
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
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.fec_extended_tagged_encoder_0_1 = fec.extended_tagged_encoder(encoder_obj_list=enc_cc, puncpat='11', lentagname=length_tag, mtu=MTU)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=enc_dummy, puncpat=puncpat, lentagname=length_tag, mtu=MTU)
        self.fec_extended_tagged_decoder_0_1 = self.fec_extended_tagged_decoder_0_1 = fec_extended_tagged_decoder_0_1 = fec.extended_tagged_decoder(decoder_obj_list=dec_cc, ann=None, puncpat=puncpat, integration_period=10000, lentagname=length_tag, mtu=MTU)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=dec_dummy, ann=None, puncpat=puncpat, integration_period=10000, lentagname=length_tag, mtu=MTU)
        self.digital_map_bb_0_1 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0_0 = digital.map_bb(([-1, 1]))
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_b(4*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, frame_size, length_tag)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_LSB_FIRST)
        self.blocks_char_to_float_1_2 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_0_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_1_1, 0), (self.fec_extended_tagged_decoder_0_1, 0))
        self.connect((self.blocks_char_to_float_1_2, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_1_1, 0))
        self.connect((self.digital_map_bb_0_1, 0), (self.blocks_char_to_float_1_2, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.fec_extended_tagged_decoder_0_1, 0), (self.blocks_char_to_float_1_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.digital_map_bb_0_1, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.digital_map_bb_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fecapi_tagged_decoders")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MTU(self):
        return self.MTU

    def set_MTU(self, MTU):
        self.MTU = MTU

    def get_frame_size(self):
        return self.frame_size

    def set_frame_size(self, frame_size):
        self.frame_size = frame_size
        self.blocks_stream_to_tagged_stream_0_0_0.set_packet_len(self.frame_size)
        self.blocks_stream_to_tagged_stream_0_0_0.set_packet_len_pmt(self.frame_size)

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_length_tag(self):
        return self.length_tag

    def set_length_tag(self, length_tag):
        self.length_tag = length_tag

    def get_enc_rep(self):
        return self.enc_rep

    def set_enc_rep(self, enc_rep):
        self.enc_rep = enc_rep

    def get_enc_dummy(self):
        return self.enc_dummy

    def set_enc_dummy(self, enc_dummy):
        self.enc_dummy = enc_dummy

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_rep(self):
        return self.dec_rep

    def set_dec_rep(self, dec_rep):
        self.dec_rep = dec_rep

    def get_dec_dummy(self):
        return self.dec_dummy

    def set_dec_dummy(self, dec_dummy):
        self.dec_dummy = dec_dummy

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--MTU", dest="MTU", type="intx", default=1500,
        help="Set MTU [default=%default]")
    parser.add_option(
        "", "--frame-size", dest="frame_size", type="intx", default=30,
        help="Set Frame Size [default=%default]")
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=fecapi_tagged_decoders, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(MTU=options.MTU, frame_size=options.frame_size, puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
