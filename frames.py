from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://www.londonfreelance.org/courses/frames/index.html")
driver.maximize_window()

driver.switch_to.frame(2)
header_text = driver.find_element(By.CSS_SELECTOR, "body > h2").text
print(header_text)
driver.switch_to.default_content()
