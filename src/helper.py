from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import math
import time

#code to get review and put it into a dataframe
def get_review():
    """
    input: none
    output: x - pd Dataframe of reviews
    """
    reviews = driver.find_elements_by_class_name('review-text')
    review_list = []
    for review in reviews:
        z = review.text.lower().replace('\n',' ')
        review_list.append(z)
    x = pd.DataFrame(review_list)
    return x

#this code extract reviews stars
def get_stars():
    """
    intput:
    output:
    """
    stars = driver.find_elements_by_class_name("review-rating")[2:]
    star_reviews = []
    for star in stars:
        star_reviews.append(star.get_attribute("innerText"))
    return star_reviews

#clicking next
def click_next():
    """
    input:
    outpu:
    """
    nx = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[1]/div[5]/div[3]/div/div/span/div/ul/li[2]/a')
    nx.click()

#find how many reviews a product has
#get rid of the comma in a number example: 1,000
#divide number of reviews by 10 - each page has 10 reviews
#round up to get the number of pages we have to scrape
def num_pages():
    """
    input:
    output:
    """
    number_reviews_string = driver.find_element_by_xpath('//*[@id="filter-info-section"]/div/span').text
    num = number_reviews_string.split('|')[1].replace(',','')
    number_reviews = [int(s) for s in str.split(num) if s.isdigit()]
    return number_reviews[0]

    #assign number of pages to num_pages: how many pages of reviews do the item has?
    num_pages = num_pages()

    review_table = []
    star_table = []
