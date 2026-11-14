from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
#1)scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)")
value = driver.execute_script("return window.pageYOffset;")
print(value)

#2)scroll down page till the element is visible
flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView()", flag)
time.sleep(2)
value = driver.execute_script("return window.pageYOffset;")
print(value)

#3)scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print(value)

#4)scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print(value)

driver.quit()
