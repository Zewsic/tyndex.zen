import json
import urllib

import requests
from random import randint


def balaboba(text=str(randint(1, 4999999)), style=randint(0, 12), count=1):
    for i in range(count):
        try:
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                              '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
                'Origin': 'https://yandex.ru',
                'Referer': 'https://yandex.ru/',
            }

            API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
            payload = {"query": text, "intro": int(style)}
            params = json.dumps(payload).encode('utf8')
            req = urllib.request.Request(API_URL, data=params, headers=headers)
            response = urllib.request.urlopen(req)

            balabob = eval(response.read().decode('unicode_escape').replace("\n", "!_!"))
            text = (balabob["query"] + " " + balabob["text"]).replace("!_!", "\n")
        except:
            pass
    return text