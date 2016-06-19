#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import random
import datetime
import requests
from qrmaker import QR_Maker
import json


PRODUCTS = ["Raspberry Pi", "kolle-mate", "Bildschirm", "Tofu",
            "Banane", "Apfel", "Backfisch", "Handy", "mio mio Mate", "Nudeln"]
IP = "tmp.pajowu.de"
BACKEND_POST_URL = "http://tmp.pajowu.de/backend/index.php/qrbon/speichern/"


def send_random_test_bon():
    bon = {}
    bon["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bon["store"] = "Jugend hackt Techmarkt, ​TU Informationsfakultät,"\
                   "Nöthnitzer Straße 46, 01187 Dresden"
    bon["items"] = []
    random.shuffle(PRODUCTS)
    rand_list = PRODUCTS[:random.randint(1,6)]
    rand_list.append("Show-Alpaka")
    for i in rand_list:
        bon["items"].append({"name": i,
                             "price": random.randrange(0, 1000),
                             "amount": random.randint(0, 100),
                             "ean": str(random.randint(0, 9999999999999)).ljust(13, "0"),
                             "tax": random.randint(1, 25)})
    post_data = {"json":json.dumps(bon)}
    save_bon_request = requests.post(BACKEND_POST_URL, data=post_data)
    #print(save_bon_request.request.body)
    print(save_bon_request.text)
    #import pdb;pdb.set_trace()
    return save_bon_request.text


def generate_bon():
    bon_id = send_random_test_bon()
    bon_url = "http://{}/frontend/#!/bon/{}".format(IP, bon_id)
    qrmaker = QR_Maker(bon_url, pattern=14)
    qrmaker.run()


if __name__ == "__main__":
    generate_bon()
