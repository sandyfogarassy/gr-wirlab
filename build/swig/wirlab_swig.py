# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_wirlab_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_wirlab_swig')
    _wirlab_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_wirlab_swig', [dirname(__file__)])
        except ImportError:
            import _wirlab_swig
            return _wirlab_swig
        try:
            _mod = imp.load_module('_wirlab_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _wirlab_swig = swig_import_helper()
    del swig_import_helper
else:
    import _wirlab_swig
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _wirlab_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _wirlab_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _wirlab_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _wirlab_swig.high_res_timer_epoch()
class CSI_to_File(object):
    """<+description of block+>"""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(sizeof_stream_item, keyFilter, fileName, append):
        """
        make(size_t sizeof_stream_item, std::string const & keyFilter, std::string const & fileName, bool append) -> CSI_to_File_sptr

        Return a shared_ptr to a new instance of wirlab::CSI_to_File.

        To avoid accidental use of raw pointers, wirlab::CSI_to_File's constructor is in a private implementation class. wirlab::CSI_to_File::make is the public interface for creating new instances.

        Params: (sizeof_stream_item, keyFilter, fileName, append)
        """
        return _wirlab_swig.CSI_to_File_make(sizeof_stream_item, keyFilter, fileName, append)

    make = staticmethod(make)
    __swig_destroy__ = _wirlab_swig.delete_CSI_to_File
    __del__ = lambda self: None
CSI_to_File_swigregister = _wirlab_swig.CSI_to_File_swigregister
CSI_to_File_swigregister(CSI_to_File)

def CSI_to_File_make(sizeof_stream_item, keyFilter, fileName, append):
    """
    CSI_to_File_make(size_t sizeof_stream_item, std::string const & keyFilter, std::string const & fileName, bool append) -> CSI_to_File_sptr

    Return a shared_ptr to a new instance of wirlab::CSI_to_File.

    To avoid accidental use of raw pointers, wirlab::CSI_to_File's constructor is in a private implementation class. wirlab::CSI_to_File::make is the public interface for creating new instances.

    Params: (sizeof_stream_item, keyFilter, fileName, append)
    """
    return _wirlab_swig.CSI_to_File_make(sizeof_stream_item, keyFilter, fileName, append)

class CSI_to_File_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::wirlab::CSI_to_File)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::wirlab::CSI_to_File)> self) -> CSI_to_File_sptr
        __init__(boost::shared_ptr<(gr::wirlab::CSI_to_File)> self, CSI_to_File p) -> CSI_to_File_sptr
        """
        this = _wirlab_swig.new_CSI_to_File_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(CSI_to_File_sptr self) -> CSI_to_File"""
        return _wirlab_swig.CSI_to_File_sptr___deref__(self)

    __swig_destroy__ = _wirlab_swig.delete_CSI_to_File_sptr
    __del__ = lambda self: None

    def make(self, sizeof_stream_item, keyFilter, fileName, append):
        """
        make(CSI_to_File_sptr self, size_t sizeof_stream_item, std::string const & keyFilter, std::string const & fileName, bool append) -> CSI_to_File_sptr

        Return a shared_ptr to a new instance of wirlab::CSI_to_File.

        To avoid accidental use of raw pointers, wirlab::CSI_to_File's constructor is in a private implementation class. wirlab::CSI_to_File::make is the public interface for creating new instances.

        Params: (sizeof_stream_item, keyFilter, fileName, append)
        """
        return _wirlab_swig.CSI_to_File_sptr_make(self, sizeof_stream_item, keyFilter, fileName, append)


    def history(self):
        """history(CSI_to_File_sptr self) -> unsigned int"""
        return _wirlab_swig.CSI_to_File_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(CSI_to_File_sptr self, int which, int delay)
        declare_sample_delay(CSI_to_File_sptr self, unsigned int delay)
        """
        return _wirlab_swig.CSI_to_File_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(CSI_to_File_sptr self, int which) -> unsigned int"""
        return _wirlab_swig.CSI_to_File_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(CSI_to_File_sptr self) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(CSI_to_File_sptr self) -> double"""
        return _wirlab_swig.CSI_to_File_sptr_relative_rate(self)


    def start(self):
        """start(CSI_to_File_sptr self) -> bool"""
        return _wirlab_swig.CSI_to_File_sptr_start(self)


    def stop(self):
        """stop(CSI_to_File_sptr self) -> bool"""
        return _wirlab_swig.CSI_to_File_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(CSI_to_File_sptr self, unsigned int which_input) -> uint64_t"""
        return _wirlab_swig.CSI_to_File_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(CSI_to_File_sptr self, unsigned int which_output) -> uint64_t"""
        return _wirlab_swig.CSI_to_File_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(CSI_to_File_sptr self) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(CSI_to_File_sptr self, int m)"""
        return _wirlab_swig.CSI_to_File_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(CSI_to_File_sptr self)"""
        return _wirlab_swig.CSI_to_File_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(CSI_to_File_sptr self) -> bool"""
        return _wirlab_swig.CSI_to_File_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(CSI_to_File_sptr self, int m)"""
        return _wirlab_swig.CSI_to_File_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(CSI_to_File_sptr self) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(CSI_to_File_sptr self, int i) -> long"""
        return _wirlab_swig.CSI_to_File_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(CSI_to_File_sptr self, long max_output_buffer)
        set_max_output_buffer(CSI_to_File_sptr self, int port, long max_output_buffer)
        """
        return _wirlab_swig.CSI_to_File_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(CSI_to_File_sptr self, int i) -> long"""
        return _wirlab_swig.CSI_to_File_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(CSI_to_File_sptr self, long min_output_buffer)
        set_min_output_buffer(CSI_to_File_sptr self, int port, long min_output_buffer)
        """
        return _wirlab_swig.CSI_to_File_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(CSI_to_File_sptr self, int which) -> float
        pc_input_buffers_full(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(CSI_to_File_sptr self, int which) -> float
        pc_input_buffers_full_avg(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(CSI_to_File_sptr self, int which) -> float
        pc_input_buffers_full_var(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(CSI_to_File_sptr self, int which) -> float
        pc_output_buffers_full(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(CSI_to_File_sptr self, int which) -> float
        pc_output_buffers_full_avg(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(CSI_to_File_sptr self, int which) -> float
        pc_output_buffers_full_var(CSI_to_File_sptr self) -> pmt_vector_float
        """
        return _wirlab_swig.CSI_to_File_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(CSI_to_File_sptr self) -> float"""
        return _wirlab_swig.CSI_to_File_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(CSI_to_File_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _wirlab_swig.CSI_to_File_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(CSI_to_File_sptr self)"""
        return _wirlab_swig.CSI_to_File_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(CSI_to_File_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _wirlab_swig.CSI_to_File_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(CSI_to_File_sptr self) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(CSI_to_File_sptr self) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(CSI_to_File_sptr self, int priority) -> int"""
        return _wirlab_swig.CSI_to_File_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(CSI_to_File_sptr self) -> std::string"""
        return _wirlab_swig.CSI_to_File_sptr_name(self)


    def symbol_name(self):
        """symbol_name(CSI_to_File_sptr self) -> std::string"""
        return _wirlab_swig.CSI_to_File_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(CSI_to_File_sptr self) -> io_signature_sptr"""
        return _wirlab_swig.CSI_to_File_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(CSI_to_File_sptr self) -> io_signature_sptr"""
        return _wirlab_swig.CSI_to_File_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(CSI_to_File_sptr self) -> long"""
        return _wirlab_swig.CSI_to_File_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(CSI_to_File_sptr self) -> basic_block_sptr"""
        return _wirlab_swig.CSI_to_File_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(CSI_to_File_sptr self, int ninputs, int noutputs) -> bool"""
        return _wirlab_swig.CSI_to_File_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(CSI_to_File_sptr self) -> std::string"""
        return _wirlab_swig.CSI_to_File_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(CSI_to_File_sptr self, std::string name)"""
        return _wirlab_swig.CSI_to_File_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(CSI_to_File_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _wirlab_swig.CSI_to_File_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(CSI_to_File_sptr self) -> swig_int_ptr"""
        return _wirlab_swig.CSI_to_File_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(CSI_to_File_sptr self) -> swig_int_ptr"""
        return _wirlab_swig.CSI_to_File_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(CSI_to_File_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _wirlab_swig.CSI_to_File_sptr_message_subscribers(self, which_port)

CSI_to_File_sptr_swigregister = _wirlab_swig.CSI_to_File_sptr_swigregister
CSI_to_File_sptr_swigregister(CSI_to_File_sptr)


CSI_to_File_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
CSI_to_File = CSI_to_File.make;



