import json
import requests
import time
import urllib
import re
import woo


TOKEN = open('config').read().rstrip()
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
data = woo.get_data()
print "Data loaded"


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.pathname2url(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            response = respond(text)
            send_message(response, chat)
        except Exception as e:
            print(e)

def respond(text):
    artists_in_message = []
    # print len(data.keys())
    for artist in data.keys():
        regex = r'\b(' + artist + r')\b|\A('+artist+r'\b)'
        if re.search(regex, text, re.I):
            artists_in_message.append(artist)
    if len(artists_in_message) > 1:
        print "triggered multiple artists: {}".format(artists_in_message)
        regex_res = re.search(r'(\d+)', text, re.I)
        if regex_res is not None:
            return woo.get_mashup(artists_in_message, regex_res.group(0), data)
        return woo.get_mashup(artists_in_message, data)
    if len(artists_in_message) == 1:
        print "triggered single artist: {}".format(artists_in_message)
        regex_res = re.search(r'(\d+)', text, re.I)
        if regex_res is not None:
            return woo.get_lyric(artists_in_message[0], regex_res.group(0), data)
        return woo.get_lyric(artists_in_message[0], data)
    if re.search(r'\Ahey', text, re.I):
        return "Hey! I'm the LyrifyBot and I can help you get lyrics inspired by specific artists."
    if len(artists_in_message) == 0:
        return "No artist found in message. Please send a new one!"


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
    # print respond("hey botje")
