import os
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    userMail = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setUp):
        self.logger.info("*************** Test_001_Login :: test_homePageTitle started ***************")
        self.driver = setUp
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "nopCommerce demo store. Login":   # <-- correct title
            self.logger.info("*************** Home Page title is correct ***************")
            self.driver.quit()
            assert True
        else:
            self.logger.error(f"*************** Home Page title is wrong! Got: {act_title} ***************")
            self.driver.save_screenshot(os.getcwd() + "/Screenshots/test_homePageTitle.png")
            self.driver.quit()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUp):
        self.logger.info("*************** Test_001_Login :: test_login started ***************")
        self.driver = setUp
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.userMail)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title  #Dashboard / nopCommerce administration

        if act_title == "Dashboard / nopCommerce administration":   # <-- correct title
            self.logger.info("*************** Login test passed ***************")
            self.driver.quit()
            assert True
        else:
            self.logger.error(f"*************** Login test failed! Got: {act_title} ***************")
            self.driver.save_screenshot(os.getcwd() + "/Screenshots/test_login.png")
            self.driver.quit()
            assert False
