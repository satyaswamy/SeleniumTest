from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import time
import subprocess

subprocess.call("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
driver.maximize_window()
time.sleep(3)

#function to select reqied options in the list(multiple/single)


def multiSelect(mlist, values):
    if not values[0] == "all":
        for ele in mlist:
            for k in range(len(values)):
                if ele.text == values[k]:
                    ele.click()
                    break
    else:
        for ele in mlist:
               ele.click()

driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(3)
multi_list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
value_list = ["choice 2", "choice 6 2 1"]
multiSelect(multi_list, value_list)
'''
for ele in multi_list:
    print(ele.text)
    if ele.text == "choice 2":
        ele.click()
        break
'''