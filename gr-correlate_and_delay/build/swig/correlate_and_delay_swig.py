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
        mname = '.'.join((pkg, '_correlate_and_delay_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_correlate_and_delay_swig')
    _correlate_and_delay_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_correlate_and_delay_swig', [dirname(__file__)])
        except ImportError:
            import _correlate_and_delay_swig
            return _correlate_and_delay_swig
        try:
            _mod = imp.load_module('_correlate_and_delay_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _correlate_and_delay_swig = swig_import_helper()
    del swig_import_helper
else:
    import _correlate_and_delay_swig
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
    return _correlate_and_delay_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _correlate_and_delay_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _correlate_and_delay_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _correlate_and_delay_swig.high_res_timer_epoch()
class corr_and_delay(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of correlate_and_delay::corr_and_delay.

    To avoid accidental use of raw pointers, correlate_and_delay::corr_and_delay's constructor is in a private implementation class. correlate_and_delay::corr_and_delay::make is the public interface for creating new instances.

    Args:
        number_bits : 
        interval : 
        threshold : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(number_bits, interval, threshold):
        """
        make(int number_bits, int interval, int threshold) -> corr_and_delay_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of correlate_and_delay::corr_and_delay.

        To avoid accidental use of raw pointers, correlate_and_delay::corr_and_delay's constructor is in a private implementation class. correlate_and_delay::corr_and_delay::make is the public interface for creating new instances.

        Args:
            number_bits : 
            interval : 
            threshold : 
        """
        return _correlate_and_delay_swig.corr_and_delay_make(number_bits, interval, threshold)

    make = staticmethod(make)
    __swig_destroy__ = _correlate_and_delay_swig.delete_corr_and_delay
    __del__ = lambda self: None
corr_and_delay_swigregister = _correlate_and_delay_swig.corr_and_delay_swigregister
corr_and_delay_swigregister(corr_and_delay)

def corr_and_delay_make(number_bits, interval, threshold):
    """
    corr_and_delay_make(int number_bits, int interval, int threshold) -> corr_and_delay_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of correlate_and_delay::corr_and_delay.

    To avoid accidental use of raw pointers, correlate_and_delay::corr_and_delay's constructor is in a private implementation class. correlate_and_delay::corr_and_delay::make is the public interface for creating new instances.

    Args:
        number_bits : 
        interval : 
        threshold : 
    """
    return _correlate_and_delay_swig.corr_and_delay_make(number_bits, interval, threshold)

class corr_and_delay_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::correlate_and_delay::corr_and_delay)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::correlate_and_delay::corr_and_delay)> self) -> corr_and_delay_sptr
        __init__(boost::shared_ptr<(gr::correlate_and_delay::corr_and_delay)> self, corr_and_delay p) -> corr_and_delay_sptr
        """
        this = _correlate_and_delay_swig.new_corr_and_delay_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(corr_and_delay_sptr self) -> corr_and_delay"""
        return _correlate_and_delay_swig.corr_and_delay_sptr___deref__(self)

    __swig_destroy__ = _correlate_and_delay_swig.delete_corr_and_delay_sptr
    __del__ = lambda self: None

    def make(self, number_bits, interval, threshold):
        """
        make(corr_and_delay_sptr self, int number_bits, int interval, int threshold) -> corr_and_delay_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of correlate_and_delay::corr_and_delay.

        To avoid accidental use of raw pointers, correlate_and_delay::corr_and_delay's constructor is in a private implementation class. correlate_and_delay::corr_and_delay::make is the public interface for creating new instances.

        Args:
            number_bits : 
            interval : 
            threshold : 
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_make(self, number_bits, interval, threshold)


    def history(self):
        """history(corr_and_delay_sptr self) -> unsigned int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(corr_and_delay_sptr self, int which, int delay)
        declare_sample_delay(corr_and_delay_sptr self, unsigned int delay)
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(corr_and_delay_sptr self, int which) -> unsigned int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(corr_and_delay_sptr self) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(corr_and_delay_sptr self) -> double"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_relative_rate(self)


    def start(self):
        """start(corr_and_delay_sptr self) -> bool"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_start(self)


    def stop(self):
        """stop(corr_and_delay_sptr self) -> bool"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(corr_and_delay_sptr self, unsigned int which_input) -> uint64_t"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(corr_and_delay_sptr self, unsigned int which_output) -> uint64_t"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(corr_and_delay_sptr self) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(corr_and_delay_sptr self, int m)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(corr_and_delay_sptr self)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(corr_and_delay_sptr self) -> bool"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(corr_and_delay_sptr self, int m)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(corr_and_delay_sptr self) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(corr_and_delay_sptr self, int i) -> long"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(corr_and_delay_sptr self, long max_output_buffer)
        set_max_output_buffer(corr_and_delay_sptr self, int port, long max_output_buffer)
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(corr_and_delay_sptr self, int i) -> long"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(corr_and_delay_sptr self, long min_output_buffer)
        set_min_output_buffer(corr_and_delay_sptr self, int port, long min_output_buffer)
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(corr_and_delay_sptr self, int which) -> float
        pc_input_buffers_full(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(corr_and_delay_sptr self, int which) -> float
        pc_input_buffers_full_avg(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(corr_and_delay_sptr self, int which) -> float
        pc_input_buffers_full_var(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(corr_and_delay_sptr self, int which) -> float
        pc_output_buffers_full(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(corr_and_delay_sptr self, int which) -> float
        pc_output_buffers_full_avg(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(corr_and_delay_sptr self, int which) -> float
        pc_output_buffers_full_var(corr_and_delay_sptr self) -> pmt_vector_float
        """
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(corr_and_delay_sptr self) -> float"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(corr_and_delay_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(corr_and_delay_sptr self)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(corr_and_delay_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(corr_and_delay_sptr self) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(corr_and_delay_sptr self) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(corr_and_delay_sptr self, int priority) -> int"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(corr_and_delay_sptr self) -> std::string"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_name(self)


    def symbol_name(self):
        """symbol_name(corr_and_delay_sptr self) -> std::string"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(corr_and_delay_sptr self) -> io_signature_sptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(corr_and_delay_sptr self) -> io_signature_sptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(corr_and_delay_sptr self) -> long"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(corr_and_delay_sptr self) -> basic_block_sptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(corr_and_delay_sptr self, int ninputs, int noutputs) -> bool"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(corr_and_delay_sptr self) -> std::string"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(corr_and_delay_sptr self, std::string name)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(corr_and_delay_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _correlate_and_delay_swig.corr_and_delay_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(corr_and_delay_sptr self) -> swig_int_ptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(corr_and_delay_sptr self) -> swig_int_ptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(corr_and_delay_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _correlate_and_delay_swig.corr_and_delay_sptr_message_subscribers(self, which_port)

corr_and_delay_sptr_swigregister = _correlate_and_delay_swig.corr_and_delay_sptr_swigregister
corr_and_delay_sptr_swigregister(corr_and_delay_sptr)


corr_and_delay_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
corr_and_delay = corr_and_delay.make;



