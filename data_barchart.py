#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
import time


# In[ ]:


def get_all_data_barchart():
    try:
        
        #nCompany = nCompany["symbol"].upper()

        l = []

        url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol=AAPL&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1"

        payload = {}
        headers = {
          'authority': 'www.barchart.com',
          'accept': 'application/json',
          'sec-fetch-dest': 'empty',
          'x-xsrf-token': 'eyJpdiI6ImRlcnJET3Z1R2dCUlJoZlZHU2EyT2c9PSIsInZhbHVlIjoieVpxZ2s3ZEE4ZE85TmlJMkpQdkZqWTRnckM5OTlRUmR4MFFOY25kVlwveHphaVROTitSWlpveTZYY24zTVNhSlEiLCJtYWMiOiJmZTM5NDJjMDBiODAwNmYwYzZkOGQ4MWNlNGVhYjk5NjdjNGE2OGE3ZWJhZjg2ZGFjODkxNGUyOGJmMDUyMTk0In0=',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/AAPL/options?moneyness=allRows',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': 'XSRF-TOKEN=eyJpdiI6ImRlcnJET3Z1R2dCUlJoZlZHU2EyT2c9PSIsInZhbHVlIjoieVpxZ2s3ZEE4ZE85TmlJMkpQdkZqWTRnckM5OTlRUmR4MFFOY25kVlwveHphaVROTitSWlpveTZYY24zTVNhSlEiLCJtYWMiOiJmZTM5NDJjMDBiODAwNmYwYzZkOGQ4MWNlNGVhYjk5NjdjNGE2OGE3ZWJhZjg2ZGFjODkxNGUyOGJmMDUyMTk0In0%3D; laravel_session=eyJpdiI6IjVVcW5EU0NSdVlnemNHNndMc3grNXc9PSIsInZhbHVlIjoiWUtNMm91WDVFV1wvM3BQc1RSSUF3YXoxRFlESzEwaTlkSTZjY29RWTE5dmJQeDFjUENcL3RaOXZlVngrNjVpWGtYIiwibWFjIjoiYjIwNmYxNWM4OGZjZDYyMmMzMzQyMjljOTc1MTQyNzM2NzZhNWJhMDA2MmQ5YzUzNDRjNzA5MmJmOWJkMjU3MiJ9; market=eyJpdiI6IllhM24rRXo0MDh3UUoyR3lBOVlPXC9BPT0iLCJ2YWx1ZSI6IjBJUjloWDNHTG82UktsaWNOdThYNFE9PSIsIm1hYyI6IjAxMTQwOTZhNjdhZTU2ZGVlZWMwZTZlOTkyZjY1ZDFkZjA4NThmYTRiZWJiYWQyZmY1ZDVjNjEwMTcwZjM5YzIifQ%3D%3D; IC_ViewCounter_www.barchart.com=1; _gcl_au=1.1.1247577706.1584746654; _ga=GA1.2.705207734.1584746654; _gid=GA1.2.1169490786.1584746654; _gat_UA-2009749-51=1; __gads=ID=2607ea29ff9d5f72:T=1584746656:S=ALNI_Mb52y6JNWa1MuAua3ZJHLV-n_S9CA'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        response = json.loads(response.text)
        
        return response
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#get_all_data_barchart()


# In[ ]:


def get_Call_And_Put():
    try:
        
        #nCompany = nCompany["symbol"].upper()

        l = []
        
        response = get_all_data_barchart()
        
        df = pd.DataFrame(response["data"])
        
        list_Call = df.apply(lambda x: [x.get("Call").get("strikePrice"), x.get("Put").get("strikePrice")], axis=1, result_type="expand")
        list_Put = df.apply(lambda x: x.get("Put").get("strikePrice"), axis=1, result_type="expand")
        
        json_strikePrice = {
            "list_Call": list_Call,
            "list_Pat": list_Put
        }
        
        return list_Call
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#get_Call_And_Put()


# In[ ]:


def get_volatility():
    
    try:
    
        #nCompany = nCompany["symbol"].upper()

        l_volatility = []

        l = []
        
        response = get_all_data_barchart()
        
        print(response)
        print(type(response))

        for k,v in response.items():
            if k == 'data':
                for a,c in v.items():
                    for x in c:
                        del x['raw']
                        for z,t in x.items():
                            if z == "strikePrice":  
                                if t == "215.00":
                                    for x1,x2 in x.items():
                                        if x1 == "volatility":
                                            print(x1, x2)
                                            l_volatility.append(x2)


                df = pd.DataFrame(l_volatility)
                df.to_csv('volatility_question_3.csv', index=False, header=True, mode='a')
        
        return l_volatility
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#get_volatility()


# In[ ]:


def get_strikePrice():
    
    try:
    
        #nCompany = nCompany["symbol"].upper()

        l_all = []

        l = []
        
        response = get_all_data_barchart()

        for k,v in response.items():
            if k == 'data':
                for a,c in v.items():
                    for x in c:
                        del x['raw']
                        for z,t in x.items():
                            if z == "strikePrice":  
                                if t == "350.00":
                                    l_all.append(x)

                    df = pd.DataFrame(l_all)
                    df.to_csv('all_data_strikePrice_350_question_1.csv', index=False, header=True, mode='a')
        
        print(l_all)
    
        return l_all
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
get_strikePrice()


# In[ ]:




