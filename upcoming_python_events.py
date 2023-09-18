from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org")

events_calendar = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_list = events_calendar.text.split(sep="\n")

core_dict_list = [{"time": events_list[i], "name": events_list[i + 1]} for i in range(0, len(events_list), 2)]

events = {i: j for i, j in zip(range(len(events_list)), core_dict_list)}
print(events)
driver.quit()
