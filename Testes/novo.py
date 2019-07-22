#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Novo
# Generated: Mon Jul 22 19:32:57 2019
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


class novo(gr.top_block, Qt.QWidget):

    def __init__(self, hdr_const=digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base(), hdr_dec= fec.dummy_decoder.make(8000), hdr_enc= fec.dummy_encoder_make(8000), hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0), pld_const=digital.constellation_calcdist((digital.psk_2()[0]), (digital.psk_2()[1]), 2, 1).base()):
        gr.top_block.__init__(self, "Novo")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Novo")
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

        self.settings = Qt.QSettings("GNU Radio", "novo")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.hdr_const = hdr_const
        self.hdr_dec = hdr_dec
        self.hdr_enc = hdr_enc
        self.hdr_format = hdr_format
        self.pld_const = pld_const

        ##################################################
        # Variables
        ##################################################
        self.spb = spb = 4.0
        self.rolloff = rolloff = 0.35
        self.nfilts = nfilts = 32

        self.const = const = digital.constellation_qpsk().base()

        self.ac_hex = ac_hex = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.time_bw = time_bw = 0
        self.samp_rate = samp_rate = 32000
        self.rxmod = rxmod = digital.qpsk_constellation()
        self.rrctaps = rrctaps = firdes.root_raised_cosine(nfilts,1.0,1.0/(nfilts*spb), rolloff, int(11*spb*nfilts))
        self.phase_bw = phase_bw = 0
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(digital.generic_mod(const, False, spb, True, rolloff, False, False) .to_basic_block(), (ac_hex), ([1]))
        self.mark_delay = mark_delay = 87
        self.freq_bw = freq_bw = 0
        self.ac = ac = map(lambda x: int(x), list(digital.packet_utils.default_access_code))

        ##################################################
        # Blocks
        ##################################################
        self._time_bw_range = Range(0, .1, .001, 0, 200)
        self._time_bw_win = RangeWidget(self._time_bw_range, self.set_time_bw, 'Timing Loop BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._time_bw_win, 5, 2, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_bw_range = Range(0, .05, .001, 0, 200)
        self._freq_bw_win = RangeWidget(self._freq_bw_range, self.set_freq_bw, 'FLL Bandwidth', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_bw_win, 4, 2, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phase_bw_range = Range(0, .1, .001, 0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, 'Costas Loop (Phase) Bandwidth', "counter_slider", float)
        self.top_grid_layout.addWidget(self._phase_bw_win, 7, 2, 1, 1)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  spb,
                  taps=(firdes.root_raised_cosine(nfilts, 1.0, 1.0/nfilts, rolloff, int(11*spb*nfilts))),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.fec_async_encoder_0_0 = fec.async_encoder(hdr_enc, True, False, False, 1500)
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_pfb_clock_sync_xxx_0_1 = digital.pfb_clock_sync_ccf(spb, time_bw, (rrctaps), nfilts, 16, 1.5, 1)
        self.digital_fll_band_edge_cc_0_0 = digital.fll_band_edge_cc(spb, rolloff, 44, freq_bw)
        self.digital_corr_est_cc_0 = digital.corr_est_cc((modulated_sync_word), spb, mark_delay, 0.999)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((const.points()), 1)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0,
        	frequency_offset=0,
        	epsilon=1,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, 'packet_len', 0)
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'packet_len', spb)
        self.blocks_tag_debug_0_2_1_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'CORRELATION', ""); self.blocks_tag_debug_0_2_1_0.set_display(True)
        self.blocks_tag_debug_0_2_1 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'POLYFASE', ""); self.blocks_tag_debug_0_2_1.set_display(True)
        self.blocks_tag_debug_0_2_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'MODULATOR', ""); self.blocks_tag_debug_0_2_0.set_display(True)
        self.blocks_tag_debug_0_2 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'MULTIPLY', ""); self.blocks_tag_debug_0_2.set_display(True)
        self.blocks_tag_debug_0_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'MUX', ""); self.blocks_tag_debug_0_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 96, "packet_len")
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, const.bits_per_symbol(), 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, const.bits_per_symbol(), 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_0_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/andre/Desktop/transmit_maior.txt', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_protocol_formatter_async_0, 'in'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.blocks_pdu_to_tagged_stream_0_1, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.fec_async_encoder_0_0, 'in'))
        self.msg_connect((self.fec_async_encoder_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0, 'pdus'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.blocks_tag_debug_0_2, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.blocks_tag_debug_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_fll_band_edge_cc_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_tag_debug_0_2_1_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.digital_corr_est_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_1, 0), (self.blocks_tag_debug_0_2_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tag_debug_0_2_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "novo")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_hdr_const(self):
        return self.hdr_const

    def set_hdr_const(self, hdr_const):
        self.hdr_const = hdr_const

    def get_hdr_dec(self):
        return self.hdr_dec

    def set_hdr_dec(self, hdr_dec):
        self.hdr_dec = hdr_dec

    def get_hdr_enc(self):
        return self.hdr_enc

    def set_hdr_enc(self, hdr_enc):
        self.hdr_enc = hdr_enc

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_pld_const(self):
        return self.pld_const

    def set_pld_const(self, pld_const):
        self.pld_const = pld_const

    def get_spb(self):
        return self.spb

    def set_spb(self, spb):
        self.spb = spb
        self.set_rrctaps(firdes.root_raised_cosine(self.nfilts,1.0,1.0/(self.nfilts*self.spb), self.rolloff, int(11*self.spb*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, 1.0, 1.0/self.nfilts, self.rolloff, int(11*self.spb*self.nfilts))))
        self.pfb_arb_resampler_xxx_0.set_rate(self.spb)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(self.spb)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_rrctaps(firdes.root_raised_cosine(self.nfilts,1.0,1.0/(self.nfilts*self.spb), self.rolloff, int(11*self.spb*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, 1.0, 1.0/self.nfilts, self.rolloff, int(11*self.spb*self.nfilts))))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrctaps(firdes.root_raised_cosine(self.nfilts,1.0,1.0/(self.nfilts*self.spb), self.rolloff, int(11*self.spb*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, 1.0, 1.0/self.nfilts, self.rolloff, int(11*self.spb*self.nfilts))))

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const

    def get_ac_hex(self):
        return self.ac_hex

    def set_ac_hex(self, ac_hex):
        self.ac_hex = ac_hex

    def get_time_bw(self):
        return self.time_bw

    def set_time_bw(self, time_bw):
        self.time_bw = time_bw
        self.digital_pfb_clock_sync_xxx_0_1.set_loop_bandwidth(self.time_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_rrctaps(self):
        return self.rrctaps

    def set_rrctaps(self, rrctaps):
        self.rrctaps = rrctaps
        self.digital_pfb_clock_sync_xxx_0_1.update_taps((self.rrctaps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_mark_delay(self):
        return self.mark_delay

    def set_mark_delay(self, mark_delay):
        self.mark_delay = mark_delay
        self.digital_corr_est_cc_0.set_mark_delay(self.mark_delay)

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw
        self.digital_fll_band_edge_cc_0_0.set_loop_bandwidth(self.freq_bw)

    def get_ac(self):
        return self.ac

    def set_ac(self, ac):
        self.ac = ac


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=novo, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

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
