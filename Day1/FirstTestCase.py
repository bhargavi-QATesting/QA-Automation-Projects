from sys import executable
from telnetlib import EC

import selenium.webdriver as webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#OrangeHRM
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
Title = driver.title
print(Title)
exp_title = "OrangeHRM"

if Title == exp_title:
    print(True)
else:
    print(False)

time.sleep(5)

#NopCommerce
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
username = driver.find_element(By.ID, "Email")
username.clear()
username.send_keys("admin@yourstore.com")
password = driver.find_element(By.ID, "Password")
password.clear()
password.send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
Title = driver.title
print(Title)

exp_title = "Dashboard / nopCommerce administration"

if Title == exp_title:
    print(True)
else:
    print(False)
driver.quit()