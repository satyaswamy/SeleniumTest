from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.crmpro.com/index.html")
driver.maximize_window()

user_name = driver.find_element(By.NAME, "username")
user_passwd = driver.find_element(By.NAME, "password")
Submit_click = driver.find_element(By.XPATH, '//input[@type="submit"]')

act_chain = ActionChains(driver)
act_chain.send_keys_to_element(user_name, "satya@gmail.com")
time.sleep(3)
act_chain.send_keys_to_element(user_passwd, "123gfh")
time.sleep(3)
act_chain.click(Submit_click).perform()
time.sleep(3)

