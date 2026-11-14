from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#self XPATH
#text1 = driver.find_element(By.XPATH, "//a[text()='Hidden Elements & AJAX']/self::a")
#print(text1.text)

#parent XPATH
#text1 = driver.find_element(By.XPATH, "//a[text()='Hidden Elements & AJAX']/parent::li")
#print(text1.text)

#child XPATH (no child elements are present go to ancestor element and find elements of ancestor element
#childs = driver.find_elements(By.XPATH, "//a[text()='Hidden Elements & AJAX']/ancestor::ul/child::li")
#print(len(childs))

#ancestror XPATH
#text1 = driver.find_element(By.XPATH, "//a[text()='Hidden Elements & AJAX']/ancestor::ul")
#print(text1.text)

#or
#childs = driver.find_elements(By.XPATH, "//a[text()='Hidden Elements & AJAX']/ancestor::ul")
#for i in childs:
    #print(i.text)

#descendant XPATH
#descendants = driver.find_elements(By.XPATH, "//a[text()='Hidden Elements & AJAX']/ancestor::ul/descendant::a")
#print(len(descendants))

#or
#descendants = driver.find_elements(By.XPATH, "//a[text()='Hidden Elements & AJAX']/ancestor::ul/descendant::*")
#print(len(descendants))
#for descendant in descendants:
    #print(descendant.text)

#following XPATH
#Followings = driver.find_elements(By.XPATH, "//a[contains(text(),'Hidden Elements & AJAX')]/ancestor::ul/following::*")
#print(len(Followings))

#following-sibling XPATH
#Following_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Hidden Elements & AJAX')]/ancestor::ul/following-sibling::*")
#print(len(Following_siblings))

#Preceding XPATH
#Preceding= driver.find_elements(By.XPATH, "//a[contains(text(),'Hidden Elements & AJAX')]/ancestor::ul/preceding::*")
#print(len(Preceding))

#Preceding-sibling XPATH
Preceding_sibling= driver.find_elements(By.XPATH, "//a[contains(text(),'Hidden Elements & AJAX')]/ancestor::ul/preceding-sibling::ul")
print(len(Preceding_sibling))

driver.implicitly_wait(5)

driver.quit()