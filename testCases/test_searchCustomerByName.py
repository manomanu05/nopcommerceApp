import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName_004:
    base_url = ReadConfig.getApplicationURL()
    userMail = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_scearchCustomerByName(self,setUp):
        self.logger.info("** Scearchcustomerby Name**")
        self.driver=setUp
        self.driver.get(self.base_url)


        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.userMail)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("** Login Successful**")

        time.sleep(2)
        self.addcust=AddCustomer(self.driver)
        time.sleep(1)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("****searching started")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Steve")   #Steve Gatess
        searchcust.setLastName("Gates")
        time.sleep(3)
        status=searchcust.searchCustomerByName("Steve Gates")
        assert True==status
        self.logger.info("*** TC finisheddd  by Test case of finding by name ")
