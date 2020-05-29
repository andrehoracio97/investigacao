#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jul 29 10:20:28 2019
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

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.pkt_len = pkt_len = 100
        self.k = k = 7
        self.samp_rate = samp_rate = 320000
        self.puncpat = puncpat = '11'


        self.pld_enc = pld_enc = fec.cc_encoder_make((pkt_len*8), k, rate, (polys), 0, fec.CC_TERMINATED, True)



        self.pld_dec = pld_dec = fec.cc_decoder.make(800, k, rate, (polys), 0, -1, fec.CC_TERMINATED, True)


        self.pld_const = pld_const = digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base()

        self.pld_const.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=pld_enc, puncpat=puncpat, lentagname="packet_len", mtu=pkt_len)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=pld_dec, ann=None, puncpat=puncpat, integration_period=10000, lentagname='', mtu=800)
        self.digital_map_bb_1_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(pld_const)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, True)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_tag_debug_0_0 = blocks.tag_debug(gr.sizeof_float*1, 'SAI_DECODER', ""); self.blocks_tag_debug_0_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, pkt_len, "packet_len")
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1_1_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", True, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/book.txt', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/transmitido/depois.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_1_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.blocks_tag_debug_0_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.digital_map_bb_1_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_repack_bits_bb_0_1_1_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
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

    def get_pkt_len(self):
        return self.pkt_len

    def set_pkt_len(self, pkt_len):
        self.pkt_len = pkt_len
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.pkt_len)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.pkt_len)

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_pld_enc(self):
        return self.pld_enc

    def set_pld_enc(self, pld_enc):
        self.pld_enc = pld_enc

    def get_pld_dec(self):
        return self.pld_dec

    def set_pld_dec(self, pld_dec):
        self.pld_dec = pld_dec

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const


def main(top_block_cls=top_block, options=None):

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
