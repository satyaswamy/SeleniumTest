from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

r_click_ele = driver.find_element(By.XPATH, '//span[text()="right click me"]')
act_process = ActionChains(driver)
act_process.context_click(r_click_ele).perform()

r_click_menu = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-icon span")
for ele in r_click_menu:
    if ele.text == "Copy":
        ele.click()