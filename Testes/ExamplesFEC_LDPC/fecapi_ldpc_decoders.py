#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fecapi Ldpc Decoders
# Generated: Wed Jul 17 11:09:15 2019
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


class fecapi_ldpc_decoders(gr.top_block, Qt.QWidget):

    def __init__(self, frame_size=100, puncpat='11'):
        gr.top_block.__init__(self, "Fecapi Ldpc Decoders")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fecapi Ldpc Decoders")
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

        self.settings = Qt.QSettings("GNU Radio", "fecapi_ldpc_decoders")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.frame_size = frame_size
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.H = H = fec.ldpc_H_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 2)
        self.G = G = fec.ldpc_G_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0058_gen_matrix.alist")
        self.samp_rate = samp_rate = 50000


        self.ldpc_enc_H = ldpc_enc_H = fec.ldpc_par_mtrx_encoder_make_H(H)


        self.ldpc_enc_G = ldpc_enc_G = fec.ldpc_gen_mtrx_encoder_make(G)


        self.ldpc_enc = ldpc_enc = fec.ldpc_encoder_make(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist");


        self.ldpc_dec_H = ldpc_dec_H = fec.ldpc_bit_flip_decoder.make(H.get_base_sptr(), 100)


        self.ldpc_dec_G = ldpc_dec_G = fec.ldpc_bit_flip_decoder.make(G.get_base_sptr(), 100)


        self.ldpc_dec = ldpc_dec = fec.ldpc_decoder.make(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 0.5, 50);

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	'', #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Input', 'LDPC (alist)', 'LDPC (H)', 'LDPC (G)', 'CCSDS',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 0.6, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.fec_extended_encoder_1_0_0 = fec.extended_encoder(encoder_obj_list=ldpc_enc, threading= None, puncpat=puncpat)
        self.fec_extended_encoder_1_0 = fec.extended_encoder(encoder_obj_list=ldpc_enc_H, threading= None, puncpat=puncpat)
        self.fec_extended_encoder_1 = fec.extended_encoder(encoder_obj_list=ldpc_enc_G, threading= None, puncpat=puncpat)
        self.fec_extended_decoder_0_1_0 = fec.extended_decoder(decoder_obj_list=ldpc_dec, threading= None, ann=None, puncpat=puncpat, integration_period=10000)
        self.fec_extended_decoder_0_1 = fec.extended_decoder(decoder_obj_list=ldpc_dec_H, threading= None, ann=None, puncpat=puncpat, integration_period=10000)
        self.fec_extended_decoder_0 = fec.extended_decoder(decoder_obj_list=ldpc_dec_G, threading= None, ann=None, puncpat=puncpat, integration_period=10000)
        self.digital_map_bb_0_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0_0_0 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0_0 = digital.map_bb(([-1, 1]))
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_b((frame_size/15)*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], True, 1, [])
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_char_to_float_0_2_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_2 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.fec_extended_decoder_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_char_to_float_0_0_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0_2, 0), (self.fec_extended_decoder_0_1, 0))
        self.connect((self.blocks_char_to_float_0_2_0, 0), (self.fec_extended_decoder_0_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_1_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.fec_extended_encoder_1_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_map_bb_0_0_0, 0), (self.blocks_char_to_float_0_2, 0))
        self.connect((self.digital_map_bb_0_0_0_0, 0), (self.blocks_char_to_float_0_2_0, 0))
        self.connect((self.fec_extended_decoder_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.fec_extended_decoder_0_1, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.fec_extended_decoder_0_1_0, 0), (self.blocks_char_to_float_0_0_0_0, 0))
        self.connect((self.fec_extended_encoder_1, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.fec_extended_encoder_1_0, 0), (self.digital_map_bb_0_0_0, 0))
        self.connect((self.fec_extended_encoder_1_0_0, 0), (self.digital_map_bb_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fecapi_ldpc_decoders")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_size(self, frame_size):
        self.frame_size = frame_size
        self.blocks_vector_source_x_0_1_0.set_data((self.frame_size/15)*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127], [])

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_H(self):
        return self.H

    def set_H(self, H):
        self.H = H

    def get_G(self):
        return self.G

    def set_G(self, G):
        self.G = G

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_ldpc_enc_H(self):
        return self.ldpc_enc_H

    def set_ldpc_enc_H(self, ldpc_enc_H):
        self.ldpc_enc_H = ldpc_enc_H

    def get_ldpc_enc_G(self):
        return self.ldpc_enc_G

    def set_ldpc_enc_G(self, ldpc_enc_G):
        self.ldpc_enc_G = ldpc_enc_G

    def get_ldpc_enc(self):
        return self.ldpc_enc

    def set_ldpc_enc(self, ldpc_enc):
        self.ldpc_enc = ldpc_enc

    def get_ldpc_dec_H(self):
        return self.ldpc_dec_H

    def set_ldpc_dec_H(self, ldpc_dec_H):
        self.ldpc_dec_H = ldpc_dec_H

    def get_ldpc_dec_G(self):
        return self.ldpc_dec_G

    def set_ldpc_dec_G(self, ldpc_dec_G):
        self.ldpc_dec_G = ldpc_dec_G

    def get_ldpc_dec(self):
        return self.ldpc_dec

    def set_ldpc_dec(self, ldpc_dec):
        self.ldpc_dec = ldpc_dec


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--frame-size", dest="frame_size", type="intx", default=100,
        help="Set Frame Size [default=%default]")
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=fecapi_ldpc_decoders, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(frame_size=options.frame_size, puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
