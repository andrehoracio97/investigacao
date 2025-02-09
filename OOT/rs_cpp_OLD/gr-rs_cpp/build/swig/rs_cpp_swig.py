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
        mname = '.'.join((pkg, '_rs_cpp_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_rs_cpp_swig')
    _rs_cpp_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rs_cpp_swig', [dirname(__file__)])
        except ImportError:
            import _rs_cpp_swig
            return _rs_cpp_swig
        try:
            _mod = imp.load_module('_rs_cpp_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _rs_cpp_swig = swig_import_helper()
    del swig_import_helper
else:
    import _rs_cpp_swig
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
    return _rs_cpp_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _rs_cpp_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _rs_cpp_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _rs_cpp_swig.high_res_timer_epoch()
class rs_encoder_custom(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rs_cpp::rs_encoder_custom.

    To avoid accidental use of raw pointers, rs_cpp::rs_encoder_custom's constructor is in a private implementation class. rs_cpp::rs_encoder_custom::make is the public interface for creating new instances.

    Args:
        test : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(test):
        """
        make(int test) -> rs_encoder_custom_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rs_cpp::rs_encoder_custom.

        To avoid accidental use of raw pointers, rs_cpp::rs_encoder_custom's constructor is in a private implementation class. rs_cpp::rs_encoder_custom::make is the public interface for creating new instances.

        Args:
            test : 
        """
        return _rs_cpp_swig.rs_encoder_custom_make(test)

    make = staticmethod(make)
    __swig_destroy__ = _rs_cpp_swig.delete_rs_encoder_custom
    __del__ = lambda self: None
rs_encoder_custom_swigregister = _rs_cpp_swig.rs_encoder_custom_swigregister
rs_encoder_custom_swigregister(rs_encoder_custom)

def rs_encoder_custom_make(test):
    """
    rs_encoder_custom_make(int test) -> rs_encoder_custom_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rs_cpp::rs_encoder_custom.

    To avoid accidental use of raw pointers, rs_cpp::rs_encoder_custom's constructor is in a private implementation class. rs_cpp::rs_encoder_custom::make is the public interface for creating new instances.

    Args:
        test : 
    """
    return _rs_cpp_swig.rs_encoder_custom_make(test)

class rs_encoder_custom_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::rs_cpp::rs_encoder_custom)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::rs_cpp::rs_encoder_custom)> self) -> rs_encoder_custom_sptr
        __init__(boost::shared_ptr<(gr::rs_cpp::rs_encoder_custom)> self, rs_encoder_custom p) -> rs_encoder_custom_sptr
        """
        this = _rs_cpp_swig.new_rs_encoder_custom_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(rs_encoder_custom_sptr self) -> rs_encoder_custom"""
        return _rs_cpp_swig.rs_encoder_custom_sptr___deref__(self)

    __swig_destroy__ = _rs_cpp_swig.delete_rs_encoder_custom_sptr
    __del__ = lambda self: None

    def make(self, test):
        """
        make(rs_encoder_custom_sptr self, int test) -> rs_encoder_custom_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rs_cpp::rs_encoder_custom.

        To avoid accidental use of raw pointers, rs_cpp::rs_encoder_custom's constructor is in a private implementation class. rs_cpp::rs_encoder_custom::make is the public interface for creating new instances.

        Args:
            test : 
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_make(self, test)


    def history(self):
        """history(rs_encoder_custom_sptr self) -> unsigned int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(rs_encoder_custom_sptr self, int which, int delay)
        declare_sample_delay(rs_encoder_custom_sptr self, unsigned int delay)
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(rs_encoder_custom_sptr self, int which) -> unsigned int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(rs_encoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(rs_encoder_custom_sptr self) -> double"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_relative_rate(self)


    def start(self):
        """start(rs_encoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_start(self)


    def stop(self):
        """stop(rs_encoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(rs_encoder_custom_sptr self, unsigned int which_input) -> uint64_t"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(rs_encoder_custom_sptr self, unsigned int which_output) -> uint64_t"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(rs_encoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(rs_encoder_custom_sptr self, int m)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(rs_encoder_custom_sptr self)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(rs_encoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(rs_encoder_custom_sptr self, int m)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(rs_encoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(rs_encoder_custom_sptr self, int i) -> long"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(rs_encoder_custom_sptr self, long max_output_buffer)
        set_max_output_buffer(rs_encoder_custom_sptr self, int port, long max_output_buffer)
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(rs_encoder_custom_sptr self, int i) -> long"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(rs_encoder_custom_sptr self, long min_output_buffer)
        set_min_output_buffer(rs_encoder_custom_sptr self, int port, long min_output_buffer)
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(rs_encoder_custom_sptr self, int which) -> float
        pc_input_buffers_full(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(rs_encoder_custom_sptr self, int which) -> float
        pc_input_buffers_full_avg(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(rs_encoder_custom_sptr self, int which) -> float
        pc_input_buffers_full_var(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(rs_encoder_custom_sptr self, int which) -> float
        pc_output_buffers_full(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(rs_encoder_custom_sptr self, int which) -> float
        pc_output_buffers_full_avg(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(rs_encoder_custom_sptr self, int which) -> float
        pc_output_buffers_full_var(rs_encoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(rs_encoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(rs_encoder_custom_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(rs_encoder_custom_sptr self)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(rs_encoder_custom_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(rs_encoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(rs_encoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(rs_encoder_custom_sptr self, int priority) -> int"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(rs_encoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_name(self)


    def symbol_name(self):
        """symbol_name(rs_encoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(rs_encoder_custom_sptr self) -> io_signature_sptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(rs_encoder_custom_sptr self) -> io_signature_sptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(rs_encoder_custom_sptr self) -> long"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(rs_encoder_custom_sptr self) -> basic_block_sptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(rs_encoder_custom_sptr self, int ninputs, int noutputs) -> bool"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(rs_encoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(rs_encoder_custom_sptr self, std::string name)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(rs_encoder_custom_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _rs_cpp_swig.rs_encoder_custom_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(rs_encoder_custom_sptr self) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(rs_encoder_custom_sptr self) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(rs_encoder_custom_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_encoder_custom_sptr_message_subscribers(self, which_port)

rs_encoder_custom_sptr_swigregister = _rs_cpp_swig.rs_encoder_custom_sptr_swigregister
rs_encoder_custom_sptr_swigregister(rs_encoder_custom_sptr)


rs_encoder_custom_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
rs_encoder_custom = rs_encoder_custom.make;

class rs_decoder_custom(object):
    """Proxy of C++ gr::rs_cpp::rs_decoder_custom class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(teste):
        """make(int teste) -> rs_decoder_custom_sptr"""
        return _rs_cpp_swig.rs_decoder_custom_make(teste)

    make = staticmethod(make)
    __swig_destroy__ = _rs_cpp_swig.delete_rs_decoder_custom
    __del__ = lambda self: None
rs_decoder_custom_swigregister = _rs_cpp_swig.rs_decoder_custom_swigregister
rs_decoder_custom_swigregister(rs_decoder_custom)

def rs_decoder_custom_make(teste):
    """rs_decoder_custom_make(int teste) -> rs_decoder_custom_sptr"""
    return _rs_cpp_swig.rs_decoder_custom_make(teste)

class rs_decoder_custom_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::rs_cpp::rs_decoder_custom)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::rs_cpp::rs_decoder_custom)> self) -> rs_decoder_custom_sptr
        __init__(boost::shared_ptr<(gr::rs_cpp::rs_decoder_custom)> self, rs_decoder_custom p) -> rs_decoder_custom_sptr
        """
        this = _rs_cpp_swig.new_rs_decoder_custom_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(rs_decoder_custom_sptr self) -> rs_decoder_custom"""
        return _rs_cpp_swig.rs_decoder_custom_sptr___deref__(self)

    __swig_destroy__ = _rs_cpp_swig.delete_rs_decoder_custom_sptr
    __del__ = lambda self: None

    def make(self, teste):
        """make(rs_decoder_custom_sptr self, int teste) -> rs_decoder_custom_sptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_make(self, teste)


    def history(self):
        """history(rs_decoder_custom_sptr self) -> unsigned int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(rs_decoder_custom_sptr self, int which, int delay)
        declare_sample_delay(rs_decoder_custom_sptr self, unsigned int delay)
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(rs_decoder_custom_sptr self, int which) -> unsigned int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(rs_decoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(rs_decoder_custom_sptr self) -> double"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_relative_rate(self)


    def start(self):
        """start(rs_decoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_start(self)


    def stop(self):
        """stop(rs_decoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(rs_decoder_custom_sptr self, unsigned int which_input) -> uint64_t"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(rs_decoder_custom_sptr self, unsigned int which_output) -> uint64_t"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(rs_decoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(rs_decoder_custom_sptr self, int m)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(rs_decoder_custom_sptr self)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(rs_decoder_custom_sptr self) -> bool"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(rs_decoder_custom_sptr self, int m)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(rs_decoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(rs_decoder_custom_sptr self, int i) -> long"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(rs_decoder_custom_sptr self, long max_output_buffer)
        set_max_output_buffer(rs_decoder_custom_sptr self, int port, long max_output_buffer)
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(rs_decoder_custom_sptr self, int i) -> long"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(rs_decoder_custom_sptr self, long min_output_buffer)
        set_min_output_buffer(rs_decoder_custom_sptr self, int port, long min_output_buffer)
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(rs_decoder_custom_sptr self, int which) -> float
        pc_input_buffers_full(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(rs_decoder_custom_sptr self, int which) -> float
        pc_input_buffers_full_avg(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(rs_decoder_custom_sptr self, int which) -> float
        pc_input_buffers_full_var(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(rs_decoder_custom_sptr self, int which) -> float
        pc_output_buffers_full(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(rs_decoder_custom_sptr self, int which) -> float
        pc_output_buffers_full_avg(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(rs_decoder_custom_sptr self, int which) -> float
        pc_output_buffers_full_var(rs_decoder_custom_sptr self) -> pmt_vector_float
        """
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(rs_decoder_custom_sptr self) -> float"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(rs_decoder_custom_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(rs_decoder_custom_sptr self)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(rs_decoder_custom_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(rs_decoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(rs_decoder_custom_sptr self) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(rs_decoder_custom_sptr self, int priority) -> int"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(rs_decoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_name(self)


    def symbol_name(self):
        """symbol_name(rs_decoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(rs_decoder_custom_sptr self) -> io_signature_sptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(rs_decoder_custom_sptr self) -> io_signature_sptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(rs_decoder_custom_sptr self) -> long"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(rs_decoder_custom_sptr self) -> basic_block_sptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(rs_decoder_custom_sptr self, int ninputs, int noutputs) -> bool"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(rs_decoder_custom_sptr self) -> std::string"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(rs_decoder_custom_sptr self, std::string name)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(rs_decoder_custom_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _rs_cpp_swig.rs_decoder_custom_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(rs_decoder_custom_sptr self) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(rs_decoder_custom_sptr self) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(rs_decoder_custom_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _rs_cpp_swig.rs_decoder_custom_sptr_message_subscribers(self, which_port)

rs_decoder_custom_sptr_swigregister = _rs_cpp_swig.rs_decoder_custom_sptr_swigregister
rs_decoder_custom_sptr_swigregister(rs_decoder_custom_sptr)


rs_decoder_custom_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
rs_decoder_custom = rs_decoder_custom.make;



