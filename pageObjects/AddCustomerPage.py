import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer():  # /html/body/div[3]/aside/div/nav/ul/li[4]/a/p
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"  # //input[@id='Email']
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"

    txtCustomerRoles_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    listItemAdministrators_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-zrhs-1']"
    lstItemRegistered_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-16zs-3']"
    listItemGuests_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-qtqt-4']"
    lstItemVendors_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-u5r1-5']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"

    txtCompanyName_xpath = "//input[@id='Company']"
    # drpdownNewsletter_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lastName)

    # def setCustomerRole(self, role):
    #     self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
    #     time.sleep(5)
    #     if role == "Administrators11":
    #         self.lstItem = self.driver.find_element(By.XPATH, self.listItemAdministrators_xpath)
    #     elif role == "Registered":
    #         self.lstItem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)
    #     elif role == "Registered":
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()
    #         self.lstItem = self.driver.find_element(By.XPATH, self.lstItemVendors_xpath)
    #     elif role == "Administrators11":
    #         self.lstItem = self.driver.find_element(By.XPATH, self.listItemAdministrators_xpath)
    #     elif role == "Vendors":
    #         self.lstItem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)
    #     else:
    #         self.lstItem = self.driver.find_element(By.XPATH, self.lstItemVendors_xpath)
    #     time.sleep(3)
    #     self.driver.execute_script("arguments[0].click();", self.lstItem)

    def setCustomerRole(self,v):
        dp=Select(self.driver.find_element(By.XPATH,"(//input[@role='searchbox'])[2]"))
        dp.select_by_visible_text(v)

    def setMgrOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.ID, self.btnSave_xpath).click()
