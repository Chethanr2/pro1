import unittest
#import HtmlTestRunner
from VPSD.Stop_tab import VPSD_bStop_Tab
#from VPSD.VPSD_home_page_login import VPSD_aLogin
from VPSD.Route_tab import VPSD_cRoute_Tab
from VPSD.Vehicle_schedule_tab import VPSD_dVehicle_schedule_tab
from VPSD.Interface_file_download import VPSD_eInterface_Tab
from VPSD.Masters import VPSD_fMasters
from VPSD.Reports import VPSD_gReports
from VPSD.User_management import VPSD_hUser_management
from VPSD.BusinessRules import VPSD_iBussiness_rules


#login_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_aLogin)
Stop_tab_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_bStop_Tab)
Route_tab_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_cRoute_Tab)
Vehicle_tab_test = unittest.defaultTestLoader.loadTestsFromModule(VPSD_dVehicle_schedule_tab)
Interface_tab_test = unittest.defaultTestLoader.loadTestsFromModule((VPSD_eInterface_Tab))
masters = unittest.defaultTestLoader.loadTestsFromModule(VPSD_fMasters)
reports = unittest.defaultTestLoader.loadTestsFromModule(VPSD_gReports)
user_management = unittest.defaultTestLoader.loadTestsFromModule(VPSD_hUser_management)
Buss_rules = unittest.defaultTestLoader.loadTestsFromModule(VPSD_iBussiness_rules)

# create a test suite combining Login_test,Stop_tab_test,Route tab test,Vehicle schedule test, interface files download test
test_suite = unittest.TestSuite([Stop_tab_test,Route_tab_test,Vehicle_tab_test,Interface_tab_test,masters,reports,user_management,Buss_rules])

unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    unittest.main()