#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/sandy/gr-wirlab/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/sandy/gr-wirlab/build/lib:$PATH
export LD_LIBRARY_PATH=/home/sandy/gr-wirlab/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-wirlab 
