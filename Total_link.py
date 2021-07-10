from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

Links = []
linklist = driver.find_elements(By.TAG_NAME, "a")
print("The total no of tags in the page are", len(linklist))
for i in linklist:
    if len(i.text) > 0:
        Links.append(i)
        print(i.get_attribute("href"))
print(Links)



#driver.quit()

