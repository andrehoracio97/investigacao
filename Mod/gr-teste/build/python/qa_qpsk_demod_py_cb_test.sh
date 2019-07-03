#!/usr/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/andre/git/investigacao/Mod/gr-teste/python
export PATH=/home/andre/git/investigacao/Mod/gr-teste/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/andre/git/investigacao/Mod/gr-teste/build/swig:$PYTHONPATH
/usr/bin/python2 /home/andre/git/investigacao/Mod/gr-teste/python/qa_qpsk_demod_py_cb.py 
