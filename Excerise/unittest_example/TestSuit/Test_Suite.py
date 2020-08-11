import unittest

from Excerise.unittest_example.Package1.TC_Login import Testing_login
from Excerise.unittest_example.Package1.TC_SignUp import Testing_signUp
from Excerise.unittest_example.Package2.TC_PaymentBycash import PaymentBycash

TC1 = unittest.TestLoader().loadTestsFromTestCase(Testing_login)
TC2 = unittest.TestLoader().loadTestsFromTestCase(Testing_signUp)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentBycash)

Login_Testsuite = unittest.TestSuite([TC2,TC1])

unittest.TextTestRunner().run(Login_Testsuite)