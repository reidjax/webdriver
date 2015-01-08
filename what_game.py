import urllib
import json as js
from selenium import webdriver

search_term = raw_input('What game would you like to play?\n')
search_encoded = urllib.urlencode({'q':search_term})

response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + search_encoded).read()
search_json = js.loads(response)

url = search_json['responseData']['results'][0]['url']

print "Let's play!"

wd = webdriver.Firefox()
wd.get(url)
