#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import pmt
import random
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.value = value = int(random.random()*255)
        self.samp_rate = samp_rate = 15000000
        self.copy = copy = True

        ##################################################
        # Blocks
        ##################################################
        self._copy_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.copy,
        	callback=self.set_copy,
        	label='copy',
        	true=True,
        	false=False,
        )
        self.Add(self._copy_check_box)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.digital_scrambler_bb_0 = digital.scrambler_bb(0x19, 50, 7)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x19, 50, 7)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 1)
        self.blocks_repack_bits_bb_1_0_0_1_0 = blocks.repack_bits_bb(1, 8, '', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_MSB_FIRST)
        self.blocks_file_source_0_0_1_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/Files_To_Transmit/trasmit_10_mb.txt', False)
        self.blocks_file_source_0_0_1_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/Trasmited/depois.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_copy_0 = blocks.copy(gr.sizeof_char*1)
        self.blocks_copy_0.set_enabled(copy)
        self.blocks_char_to_float_1_0_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_0_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_copy_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_char_to_float_1_0_0, 0))
        self.connect((self.blocks_file_source_0_0_1_0, 0), (self.blocks_repack_bits_bb_1_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1, 0), (self.digital_scrambler_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_1_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_copy_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.blocks_repack_bits_bb_1_0_0_1_0, 0))
        self.connect((self.digital_scrambler_bb_0, 0), (self.blocks_throttle_0, 0))

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_copy(self):
        return self.copy

    def set_copy(self, copy):
        self.copy = copy
        self._copy_check_box.set_value(self.copy)
        self.blocks_copy_0.set_enabled(self.copy)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
