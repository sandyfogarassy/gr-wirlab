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

#ifndef INCLUDED_WIRLAB_CSI_TO_FILE_IMPL_H
#define INCLUDED_WIRLAB_CSI_TO_FILE_IMPL_H

#include <wirlab/CSI_to_File.h>
#include <gnuradio/thread/thread.h>
#include <stddef.h>

namespace gr {
  namespace wirlab {

    class CSI_to_File_impl : public CSI_to_File
    {
     private:
       std::string d_fileName;
       std::vector<tag_t> d_tags;
       std::vector<tag_t>::iterator d_tags_itr;
       bool d_append;
       pmt::pmt_t d_filter;
       gr::thread::mutex d_mutex;

     public:
      CSI_to_File_impl(size_t sizeof_stream_item, const std::string &keyFilter, const std::string &fileName, bool append);
      ~CSI_to_File_impl();
      void set_key_filter(const std::string &key_filter);

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace wirlab
} // namespace gr

#endif /* INCLUDED_WIRLAB_CSI_TO_FILE_IMPL_H */
