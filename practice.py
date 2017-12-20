import grequests
import urllib
import json
import time
import requests


TOKEN="504394990:AAHhQw6BBO_i7pVmIc2duXxIqFhUNADUh-o"
URL="https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    request=grequests.get(url)
    content=grequests.map([request])
    content=content[0].text
    return content

def get_json_from_url(url):
    content = get_url(url)
    js =json.loads(content)
    return js

def get_updates():
    url=URL+"getUpdates"
    js=get_json_from_url(url)
    return js

def get_last_info(updates):
    num_updates=len(updates["result"])
    last_update=num_updates-1
    text=updates["result"][last_update]["message"]["text"]
    chat_id=updates["result"][last_update]["message"]["chat"]["id"]
    message_id=updates["result"][last_update]["message"]["message_id"]
    return text, chat_id,message_id

def send_message(text,chat_id):
    ##print (translate("test")[3][0])
    #text
    url=URL+"sendMessage?text={}&chat_id={}&parse_mode=markdown".format(text, chat_id)
    get_url(url)

if __name__=='__main__':
    last_message_id=""
    print ("The Chatbot is running")
    while(True):
        text, chat_id, message_id=get_last_info(get_updates())
        intent=NLP(text)
        sendMesage(intent)
        if(last_message_id!=message_id):
            send_message(text,chat_id)
            last_message_id=message_id
            time.sleep(0.05)
