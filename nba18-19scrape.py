# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.basketball-reference.com/boxscores/?month=10&day=16&year=2018'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

name_Atlanta = soup.find('a', string = 'Atlanta')
name_Boston = soup.find('a' , string = 'Boston')
name_Brooklyn = soup.find('a', string = 'Brooklyn')
name_Charlotte = soup.find('a', string = 'Charlotte')
name_Chicago = soup.find('a', string = 'Chicago')
name_Cleveland = soup.find('a', string = 'Cleveland')
name_Dallas = soup.find('a', string = 'Dallas')
name_Denver = soup.find('a', string = 'Denver')
name_Detroit = soup.find('a', string = 'Detroit')
name_GoldenState = soup.find('a', string = 'GoldenState')
name_Houston = soup.find('a', string = 'Houston')
name_Indiana = soup.find('a', string = 'Indiana')
name_LA_Clippers = soup.find('a', string = 'LA_Clippers')
name_LA_Lakers = soup.find('a', string = 'LA_Lakers')
name_Memphis = soup.find('a', string = 'Memphis')
name_Miami = soup.find('a', string = 'Miami')
name_Milwaukee = soup.find('a', string = 'Milwaukee')
name_Minnesota = soup.find('a', string = 'Minnesota')
name_NewOrleans = soup.find('a', string = 'NewOrleans')
name_NewYork = soup.find('a', string = 'NewYork')
name_OklahomaCity = soup.find('a', string = 'OklahomaCity')
name_Orlando = soup.find('a', string = 'Orlando')
name_Philadelphia = soup.find('a', string = 'Philadelphia')
name_Phoenix = soup.find('a', string = 'Phoenix')
name_Portland = soup.find('a', string = 'Portland')
name_Sacramento = soup.find('a', string = 'Sacramento')
name_SanAntonio = soup.find('a', string = 'SanAntonio')
name_Toronto = soup.find('a', string = 'Toronto')
name_Utah = soup.find('a', string = 'Utah')
name_Washington = soup.find('a', string = 'Washington')

name_Atlanta_text = name_Atlanta.text
name_Boston_text = name_Boston.text
name_Brooklyn_text = name_Brooklyn.text
name_Charlotte_text = name_Charlotte.text
name_Chicago_text = name_Chicago.text
name_Cleveland_text = name_Cleveland.text
name_Dallas_text = name_Dallas.text
name_Denver_text = name_Denver.text
name_Detroit_text = name_Detroit.text
name_GoldenState_text = name_GoldenState.text
name_Houston_text = name_Houston.text
name_Indiana_text = name_Indiana.text
name_LA_Clippers_text = name_LA_Clippers.text
name_LA_Lakers_text = name_LA_Lakers.text
name_Memphis_text = name_Memphis.text
name_Miami_text = name_Miami.text
name_Milwaukee_text = name_Milwaukee.text
name_Minnesota_text = name_Minnesota.text
name_NewOrleans_text = name_NewOrleans.text
name_NewYork_text = name_NewYork.text
name_OklahomaCity_text = name_OklahomaCity.text
name_Orlando_text = name_Orlando.text
name_Philadelphia_text = name_Philadelphia.text
name_Phoenix_text = name_Phoenix.text
name_Portland_text = name_Portland.text
name_Sacramento_text = name_Sacramento.text
name_SanAntonio_text = name_SanAntonio.text
name_Toronto_text = name_Toronto.text
name_Utah_text = name_Utah.text
name_Washington_text = name_Washington.text


nba_teams = [name_Atlanta_text, name_Boston_text, name_Brooklyn_text, name_Charlotte_text, name_Chicago_text, name_Cleveland_text, name_Dallas_text, name_Denver_text, name_Detroit_text, name_GoldenState_text, name_Houston_text, name_Indiana_text,
name_LA_Clippers_text, name_LA_Lakers_text, name_Memphis_text, name_Miami_text, name_Milwaukee_text, name_Minnesota_text, name_NewOrleans_text, name_NewYork_text, name_OklahomaCity_text, name_Orlando_text, name_Philadelphia_text,
name_Phoenix_text, name_Portland_text, name_Sacramento_text, name_SanAntonio_text, name_Toronto_text, name_Utah_text, name_Washington_text]

soup.find_all('td', attrs = {'class' : 'center'})[0::4]
quarter_Numbers = soup.find_all


import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index1.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([nba_teams,quarter_Numbers, datetime.now()])




