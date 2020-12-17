import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
dateTime=[]
prices=[]
names=[]
changes=[]
percentChanges=[]
marketTimes=[]
totalVolumes=[]
openInterests=[]

CommoditiesUrl = "https://in.finance.yahoo.com/commodities"
r= requests.get(CommoditiesUrl)
data=r.text
soup=BeautifulSoup(data)
ct = datetime.datetime.now() 
counter = 40
for i in range(40, 404, 14):
   for row in soup.find_all('tbody'):
      for srow in row.find_all('tr'):
         for name in srow.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
            dateTime.append(ct)
         for price in srow.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text)
         for time in srow.find_all('td', attrs={'class':'data-col3'}):
            marketTimes.append(time.text)
         for change in srow.find_all('td', attrs={'class':'data-col4'}):
            changes.append(change.text)
         for percentChange in srow.find_all('td', attrs={'class':'data-col5'}):
            percentChanges.append(percentChange.text)
         for volume in srow.find_all('td', attrs={'class':'data-col6'}):
            totalVolumes.append(volume.text)
         for openInterest in srow.find_all('td', attrs={'class':'data-col7'}):
            openInterests.append(openInterest.text)
         
 
CommoditiesDF=pd.DataFrame({"Date Time":dateTime,"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Time": marketTimes,'Open Interest': openInterests ,"Volume": totalVolumes})

