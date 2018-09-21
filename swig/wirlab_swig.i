/* -*- c++ -*- */

#define WIRLAB_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "wirlab_swig_doc.i"

%{
#include "wirlab/CSI_to_File.h"
%}


%include "wirlab/CSI_to_File.h"
GR_SWIG_BLOCK_MAGIC2(wirlab, CSI_to_File);
