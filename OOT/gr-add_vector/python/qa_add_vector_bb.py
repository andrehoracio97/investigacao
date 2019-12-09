#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 gr-add_vector author.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from add_vector_bb import add_vector_bb

class qa_add_vector_bb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
    	src_data = [0,1,2,3,4,5,6,7,8,9]
    	expected_result = [1,2,3,0,1,2,3,4,5,6]
    	#expected_result = (0,2,4,6,8,10,12,14,16,18)
    	
    	src = blocks.vector_source_f (src_data)
    	add = add_vector_bb ([1,2,3])
    	snk = blocks.vector_sink_f ()
    	self.tb.connect (src, add)
    	self.tb.connect (add, snk)
    	self.tb.run ()
    	result_data = snk.data()
    	#for i in range(len(snk.data())):
    	#	print(snk.data()[i])

    	self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_add_vector_bb, "qa_add_vector_bb.xml")
