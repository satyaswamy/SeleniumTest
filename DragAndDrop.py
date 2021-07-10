import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

source = driver.find_element(By.ID, "draggable")
desti = driver.find_element(By.ID, "droppable")

act_chain = ActionChains(driver)
'''
#procedure - 1
act_chain.drag_and_drop(source, desti).perform()
'''
#procedure - 2
act_chain.click_and_hold(source).move_to_element(desti).release().perform()


