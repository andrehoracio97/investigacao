#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Stage3
# Generated: Mon Jul 22 12:43:31 2019
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class tx_stage3(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Tx Stage3")

        ##################################################
        # Variables
        ##################################################
        self.thresh = thresh = 3
        self.bps = bps = 2
        self.hdr_format = hdr_format = digital.header_format_counter(digital.packet_utils.default_access_code, thresh, bps)

        ##################################################
        # Blocks
        ##################################################
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.blocks_random_pdu_0 = blocks.random_pdu(15, 50, chr(0xff), 1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.PMT_T, 2000)
        self.blocks_message_debug_0 = blocks.message_debug()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_1, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.digital_protocol_formatter_async_0, 'in'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.blocks_message_debug_0, 'print_pdu'))

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.set_hdr_format(digital.header_format_counter(digital.packet_utils.default_access_code, self.thresh, self.bps))

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_hdr_format(digital.header_format_counter(digital.packet_utils.default_access_code, self.thresh, self.bps))

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format


def main(top_block_cls=tx_stage3, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
