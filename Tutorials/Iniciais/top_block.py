#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun 27 17:25:17 2019
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.D = D = 2
        self.C = C = 1

        ##################################################
        # Blocks
        ##################################################
        _D_sizer = wx.BoxSizer(wx.VERTICAL)
        self._D_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_D_sizer,
        	value=self.D,
        	callback=self.set_D,
        	label='D',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._D_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_D_sizer,
        	value=self.D,
        	callback=self.set_D,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_D_sizer)
        _C_sizer = wx.BoxSizer(wx.VERTICAL)
        self._C_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_C_sizer,
        	value=self.C,
        	callback=self.set_C,
        	label='C',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._C_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_C_sizer,
        	value=self.C,
        	callback=self.set_C,
        	minimum=0,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_C_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((C, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, D)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self._D_slider.set_value(self.D)
        self._D_text_box.set_value(self.D)
        self.blocks_delay_0.set_dly(self.D)

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C
        self._C_slider.set_value(self.C)
        self._C_text_box.set_value(self.C)
        self.blocks_multiply_const_vxx_0.set_k((self.C, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
