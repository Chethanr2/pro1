import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_Search(self):
        print("This is search method")


    @unittest.skip("This test case is not yet ready to exicute")
    def test_AdvancedSearch(self):
        print("This is Advanced search method")

    @unittest.skipIf(1==1, "The condition is satisfied so test case is skipped")
    def test_Prepaid_Search(self):
        print("This is Prepaid search method")

    def test_PostPaid_Search(self):
        print("This is post paid serach")


if __name__ == "__main__":
    unittest.main()