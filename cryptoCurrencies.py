import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os
from utils import *

def GetCryptoCurrencies():
  names=[]
  prices=[]
  changes=[]
  percentChanges=[]
  marketCaps=[]
  totalVolumes=[]
  circulatingSupplys=[]
  dateTime=[]

  for i in range(0,10):
    CryptoCurrenciesUrl = "https://in.finance.yahoo.com/cryptocurrencies?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=50"
    print('Getting CryptoCurrencies')
    r= requests.get(CryptoCurrenciesUrl)
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
      for totalVolume in listing.find_all('td', attrs={'aria-label':'Total volume all currencies (24 hrs)'}):
        totalVolumes.append(totalVolume.text)
      for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating supply'}):
        circulatingSupplys.append(circulatingSupply.text)

  CryptoCurrenciesDF=pd.DataFrame({"Date Time":dateTime,"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges,"Market Caps":marketCaps,"Total Volume":totalVolumes,"Circulating Supplys":circulatingSupplys})
  print('Writing CryptoCurrencies CSV')
  FILE_DIR = os.path.dirname(os.path.abspath(__file__))
  path = os.path.join(FILE_DIR, "data/CryptoCurrencies.csv")
  main_df=open_csv(path)
  if main_df is not None:
      result=merge_pf(main_df,CryptoCurrenciesDF)
      result.to_csv(path,index=False)
  else:
      CryptoCurrenciesDF.to_csv(path,index=False)

if __name__ == '__main__':
  GetCryptoCurrencies()