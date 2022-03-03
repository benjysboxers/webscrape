'''
Retrieve unstructured data from a website and
have it stored in a structured format
send a request to the server and the data is contained in the response you get.
What you then do is parse the response data and extract out the parts you want.

think about website content structure
'''

'''
steps for scraping
1. inspection of website HTML you want to crawl
2. Access website url with code and download all html contents on the page
3. Format downloaded content to a readable format
4. Extract the useful information and save to structured format
5. for info displayed on multiple pages of website you may need to repeat step 2-4 to accquire complete info
'''

import requests
from bs4 import BeautifulSoup
import csv

#make a request to the http site
web_page = requests.get('https://www.worldometers.info/coronavirus/#countries')
#parsing data in html format
soup = BeautifulSoup(web_page.content, 'html.parser')

#empty array to store all links
data_populate = []

#accepts css selectors, this will allow us to locate elements by class attribute name
data = soup.select('div.thumbnail')

#getting data from spans
for i in data:
    data = i.find('span')
    data_populate.append(data.string)

#display # of cases
print(data_populate)




