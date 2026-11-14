from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

#Ctrl+return to open link in new tab
driver = webdriver.Chrome()
'''driver.get("https://www.wix.com/blog/how-to-set-up-and-manage-your-online-store-with-wix?utm_source=bing&utm_campaign=506190452^1262241004716802^search%20-%20dsa&experiment_id=https%3A%2F%2Fwww.wix.com%2Fblog%2Fecommerce%2F2020%2F01%2Fhow-to-set-up-and-manage-your-online-store-with-wix^b^^&msclkid=961b05a5504b103228236f5d49b13aff&utm_medium=cpc")
driver.maximize_window()
time.sleep(5)
pricelink = Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH,"//a[normalize-space()='Pricing']").send_keys(pricelink)
time.sleep(5)'''

#selenium 4 - New Tab - opens a new tab and switches to new tab
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.switch_to.new_window('tab')
#driver.switch_to.new_window('window') #New Window - opens a new browser window and switches to new window
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html#")

driver.quit()

