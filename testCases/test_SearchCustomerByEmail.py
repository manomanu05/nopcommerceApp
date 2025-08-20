import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail_004:
    base_url = ReadConfig.getApplicationURL()
    userMail = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_scearchCustomerByEmail(self,setUp):
        self.logger.info("** Scearchcustomerby Email**")
        self.driver=setUp
        self.driver.get(self.base_url)


        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.userMail)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.logger.info("** Login Successful**")

        time.sleep(2)
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("****searching started")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("l2odvssp@gmail.com")
        time.sleep(3)
        status=searchcust.searchCustomerByEmail("l2odvssp@gmail.com")
        assert True==status
        self.logger.info("*** TC finisheddd")