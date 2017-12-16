import json
import requests
import urllib
import grequests

TOKEN = "444874958:AAGjLuhNCjvZGJkNnwCCP5c4cffIMy_vkNA"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    request = grequests.get(url)
    content = grequests.map([request])
    content = content[0].text
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

##with offset added a default value just in case
def get_updates(offset="41718998"):
    url = URL + "getUpdates"+"?&offset="+str(offset)
    js = get_json_from_url(url)
    return js


##function to reduce the number of messages received to the last 10 to 5 messages
##Change 5 and 10 to how you would like them accordingly
def get_latest_messages(offset="41718998"):
    update_json=get_updates(offset)
    number_of_messages=len(update_json["result"])
    #to test replace 50
    while (number_of_messages>10):
        offset=update_json["result"][number_of_messages-5]["update_id"]
        update_json=get_updates(offset)
        number_of_messages=len(update_json["result"])
    return offset ,number_of_messages

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
    print ("The Chatbot Terminated")
    while(True):
        text, chat, message_id = get_last_chat_id_and_text(get_updates())
        if (last_message_id!=message_id):
            send_message( text, chat)
        last_message_id=message_id
