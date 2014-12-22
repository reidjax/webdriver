# standard library
import sys
import random
import time
 
# need to pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
 
# wait this long before hitting arrow keys
wait_time = 0.05
 
# choose from these
possible_keys = [
    Keys.ARROW_UP,
    Keys.ARROW_DOWN,
    Keys.ARROW_LEFT,
    Keys.ARROW_RIGHT,
]
 
# open up a browser to the game on the web
wd = webdriver.Firefox()
wd.get('http://gabrielecirulli.github.io/2048/')
 
# get new game element
new_game = wd.find_element_by_xpath('/html/body/div/div[2]/a')
 
# keep playing games and recording the score
score = None
while True:
 
    # break and get score if game is over
    try:
        game_ended = wd.find_element_by_class_name('game-message game-over')
    except NoSuchElementException:
        print 'yo'
    else:
        print 'hey'
    # wait for some time for move to take place
    time.sleep(wait_time)
 
    # choose a random direction to push
    new_game.send_keys(random.choice(possible_keys))
 
wd.quit()