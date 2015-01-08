from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search_term = raw_input('What would you like to search?\n')

browser = webdriver.Firefox()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')  # Find the search box
search.send_keys(search_term)
search.send_keys(Keys.RETURN)
print browser.title

