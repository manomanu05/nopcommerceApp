import os
import random
import string
import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects import AddCustomerPage
from pageObjects.LoginPage import LoginPage


class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setUp):
        self.logger.info("**TEST 003  Add Customer")
        self.driver = setUp
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("** Login Successfully")

        self.addCust = AddCustomer(self.driver)
        time.sleep(2)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOnCustomerMenuItem()

        self.addCust.clickOnAddNew()
        self.logger.info("** providing customer info**")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("ABCD@123")
        self.addCust.setFirstName("Rj")
        self.addCust.setLastName("MAnoj")
        self.addCust.setGender("Male")
        self.addCust.setAdminContent("ugo;li")
        self.addCust.setMgrOfVendor("Vendor 2")
        self.addCust.setCustomerRole("Vendors")


        self.addCust.clickOnSave()

        self.logger.info("** saving customer iNfo ")

        self.logger.info("** AAdd Customer validation started")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)

        if "customer has been added sucessfully." in self.msg:
            assert True == True
            self.logger.info("** Add sustomer Test Passed")
        else:
            # self.driver.save_screenshot(os.getcwd() + "/Screenshots/test_homePageTitle.png")
            self.driver.save_screenshot(os.getcwd() + "/Screeenshot/test_addcustomer.png")
            self.logger.error("**Failed **")
            assert True == False

        self.driver.close()
        self.logger.info("**Ending home page title test** ")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
