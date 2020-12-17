from multiprocessing import Process
from Commodities import getCommodities
from cryptoCurrencies import GetCryptoCurrencies
from Currencies import getCurrencies
from mostActive import getMostActive
from worldIndices import getWorldIndices

def runInParallel(*fns):
  proc = []
  for fn in fns:
    
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

if __name__ == '__main__':
  runInParallel(getCommodities, GetCryptoCurrencies,getCurrencies,getMostActive,getWorldIndices)
