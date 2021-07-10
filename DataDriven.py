from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import xlrd
import time
import subprocess

data_sheet = xlrd.open_workbook("MyTestSelenium.xlsx")
sheet = data_sheet.sheet_by_name("Mytest")

'''
subprocess.call("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/")
driver.maximize_window()


#click on 30days trail
driver.find_element(By.PARTIAL_LINK_TEXT, "FREE").click()
'''

print(sheet.ncols)
print(sheet.nrows)