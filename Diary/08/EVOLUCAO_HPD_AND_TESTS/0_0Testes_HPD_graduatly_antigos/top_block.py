#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Jul 23 16:44:03 2019
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import pmt
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.length_tag_key = length_tag_key = "packet_len"
        self.hsize = hsize = 96
        self.sym = sym = -1,1
        self.samp_rate = samp_rate = 32000
        self.header_formatter = header_formatter = digital.packet_header_default(hsize,length_tag_key)

        self.hdr_format = hdr_format = digital.header_format_default(digital.packet_utils.default_access_code, 1, 1)


        self.const = const = digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base()

        self.const.gen_soft_dec_lut(8)

        ##################################################
        # Blocks
        ##################################################
        self.digital_packet_headerparser_b_0_0 = digital.packet_headerparser_b(header_formatter)
        self.digital_packet_headergenerator_bb_0_0 = digital.packet_headergenerator_bb(header_formatter.formatter(), "packet_len")
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  hdr_format.header_nbits(),
        	  1,
        	  0,
        	  length_tag_key,
        	  length_tag_key,
        	  True,
        	  gr.sizeof_gr_complex,
        	  "rx_time",
                  samp_rate,
                  (),
                  0,
            )
        self.digital_constellation_decoder_cb_0_1 = digital.constellation_decoder_cb(const.base())
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(const.base())
        self.digital_chunks_to_symbols_xx_0_1 = digital.chunks_to_symbols_bc((const.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((const.points()), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, length_tag_key, 0)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, length_tag_key, 8)
        self.blocks_tag_debug_1_0 = blocks.tag_debug(gr.sizeof_char*1, 'Rx Bytes', ""); self.blocks_tag_debug_1_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 96, length_tag_key)
        self.blocks_repack_bits_bb_0_3_0 = blocks.repack_bits_bb(8, 1, length_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_3 = blocks.repack_bits_bb(8, 1, length_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0_0 = blocks.repack_bits_bb(const.bits_per_symbol(), 8, '', False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(const.bits_per_symbol(), 8, length_tag_key, False, gr.GR_LSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/transmit_maior.txt', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/transmitido/depois.txt', False)
        self.blocks_file_sink_0_1.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_0_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_tag_debug_1_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0_0, 0), (self.digital_packet_headerparser_b_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_3, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_3_0, 0), (self.digital_chunks_to_symbols_xx_0_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_repack_bits_bb_0_3, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_packet_headergenerator_bb_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_1, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_1, 0), (self.blocks_repack_bits_bb_0_0_0_0, 0))
        self.connect((self.digital_header_payload_demux_0, 1), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.digital_header_payload_demux_0, 0), (self.digital_constellation_decoder_cb_0_1, 0))
        self.connect((self.digital_packet_headergenerator_bb_0_0, 0), (self.blocks_repack_bits_bb_0_3_0, 0))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_default(self.hsize,self.length_tag_key))

    def get_hsize(self):
        return self.hsize

    def set_hsize(self, hsize):
        self.hsize = hsize
        self.set_header_formatter(digital.packet_header_default(self.hsize,self.length_tag_key))

    def get_sym(self):
        return self.sym

    def set_sym(self, sym):
        self.sym = sym

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
