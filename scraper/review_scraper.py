from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from pprint import pprint
import sqlite3
import os

URL = "https://www.google.com/search?q=bmw+of+austin#lrd=0x8644cd1fdca503e1:0x49fed3597ce3a823,1,,,"

options = Options()

# options.add_argument("--headless")
# options.add_argument("--window-size=1366,768")

options.add_argument("--disable-notifications")
options.add_argument("--lang=en-GB")

file_path = os.path.dirname(os.path.realpath(__file__))
driver_path = os.path.join(file_path, "chromedriver")

driver = webdriver.Chrome(driver_path, options=options)
driver.get(URL)

wait = WebDriverWait(driver, 30)
try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "review-dialog-body"))) 
except TimeoutException as e:
        print("Wait Timed out")
        print(e)

# newest = driver.find_elements_by_class_name("AxAp9e")
# newest[1].click()

# time.sleep(3)

# reviews_header = driver.find_element_by_css_selector('div.kp-header')
# reviews_link = reviews_header.find_element_by_partial_link_text('Google reviews')
# number_of_reviews = int(reviews_link.text.split()[0].replace(",", ""))

# print("Total Number of reviews", number_of_reviews)

# x=0
# desiredReviewsCount=700
# while x<desiredReviewsCount:
#     driver.find_elements_by_class_name("gws-localreviews__google-review")[-1].location_once_scrolled_into_view
#     driver.find_elements_by_class_name("icGDpd")[-1].location_once_scrolled_into_view
#     driver.find_elements_by_class_name("pi8uOe")[-1].location_once_scrolled_into_view
#     x = len(driver.find_elements_by_class_name("gws-localreviews__google-review"))
#     if x % 10 == 0:
#         print("Loaded Count", x)

# user_reviews = []
# counter = 1

# for review in driver.find_elements_by_class_name("gws-localreviews__google-review"):
#     user = {}
#     try:
#         Name = review.find_element_by_class_name("TSUbDb")
#         user["Reviewers_Name"]= Name.text
#     except NoSuchElementException:
#         user["Reviewers_Name"]= ""
    
#     try:
#         ReviewByuser = review.find_element_by_class_name("A503be")
#         user["TotalReviewsByUser"] = ReviewByuser.text
#     except NoSuchElementException:
#         user["TotalReviewsByUser"] = ""
        
#     try:
#         star = review.find_element_by_class_name("Fam1ne")
#         ReviewStar = star.get_attribute("aria-label")
#         user["ReviewRating"] = ReviewStar
#     except NoSuchElementException:
#         user["ReviewRating"] = ""

#     try:
#         Date = review.find_element_by_class_name("dehysf")
#         user["ReviewDate"] = Date.text
#     except NoSuchElementException:
#         user["ReviewDate"] = ""

#     Body = review.find_element_by_class_name('Jtu6Td')
#     try:
#         review.find_element_by_class_name('review-snippet').click()
#         full_text = review.find_element_by_class_name('review-full-text')
#         user["ReviewDescription"] = full_text.text
#     except NoSuchElementException:
#         user["ReviewDescription"] = Body.text
    
#     print(f'Processed {counter} Review..')
#     counter += 1
#     user_reviews.append(user)
# print("All Done")

# driver.close()

# pprint(user_reviews)

# conn = sqlite3.connect('reviews.db')
# cursor = conn.cursor()

# # Reviewers_Name
# # TotalReviewsByUser
# # ReviewRating
# # ReviewDate
# # ReviewDescription
# cursor.execute('''CREATE TABLE IF NOT EXISTS reviews
#                (Reviewers_Name TEXT, TotalReviewsByUser TEXT, ReviewRating TEXT, 
#                ReviewDate TEXT, ReviewDescription TEXT)''')

# for user_review in user_reviews:
#     cursor.execute('''INSERT INTO reviews(
#     Reviewers_Name, TotalReviewsByUser, ReviewRating, ReviewDate, ReviewDescription) VALUES 
#     (?, ?, ?, ?, ?)''', (
#         user_review["Reviewers_Name"], user_review["TotalReviewsByUser"], user_review["ReviewRating"],
#         user_review["ReviewDate"], user_review["ReviewDescription"]
#         ) 
#     )


# conn.commit()
# print("Records inserted in database")

# conn.close()
