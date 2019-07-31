#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Stage2
# Generated: Mon Jul 22 12:41:18 2019
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class tx_stage2(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Tx Stage2")

        ##################################################
        # Variables
        ##################################################


        self.enc = enc = fec.repetition_encoder_make(8000, 3)


        ##################################################
        # Blocks
        ##################################################
        self.fec_async_encoder_0 = fec.async_encoder(enc, True, False, False, 1500)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.blocks_random_pdu_0 = blocks.random_pdu(15, 50, chr(0xff), 1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.PMT_T, 2000)
        self.blocks_message_debug_0 = blocks.message_debug()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.digital_crc32_async_bb_1, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.fec_async_encoder_0, 'in'))
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))

    def get_enc(self):
        return self.enc

    def set_enc(self, enc):
        self.enc = enc


def main(top_block_cls=tx_stage2, options=None):

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
