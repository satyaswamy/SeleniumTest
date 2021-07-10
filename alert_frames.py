from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

#driver.find_element(By.NAME, "login").send_keys("satyanarayan")
#driver.find_element(By.NAME, "passwd").send_keys("hdwcbcbc")
driver.find_element(By.NAME, "proceed").click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.switch_to.default_content()
