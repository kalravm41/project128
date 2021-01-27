# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time,csv

# start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
# browser = webdriver.Chrome('/Users/kalravmineshbhatt/Dropbox/My Mac (Jack’s MacBook Air)/Downloads/chromedriver')
# browser.get(start_url)

# time.sleep(10)

# def Scrape():
#     headers = ['NAME','Distance','Mass','Radius']
#     PlanetData = []
#     Soup = BeautifulSoup(browser.page_source, 'html.parser')

#     tables = Soup.find("table", attrs={'class',"wikitable sortable jquery-tablesorter"})
#     # print(tables)

#     tableData = tables.find('tbody')

#     for tr_tag in tableData.find_all('tr'):
#         temp_list = []

#         td_tag = tr_tag.find('td')
#         # print(td_tag)

# #     # browser.find_element_by_xpath('//*[@id="bodyContent"]/footer/div/div/div/nav/span[2]/a').click()

#         for index,td_tag in enumerate(td_tag):

#             if index == 0:

#                 # temp_list.append(td_tag.find_all('a')[0].contents[0])

#     #         else:
#     #             try:
#     #                 temp_list.append(td_tag.contents[0])

#     #             except:
#     #                 temp_list.append('')
#     #     PlanetData.append(temp_list)  

#     # with open('scraper.csv','w') as f:
#     #     csvWriter = csv.writer(f)
#     #     csvWriter.writerow(headers)
#     #     csvWriter.writerows(PlanetData)                

# Scrape()

import requests
from bs4 import BeautifulSoup
import csv

res = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")                                                  
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find("table",class_="wikitable")
headers = ['NAME','Distance','Mass','Radius']
data = []

for items in table.find_all("tr")[:-1]:
    data.append(list(' '.join(item.text.split()) for item in items.find_all(['th','td'])))

name = []
distance = []
mass = []
radius = []
finalData = []
for i in range(1,96):
    name.append(data[i][1])

for i in range(1,96):
    distance.append(data[i][3])    

for i in range(1,96):
    mass.append(data[i][5])

for i in range(1,96):
    radius.append(data[i][6])

for i in range(95):   
    finalData.append([name[i],distance[i],mass[i],radius[i]])   


with open('DwarfPlanetData.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(finalData)    