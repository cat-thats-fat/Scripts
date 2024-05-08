import os
import time
import json

import requests
import threading

def clearterm():
    os.system('clear || cls')

def check(status, endtime):

    interval = 5

    while status[0] == False and time.time() < endtime:
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

        response = requests.get(url, headers=headers)

        responsedict = response.json()

        if responsedict["IsBusinessOpen"] == True:
            status[0] = True
            break
        else:
            print("Queue closed.")

        time.sleep(interval)

def signup():

    url = "https://api.waitwell.ca/api/035301/client/ticket"

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://35301.waitwell.ca",
        "Referer": "https://35301.waitwell.ca/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }

    data = {
        "AdditionalServices_id": None,
        "Category_id": None,
        "CustomField1": "32456432",
        "CustomField2": "3",
        "Email": "s@gmail.com",
        "FirstName": "ss",
        "FormToken": "7c6053297c415870567053524f284870555a53717b5e7a70567053504c63502857705320377c6053757c51587056735c2a544d4c61564d546157634b20374b4f4a6a6d694a545b2d5f46572f5c787a686d4d697e53784c486d4a5d692b4f6f4a34414f69435f6b5076",
        "LastName": "s",
        "MeetMethod": None,
        "Passcode": "",
        "PhoneNumber": "+1 647-879-9876",
        "Queue_id": "1",
        "ServiceType_id": "1",
    }

    response = requests.post(url=url, headers=headers, json=data)
    print(response.status_code, response.text)

    return

def main():

    clearterm()

    time2run = int(input("How many seconds would you like to aim for?"))

    endtime = time.time() + time2run

    status = [False]

    thread = threading.Thread(target=check, args=(status, endtime,))

    thread.start()

    print(f"waiting for {time2run} seconds")

    thread.join()

    print("Aiming complete")


    return

signup()