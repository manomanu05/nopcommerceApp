from selenium.webdriver.common.by import By

class SearchCustomer:
    # Locators
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    btnSrch_xpath = "//button[@id='search-customers']"

    tblSearchResults_xpath = "//div[@id='customers-grid_wrapper']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    # ----------- Search Filters -----------
    def setEmail(self, email):
        email_field = self.driver.find_element(By.XPATH, self.txtEmail_xpath)
        email_field.clear()
        email_field.send_keys(email)

    def setFirstName(self, fname):
        fname_field = self.driver.find_element(By.XPATH, self.txtFstName_xpath)
        fname_field.clear()
        fname_field.send_keys(fname)

    def setLastName(self, lname):
        lname_field = self.driver.find_element(By.XPATH, self.txtLastName_xpath)
        lname_field.clear()
        lname_field.send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSrch_xpath).click()

    # ----------- Table Info -----------
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    # ----------- Search in Table -----------
    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            emailid = self.driver.find_element(
                By.XPATH,
                f"//table[@id='customers-grid']/tbody/tr[{r}]/td[2]"
            ).text
            if emailid.strip() == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            customer_name = self.driver.find_element(
                By.XPATH,
                f"//table[@id='customers-grid']/tbody/tr[{r}]/td[3]"
            ).text
            if customer_name.strip() == name:
                flag = True
                break
        return flag

# from selenium.webdriver.common.by import By
#
#
# class SearchCustomer():
#     txtEmail_xpath="//input[@id='SearchEmail']"
#     txtFstName_xpath="//input[@id='SearchFirstName']"
#     txtLastName_xpath="//input[@id='SearchLastName']"
#     btnSrch_xpath="//button[@id='search-customers']"
#
#     tblSearchResults_xpath="//div[@id='customers-grid_wrapper']"
#     table_xpath="//table[id='customers-grid']"
#     tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
#     tableColumn_xpath="//table[@id='customers-grid']//tbody/tr/td"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def setMail(self,email):
#         self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
#         self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)
#
#     def setFirstName(self,fname):
#         self.driver.find_element(By.XPATH,self.txtFstName_xpath).clear()
#         self.driver.find_element(By.XPATH,self.txtFstName_xpath).send_keys(fname)
#
#     def setLname(self,lname):
#         self.driver.find_element(By.XPATH,self.txtLastName_xpath).clear()
#         self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)
#
#     def clickbtn(self):
#         self.driver.find_element(By.XPATH,self.btnSrch_xpath).click()
#
#     def getNoofCols(self):
#         return len(self.driver.find_element(By.XPATH,self.getNoofCols()))
#
#     def getNoRow(self):
#         return len(self.driver.find_element(By.XPATH,self.getNoRow()))
#
#     def searchCustomerByEmail(self,email):
#         flag=False
#         for r in range(1,self.getNoRow()+1):
#             table=self.driver.find_element(By.XPATH,self.table_xpath)
#             emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
#             if emailid==email:
#                 flag=True
#                 break
#         return flag
#
#     def searchCustomerByEmail(self,Name):
#         flag=False
#         for r in range(1,self.getNoRow()+1):
#             table=self.driver.find_element(By.XPATH,self.table_xpath)
#             name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
#             if name==Name:
#                 flag=True
#                 break
#         return flag