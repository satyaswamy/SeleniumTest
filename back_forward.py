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

driver.find_element(By.LINK_TEXT, "Best Sellers").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(3)
driver.refresh()
