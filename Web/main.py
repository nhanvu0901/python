from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path="D:/SeleniumDrivers/geckodriver.exe")

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
driver.implicitly_wait(10)
try:
    no_button = driver.find_element(By.CLASS_NAME, "at-cm-no-button")
    no_button.click()
except:
    print('No element with this class name. Skipping ....')
sum1 = driver.find_element(By.XPATH, "//*[@id='sum1']")
sum2 = driver.find_element(By.XPATH, "//*[@id='sum2']")
btn = driver.find_element(By.XPATH, '//button[text()="Get Total"]')
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD3)
sum2.send_keys(69)
btn.click()
