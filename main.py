from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3786715581&f_AL=true&geoId=103644278&keywords=software%20developer%20intern&location=United%20States&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
button = driver.find_element(By.LINK_TEXT,value="Sign in")
button.click()
time.sleep(1)


username = driver.find_element(By.ID,value="username")
username.send_keys("Enter your username")

password = driver.find_element(By.ID,value="password")
password.send_keys("Enter your password")

second_sign_in = driver.find_element(By.CSS_SELECTOR,value=".login__form_action_container button")
second_sign_in.click()

easy_apply_button = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
easy_apply_button.click()


