from xmlrpc.client import DateTime

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

web = webdriver.Chrome()
web.get('http://localhost:4200/')
time.sleep(1)

sname = "Akhaury Nimitt Verma"
name =web.find_element('xpath', '//*[@id="name"]')
name.send_keys(sname)

date_of_birth= "11/05/1999"
dob =web.find_element('xpath', '//*[@id="dob"]')
dob.send_keys(date_of_birth)

# Wait for the dropdown to be clickable
sel_country= web.find_element('xpath', '//*[@id="country"]')
dropdown_element = Select(WebDriverWait(web, 10).until(EC.element_to_be_clickable(sel_country)))
dropdown_element.select_by_value("India")
# Click the dropdown

gender = web.find_element('xpath', '//*[@id="myForm"]/div[4]/div[1]/label')
gender.click()
time.sleep(5)

submit = web.find_element('xpath', '//*[@id="myForm"]/button')
time.sleep(5)
submit.click()
