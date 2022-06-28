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
# driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
# driver.implicitly_wait(5)
# my_element= driver.find_element(By.XPATH, "//*[@id='downloadButton']")
# my_element.click()
#
# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, 'progress-label') , # Element filtration
#         'Complete!'# The expected text
#     )
# )
# close = driver.find_element(By.XPATH, '//button[text()="Close"]')
# close.click()

driver.get("https://lovestagram-76a4b.web.app/")
driver.implicitly_wait(5)
user_email = driver.find_element(By.XPATH, "//*[@id='email']")
user_email.send_keys("neopet20001@gmail.com")
user_pass = driver.find_element(By.ID, 'password')
user_pass.send_keys("nhandeptrai123")

submit = driver.find_element(By.XPATH, '//button[text()=" Log In "]')
submit.click()
