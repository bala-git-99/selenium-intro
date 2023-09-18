from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
article_count.click()

next_click = driver.find_element(by=By.LINK_TEXT, value="Most viewed pages")
next_click.click()

search_box = driver.find_element(by=By.ID, value="topviews_search_field")
search_box.send_keys("Oppenheimer")
search_box.send_keys(Keys.ENTER)

# driver.quit()
