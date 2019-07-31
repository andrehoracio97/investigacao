#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Tx Stage0
# Generated: Mon Jul 22 12:38:01 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt


class tx_stage0(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Tx Stage0")

        ##################################################
        # Blocks
        ##################################################
        self.blocks_random_pdu_0 = blocks.random_pdu(15, 150, chr(0xff), 1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.PMT_T, 2000)
        self.blocks_message_debug_0 = blocks.message_debug()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.blocks_message_debug_0, 'print_pdu'))


def main(top_block_cls=tx_stage0, options=None):

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
