from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v153.dom import get_attributes
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.XPATH, '//*[@id="country"]'))
#dropdown.select_by_visible_text("India")
#dropdown.select_by_value("india")
dropdown.select_by_index(9)
time.sleep(2)

#for i in dropdown.options:
    #print(i.get_attribute('value'))

#or

#capture all the options and print them
alloptions = dropdown.options
print(len(alloptions))

for j in alloptions:
    print(j.text)
    #print(j.get_attribute('value'))

#select option from dropdown without using built-in method
for opt in alloptions:
    if opt.text == 'India':
        opt.click()
        break

#dropdown2 = Select(driver.find_element(By.XPATH, "//select[@id='country']/option"))
#print(len(dropdown2))

driver.quit()
