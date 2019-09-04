#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/investigacao/gr-add_vector/python
export PATH=/home/andre/investigacao/gr-add_vector/build/python:$PATH
export LD_LIBRARY_PATH=/home/andre/investigacao/gr-add_vector/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/andre/investigacao/gr-add_vector/build/swig:$PYTHONPATH
/usr/bin/python2 /home/andre/investigacao/gr-add_vector/python/qa_multiply.py 
