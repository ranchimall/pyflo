import unittest

import pyflo.test

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(pyflo.test)

runner = unittest.TextTestRunner(verbosity=1)
runner.run(suites)
