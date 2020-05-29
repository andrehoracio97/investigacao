#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Evolucao
# Generated: Wed Jul 24 13:13:03 2019
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
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sys
from gnuradio import qtgui


class evolucao(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Evolucao")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Evolucao")
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

        self.settings = Qt.QSettings("GNU Radio", "evolucao")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################

        self.pld_const = pld_const = digital.constellation_calcdist((digital.psk_4()[0]), (digital.psk_4()[1]), 4, 1).base()

        self.pld_const.gen_soft_dec_lut(8)
        self.sps = sps = 2
        self.rep = rep = 3
        self.preamble_rep = preamble_rep = [0xe3, 0x8f, 0xc0, 0xfc, 0x7f, 0xc7, 0xe3, 0x81, 0xc0, 0xff, 0x80, 0x38, 0xff, 0xf0, 0x38, 0xe0, 0x0f, 0xc0, 0x03, 0x80, 0x00, 0xff, 0xff, 0xc0]
        self.preamble_dummy = preamble_dummy = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.nfilts = nfilts = 32
        self.hdr_format = hdr_format = digital.header_format_counter(digital.packet_utils.default_access_code, 3, pld_const.bits_per_symbol())
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.rate = rate = 2
        self.preamble_select = preamble_select = {1: preamble_dummy, 3: preamble_rep}

        self.hdr_const = hdr_const = digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base()

        self.hdr_const.gen_soft_dec_lut(8)


        self.dec_hdr = dec_hdr = fec.repetition_decoder.make(hdr_format.header_nbits(), rep, 0.5)

        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.rxmod = rxmod = digital.generic_mod(hdr_const, False, sps, True, eb, False, False)
        self.preamble = preamble = preamble_select[int(1.0/dec_hdr.rate())]
        self.polys = polys = [109, 79]
        self.mark_delays = mark_delays = [0, 0, 34, 56, 87, 119]
        self.k = k = 7
        self.time_offset = time_offset = 1.0
        self.sps_0 = sps_0 = 2
        self.samp_rate = samp_rate = 32000

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, eb, 11*sps*nfilts)

        self.noise = noise = 0.0
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), (preamble), ([1]))
        self.mark_delay = mark_delay = mark_delays[sps]
        self.freq_offset = freq_offset = 0
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2


        self.enc_hdr = enc_hdr = fec.repetition_encoder_make(8000, rep)



        self.enc = enc = fec.cc_encoder_make(8000, k, rate, (polys), 0, fec.CC_TERMINATED, False)



        self.dec = dec = fec.cc_decoder.make(8000, k, rate, (polys), 0, -1, fec.CC_TERMINATED, False)

        self.amp = amp = 1.0

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.99, 1.01, 0.00001, 1.0, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Time Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._noise_range = Range(0, 5, 0.01, 0.0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise Amp', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_offset_range = Range(-0.5, 0.5, 0.0001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Freq. Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._amp_range = Range(0, 2, 0.01, 1.0, 200)
        self._amp_win = RangeWidget(self._amp_range, self.set_amp, 'Amplitude', "counter_slider", float)
        self.top_grid_layout.addWidget(self._amp_win)
        self.tab1 = Qt.QTabWidget()
        self.tab1_widget_0 = Qt.QWidget()
        self.tab1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_0)
        self.tab1_grid_layout_0 = Qt.QGridLayout()
        self.tab1_layout_0.addLayout(self.tab1_grid_layout_0)
        self.tab1.addTab(self.tab1_widget_0, 'Time')
        self.tab1_widget_1 = Qt.QWidget()
        self.tab1_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_1)
        self.tab1_grid_layout_1 = Qt.QGridLayout()
        self.tab1_layout_1.addLayout(self.tab1_grid_layout_1)
        self.tab1.addTab(self.tab1_widget_1, 'Freq.')
        self.tab1_widget_2 = Qt.QWidget()
        self.tab1_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab1_widget_2)
        self.tab1_grid_layout_2 = Qt.QGridLayout()
        self.tab1_layout_2.addLayout(self.tab1_grid_layout_2)
        self.tab1.addTab(self.tab1_widget_2, 'Const.')
        self.top_grid_layout.addWidget(self.tab1, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self.fec_generic_decoder_0 = fec.decoder(dec_hdr, gr.sizeof_float, gr.sizeof_char)
        self.fec_async_encoder_0_0 = fec.async_encoder(enc, True, False, False, 1500)
        self.fec_async_encoder_0 = fec.async_encoder(enc, True, False, False, 1500)
        self.fec_async_decoder_0 = fec.async_decoder(dec_hdr, True, False, 1500*8)
        self.digital_protocol_parser_b_0 = digital.protocol_parser_b(hdr_format)
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 6.28/400.0, (rx_rrc_taps), nfilts, nfilts/2, 1.5, 1)
        self.digital_map_bb_1_0 = digital.map_bb((pld_const.pre_diff_code()))
        self.digital_map_bb_1 = digital.map_bb((hdr_const.pre_diff_code()))
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  (hdr_format.header_nbits() * int(1.0/dec_hdr.rate())) /  hdr_const.bits_per_symbol(),
        	  1,
        	  0,
        	  "payload symbols",
        	  "time_est",
        	  True,
        	  gr.sizeof_gr_complex,
        	  "rx_time",
                  1,
                  "",
                  0,
            )
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.digital_costas_loop_cc_0_0_0 = digital.costas_loop_cc(6.28/200.0, pld_const.arity(), False)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(6.28/200.0, hdr_const.arity(), False)
        self.digital_corr_est_cc_0 = digital.corr_est_cc((modulated_sync_word), sps, mark_delay, 0.999)
        self.digital_constellation_soft_decoder_cf_0_0 = digital.constellation_soft_decoder_cf(hdr_const)
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(pld_const)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((pld_const.points()), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((hdr_const.points()), 1)
        self.digital_burst_shaper_xx_0 = digital.burst_shaper_cc((firdes.window(firdes.WIN_HANN, 20, 0)), 0, filt_delay, True, 'packet_len')
        (self.digital_burst_shaper_xx_0).set_block_alias("burst_shaper0")
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_to_pdu_0_0 = blocks.tagged_stream_to_pdu(blocks.float_t, "payload symbols")
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'pacote')
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, 'packet_len', 0)
        self.blocks_tagged_stream_multiply_length_0_0 = blocks.tagged_stream_multiply_length(gr.sizeof_float*1, "payload symbols", pld_const.bits_per_symbol())
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'packet_len', sps)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 100, 'pacote')
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, pld_const.bits_per_symbol(), 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, hdr_const.bits_per_symbol(), 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((amp, ))
        self.blocks_multiply_by_tag_value_cc_0 = blocks.multiply_by_tag_value_cc("amp_est", 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/transmit_maior.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/andre/Desktop/transmitido/depois.txt', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc32_async_bb_1, 'in'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0_0, 'pdus'), (self.fec_async_decoder_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.fec_async_encoder_0, 'in'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.fec_async_encoder_0_0, 'in'))
        self.msg_connect((self.digital_protocol_parser_b_0, 'info'), (self.digital_header_payload_demux_0, 'header_data'))
        self.msg_connect((self.fec_async_decoder_0, 'out'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.digital_protocol_formatter_async_0, 'in'))
        self.msg_connect((self.fec_async_encoder_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_by_tag_value_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.digital_corr_est_cc_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_map_bb_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0_0, 0), (self.blocks_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_burst_shaper_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_burst_shaper_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.blocks_tagged_stream_multiply_length_0_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0_0, 0), (self.fec_generic_decoder_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_multiply_by_tag_value_cc_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_soft_decoder_cf_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_header_payload_demux_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_header_payload_demux_0, 1), (self.digital_costas_loop_cc_0_0_0, 0))
        self.connect((self.digital_map_bb_1, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_map_bb_1_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.fec_generic_decoder_0, 0), (self.digital_protocol_parser_b_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "evolucao")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_mark_delay(self.mark_delays[self.sps])
        self.set_rxmod(digital.generic_mod(self.hdr_const, False, self.sps, True, self.eb, False, False))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(self.sps)

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_preamble_rep(self):
        return self.preamble_rep

    def set_preamble_rep(self, preamble_rep):
        self.preamble_rep = preamble_rep
        self.set_preamble_select({1: self.preamble_dummy, 3: self.preamble_rep})

    def get_preamble_dummy(self):
        return self.preamble_dummy

    def set_preamble_dummy(self, preamble_dummy):
        self.preamble_dummy = preamble_dummy
        self.set_preamble_select({1: self.preamble_dummy, 3: self.preamble_rep})

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rxmod(digital.generic_mod(self.hdr_const, False, self.sps, True, self.eb, False, False))

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_rrc_taps))

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_preamble_select(self):
        return self.preamble_select

    def set_preamble_select(self, preamble_select):
        self.preamble_select = preamble_select
        self.set_preamble(self.preamble_select[int(1.0/dec_hdr.rate())])

    def get_hdr_const(self):
        return self.hdr_const

    def set_hdr_const(self, hdr_const):
        self.hdr_const = hdr_const
        self.set_rxmod(digital.generic_mod(self.hdr_const, False, self.sps, True, self.eb, False, False))

    def get_dec_hdr(self):
        return self.dec_hdr

    def set_dec_hdr(self, dec_hdr):
        self.dec_hdr = dec_hdr

    def get_taps_per_filt(self):
        return self.taps_per_filt

    def set_taps_per_filt(self, taps_per_filt):
        self.taps_per_filt = taps_per_filt
        self.set_filt_delay(1+(self.taps_per_filt-1)/2)

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_mark_delays(self):
        return self.mark_delays

    def set_mark_delays(self, mark_delays):
        self.mark_delays = mark_delays
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_sps_0(self):
        return self.sps_0

    def set_sps_0(self, sps_0):
        self.sps_0 = sps_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rx_rrc_taps))

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_mark_delay(self):
        return self.mark_delay

    def set_mark_delay(self, mark_delay):
        self.mark_delay = mark_delay
        self.digital_corr_est_cc_0.set_mark_delay(self.mark_delay)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay

    def get_enc_hdr(self):
        return self.enc_hdr

    def set_enc_hdr(self, enc_hdr):
        self.enc_hdr = enc_hdr

    def get_enc(self):
        return self.enc

    def set_enc(self, enc):
        self.enc = enc

    def get_dec(self):
        return self.dec

    def set_dec(self, dec):
        self.dec = dec

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self.blocks_multiply_const_vxx_0.set_k((self.amp, ))


def main(top_block_cls=evolucao, options=None):

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
