from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\Automation\drivers\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Naveen Automation Lab")
option_list = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(option_list))
for ele in option_list:
    print(ele.text)
    if ele.text == "naveen automation labs blogc" :
        print("text found")
        break
    else:
        print("The required text not found in the list")

driver.quit()