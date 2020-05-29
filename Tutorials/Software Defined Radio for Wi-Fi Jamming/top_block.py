#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Software Defined Radio for Wi-Fi Jamming
# Generated: Tue Jul  2 09:36:19 2019
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Software Defined Radio for Wi-Fi Jamming")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sample_rate_1_0 = sample_rate_1_0 = 32000
        self.sample_rate_1 = sample_rate_1 = 32000
        self.samp_rate = samp_rate = 250000
        self.gain_0 = gain_0 = 0
        self.gain = gain = 0
        self.freq_0 = freq_0 = 2442000000
        self.freq = freq = 2442000000

        ##################################################
        # Blocks
        ##################################################
        _sample_rate_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sample_rate_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sample_rate_1_sizer,
        	value=self.sample_rate_1,
        	callback=self.set_sample_rate_1,
        	label='Sample Rate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sample_rate_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sample_rate_1_sizer,
        	value=self.sample_rate_1,
        	callback=self.set_sample_rate_1,
        	minimum=0,
        	maximum=20000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sample_rate_1_sizer)
        _gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	label='Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_sizer,
        	value=self.gain,
        	callback=self.set_gain,
        	minimum=0,
        	maximum=90,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_sizer)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq,
        	callback=self.set_freq,
        	label='Frequencia',
        	converter=forms.float_converter(),
        )
        self.Add(self._freq_text_box)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("serial=F5EAC0", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_samp_rate(sample_rate_1)
        self.uhd_usrp_sink_0_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("serial=F5EAE1", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_rate(30.72e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_samp_rate(sample_rate_1)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        _sample_rate_1_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sample_rate_1_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sample_rate_1_0_sizer,
        	value=self.sample_rate_1_0,
        	callback=self.set_sample_rate_1_0,
        	label='Sample Rate',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sample_rate_1_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sample_rate_1_0_sizer,
        	value=self.sample_rate_1_0,
        	callback=self.set_sample_rate_1_0,
        	minimum=0,
        	maximum=20000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sample_rate_1_0_sizer)
        _gain_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain_0_sizer,
        	value=self.gain_0,
        	callback=self.set_gain_0,
        	label='Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain_0_sizer,
        	value=self.gain_0,
        	callback=self.set_gain_0,
        	minimum=0,
        	maximum=90,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gain_0_sizer)
        self._freq_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.freq_0,
        	callback=self.set_freq_0,
        	label='Frequencia',
        	converter=forms.float_converter(),
        )
        self.Add(self._freq_0_text_box)
        self.analog_fastnoise_source_x_0_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 0, 8192)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.analog_fastnoise_source_x_0_0, 0), (self.uhd_usrp_sink_0_0, 0))

    def get_sample_rate_1_0(self):
        return self.sample_rate_1_0

    def set_sample_rate_1_0(self, sample_rate_1_0):
        self.sample_rate_1_0 = sample_rate_1_0
        self._sample_rate_1_0_slider.set_value(self.sample_rate_1_0)
        self._sample_rate_1_0_text_box.set_value(self.sample_rate_1_0)

    def get_sample_rate_1(self):
        return self.sample_rate_1

    def set_sample_rate_1(self, sample_rate_1):
        self.sample_rate_1 = sample_rate_1
        self._sample_rate_1_slider.set_value(self.sample_rate_1)
        self._sample_rate_1_text_box.set_value(self.sample_rate_1)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.sample_rate_1)
        self.uhd_usrp_sink_0.set_samp_rate(self.sample_rate_1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_gain_0(self):
        return self.gain_0

    def set_gain_0(self, gain_0):
        self.gain_0 = gain_0
        self._gain_0_slider.set_value(self.gain_0)
        self._gain_0_text_box.set_value(self.gain_0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self._gain_slider.set_value(self.gain)
        self._gain_text_box.set_value(self.gain)
        self.uhd_usrp_sink_0_0.set_gain(self.gain, 0)

        self.uhd_usrp_sink_0.set_gain(self.gain, 0)


    def get_freq_0(self):
        return self.freq_0

    def set_freq_0(self, freq_0):
        self.freq_0 = freq_0
        self._freq_0_text_box.set_value(self.freq_0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_text_box.set_value(self.freq)
        self.uhd_usrp_sink_0_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
