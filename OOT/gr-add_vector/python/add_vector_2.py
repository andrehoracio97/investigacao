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

import numpy
from gnuradio import gr

class add_vector_2(gr.sync_block):
    """
    docstring for block add_vector_2
    """
    def __init__(self, vec):
        self.vec=vec
        self.index_vector=0
        self.data_fifo = []
        gr.sync_block.__init__(self,
            name="add_vector_2",
            in_sig=[numpy.int8],
            out_sig=[numpy.int8])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]


        for i in range(len(in0)):
            if self.index_vector<len(self.vec):
                self.data_fifo.append(in0[i])
                out[i]=self.vec[self.index_vector]
                self.index_vector=self.index_vector+1
                #print(out[i])
            else:
                out[i]=self.data_fifo.pop(0)
                #print("MUDA")
                #print(out[i])
                self.data_fifo.append(in0[i])

        #for i in range(len(self.data_fifo)):
        #    out[len(in0)+i]=self.data_fifo.pop(0)
        #out[10]=self.data_fifo.pop(0)
        return len(output_items[0])

