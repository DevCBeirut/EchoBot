import json
import urllib
import grequests
import time


TOKEN = "444874958:AAGjLuhNCjvZGJkNnwCCP5c4cffIMy_vkNA"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    #Asynchronous call for the URL
    request = grequests.get(url)
    content = grequests.map([request])
    content = content[0].text
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

##with offset added a default value just in case
def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    message_id=updates["result"][last_update]["message"]["message_id"]
    return (text, chat_id, message_id)



def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=markdown".format(text, chat_id)
    get_url(url)



if __name__ == '__main__':
    last_message_id=""
    print ("The Chatbot is Running. Press Enter to Exit")
    while(True):
        text, chat, message_id = get_last_chat_id_and_text(get_updates())
        if (last_message_id!=message_id):
            send_message( text, chat)
        last_message_id=message_id
        ## Let it wait 50 ms before doing the next loop
        time.sleep(0.05)
    print ("Chat Bot has terminated")
