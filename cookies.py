from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

#driver.add_cookie("") // for adding cookies with all the valid parameters

cookies = driver.get_cookies()
for cook in cookies:
    print(cook)