import unittest

class test_Setup_method(unittest.TestCase):

    @classmethod
    def setUp(self):    # Execute after every successful login
        print("Login verification")

    @classmethod
    def tearDown(self): # Execute after every successful logout
        print("Logout verification")

    @classmethod
    def setUpClass(cls):    # Execute once when application opens
        print("Login to application ")

    @classmethod
    def tearDownClass(cls):     # Execute once when the control available in the class
        print("Logout once the application closed")

    def test_search(self):
        print("this is search method")

    def test_advanced_search(self):
        print("This is advanced search")

    def test_prepaid(self):
        print("this is reacharge of prepaid")

    def test_postpaid(self):
        print("This is postpaid recharge")

if __name__ == "__main__":
    unittest.main()