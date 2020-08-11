import unittest

class Testing_signUp(unittest.TestCase):

    def test_signUp_gmail(self):
        print("This test will verify signUp to gmail")
        self.assertTrue(True)


    def test_signUp_facebook(self):
        print("This test will verify signUp to facebook")
        self.assertTrue(True)

    def test_signUp_Twiter(self):
        print("This test will verify signUp to twiter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()