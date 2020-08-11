import unittest

class PaymentBycash(unittest.TestCase):

    def test_paymentBy_SBI(self):
        print("This is to verify payment by SBI card")
        self.assertTrue(True)

    def test_paymentBy_HDFC(self):
        print("This is to verify payment by HDFC card")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
