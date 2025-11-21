# Day 53: Web Scraping Project - Zillow Clone
# In this project, we will scrape real estate data from a Zillow clone website.
# We will extract property prices, addresses, and links to the listings.



#                           BeaytifulSoup and Requests
# We will use BeautifulSoup for web scraping and requests to fetch the webpage content.


from bs4 import BeautifulSoup
import requests
google_sheet_url="https://docs.google.com/forms/d/e/1FAIpQLSe-srMgMIGp9w1dyFFFJzQNWbw7S3SvdK68JHqxRblN3S6O0A/viewform?usp=header"
zillow_clone_link="https://appbrewery.github.io/Zillow-Clone/"

soup=BeautifulSoup(requests.get(zillow_clone_link).text,"html.parser")
prices=soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices=[price.text for price in prices]
prices_list=[i.split("+")[0] for i in prices]
addresses=soup.find_all(name="address")
addresses_list=[address.text.strip() for address in addresses]
links=soup.find_all(class_="StyledPropertyCardDataArea-anchor")
links_list=[link["href"] if "http" in link["href"] else f"https://appbrewery.github.io{link['href']}" for link in links]
#                           Selenium to Automate Form Filling
# We will use Selenium to automate the process of filling out a Google Form with the scraped data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(google_sheet_url)
time.sleep(5)
# addresses_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
# addres_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,addresses_input_xpath)))
# addres_input.send_keys(addresses_list[0])
# prices_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
# price_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,prices_input_xpath)))
# price_input.send_keys(prices_list[0])
# link_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
# link_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,link_input_xpath)))
# link_input.send_keys(links_list[0])
# submit_button_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
# submit_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,submit_button_xpath)))
# submit_button.click()
# another_response_xpath='/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
# another_response=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,another_response_xpath)))
# another_response.click()

for element in range(len(addresses_list)):
    try:
        time.sleep(10)
        addresses_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        addres_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,addresses_input_xpath)))
        addres_input.send_keys(addresses_list[element])
        prices_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        price_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,prices_input_xpath)))
        price_input.send_keys(prices_list[element])
        link_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        link_input=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,link_input_xpath)))
        link_input.send_keys(links_list[element])
        submit_button_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        submit_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,submit_button_xpath)))
        submit_button.click()
        another_response_xpath='/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
        another_response=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,another_response_xpath)))
        another_response.click()
        time.sleep(10)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
