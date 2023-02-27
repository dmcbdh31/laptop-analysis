from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

file =open("laptop.csv", "w")
writer = csv.writer(file)
writer.writerow(["ID", "Name", "Price", "Specifications", "Number of Reviews"])

browser_driver = Service(r"C:/Users/Nae/Desktop/chromedriver.exe")

scraper = webdriver.Chrome(service=browser_driver)

scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

Unique_ID = 1
while True:
    laptops = scraper.find_elements(By.CLASS_NAME, "caption")
    for caption in laptops:
        Name = caption.find_element(By.CLASS_NAME, "title") 
        Price = caption.find_element(By.CLASS_NAME, "pull-right.price")
        Specifciations = caption.find_element(By.CLASS_NAME, "description")
        writer = csv.writer(file)
        writer.writerow(
     [Unique_ID, Name.text, Price.text, Specifciations.text])
    Unique_ID += 1
    try:
        element = scraper.find_element(By.PARTIAL_LINK_TEXT, ">").click
    except NoSuchElementException:
        element = WebDriverWait(webdriver, 30).until
        EC.presence_of_all_elements_located(By.CLASS_NAME)
        break
# find elements for multiple.
file.close()
scraper.quit()

# scrape different cards that hold each laptop - replicated, css class
# for loop for list of laptops - repeat 19-22 - focus on 1st page. while loop

