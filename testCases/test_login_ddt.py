import os
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_Login:
    base_url = ReadConfig.getApplicationURL()
    path = "D:\\Selenium\\nopcommerceApp\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setUp):
        self.logger.info("*********Test_002_Login***********")
        self.logger.info("*********Verifing Login DDT test***********")
        self.driver = setUp
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print(self.rows)

        lst_sts = []  # empty list

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**PASSED**")
                    self.lp.clicklogout()
                    lst_sts.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**Failed**")
                    self.lp.clicklogout()
                    lst_sts.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Fail**")
                elif self.exp == "Fail":
                    self.logger.info("**Passed**")
                    lst_sts.append("pass")

        if "Fail" not in lst_sts:
            self.logger.info("**Login DDT test passed**")
            self.driver.close()
            assert True
        else:
            self.logger.info("** LOgin DDt test failed")
            self.driver.close()
            assert False
