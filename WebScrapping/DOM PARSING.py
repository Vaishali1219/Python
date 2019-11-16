# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:53:59 2019

@author: vaish
"""

from bs4 import BeautifulSoup as soup
from time import sleep
import time 
from requests import get
import pandas as pd
from random import randint
from IPython.core.display import clear_output
from warnings import warn
from urllib.request import urlopen as uReq

#print(response.text[:500])

#print(html_soup)

starter = [str(i) for i in range(51, 300, 50)]
years_url = [str(i) for i in range(2000, 2019)]
headers = {"Accept-Language":"en-US, en;q = 0.5"}
name = []
years = []
imdb_ratings = []
metascores = []
votes = []

start_time = time.time()
requests = 0

filename = "movies.csv"
f = open(filename, "w")
headers = "Movie_Name, Release_Year, IMdb_Ratings, Meta_Score, Votes\n"
f.write(headers)

for year_url in years_url:
    for starters in starter:
        url = "https://www.imdb.com/search/title?release_date={}-01-01,{}-12-31&sort=num_votes,asc&start={}&ref_=adv_nxt".format(year_url, year_url, starter)
        response = get(url)
        
        sleep(randint(15, 20))
        requests += 1
        elapsed_time = time.time() - start_time
        print("Request: {}; Frequency: {} requests/s".format(requests, requests/elapsed_time))
        clear_output(wait = True)
        
        if response.status_code != 200:
            warn('Request: {}; Status Code: {}'.format(requests, response.status_code))
            
        if requests > 95:
            warn("Number of requests were greater than expected")
            break
        
        html_soup = soup(response.text, 'html.parser')
        
        movie_containers = html_soup.find_all('div', class_ = "lister-item mode-advanced")
#        print(len(movie_containers))
#        print(type(movie_containers))
        i = 0
        
        for container in movie_containers:
            if container.find('div', class_ = 'rating-metascore') is None:
                mc = movie_containers[i]
                movie = mc.h3.a.text
                name.append(movie)
                
                Release = mc.h3.find('span', class_ = "lister-item-year text-muted unbold")
                year = Release.text
                years.append(year[1:5])
                yr = year[1 : 5]
                
                Ratings = float(mc.strong.text)
                imdb_ratings.append(Ratings)
                
                Meta = mc.find("span", attrs={"class":"lister-item-index unbold text-primary"})
                MetaScore = float(Meta.text)
                metascores.append(MetaScore)
                
                Vot = mc.find("span", attrs={"name":"nv"})
                Votes = Vot.text
                votes.append(Votes)
                
                f.write(movie + "," + yr + "," + str(Ratings) + "," + str(MetaScore) + "," + Votes + "\n")        
                i += 1    
#print(len(name))   

f.close()
test_df = pd.DataFrame({
        'movie': name,
        'year': years,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes':votes
        })
print(test_df.info())
test_df