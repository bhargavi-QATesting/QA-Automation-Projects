from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

#example1(Authentication popup) syntax:https://username:password@website.com
#inject username and password into the url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)
print(driver.title)

if driver.title == "The Internet":
    print("Congratulations! You must have the proper credentials.")
else:
    print("Not logged in")




