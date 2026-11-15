from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Day14 import ExcelUtils

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\\SeleniumPractice\\Workbook5.xlsx"
rows = ExcelUtils.getRowCount(file,"Sheet1")

for r in range(2, rows+1):
    InvestAm = ExcelUtils.readData(file,"Sheet1",r,1)
    InvestPer = ExcelUtils.readData(file,"Sheet1",r,2)
    rateofReturn = ExcelUtils.readData(file, "Sheet1", r, 3)
    Intrestfrequency = ExcelUtils.readData(file,"Sheet1",r,4)
    TaxRate = ExcelUtils.readData(file,"Sheet1",r,5)
    expected = ExcelUtils.readData(file,"Sheet1",r,6)

    #Passing data to the application
    calvalue1 = driver.find_element(By.XPATH, "//input[@id='edulonvalue_1']")
    calvalue1.clear()
    calvalue1.send_keys(InvestAm)
    time.sleep(2)
    calvalue2 = driver.find_element(By.XPATH,"//input[@id='edulonvalue_2']")
    calvalue2.clear()
    calvalue2.send_keys(InvestPer)
    time.sleep(2)
    calvalue3 = driver.find_element(By.XPATH,"//input[@id='edulonvalue_3']")
    calvalue3.clear()
    calvalue3.send_keys(rateofReturn)
    time.sleep(2)
    # Close popup using its close button
    # Close popup
    popup_close = driver.find_element(
        By.XPATH, "//button[contains(@class,'cbmcclose')]"
    )

    driver.execute_script("arguments[0].click();", popup_close)

    time.sleep(3)

    # Check popup status
    popup = driver.find_element(By.ID, "main_popup_modal_div")

    #print("Popup displayed:", popup.is_displayed())

    overlays = driver.find_elements(By.CLASS_NAME, "wzrk-overlay")

    for overlay in overlays:
        print("Overlay displayed:", overlay.is_displayed())

    # Click interest frequency option
    calvalue4 = driver.find_element(
        By.XPATH,
        "//div[@class='clearfix range_block MT10 yesno_container']//div[@class='clearfix']"
    )

    driver.execute_script("arguments[0].click();", calvalue4)
    time.sleep(2)
    calvalue5 = driver.find_element(By.XPATH,"//input[@id='edulonvalue_4']")
    calvalue5.clear()
    calvalue5.send_keys(TaxRate)
    time.sleep(2)
    # Click Calculate button using JavaScript
    calculate_button = driver.find_element(
        By.XPATH,
        "//a[contains(@class,'btn_common') and contains(@onclick,'calculate')]"
    )

    driver.execute_script("arguments[0].click();", calculate_button)
    time.sleep(2)
    ActualValue = driver.find_element(By.XPATH,"/html/body/main/div[7]/section/div/div/div[1]/div[2]/div/div/div[7]/div[2]/div[1]/div").text

    ActualValue = ActualValue.split("\n")[0]
    ActualValue = ActualValue.replace("₹", "").replace(",", "").strip()

    if float(expected) == float(ActualValue):
        print("test Passed")
        ExcelUtils.writeData(file,"Sheet1",r,8,"Pass")
        ExcelUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test Failed")
        ExcelUtils.writeData(file, "Sheet1", r, 8, "Fail")
        ExcelUtils.fillRedColor(file, "Sheet1", r, 8,)

    reset_button = driver.find_element(By.ID, "reset_btn")

    driver.execute_script("arguments[0].click();", reset_button)

    time.sleep(2)
