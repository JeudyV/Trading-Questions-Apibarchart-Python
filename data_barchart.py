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
          'x-xsrf-token': 'eyJpdiI6Ik52dFl4N04rZTIvdzRCRFExNGUrdEE9PSIsInZhbHVlIjoiclphOG1CS0ZSTW91WHRiTnp0aUxiMjI2bnREUDkrbG1vUVpKVStxMjNMb0l6WGllWmUwRVBkL05jajJWdXUyMCIsIm1hYyI6IjAyM2U2MDQzMzUwMmI2ZWVhNjgyYzU4NzNlMTM5ODAxMGRiYzliMjBjZDY4ZTgyZDIzZTU4N2I0Yzc0M2JjYzgifQ==',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/ABT/options',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': '_gcl_au=1.1.1247577706.1584746654; _ga=GA1.2.705207734.1584746654; __gads=ID=2607ea29ff9d5f72:T=1584746656:S=ALNI_Mb52y6JNWa1MuAua3ZJHLV-n_S9CA; __qca=P0-315393063-1584746904143; fitracking_2=no; market=eyJpdiI6IkxxZ3h1OFA5ZGNpZFdRVGM1b0ZvL3c9PSIsInZhbHVlIjoialB6Ymkxc2wzWW9BbllVSG1SOUZHUT09IiwibWFjIjoiYzFlOGQyMmQ4NTJkYTM3MDhlMjUwNDJhOTY0YTRmNWVkYjg1YjU2MzYyMzNmZmEyOTgwMzQyODE5Yzg3M2VkMSJ9; _gid=GA1.2.1062799156.1585501882; fi_utm=direct%7Cdirect%7C%7C%7C%7C; _gat_UA-2009749-51=1; _awl=2.1585502067.0.4-7ba527c4-ddc2c7cb57b440fbb87b0ad327f35ca0-6763652d75732d6561737431-5e80d773-0; XSRF-TOKEN=eyJpdiI6Ik52dFl4N04rZTIvdzRCRFExNGUrdEE9PSIsInZhbHVlIjoiclphOG1CS0ZSTW91WHRiTnp0aUxiMjI2bnREUDkrbG1vUVpKVStxMjNMb0l6WGllWmUwRVBkL05jajJWdXUyMCIsIm1hYyI6IjAyM2U2MDQzMzUwMmI2ZWVhNjgyYzU4NzNlMTM5ODAxMGRiYzliMjBjZDY4ZTgyZDIzZTU4N2I0Yzc0M2JjYzgifQ%3D%3D; laravel_session=eyJpdiI6Im5FRFkzZ3hlQzFKKzZxL0cwOTFQMlE9PSIsInZhbHVlIjoieUpvQm5FSyt6dVFsMUcxcHI1U1M2bzU0THdWOGtmMUUxenpOeE1QT0JHSGE1RjBXcDc1SWxmNWtoUlkza0MwMiIsIm1hYyI6IjM2MzQzZTk4ZWE4NWE5ZWQwNzAyODUxYzc1YzEwMTllNTRlZTcyMGYyNThjYTljMzY5YmEzN2JlZWU0ZTE5MmEifQ%3D%3D; IC_ViewCounter_www.barchart.com=4',
          'Cookie': 'XSRF-TOKEN=eyJpdiI6IjU4Q3F4ekUvM1NTYjQ2dmJHSHFLbHc9PSIsInZhbHVlIjoiRDBzeExvazgyWWdMZ0wxQVlReUZyS0VNQTcxM1cwQytQZFZQcHM1N1Q5dURPYlViWDFkbFg3ZS9IdW83UE9rciIsIm1hYyI6ImNjNWU5OTZiMjQ2ZTVhZDUyODViYmNiMGZkZWNiYWNiYTdhYmVjM2Y0ODM3ODNlMTViNTk1NmNjZTIwNjg0YzYifQ%3D%3D; laravel_session=eyJpdiI6Ik1BVS84Vjhndzl0Q1A1NTFnTDk3clE9PSIsInZhbHVlIjoiVFFkeXJ3Qm54alhyWm8xdUhhRG9vVWlSd0FPMno1YlZWWWdiUldTcVJSRUdZMWFwazgrUmgveGZaYWk3Q05aRSIsIm1hYyI6IjhhOGNlZDQ3MTJiYjFmYzJkOGJjYTA0N2Y4NjM3MTVkNmY5OGI5NjIwYzVhMGE4NzEwMDk0NTNlOGViMjA2OTMifQ%3D%3D'
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




