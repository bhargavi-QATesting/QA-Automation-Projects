from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]').click()
time.sleep(2)
year = Select(driver.find_element(By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/select'))
year.select_by_visible_text("2027")
month = Select(driver.find_element(By.XPATH,'//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/select'))
month.select_by_visible_text("March")
time.sleep(2)
#date = driver.find_element(By.XPATH,"//div[contains(@class,'react-datepicker__day') and text()='13']")
#date.click()

#print(date,month,year)

dates = driver.find_elements(By.XPATH, "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month'))]")
for i in dates:
    if i.text == "13":
        i.click()
        time.sleep(2)
        break


'''for i in range(len(dates)):
    if dates[i] == dt:
        #i.click()
        time.sleep(2)
        print(dates[i], month, year)
        break'''

driver.quit()