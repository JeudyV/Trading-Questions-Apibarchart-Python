#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import json
import time
from telethon.tl.types import PeerChat

import mysql.connector
from mysql.connector import Error

import traceback
import os

import re

token = os.getenv('TOKEN_TELEGRAM', '974187013:AAEj2ppqBQySTwdOGIt7EaVaRFGQ7v_KELc')
url_server = os.getenv('SERVER_URL', 'http://127.0.0.1:5000')

#token = '1078478278:AAHLLs2LJpTFBt19ppcb0_I9kfANo3cb5gA'
url = 'https://api.telegram.org/bot{}/'.format(token)

def get_updates(offset=None):
    time.sleep(1)
    try:
        URL = url + 'getUpdates'
        if offset:
            URL += '?offset={}'.format(offset)
        res = requests.get(URL)
        print("Getting: {} elements".format(len(json.loads(res.text)["result"])))
        
        if len(json.loads(res.text)["result"]) == 0:
            
            get_updates()
        
        return res.json()

    except:
        pass


def get_last(data):
    results = data['result']
    count = len(results)
    if count == 0:
        return None
    last = count - 1
    last_update = results[last]
    return last_update


def get_last_id_text(updates):
    last_update = get_last(updates)
    if last_update is None:
        return None, None, None
    chat_id = last_update['message']['chat']['id']
    update_id = last_update['update_id']
    try:
        text = last_update['message']['text']
    except:
        text = ''
    return chat_id, text, update_id


def get_last_date_text():
    last_msg_time = 0
    text = ""
    json_test = get_updates()
    for key, value in json_test.items():
        if key == "result":
            for x in value:
                for key2, value2 in x.items():
                    if key2 == "message":
                        for key3, value3 in value2.items():
                            if key3 == "date":
                                last_msg_time = value3
                            if key3 == "text":
                                text = value3
    return last_msg_time, text


def reply_markup_maker(data):
    keyboard = []
    for i in range(0, len(data), 2):
        key = []
        key.append(data[i].title())
        try:
            key.append(data[i + 1].title())
        except:
            pass
        keyboard.append(key)

    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)



def send_message(chat_id, text, reply_markup=None):
    print(chat_id)
    URL = url + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        URL += '&reply_markup={}'.format(reply_markup)
    res = requests.get(URL)
    while res.status_code != 200:
        res = requests.get(URL)
    print(res.status_code)


def start(chat_id):
    message = 'Do you want to start?'
    reply_markup = reply_markup_maker(['Start'])
    send_message(chat_id, message, reply_markup)

    chat_id, text, update_id = get_last_id_text(get_updates())
    while (text.lower() != 'start'):
        time.sleep(1)
        chat_id, text, update_id = get_last_id_text(get_updates(update_id))

    return chat_id, text, update_id


def welcome_note(chat_id, commands):
    text = "Welcome to Test Bot"
    send_message(chat_id, text)
    text = 'Select an Option'
    reply_markup = reply_markup_maker(commands)
    send_message(chat_id, text, reply_markup)


def end(chat_id, text, update_id):
    message = 'Do you want to end?'
    reply_markup = reply_markup_maker(['Yes', 'No'])
    send_message(chat_id, message, reply_markup)

    new_text = text
    while (text == new_text):
        time.sleep(1)
        chat_id, new_text, update_id = get_last_id_text(get_updates(update_id))

    if new_text == 'Yes':
        return 'y'
    else:
        return 'n'
    
def test(chat_id, update_id):
    
    #-------------------------------------------
    
    try:
        plistas = []
        
        from data_barchart import get_Call_And_Put
        
        get_list_response = get_Call_And_Put()
            
        send_message(chat_id, get_list_response)                        
        
    except Exception as error:
        print(error)
        traceback.print_exc()
    
    print("entro")
    
    #-------------------------------------------
    
def test_(chat_id, update_id):
    
    #-------------------------------------------
    
    try:
        plistas = []
        
        from data_barchart import get_volatility
        
        get_list_response = get_volatility()
        
        send_message(chat_id, get_list_response)                        
        
    except Exception as error:
        print(error)
        traceback.print_exc()
    
    print("entro")
    
    #-------------------------------------------
    
def _test_(chat_id, update_id):
    
    #-------------------------------------------
    
    try:
        plistas = []
        
        from data_barchart import get_strikePrice
        
        get_list_response = get_strikePrice()
        
        send_message(chat_id, get_list_response)                        
        
    except Exception as error:
        print(error)
        traceback.print_exc()
    
    print("entro")
    
    #-------------------------------------------
        
def menu(chat_id, text, update_id):
    commands = ["Money Strike Price", "What Is The Iv", "What Is The Strike Price"]
    welcome_note(chat_id, commands)

    while text.lower() == 'start':
        time.sleep(1)
        chat_id, text, update_id = get_last_id_text(get_updates(update_id))
        print("waiting")
    print(text)
    while text not in commands:
        time.sleep(1)
        chat_id, text, update_id = get_last_id_text(get_updates(update_id))
        print("waiting 2")

    if text == "Money Strike Price":
        test(chat_id, update_id)
    elif text == "What Is The Iv":
        test_(chat_id, update_id)
    elif text == "What Is The Strike Price":
        _test_(chat_id, update_id)
        
    text = 'start' 
                

def main():
    try:
        text = ''
        print('Started step 1.0')
        chat_id, text, update_id = get_last_id_text(get_updates())
        print("Update ID: {}".format(update_id))
        chat_id, text, update_id = start(chat_id)
        print('Started step 1.2')
        
#         if text is None:
            
#             print("main 1")
#             main()

#         while text.lower() != 'y':
#             print("while main 2")
#             time.sleep(1)
#             text = 'start'
#             menu(chat_id, text, update_id)
#             text = 'y'
#             chat_id, text, update_id = get_last_id_text(get_updates())

        menu(chat_id, text, update_id)
        
        print("main 2")
        main()

                
    except Error as e:
        
        print("Error: ", e)


main()

