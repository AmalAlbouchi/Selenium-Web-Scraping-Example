from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

url = "https://www.vesselfinder.com/vessels?page=1"

driver.get(url)

total = []

rows = driver.find_elements(by=By.XPATH, value="/html/body/div/div/main/div/section/table/tbody/tr")
for row in rows:
    vessel = row.find_element(by=By.CLASS_NAME, value='slna').text + ' (' + \
             row.find_element(by=By.CLASS_NAME, value='slty').text + ')'
    quote_text = row.find_element(by=By.CLASS_NAME, value='v2').text
    built = row.find_element(by=By.CLASS_NAME, value='v3').text
    gt = row.find_element(by=By.CLASS_NAME, value='v4').text
    dwt = row.find_element(by=By.CLASS_NAME, value='v5').text
    size = row.find_element(by=By.CLASS_NAME, value='v6').text
    countryaux = row.find_element(by=By.CLASS_NAME, value='flag-icon')
    country = countryaux.get_attribute('title')
    linkaux = row.find_element(by=By.CLASS_NAME, value='ship-link')
    link = linkaux.get_attribute('href')
    new = (vessel, built, dwt, gt, size, country, link)
    total.append(new)
df = pd.DataFrame(total, columns=['Vessel', 'Built', 'DWT', 'GT', 'Size', 'Country', 'Link'])
df.to_csv('Vessels.csv')

driver.close()
