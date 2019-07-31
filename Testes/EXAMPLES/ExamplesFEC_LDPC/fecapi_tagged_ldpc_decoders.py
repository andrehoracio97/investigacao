#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fecapi Tagged Ldpc Decoders
# Generated: Thu Jul 25 17:29:28 2019
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


class fecapi_tagged_ldpc_decoders(gr.top_block, Qt.QWidget):

    def __init__(self, puncpat='11'):
        gr.top_block.__init__(self, "Fecapi Tagged Ldpc Decoders")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fecapi Tagged Ldpc Decoders")
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

        self.settings = Qt.QSettings("GNU Radio", "fecapi_tagged_ldpc_decoders")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.H_dec = H_dec = fec.ldpc_H_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 2)
        self.H = H = fec.ldpc_H_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 2)
        self.G_dec = G_dec = fec.ldpc_G_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0058_gen_matrix.alist")
        self.G = G = fec.ldpc_G_matrix(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0058_gen_matrix.alist")
        self.samp_rate = samp_rate = 50000
        self.length_tag = length_tag = "packet_len"


        self.ldpc_enc_H = ldpc_enc_H = fec.ldpc_par_mtrx_encoder_make_H(H)


        self.ldpc_enc_G = ldpc_enc_G = fec.ldpc_gen_mtrx_encoder_make(G)


        self.ldpc_enc = ldpc_enc = fec.ldpc_encoder_make(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist");


        self.ldpc_dec_H = ldpc_dec_H = fec.ldpc_bit_flip_decoder.make(H_dec.get_base_sptr(), 100)


        self.ldpc_dec_G = ldpc_dec_G = fec.ldpc_bit_flip_decoder.make(G_dec.get_base_sptr(), 100)


        self.ldpc_dec = ldpc_dec = fec.ldpc_decoder.make(gr.prefix() + "/share/gnuradio/fec/ldpc/" + "n_0100_k_0042_gap_02.alist", 0.5, 50);
        self.frame_size_H = frame_size_H = 42
        self.frame_size_G = frame_size_G = 58
        self.MTU_H = MTU_H = 1512
        self.MTU_G = MTU_G = 1508

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	'', #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.01)
        self.qtgui_time_sink_x_1_0.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, length_tag)
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

        labels = ['LDPC (G)', 'Input', 'Input', 'Input', '',
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
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	'', #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.01)
        self.qtgui_time_sink_x_1.set_y_axis(-0.5, 1.5)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, length_tag)
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['LDPC (alist)', 'LDPC (H)', 'Input', 'Input', '',
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

        for i in xrange(3):
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
        self.fec_extended_tagged_encoder_0_1 = fec.extended_tagged_encoder(encoder_obj_list=ldpc_enc_G, puncpat=puncpat, lentagname=length_tag, mtu=MTU_G)
        self.fec_extended_tagged_encoder_0_0 = fec.extended_tagged_encoder(encoder_obj_list=ldpc_enc_H, puncpat=puncpat, lentagname=length_tag, mtu=MTU_H)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=ldpc_enc, puncpat=puncpat, lentagname=length_tag, mtu=MTU_H)
        self.fec_extended_tagged_decoder_0_1 = self.fec_extended_tagged_decoder_0_1 = fec_extended_tagged_decoder_0_1 = fec.extended_tagged_decoder(decoder_obj_list=ldpc_dec_G, ann=None, puncpat=puncpat, integration_period=10000, lentagname=length_tag, mtu=MTU_G)
        self.fec_extended_tagged_decoder_0_0 = self.fec_extended_tagged_decoder_0_0 = fec_extended_tagged_decoder_0_0 = fec.extended_tagged_decoder(decoder_obj_list=ldpc_dec_H, ann=None, puncpat=puncpat, integration_period=10000, lentagname=length_tag, mtu=MTU_H)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=ldpc_dec, ann=None, puncpat=puncpat, integration_period=10000, lentagname=length_tag, mtu=MTU_H)
        self.digital_map_bb_0_1 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0_0 = digital.map_bb(([-1, 1]))
        self.digital_map_bb_0 = digital.map_bb(([-1, 1]))
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_b(4*[0, 0, 1, 0, 3, 0, 7, 0, 15, 0, 31, 0, 63, 0, 127, 0], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, frame_size_G, length_tag)
        self.blocks_stream_to_tagged_stream_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, frame_size_H, length_tag)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_LSB_FIRST)
        self.blocks_char_to_float_1_2 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1, 0), (self.fec_extended_tagged_decoder_0_0, 0))
        self.connect((self.blocks_char_to_float_1_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_char_to_float_1_0_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_char_to_float_1_0_0_0, 0), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.blocks_char_to_float_1_0_0_0_0, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.blocks_char_to_float_1_0_1, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_1_1, 0), (self.fec_extended_tagged_decoder_0_1, 0))
        self.connect((self.blocks_char_to_float_1_2, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_char_to_float_1_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_extended_tagged_encoder_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_char_to_float_1_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_extended_tagged_encoder_0_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_char_to_float_1_1, 0))
        self.connect((self.digital_map_bb_0_1, 0), (self.blocks_char_to_float_1_2, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_char_to_float_1_0_1, 0))
        self.connect((self.fec_extended_tagged_decoder_0_0, 0), (self.blocks_char_to_float_1_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0_1, 0), (self.blocks_char_to_float_1_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.digital_map_bb_0_1, 0))
        self.connect((self.fec_extended_tagged_encoder_0_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_1, 0), (self.digital_map_bb_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fecapi_tagged_ldpc_decoders")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_H_dec(self):
        return self.H_dec

    def set_H_dec(self, H_dec):
        self.H_dec = H_dec

    def get_H(self):
        return self.H

    def set_H(self, H):
        self.H = H

    def get_G_dec(self):
        return self.G_dec

    def set_G_dec(self, G_dec):
        self.G_dec = G_dec

    def get_G(self):
        return self.G

    def set_G(self, G):
        self.G = G

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_length_tag(self):
        return self.length_tag

    def set_length_tag(self, length_tag):
        self.length_tag = length_tag
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, self.length_tag)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.1, 0, 0, self.length_tag)

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

    def get_frame_size_H(self):
        return self.frame_size_H

    def set_frame_size_H(self, frame_size_H):
        self.frame_size_H = frame_size_H
        self.blocks_stream_to_tagged_stream_0_0_0.set_packet_len(self.frame_size_H)
        self.blocks_stream_to_tagged_stream_0_0_0.set_packet_len_pmt(self.frame_size_H)

    def get_frame_size_G(self):
        return self.frame_size_G

    def set_frame_size_G(self, frame_size_G):
        self.frame_size_G = frame_size_G
        self.blocks_stream_to_tagged_stream_0_0_0_0.set_packet_len(self.frame_size_G)
        self.blocks_stream_to_tagged_stream_0_0_0_0.set_packet_len_pmt(self.frame_size_G)

    def get_MTU_H(self):
        return self.MTU_H

    def set_MTU_H(self, MTU_H):
        self.MTU_H = MTU_H

    def get_MTU_G(self):
        return self.MTU_G

    def set_MTU_G(self, MTU_G):
        self.MTU_G = MTU_G


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=fecapi_tagged_ldpc_decoders, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
