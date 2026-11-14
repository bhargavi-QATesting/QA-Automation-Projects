from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Ctrl+return to open link in new tab
driver = webdriver.Chrome()
driver.get("https://www.wix.com/blog/how-to-set-up-and-manage-your-online-store-with-wix?utm_source=bing&utm_campaign=506190452^1262241004716802^search%20-%20dsa&experiment_id=https%3A%2F%2Fwww.wix.com%2Fblog%2Fecommerce%2F2020%2F01%2Fhow-to-set-up-and-manage-your-online-store-with-wix^b^^&msclkid=961b05a5504b103228236f5d49b13aff&utm_medium=cpc")
driver.maximize_window()

#Capture cookies from the browser
#cookie--> name="xyz", value=1234, expirydate=date .... etc and stores all the data in dictionary format
cookies=driver.get_cookies()
print(len(cookies))

#print details of all cookies created by the browser
for c in cookies:
    #print(c)
    print(c.get("name"),":",c.get("value"))

#Add new cookie to the browser
driver.add_cookie({"name":"MyCookie","value":"26"})
cookies=driver.get_cookies()
print(len(cookies))

#delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print(len(cookies))

#delete all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))

driver.quit()