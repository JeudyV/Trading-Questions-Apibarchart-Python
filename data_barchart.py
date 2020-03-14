#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def generic_header(name_csv):
    Cov = pd.read_csv(name_csv)
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
    Frame.to_csv(name_csv, sep='\t')


# In[ ]:


def Hello():
    v = {"message": "Hello, World!"}
    return v


# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
import time

def allData_Call_And_Put_Company(nCompany):
    try:
        
        nCompany = nCompany["symbol"].upper()

        l = []
        l_ = {}

        url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1".format(nCompany)

        payload = {}
        headers = {
          'authority': 'www.barchart.com',
          'accept': 'application/json',
          'sec-fetch-dest': 'empty',
          'x-xsrf-token': 'eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0=',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/AAPL/options?moneyness=allRows',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': '_gcl_au=1.1.1010588658.1582606331; _ga=GA1.2.270392010.1582606332; __gads=ID=72d4fe83c6f1b46e:T=1582606336:S=ALNI_MbAIR-3cW-trYQ0awJLtlLrAI4_Jg; OX_plg=pm; fitracking_2=no; Limelight_HTML_Player_UserId=8254E40B-EDB8-4FEF-BEEB-16C1F441C68A; __qca=P0-247333977-1582910365824; market=eyJpdiI6InRZRnN3Z241RTNiVEpQMllnRCtiamc9PSIsInZhbHVlIjoiaFwvZzN2eEI4N2E1c0YwQlwvWFdRdWVRPT0iLCJtYWMiOiIxMmMyMmRlNWU3ZjJmMTk3OWI2N2I2NzA1Y2FjNzkzYzc0NGIxNzlmNjU1YjMzZTk5NGI3N2EyOGNlZjJkOWYyIn0%3D; _gid=GA1.2.414573225.1584147264; fi_utm=direct%7Cdirect%7C%7C%7C%7C; IC_ViewCounter_www.barchart.com=2; _awl=2.1584148483.0.4-687528a2-5451e6f2ba28d5b02db6c3572a2c5043-6763652d75732d6561737431-5e6c3003-0; XSRF-TOKEN=eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0%3D; laravel_session=eyJpdiI6Ik9uZDFsV1V3SFJcL0JxeWdXS2pqdFVnPT0iLCJ2YWx1ZSI6IkdjaHo2bG5XTXZQeVFSK1hcL3NXRE84c3M5bzlNdk05b1RYNVNCNGZ1VEZBUDRUck9NYzNVc2RvMkJmSUdYc0V3IiwibWFjIjoiMjJkYzhmYmFlY2U2MzJkNzU1MGYzNWM3M2U0ODQwZmQ5NDQ4ZjhkZjIzNTBlYjI2YzQ2ZjYyMmU3Mzc4OWQyOCJ9'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        #print(response.text.encode('utf8'))


        for k,v in json.loads(response.text).items():
            if k == 'data':
                for a,c in v.items():
                    for x in c:
                        del x['raw']
                        l.append(x)
                    df = pd.DataFrame(l)
                    df.to_csv('all_data1.csv', index=False, header=True, mode='a')
                    time.sleep(1)
        #generic_header('all_data.csv')
        for l_x in l:
            print(l_x)
            l_.setdefault("item",l_x)
        print(l_)
        print(type(l_))
        #json.dumps(l_)
            
        return json.loads(l_)
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#allData_Call_And_Put_Company()


# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
import time

def strike_Price_Call_And_Put_Company(nCompany):
    
    try:
    
        nCompany = nCompany["symbol"].upper()

        l = []
        l_strikePrice = []
        l_volatility = []

        url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1".format(nCompany)

        payload = {}
        headers = {
          'authority': 'www.barchart.com',
          'accept': 'application/json',
          'sec-fetch-dest': 'empty',
          'x-xsrf-token': 'eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0=',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/AAPL/options?moneyness=allRows',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': '_gcl_au=1.1.1010588658.1582606331; _ga=GA1.2.270392010.1582606332; __gads=ID=72d4fe83c6f1b46e:T=1582606336:S=ALNI_MbAIR-3cW-trYQ0awJLtlLrAI4_Jg; OX_plg=pm; fitracking_2=no; Limelight_HTML_Player_UserId=8254E40B-EDB8-4FEF-BEEB-16C1F441C68A; __qca=P0-247333977-1582910365824; market=eyJpdiI6InRZRnN3Z241RTNiVEpQMllnRCtiamc9PSIsInZhbHVlIjoiaFwvZzN2eEI4N2E1c0YwQlwvWFdRdWVRPT0iLCJtYWMiOiIxMmMyMmRlNWU3ZjJmMTk3OWI2N2I2NzA1Y2FjNzkzYzc0NGIxNzlmNjU1YjMzZTk5NGI3N2EyOGNlZjJkOWYyIn0%3D; _gid=GA1.2.414573225.1584147264; fi_utm=direct%7Cdirect%7C%7C%7C%7C; IC_ViewCounter_www.barchart.com=2; _awl=2.1584148483.0.4-687528a2-5451e6f2ba28d5b02db6c3572a2c5043-6763652d75732d6561737431-5e6c3003-0; XSRF-TOKEN=eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0%3D; laravel_session=eyJpdiI6Ik9uZDFsV1V3SFJcL0JxeWdXS2pqdFVnPT0iLCJ2YWx1ZSI6IkdjaHo2bG5XTXZQeVFSK1hcL3NXRE84c3M5bzlNdk05b1RYNVNCNGZ1VEZBUDRUck9NYzNVc2RvMkJmSUdYc0V3IiwibWFjIjoiMjJkYzhmYmFlY2U2MzJkNzU1MGYzNWM3M2U0ODQwZmQ5NDQ4ZjhkZjIzNTBlYjI2YzQ2ZjYyMmU3Mzc4OWQyOCJ9'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        #print(response.text.encode('utf8'))

        for k,v in json.loads(response.text).items():
            if k == 'data':
                for a,c in v.items():
                    for x in c:
                        del x['raw']
                        l.append(x)
                        for z,t in x.items():
                            if z == "strikePrice":
                                l_strikePrice.append(t)

                    df = pd.DataFrame(l_strikePrice)
                    df.to_csv('strikePrice_Money_question_4.csv', index=False, header=True, mode='a')
                
        return l_strikePrice
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#strike_Price_Call_And_Put_Company('FB')


# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
import time

def IV_Call_And_Put_Company(nCompany):
    
    try:
    
        nCompany = nCompany["symbol"].upper()

        l_volatility = []

        url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1".format(nCompany)

        payload = {}
        headers = {
          'authority': 'www.barchart.com',
          'accept': 'application/json',
          'sec-fetch-dest': 'empty',
          'x-xsrf-token': 'eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0=',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/AAPL/options?moneyness=allRows',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': '_gcl_au=1.1.1010588658.1582606331; _ga=GA1.2.270392010.1582606332; __gads=ID=72d4fe83c6f1b46e:T=1582606336:S=ALNI_MbAIR-3cW-trYQ0awJLtlLrAI4_Jg; OX_plg=pm; fitracking_2=no; Limelight_HTML_Player_UserId=8254E40B-EDB8-4FEF-BEEB-16C1F441C68A; __qca=P0-247333977-1582910365824; market=eyJpdiI6InRZRnN3Z241RTNiVEpQMllnRCtiamc9PSIsInZhbHVlIjoiaFwvZzN2eEI4N2E1c0YwQlwvWFdRdWVRPT0iLCJtYWMiOiIxMmMyMmRlNWU3ZjJmMTk3OWI2N2I2NzA1Y2FjNzkzYzc0NGIxNzlmNjU1YjMzZTk5NGI3N2EyOGNlZjJkOWYyIn0%3D; _gid=GA1.2.414573225.1584147264; fi_utm=direct%7Cdirect%7C%7C%7C%7C; IC_ViewCounter_www.barchart.com=2; _awl=2.1584148483.0.4-687528a2-5451e6f2ba28d5b02db6c3572a2c5043-6763652d75732d6561737431-5e6c3003-0; XSRF-TOKEN=eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0%3D; laravel_session=eyJpdiI6Ik9uZDFsV1V3SFJcL0JxeWdXS2pqdFVnPT0iLCJ2YWx1ZSI6IkdjaHo2bG5XTXZQeVFSK1hcL3NXRE84c3M5bzlNdk05b1RYNVNCNGZ1VEZBUDRUck9NYzNVc2RvMkJmSUdYc0V3IiwibWFjIjoiMjJkYzhmYmFlY2U2MzJkNzU1MGYzNWM3M2U0ODQwZmQ5NDQ4ZjhkZjIzNTBlYjI2YzQ2ZjYyMmU3Mzc4OWQyOCJ9'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        #print(response.text.encode('utf8'))


        for k,v in json.loads(response.text).items():
            if k == 'data':
                for a,c in v.items():
                    for x in c:
                        del x['raw']
                        for z,t in x.items():
                            if z == "strikePrice":  
                                if t == "200.00":
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
                    
#IV_Call_And_Put_Company('FB')


# In[ ]:


import requests
import json
import pandas as pd
import csv
import os.path
import time

def strikePrice_350_Call_And_Put_Company(nCompany):
    
    try:
    
        nCompany = nCompany["symbol"].upper()

        l_all = []

        url = "https://www.barchart.com/proxies/core-api/v1/options/get?symbol={}&fields=strikePrice%2ClastPrice%2CpercentFromLast%2CbidPrice%2Cmidpoint%2CaskPrice%2CpriceChange%2CpercentChange%2Cvolatility%2Cvolume%2CopenInterest%2CoptionType%2CdaysToExpiration%2CexpirationDate%2CtradeTime%2CsymbolCode%2CsymbolType&groupBy=optionType&expirationDate=nearest&meta=field.shortName%2Cexpirations%2Cfield.description&raw=1".format(nCompany)

        payload = {}
        headers = {
          'authority': 'www.barchart.com',
          'accept': 'application/json',
          'sec-fetch-dest': 'empty',
          'x-xsrf-token': 'eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0=',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
          'dnt': '1',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-mode': 'cors',
          'referer': 'https://www.barchart.com/stocks/quotes/AAPL/options?moneyness=allRows',
          'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
          'cookie': '_gcl_au=1.1.1010588658.1582606331; _ga=GA1.2.270392010.1582606332; __gads=ID=72d4fe83c6f1b46e:T=1582606336:S=ALNI_MbAIR-3cW-trYQ0awJLtlLrAI4_Jg; OX_plg=pm; fitracking_2=no; Limelight_HTML_Player_UserId=8254E40B-EDB8-4FEF-BEEB-16C1F441C68A; __qca=P0-247333977-1582910365824; market=eyJpdiI6InRZRnN3Z241RTNiVEpQMllnRCtiamc9PSIsInZhbHVlIjoiaFwvZzN2eEI4N2E1c0YwQlwvWFdRdWVRPT0iLCJtYWMiOiIxMmMyMmRlNWU3ZjJmMTk3OWI2N2I2NzA1Y2FjNzkzYzc0NGIxNzlmNjU1YjMzZTk5NGI3N2EyOGNlZjJkOWYyIn0%3D; _gid=GA1.2.414573225.1584147264; fi_utm=direct%7Cdirect%7C%7C%7C%7C; IC_ViewCounter_www.barchart.com=2; _awl=2.1584148483.0.4-687528a2-5451e6f2ba28d5b02db6c3572a2c5043-6763652d75732d6561737431-5e6c3003-0; XSRF-TOKEN=eyJpdiI6InlFRHBXSlh5c0xwamFnaXhES1wvQ053PT0iLCJ2YWx1ZSI6Ik5zOVpPT0gwb1dHMTBDZFdNOTNESG1WSUFqbkJpTW1FMmVVOGVteURnSWltNnNhSjNmcFFZZVluVSthaTRCYVUiLCJtYWMiOiIzNjYyNWRlZGIxYjExYzQ0OWExODc0YWVmNjQ0MThmNzMzY2NjYmQ4YjBiOWNiMGNmYTNmYjEyOThlODk5OGNlIn0%3D; laravel_session=eyJpdiI6Ik9uZDFsV1V3SFJcL0JxeWdXS2pqdFVnPT0iLCJ2YWx1ZSI6IkdjaHo2bG5XTXZQeVFSK1hcL3NXRE84c3M5bzlNdk05b1RYNVNCNGZ1VEZBUDRUck9NYzNVc2RvMkJmSUdYc0V3IiwibWFjIjoiMjJkYzhmYmFlY2U2MzJkNzU1MGYzNWM3M2U0ODQwZmQ5NDQ4ZjhkZjIzNTBlYjI2YzQ2ZjYyMmU3Mzc4OWQyOCJ9'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        #print(response.text.encode('utf8'))


        for k,v in json.loads(response.text).items():
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
        #generic_header('all_data_strikePrice_350_question_1.csv')
    
        return l_all
    except Exception as error:
        print({"result":False, "message":"Something went wrong, error details: {}".format(error)})
        return False
                    
#strikePrice_350_Call_And_Put_Company('FB')


# In[ ]:




