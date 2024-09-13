from kopeechka import AsyncMailActivations
import requests
from capmonster_python import RecaptchaV2Task
import time
from kopeechka import AsyncMailActivations
import requests
from capmonster_python import RecaptchaV2Task
import time
import asyncio
import threading
import requests
import random
import time
import threading
import httpx
from capmonster_python import HCaptchaTask
import time, re
from requests import Session
import string
import re
import base64


password = "" ##my api key
apikey = "" ##apikey for email
apikeycaptcha = "" #capmonster


def buy_email():
    url = "https://api.kopeechka.store/mailbox-get-email"
    params = {
    "site": "webshare.io",
    "mail_type": "hotmail.com",
    "token": apikey,
    "password": "0",
    "regex": "(https://proxy2.webshare.io/activation/[\\s\\S][^\"]*)",
    "subject": "",
    "investor": "",
    "soft": "",
    "type": "json",
    "api": "2.0"
}       

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            email = data['mail']
            id = data['id']
            return email, id
        else:
            print("Error:", data['status'])
    else:
        print(f"Request failed with status code {response.status_code}")
        return email, id
    

def get_random_proxy():
    with open('proxies.txt', 'r') as f:
        proxies = f.readlines()
    return random.choice(proxies).strip()


def get_message_value():
    url = "https://api.kopeechka.store/mailbox-get-message"
    params = {
        "id": id,
        "token": apikey,
        "full": "",
        "type": "json",
        "api": "2.0"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            return data['value']
            print(value)
        else:
            print("Error:", data['status'])
            return None
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
    



def solve():
  capmonster = RecaptchaV2Task(apikeycaptcha)
  task_id = capmonster.create_task("https://proxy2.webshare.io/register", "6LeHZ6UUAAAAAKat_YS--O2tj_by3gv3r_l03j9d")
  result = capmonster.join_task_result(task_id)
  return result.get("gRecaptchaResponse")
solution = solve()
print(solution)









def printa():
    global start_time
    for _ in range(10):
        email, id = buy_email()
        email = buy_email()
    print(f"Email: {email}")
    print(f"ID: {id}")
    print("thread gang")

url = "https://proxy.webshare.io/api/v2/register/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "Origin": "https://proxy2.webshare.io",
    "Connection": "keep-alive",
    "Referer": "https://proxy2.webshare.io/",
    "Cookie": "_ga_Z1CFG0XGWL=GS1.1.1713535962.3.1.1713535978.44.0.0; _tid=8870c399-69e7-4c1f-b3b6-23226a62d0f0; _gcl_au=1.1.1315505331.1711665198; _ga=GA1.1.1703772599.1711665198; intercom-device-id-zsppwl0f=ad8715bd-d3ed-46ca-b115-26457e8abcbf; _did=1703772599.1711665198; _sid=1713535962; _ir=no-referrer; ph_phc_SgStpNtFchAMqb1IKSAIPiDKGdGrkEYEap1wqhRjcD8_posthog=^%^7B^%^22distinct_id^%^22^%^3A^%^22018ef6b4-02fb-71a1-b0fe-77c47a1b31db^%^22^%^2C^%^22^%^24sesid^%^22^%^3A^%^5B1713535992766^%^2C^%^22018ef6b4-044d-7aa1-9bd4-de316114b180^%^22^%^2C1713535976525^%^5D^%^7D; sessionid=; intercom-id-zsppwl0f=9c1f0eed-560e-49e5-9984-c6d510781c9f; intercom-session-zsppwl0f=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}


data = {
    "email": "okkokq@gmail.com",
    "password": "webshareisgay222",
    "tos_accepted": True,
    "recaptcha": solution, 
}


proxy = get_random_proxy()
proxies = {"https": "http://" + proxy}  # Assuming your proxies are HTTP, change if needed
try:
    response = requests.post(url, headers=headers, json=data, proxies=proxies, timeout=10)
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)


time.sleep(2)
if response.status_code == 200:
    token = response.json().get('token')
    print("Token:", token)
else:
    print("Error:", response.text)
    
with open("token.txt", "a") as file:
                file.write(f"{email}:webshareisgay222:{token}\n")
                




# Create threads and start them
threads = []
for _ in range(3):
    thread = threading.Thread(target=printa, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
