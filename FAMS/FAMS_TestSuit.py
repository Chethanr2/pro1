#import os
import unittest
#import HtmlTestRunner
from FAMS.Masters import FAMS_aMasters

Masters_tab_test = unittest.defaultTestLoader.loadTestsFromModul(FAMS_aMasters)
"""Route_tab_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_cRoute_Tab)
Vehicle_tab_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_dVehicle_schedule_tab)
Interface_tab_test = unittest.defaultTestLoader.loadTestsFromModule((VPSD_eInterface_Tab))
masters = unittest.defaultTestLoader.loadTestsFromModule(VPSD_fMasters)
reports = unittest.defaultTestLoader.loadTestsFromModule(VPSD_gReports)
user_management = unittest.defaultTestLoader.loadTestsFromModule(VPSD_hUser_management)
Buss_rules = unittest.defaultTestLoader.loadTestsFromModule(VPSD_iBussiness_rules)
"""
# create a test suite combining Login_test,Stop_tab_test,Route tab test,Vehicle schedule test, interface files download test
test_suite = unittest.TestSuite([Masters_tab_test])

unittest.TextTestRunner(verbosity=3).run(test_suite)

if __name__ == "__main__":
    unittest.main(verbosity=2)