import time
import json
import requests

url = "https://api.waitwell.ca/api/035301/client/locationstatus?Queue_id=1"

headers = {
    "Host": "api.waitwell.ca",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "X-AppName": "Client 2.19.0",
    "X-AppToken": "1715103664115683",
    "Content-Type": "application/json",
    "Origin": "https://35301.waitwell.ca",
    "Connection": "keep-alive",
    "Referer": "https://35301.waitwell.ca/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers",
}

while True:
    response = requests.get(url, headers=headers)
    dict = response.json()
    if dict["IsBusinessOpen"] == False:
        print("\033[31m", "Queue is closed.")
    elif dict["IsBusinessOpen"] == True:
        print("\033[32m", "Queue is open.")
    time.sleep(5)