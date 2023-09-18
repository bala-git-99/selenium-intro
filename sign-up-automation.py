from selenium import webdriver
from selenium.webdriver.common.by import By

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
email_id = input("Please enter your email-id: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

fname_tag = driver.find_element(by=By.NAME, value="fName")
fname_tag.send_keys(first_name)

lname_tag = driver.find_element(by=By.NAME, value="lName")
lname_tag.send_keys(last_name)

email_tag = driver.find_element(by=By.NAME, value="email")
email_tag.send_keys(email_id)

submit = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit.click()

# driver.quit()
