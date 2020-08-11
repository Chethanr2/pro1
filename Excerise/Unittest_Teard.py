import unittest

def setUpModule():
    print("This is in SetUp Module")

def tearDownModule():
    print("This is in Tear Down Module")

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is set up method")

    @classmethod
    def tearDown(self):
        print("This is teardown method")

    @classmethod
    def setUpClass(cls):
        print("Loging in to application")

    @classmethod
    def tearDownClass(cls):
        print("Logout from the application")

    def test_Search(self):
        print("This is search method")

    def test_AdvancedSearch(self):
        print("This is Advanced search method")

    def test_Prepaid_Search(self):
        print("This is Prepaid search method")

    def test_PostPaid_Search(self):
        print("This is post paid serach")


if __name__ == "__main__":
    unittest.main()