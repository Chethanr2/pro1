import allure
import pytest
import logging

logging.basicConfig(level=logging.INFO)

@pytest.fixture()
def setup():
    logging.info("This is setup method")

def testmethod1(setup):
    bus = 'chethan'
    nus = 'Bhagya'
    logging.info("%s This is test case 1 : %s",bus,nus)

def testmethod2(setup):
    print("This is test case 2")