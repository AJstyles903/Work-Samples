'''
Work : Login To The Website Without Touch Your PC
Author : Mr.Aryan (AJstyles903)
'''

from time import sleep
from selenium import webdriver
from  random import randint
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver')
driver.get('https://acme-test.uipath.com/login')
print ("Opened Website")

sleep(randint(1,4))
username = driver.find_element('name','email')
username.send_keys('dhruval@gmail.com')# here pass your username
password = driver.find_element('name','password')
password.send_keys('Dhruval@123')# here pass your password

button_login = driver.find_element(By.CSS_SELECTOR, 'body > div > div.main-container > div > div > div > form > button')
button_login.click()

button_work_items = driver.find_element(By.CSS_SELECTOR, '#dashmenu > div:nth-child(2) > a > button')
button_work_items.click()
