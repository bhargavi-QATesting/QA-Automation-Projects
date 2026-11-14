from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v153.dom import get_attributes

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#to select one checkbox
#driver.find_element(By.XPATH, "//input[@id='sunday']").click()
time.sleep(2)

#to select multiple checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@class= 'form-check-input' and @type='checkbox']")
print(len(checkboxes))


#1)Approach 1 (to select all the checkboxes at a time using range function)
"""for i in range(len(checkboxes)):
    checkboxes[i].click()
    print(checkboxes[i].is_selected())
    print(checkboxes[i].get_attribute('value'))"""

#2)Approach 2 (to select all the checkboxes one after another)
"""for j in checkboxes:
    j.click()
    time.sleep(1)
    print(j.get_attribute('value'))"""


#3)to select multiple checkboxes
"""for checkbox in checkboxes:
    weekname = checkbox.get_attribute("id")
    if weekname== 'sunday' or weekname== 'saturday' or weekname=='sunday':
        checkbox.click()"""

#4)to select multiple checkboxes by using range function
"""for i in range(len(checkboxes)):
    checkboxes[0].click()
    checkboxes[2].click()
    checkboxes[5].click()
    break

print(checkboxes[0].get_attribute('value'))
print(checkboxes[2].get_attribute('value'))
print(checkboxes[5].get_attribute('value'))

print(checkboxes[0].is_selected())
print(checkboxes[2].is_selected())
print(checkboxes[5].is_selected())
print(checkboxes[1].is_selected())
print(checkboxes[3].is_selected())"""

#5)to select last 2 elements
"""for i in range(len(checkboxes)-2, len(checkboxes)):   #(5,7)
    checkboxes[i].click()"""

#6)to select first 2 checkboxes
"""for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
        print(checkboxes[i].get_attribute('value'))"""

#7)clearing all the checkboxes at a time
"""for j in checkboxes:
    j.click()

for i in checkboxes:
    if i.is_selected():
        i.click()"""


time.sleep(2)
driver.quit()


