from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome("c:\chromedriver.exe")
        self.url = "http://www.emlakjet.com/satilik-konut/1"
        self.hrefs = []
        self.columns = ['City', 'District', 'Neighborhood', 'Price', 'Gross Square Meter', 'Net Square Meter',
                        'Number of Rooms', 'Building Age', 'Floor Location', 'Number of Bathrooms', 'Number of Toilets',
                        'Within the Site']

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_hrefs(self):
        return self.hrefs

    def set_hrefs(self, elem):
        self.hrefs.append(elem)

    def dump_hrefs(self):
        self.hrefs = []

    def set_columns(self, column):
        self.columns.append(column)

    def get_columns(self):
        return self.columns

    def unique_columns(self, lst):
        return list(set(lst))

    def load_url(self):
        self.driver.get(self.url)

    def read_data(self):
        main = WebDriverWait(self.driver, 200).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div/div[5]/div[1]')))
        soup = bs(main.get_attribute("innerHTML"), "html.parser")

        for elem in soup.findAll('div', {'class': 'styles_listingItem__1asTK'}):
            self.set_hrefs(elem.a['href'])

    def get_columns_from_url(self, url):
        self.driver.get(url)
        cf = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bilgiler"]/div/div[2]/div/div[1]')))
        soup = bs(cf.get_attribute("innerHTML"), "html.parser")

        attributes = soup.findAll('div', {'class': 'styles_tableColumn__2x6nG'})
        for div in attributes:
            text = div.text
            self.set_columns(text)

    def get_info(self, url):
        self.driver.get(url)
        cf = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bilgiler"]/div/div[2]/div/div[1]')))
        soup = bs(cf.get_attribute("innerHTML"), "html.parser")

        master_new = []
        for div in soup.findAll('div', {'class': 'styles_tableColumn__2x6nG'}):
            text = div.text
            master_new.append(text)

        loc_elem = self.driver.find_element(By.CLASS_NAME, 'styles_locationInfo__3adCH')
        loc = loc_elem.text.strip('location_on')
        city, district, neighborhood = map(str.strip, loc.split(" - "))

        master_new.extend([city, district, neighborhood])

        prc_elem = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[2]/div[2]/div[1]/div')
        price = prc_elem.text.replace('.', "")[:-2]
        master_new.append(price)

        for xpath in ['//*[@id="bilgiler"]/div/div[2]/div/div[1]/div[1]/div[4]/div[2]',
                      '//*[@id="bilgiler"]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]',
                      '//*[@id="bilgiler"]/div/div[2]/div/div[1]/div[2]/div[4]/div[2]',
                      '//*[@id="bilgiler"]/div/div[2]/div/div[1]/div[1]/div[5]/div[2]',
                      '//*[@id="bilgiler"]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]']:
            elem = self.driver.find_element(By.XPATH, xpath)
            master_new.append(elem.text)

        return master_new
