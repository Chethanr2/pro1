#import os
import unittest
from VPSD.Test_bus import VPSD_Bussiness_rules

B_rules = unittest.defaultTestLoader.loadTestsFromModule(VPSD_Bussiness_rules)

# create a test suite combining Login_test,Stop_tab_test,Route tab test,Vehicle schedule test, interface files download test
test_suite = unittest.TestSuite([B_rules])

unittest.TextTestRunner(verbosity=3).run(test_suite)

if __name__ == "__main__":
    unittest.main(verbosity=2)