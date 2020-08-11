import os
import unittest
import HtmlTestRunner
from unittest_module.FAMS_Login import FAMSLogin

#from unittest_module.FAMS_Navigation import FAMS_NAVIGATION

dir=os.getcwd()

#search_text = unittest.TestLoader().loadTestsFromTestCase(FAMSLogin)
search_text = unittest.defaultTestLoader.loadTestsFromModule(FAMSLogin)
#search_text = unittest.TestLoader().loadTestsFromTestCase(FAMS_NAVIGATION)

outfile = open("F:\\Chethan\\STUDY\\Python notes\\Selenium programs\\unittest_module\\Reports"+"FAMS_Login.HRML", "w")
# create a test suite combining search_text and home_page_test
#test_suite = unittest.TestSuite(search_text)

#unittest.TextTestRunner(verbosity=3).run(test_suite)

runner1 = HtmlTestRunner.HTMLTestRunner(stream=outfile,report_title='Test_Result',descriptions='Acceptance Test')
#runner1 = HTMLTestRunner(stream=outfile,report_title="test_result",descriptions="Acceptance test")
runner1.run(search_text)

if __name__ == "__main__":
    unittest.main(verbosity=2)