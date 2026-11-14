from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

#count no of rows and columns
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

print("Total no of rows are:", rows)
print("Total no of columns are:", columns)

#read specific row data and specific column data
specificrow = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]")
print(specificrow.text)
specificcolumn = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[2]")

for i in specificcolumn:
    print(i.text)

#read specific data from the table
specificdata = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[2]/td[1]")
print(specificdata.text)
specificdata2 = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[3]")
print(specificdata2.text)

#read all the rows and column data
alldata = driver.find_element(By.XPATH, "//table[@name='BookTable']")
print(alldata.text)
#or
for r in range(2,rows+1):
    for c in range(1,columns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

#read data based on condition(list books name whose author is mukesh)
authorcolumn = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//td[2]")
bookcolumn = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//td[1]")
pricecolumn = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody//td[4]")

for i in range(len(authorcolumn)):
    if authorcolumn[i].text == "Mukesh":
        print(bookcolumn[i].text, authorcolumn[i].text, pricecolumn[i].text)

#or

for r in range(2,rows+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName,authorName,price)

driver.quit()