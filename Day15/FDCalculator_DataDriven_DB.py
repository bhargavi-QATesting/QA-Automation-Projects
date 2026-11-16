from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mysql.connector

driver = webdriver.Chrome()
driver.get(
"https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="Root@123", database="mydb")
    curs = conn.cursor()
    curs.execute("select * from fixeddeposit_data")

    for row in curs:

        InvestAm = row[1]
        InvestPer = row[2]
        rateofReturn = row[3]
        Intrestfrequency = row[4]
        TaxRate = row[5]
        expected = row[6]

        # Passing data to the application
        calvalue1 = driver.find_element(By.XPATH, "//input[@id='edulonvalue_1']")
        calvalue1.clear()
        calvalue1.send_keys(str(InvestAm))
        time.sleep(2)

        calvalue2 = driver.find_element(By.XPATH, "//input[@id='edulonvalue_2']")
        calvalue2.clear()
        calvalue2.send_keys(str(InvestPer))
        time.sleep(2)

        calvalue3 = driver.find_element(By.XPATH, "//input[@id='edulonvalue_3']")
        calvalue3.clear()
        calvalue3.send_keys(str(rateofReturn))
        time.sleep(2)

        overlays = driver.find_elements(By.CLASS_NAME, "wzrk-overlay")

        for overlay in overlays:
            print("Overlay displayed:", overlay.is_displayed())

        calvalue4 = driver.find_element(
            By.XPATH,
            "//div[@class='clearfix range_block MT10 yesno_container']//div[@class='clearfix']"
        )
        driver.execute_script("arguments[0].click();", calvalue4)
        time.sleep(2)

        calvalue5 = driver.find_element(By.XPATH, "//input[@id='edulonvalue_4']")
        calvalue5.clear()
        calvalue5.send_keys(str(TaxRate))
        time.sleep(2)

        calculate_button = driver.find_element(
            By.XPATH,
            "//a[contains(@class,'btn_common') and contains(@onclick,'calculate')]"
        )
        driver.execute_script("arguments[0].click();", calculate_button)
        time.sleep(2)

        ActualValue = driver.find_element(
            By.XPATH,
            "/html/body/main/div[7]/section/div/div/div[1]/div[2]/div/div/div[7]/div[2]/div[1]/div"
        ).text

        ActualValue = ActualValue.split("\n")[0]
        ActualValue = ActualValue.replace("₹", "").replace(",", "").strip()

        if float(expected) == float(ActualValue):
            print("Test Passed")
        else:
            print("Test Failed")

        reset_button = driver.find_element(By.ID, "reset_btn")
        driver.execute_script("arguments[0].click();", reset_button)
        time.sleep(2)
    conn.close()
except:
    print("Test Failed")

driver.close()
