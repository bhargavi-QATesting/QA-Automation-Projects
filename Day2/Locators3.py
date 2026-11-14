from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# To find multiple webelements
driver = webdriver.Edge()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#use either tagname#id or #id --> for TAG and ID
#use either tagname.class or .class --> for TAG and CLASS
#use either [attribute=value] or tagname[attribute=value] and quotes are not required for value--> for TAG and ATTRIBUTE
#use either tagname.class[attribute=value] or .class[attribute=value] when both tag and class are same for two elements --> for tag class and attribute

#driver.find_element(By.CSS_SELECTOR,"input.x1i10hfl").send_keys("abc")
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.x1i10hfl[type=password]").send_keys("abc")

driver.implicitly_wait(5)