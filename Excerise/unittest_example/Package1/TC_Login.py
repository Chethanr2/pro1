import unittest

class Testing_login(unittest.TestCase):

    def test_login_gmail(self):
        print("This test will verify login to gmail")
        self.assertTrue(True)


    def test_login_facebook(self):
        print("This test will verify login to facebook")
        self.assertTrue(True)

    def test_login_Twiter(self):
        print("This test will verify login to twiter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()