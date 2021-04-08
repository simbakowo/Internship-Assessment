import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.takealot.com/russell-hobbs-2200w-crease-control-iron/PLID34147865'
driver = webdriver.Chrome(executable_path="C:/Users/nssatrustee3/Documents/PYTHON_DEV/Webscrapper/chromedriver.exe")
driver.get((url))

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
divs = soup.findAll("div", attrs={ "id" : "shopfront-app" })
print (divs)
product =[]
nextProduct = []
result = [product, nextProduct]


