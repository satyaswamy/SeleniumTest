from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess

subprocess.call("TASKKILL /f /IM CHROME.exe")


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(3)

login_ele = driver.find_element(By.ID, "ctl00_HyperLinkLogin")
act_chain = ActionChains(driver)
act_chain.move_to_element(login_ele).perform()

Club_member = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
act_chain.move_to_element(Club_member).perform()

member_login = driver.find_element(By.LINK_TEXT, "Member Login")
act_chain.move_to_element(member_login).click()
