import random
import datetime
import requests
from qrmaker import QR_Maker


PRODUCTS = ["Raspberry Pi", "Show-Alpaka", "kolle-mate", "Bildschirm", "Tofu",
            "Banane", "Apfel", "Backfisch", "Handy", "mio mio Mate", "Nudeln"]
IP = "141.76.106.237"
BACKEND_POST_URL = "http://localhost:8080"


def send_random_test_bon():
    bon = {}
    bon["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bon["store"] = "Jugend hackt Techmarkt, ​TU Informationsfakultät,"\
                   "Nöthnitzer Straße 46, 01187 Dresden"
    bon["items"] = []
    for i in range(random.randint(0, len(PRODUCTS))):
        bon["items"].append({"name": random.choice(PRODUCTS),
                             "price": random.randrange(0, 1000),
                             "amount": random.randint(0, 100),
                             "ean": str(random.randint(0, 9999999999999)).ljust(13, "0"),
                             "tax": random.randint(1, 25)})
    save_bon_request = requests.post(BACKEND_POST_URL, json=bon)
    return save_bon_request.json()


def generate_bon():
    bon_id = send_random_test_bon()["id"]
    bon_url = "http://{}/#!/bon/{}".format(IP, bon_id)
    qrmaker = QR_Maker(bon_url, pattern=15)
    qrmaker.run()


if __name__ == "__main__":
    generate_bon()
