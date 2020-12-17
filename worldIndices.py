import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os
from utils import *

def getWorldIndices():
   prices=[]
   names=[]
   changes=[]
   percentChanges=[]
   dateTime=[]
   WorldIndicesUrl = "https://in.finance.yahoo.com/world-indices"
   print('Getting WorldIndicesUrl')
   r= requests.get(WorldIndicesUrl)
   data=r.text
   soup=BeautifulSoup(data,"html.parser")
   ct=datetime.datetime.now() 
   counter = 40
   for _ in range(counter, 404, 14):
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

   print('Writing WorldIndices')
   FILE_DIR = os.path.dirname(os.path.abspath(__file__))
   path = os.path.join(FILE_DIR, "data/WorldIndices.csv")
   main_df=open_csv(path)

   if main_df is not None:
      result=merge_pf(main_df,WorldIndicesDF)
      result.to_csv(path,index=False)
   else:
      WorldIndicesDF.to_csv(path,index=False)
      
if __name__=='__main__':
   getWorldIndices()