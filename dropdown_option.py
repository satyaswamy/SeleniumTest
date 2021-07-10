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
driver.get("https://www.orangehrm.com/")
driver.maximize_window()


#click on 30days trail
driver.find_element(By.PARTIAL_LINK_TEXT, "FREE").click()



#Write a function for selecting an option

def select_value(element, value):
    select = Select(element)
    select.select_by_visible_text("India")
    select.select_by_value("Country")
    select.select_by_index(4)


def select_dropdown_list(element, value):
    for indu in element:
        if indu.text == value:
            print(indu.text)
            indu.click()

list_indu = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Industry"]/option')
list_country = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
list_state = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_State"]/option')
#indust = driver.find_element(By.ID, "Form_submitForm_Industry")
select_dropdown_list(list_indu, "Travel")
select_dropdown_list(list_country, "India")
time.sleep(20)
driver.find_element(By.XPATH, '//*[@id="Form_submitForm_subdomain"]').send_keys("My First")
driver.find_element(By.NAME, "FirstName").send_keys("satya")
driver.find_element(By.NAME, "LastName").send_keys("narayan")
driver.find_element(By.NAME, "JobTitle").send_keys("Software")
driver.find_element(By.NAME, "CompanyName").send_keys("Allwell")
driver.find_element(By.NAME, "Contact").send_keys("9916199963")
driver.find_element(By.NAME, "Email").send_keys("satyanarayanswamy@gmail.com")
driver.find_element(By.ID, "recaptcha-anchor").click()
select_dropdown_list(list_state, "Karnataka")
driver.find_element(By.ID, "recaptcha-anchor").click()

#driver.quit()

'''
#Check the dropdown options
select = driver.find_element(By.ID, "Form_submitForm_Industry")
ind_list = Select(select)
industry_list = ind_list.options
print(industry_list)

print("the number of industery listed is", len(industry_list))
for indu in industry_list:
    if indu.text == "Education":
        print(indu.text)
        indu.click()
ind_list.select_by_index(3)
ind_list.select_by_value("health")
ind_list.select_by_visible_text("Travel")
'''

