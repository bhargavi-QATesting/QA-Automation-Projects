from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
time.sleep(2)
allele = driver.find_elements(By.XPATH,'//*[@id="select2-billing_country-results"]/li')
print(len(allele))


for i in allele:
    if i.text == 'Brazil':
        print(i.text)
        i.click()
        time.sleep(5)
        break

driver.save_screenshot('Brazil.png')
driver.quit()
