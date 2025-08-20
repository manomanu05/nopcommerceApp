import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chr_options = Options()
chr_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chr_options)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.XPATH, "//input[@id='Email']").clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")

driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("admin")

driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
time.sleep(3)



driver.close()