from numba.testing import SerialSuite
from numba.testing import load_testsuite
from os.path import dirname, join

import numba_dppy
import numba_dppy.config as dppy_config

# from numba_dppy.tests.dppy import *

def load_tests(loader, tests, pattern):

    suite = SerialSuite()
    # tests = loader.loadTestsFromModule(numba_dppy.tests)
    this_dir = dirname(__file__)

    if dppy_config.dppy_present:
        # suite.addTests(tests)
        suite.addTests(load_testsuite(loader, join(this_dir, 'dppy')))
    else:
        print("skipped DPPY tests")

    return suite
