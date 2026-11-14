from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
'''driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
driver.implicitly_wait(5)
date1 = driver.find_element(By.ID, 'datepicker')
date1.click()
date1.send_keys("03/13/2000")
time.sleep(2)
date2 = driver.find_element(By.ID, 'txtDate')
date2.click()
date2.send_keys("10/11/2026")
time.sleep(2)'''

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
date1 = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(date1)

#or

#driver.switch_to.frame(0)
#driver.find_element(By.ID, "datepicker").send_keys("03/13/2000")
#time.sleep(2)

#Approach 2
mon = "March"
yr = "2027"
dt = "13"

driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()
time.sleep(2)

while True:
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if month == mon and year == yr:
        break;
    else:
        #driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]').click()   #prev arrow
        driver.find_element(By.XPATH, "//a[@title='Next']").click()                 #next arrow


        #date = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]')
#for i in range(len(date)):
    #if date[i].text == dt:
        #print(date[i].text,month,year)

        dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]//table/tbody/tr/td/a')

for i in dates:
    if i.text == dt:
        i.click()
        print(i.text, month, year)
        break


