/* -*- c++ -*- */
/*
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "CSI_to_File_impl.h"
#include <fstream>
#include <iostream>
#include <iomanip>

namespace gr {
  namespace wirlab {

    CSI_to_File::sptr
    CSI_to_File::make(size_t sizeof_stream_item, const std::string &keyFilter, const std::string &fileName, bool append)
    {
      return gnuradio::get_initial_sptr
        (new CSI_to_File_impl(sizeof_stream_item, keyFilter, fileName, append));
    }

    // Private Constructor
    CSI_to_File_impl::CSI_to_File_impl(size_t sizeof_stream_item, const std::string &keyFilter, const std::string &fileName, bool append)
      : gr::sync_block("CSI_to_File",
              gr::io_signature::make(1, -1, sizeof_stream_item),
              gr::io_signature::make(0, 0, 0)),
        d_fileName(fileName), d_append(append)
    {
      set_key_filter(keyFilter);
    }

    // Virtual Constructor
    CSI_to_File_impl::~CSI_to_File_impl(){}

    void CSI_to_File_impl::set_key_filter(const std::string &key_filter) {
      if(key_filter == "")
        d_filter = pmt::PMT_NIL;
      else
        d_filter = pmt::intern(key_filter);
    }

    int CSI_to_File_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      gr::thread::scoped_lock l(d_mutex);

      const char* fileName = d_fileName.c_str();
      bool toprint = false;

      uint64_t abs_N, end_N;

      if(d_append && d_fileName != ""){
        std::ofstream ofs (fileName, std::ofstream::app);

        ofs << "[" << std::endl;
        ofs << "CSI_Start" << std::flush;

        for(size_t i = 0; i < input_items.size(); i++) {
          abs_N = nitems_read(i);
          end_N = abs_N + (uint64_t)(noutput_items);

          d_tags.clear();

          if(pmt::is_null(d_filter))
            get_tags_in_range(d_tags, i, abs_N, end_N);
          else
            get_tags_in_range(d_tags, i, abs_N, end_N, d_filter);

          if(d_tags.size() > 0) {
            toprint = true;
          }

          for(d_tags_itr = d_tags.begin(); d_tags_itr != d_tags.end(); d_tags_itr++) {
            ofs << "," << std::endl;
            ofs << d_tags_itr->value << std::flush;
          }
        }

        ofs << "]" << std::endl;
        ofs.close();
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace wirlab */
} /* namespace gr */
