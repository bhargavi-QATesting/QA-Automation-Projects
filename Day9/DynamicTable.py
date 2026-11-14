from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li').click()
totaldata = driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div')
#for i in totaldata:
    #print(i.text)


rows = driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div[@class='oxd-table-card']")
print("Total Rows:", len(rows))
#for i in rows:
    #print(i.text)


#printing first row data
rowdata = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]')
print(rowdata.text)

#printing only status column
#driver.find_elements(By.XPATH,"//div[contains(@class='oxd-table-header-cell oxd-padding-cell oxd-table-th') and contains(text(),'Status')]")
enabledtext = driver.find_elements(By.XPATH,"//div[contains(text(),'Enabled')]")
print(len(enabledtext))

for i in range(0,len(enabledtext)):
    if enabledtext[i].text == "Enabled":
        print(len(enabledtext),enabledtext[i].text)
        #print(len(enabledtext[i].text))


'''specificdata = (driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[5]'))
                #(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[5]'))
print("No of enabled content:", len(specificdata))

for i in specificdata:
    if i.text=='Enabled':
        print(i.text)'''

driver.quit()

