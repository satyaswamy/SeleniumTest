from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browser = "Chrome"

if browser == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == "Firefox":
    driver = webdriver.Firefox(GeckoDriverManager().install())
else:
    print("Enter a right browser name")

driver.get("https://www.hubspot.com/")
time.sleep(5)
driver.quit()