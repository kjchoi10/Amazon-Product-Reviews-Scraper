from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import math
import time
import helper

#Ask user which Amazon product they want to scrape.
amazon = input('Amazon Listing Review Link? ')
driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/93.0.4577.63/chromedriver')
driver.get("{}".format(amazon))

#assign number of pages to num_pages: how many pages of reviews do the item has?
num_pages = helper.num_pages()

review_table = []
star_table = []

try:
    for i in range(1, num_pages - 1):
        m = helper.get_review()
        n = helper.get_stars()
        review_table.append(m)
        star_table.append(n)
        click_next()
        time.sleep(3)
except NoSuchElementException:
        print("Completed!")

x = pd.concat(review_table, ignore_index=True)

star_table = pd.DataFrame(star_table)
stars = star_table.to_numpy().flatten().tolist()

#stars.
x = pd.DataFrame(x)
stars = pd.DataFrame(stars)

df = pd.merge(stars, x, left_index=True, right_index=True, how='outer')
df.columns = ['Stars','Reviews']

#export the file in csv
df.to_csv('rev.csv', index=False)
