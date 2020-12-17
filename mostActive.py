import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os
from utils import *

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
dateTime=[]
for i in range(0,11):
    MostActiveUrl = "https://in.finance.yahoo.com/most-active?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=100"
    r= requests.get(MostActiveUrl)
    data=r.text
    soup=BeautifulSoup(data,"html.parser")
    ct=datetime.datetime.now()
    for listing in soup.find_all('tr'):
        for name in listing.find_all('td', attrs={'aria-label':'Name'}):
            names.append(name.text)
            dateTime.append(ct)
        for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
            prices.append(price.find('span').text)
        for change in listing.find_all('td', attrs={'aria-label':'Change'}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
            percentChanges.append(percentChange.text)
        for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
            marketCaps.append(marketCap.text)
        for totalVolume in listing.find_all('td', attrs={'aria-label':'Avg vol (3-month)'}):
            totalVolumes.append(totalVolume.text)
        for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Volume'}):
            circulatingSupplys.append(circulatingSupply.text)
    
MostActiveDF=pd.DataFrame({"Date Time":dateTime,"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes,"Volume":circulatingSupplys})

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
path=data_path = os.path.join(FILE_DIR, "data/MostActive.csv")
main_df=open_csv(path)

if main_df is not None:
    result=merge_pf(main_df,MostActiveDF)
    result.to_csv(path,index=False)
else:
    MostActiveDF.to_csv(path,index=False)
    
