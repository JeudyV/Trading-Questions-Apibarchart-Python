#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import pandas as pd
import csv
import os.path
import seaborn as sb
import time

def get_data_barchart():
    
    l = []

    url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol=ABT&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1"

    payload = {}
    headers = {
      'authority': 'www.barchart.com',
      'accept': 'application/json',
      'sec-fetch-dest': 'empty',
      'x-xsrf-token': 'eyJpdiI6IkJFOFdzdFRZc2dmM1JtQVRcL1wvejV0Zz09IiwidmFsdWUiOiJjb1ZFMXNSTlwvU0ZpdWkzSlJzTGRQdnhqRjNDRzM5QlIwU1R1Yno3KzhjeTUzamNOTEx6TTVKXC9Na2pQOEJjczgiLCJtYWMiOiIyNjEyNzc2OTlhNTBmY2Y2MjhhNjNlNzI1YjkzMjE1YjI2ZTJhNzM0NDgzNTJmMGNiODc0MDUyNmI4NTRlNTliIn0=',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'referer': 'https://www.barchart.com/stocks/quotes/ABT/options',
      'accept-language': 'es-ES,es;q=0.9',
      'cookie': '_gcl_au=1.1.1787344868.1583041852; _ga=GA1.2.1991709918.1583041852; _gid=GA1.2.190165632.1583041852; kppid_managed=NQZgClZ4; __qca=P0-1258427446-1583041909777; fitracking_2=yes; fiTrackingDomainParams=%7B%22host%22%3A%22tracking1.firstimpression.io%22%2C%22type%22%3A%22full%22%7D; fi_utm=direct%7Cdirect%7C%7C%7C%7C; _pk_ses.6495.73a4=*; market=eyJpdiI6ImFydU95cm9tRTZ0dktQMTUwS1ZsbGc9PSIsInZhbHVlIjoiRzdCTVFZZFpwUHIwRGZRRDljTWsyUT09IiwibWFjIjoiMDRjNTlmNmUxYzE5YzdlOGRhYjIwYzFkMGRhNmIyMzllZjA4Nzc4ZjU0MTM3ZGM3ZTI0MjliMzZmOWMwM2I0NSJ9; __gads=ID=66b238a2004c784b:T=1583042342:S=ALNI_MYbGFh__uyVPtEvnrAJUsiZzTU6eg; _awl=2.1583042589.0.4-56aacb99-fd46bb27a73be53df9c9e2a091c4880b-6763652d75732d6561737431-5e5b501d-0; XSRF-TOKEN=eyJpdiI6IkJFOFdzdFRZc2dmM1JtQVRcL1wvejV0Zz09IiwidmFsdWUiOiJjb1ZFMXNSTlwvU0ZpdWkzSlJzTGRQdnhqRjNDRzM5QlIwU1R1Yno3KzhjeTUzamNOTEx6TTVKXC9Na2pQOEJjczgiLCJtYWMiOiIyNjEyNzc2OTlhNTBmY2Y2MjhhNjNlNzI1YjkzMjE1YjI2ZTJhNzM0NDgzNTJmMGNiODc0MDUyNmI4NTRlNTliIn0%3D; laravel_session=eyJpdiI6ImUzeVQzb3FrUFJTTzRKNlNvYUVCTVE9PSIsInZhbHVlIjoiYWVkSDBscVRNMHFxQUVGcW5mbWZGSjA2OVMxeGJncGszRzFMXC9rMDlVQU9vM0E4cTJhcFpqc0lCRktVK0p4WUYiLCJtYWMiOiI0MDQ2MmZiMzQwM2E5NmMxOWI3ZWZhZWNkZmU4MTg3M2ExYTEzMmEzMTMzNDkxN2Y1MGM1YjBkZjdmYTViYjU0In0%3D; _pk_id.6495.73a4=40d154cea06bdafb.1583041911.1.1583042688.1583041911.; _gat_UA-2009749-51=1; IC_ViewCounter_www.barchart.com=6'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    
    for k,v in json.loads(response.text).items():
        if k == 'data':
            print(type(v))
            for a,c in v.items():
                print(a)
                for x in c:
                    print(type(x))
                    print(x)
                    del x['raw']
                    l.append(x)
                df = pd.DataFrame(l)
                df.to_csv('barchart_data_stocks_quotes.csv', index=False, header=False, mode='a')
                time.sleep(1)
    
                
        
        
#         for x in json_data:
#             print(type(x))
#             del x['link']
#             del x['requestAQuoteLink']
#             del x['makeAnEnquiryLink']
#             del x['thumbLink']
#             del x['recommendationTrackLink']
#             l.append(x)
#     print(l)
#     df = pd.DataFrame(l)
#     df.to_csv('nombre8.csv', index=False, header=False, mode='a')
                    
#get_data_barchart()


# In[6]:


# dp = pd.read_csv('barchart_data_stocks_quotes.csv')
# dp.columns = ["strikePrice"
#             ,"lastPrice"
#             ,"percentFromLast"
#             ,"bidPrice"
#             ,"midpoint"
#             ,"askPrice"
#             ,"priceChange"
#             ,"percentChange"
#             ,"volatility"
#             ,"volume"
#             ,"openInterest"
#             ,"optionType"
#             ,"daysToExpiration"
#             ,"expirationDate"
#             ,"tradeTime"
#             ,"symbolType"]
# dp.to_csv('barchart_data_stocks_quotes2.csv', index=False, header=False, mode='a')
# my_CSV_File= pd.read_csv("barchart_data_stocks_quotes2.csv")
# print(my_CSV_File)

Cov = pd.read_csv("barchart_data_stocks_quotes.csv")
Frame=pd.DataFrame(Cov.values, columns = ["strikePrice"
            ,"lastPrice"
            ,"percentFromLast"
            ,"bidPrice"
            ,"midpoint"
            ,"askPrice"
            ,"priceChange"
            ,"percentChange"
            ,"volatility"
            ,"volume"
            ,"openInterest"
            ,"optionType"
            ,"daysToExpiration"
            ,"expirationDate"
            ,"tradeTime"
            ,"symbolType"])
Frame.to_csv("barchart_data_stocks_quotes3.csv", sep='\t')


# In[ ]:




