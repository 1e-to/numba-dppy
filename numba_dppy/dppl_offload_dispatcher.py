from numba.core import dispatcher, compiler
from numba.core.registry import cpu_target, dispatcher_registry
import numba_dppy.config as dppy_config


class DpplOffloadDispatcher(dispatcher.Dispatcher):
    targetdescr = cpu_target

    def __init__(self, py_func, locals={}, targetoptions={}, impl_kind='direct', pipeline_class=compiler.Compiler):
        if dppy_config.dppy_present:
            from numba_dppy.compiler import DPPLCompiler
            targetoptions['parallel'] = True
            dispatcher.Dispatcher.__init__(self, py_func, locals=locals,
                    targetoptions=targetoptions, impl_kind=impl_kind, pipeline_class=DPPLCompiler)
        else:
            print("---------------------------------------------------------------------")
            print("WARNING : DPPL pipeline ignored. Ensure OpenCL drivers are installed.")
            print("---------------------------------------------------------------------")
            dispatcher.Dispatcher.__init__(self, py_func, locals=locals,
                targetoptions=targetoptions, impl_kind=impl_kind, pipeline_class=pipeline_class)

dispatcher_registry['__dppl_offload_gpu__'] = DpplOffloadDispatcher
dispatcher_registry['__dppl_offload_cpu__'] = DpplOffloadDispatcher
