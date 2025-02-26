from xmlrpc.client import DateTime

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

web = webdriver.Chrome()
web.get('http://localhost:63342/Python_Practice_Projects/index.html?_ijt=1icjdm98nke3m0ut7m0lttm1h9')
time.sleep(1)

sname = "Akhaury Nimitt Verma"
name =web.find_element('xpath', '//*[@id="name"]')
name.send_keys(sname)

date_of_birth= "11/05/1999"
dob =web.find_element('xpath', '//*[@id="dob"]')
dob.send_keys(date_of_birth)

''''# Wait for the dropdown to be clickable
sel_country= web.find_element('xpath', '//*[@id="country"]')
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable(sel_country))

# Click the dropdown
dropdown_element.click()

time.sleep(10000)

# Wait for the options to be visible
# option_xpath = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[6]/span')
# options = WebDriverWait(web, 5).until(
#     EC.presence_of_all_elements_located((By.XPATH, option_xpath))
# )
#
# # Select an option
# for option in options:
#     if option.text =="Portugal":
#         option.click()
#         break
# while True:
#     pass
#
# sel_box = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/label/div/div[2]/div/span')
# sel_box.click()
#
# submit= web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
# submit.click()'''