import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
names=[]
prices=[]
changes=[]
percentChanges=[]
dateTime=[]
 
CurrenciesURL = "https://in.finance.yahoo.com/currencies"
r= requests.get(CurrenciesURL)
data=r.text
soup=BeautifulSoup(data,"html.parser")
ct=datetime.datetime.now()
counter = 40
for i in range(40, 404, 14):
   for listing in soup.find_all('tr', attrs={'data-reactid':i}):
      for name in listing.find_all('td', attrs={'data-reactid':i+3}):
         names.append(name.text)
         dateTime.append(ct)
      for price in listing.find_all('td', attrs={'data-reactid':i+4}):
         prices.append(price.text)
      for change in listing.find_all('td', attrs={'data-reactid':i+5}):
         changes.append(change.text)
      for percentChange in listing.find_all('td', attrs={'data-reactid':i+7}):
         percentChanges.append(percentChange.text)
CurrenciesDF=pd.DataFrame({"Date Time":dateTime,"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
import os
from utils import *

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
path=data_path = os.path.join(FILE_DIR, "data/Currencies.csv")
main_df=open_csv(path)
if main_df is not None:
   result=merge_pf(main_df,CurrenciesDF)
   result.to_csv(path,index=False)
else:
   CurrenciesDF.to_csv(path,index=False)