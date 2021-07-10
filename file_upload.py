from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")
driver.maximize_window()

driver.find_element(By.NAME, "upfile").send_keys("C:/Users/satya/Desktop/test.txt")
driver.find_element(By.XPATH, '//input[@type="submit"]').click()