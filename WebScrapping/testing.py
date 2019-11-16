from bs4 import BeautifulSoup as soup
from time import sleep
import time 
from requests import get
import pandas as pd
from random import randint
from IPython.core.display import clear_output
from warnings import warn
from urllib.request import urlopen as uReq
import sqlite3
from selenium import webdriver
import datetime
import chilkat
import sys
import time
import os

driver = webdriver.Firefox(executable_path=r"C:\Users\vaish\AppData\Local\Programs\Python\Python37\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe")
driver.get("https://www.naukri.com/jobs-in-mumbai")
Total_Rounds = driver.find_elements_by_xpath('//span[@class = "cnt"]')
Rounds = Total_Rounds[0].text
for a in range(len(Rounds), 2, -1):
    if (Rounds[2:a].isnumeric()):
        length = Rounds[2:a]
        break
total = int((Rounds[(len(length) + 6):]))
quo = total//int(length)
print(total)
print(length)
print("done")
driver.close()
