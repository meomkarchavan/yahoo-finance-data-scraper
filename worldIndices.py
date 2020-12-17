import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime

prices=[]
names=[]
changes=[]
percentChanges=[]
dateTime=[]
WorldIndicesUrl = "https://in.finance.yahoo.com/world-indices"
r= requests.get(WorldIndicesUrl)
data=r.text
soup=BeautifulSoup(data)
ct=datetime.datetime.now() 
counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
            dateTime.append(ct)
         for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for change in srow.find_all('td', attrs={'class':'data-col3'}):
            changes.append(change.text)
         for percentChange in srow.find_all('td', attrs={'class':'data-col4'}):
            percentChanges.append(percentChange.text)
 
WorldIndicesDF=pd.DataFrame({"Date Time":dateTime,"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
