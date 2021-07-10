from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
from selenium.webdriver import ActionChains


subprocess.call("TASKKILL /f /IM CHROME.exe")

head_less = webdriver.ChromeOptions()
head_less.headless = True  #first option (Full screenshot needs to be taken in headless mode only
#head_less.add_argument("--headless")  #second option
#head_less.add_argument("--incognito")  #incognito mode
driver = webdriver.Chrome(ChromeDriverManager().install(), options=head_less)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

#screenshot
#driver.get_screenshot_as_file("screenshot1.png")

#full screenshot
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S("Width"), S("Height"))
driver.find_element_by_tag_name('body').screenshot("screenshot2.png")