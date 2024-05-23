#!/usr/bin/env python3

import requests
import time
from playsound import playsound

url = "https://service2.diplo.de/rktermin/extern/choose_realmList.do?locationCode=isla&request_locale=en"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def check_appointment_availability():
    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            if 'application/json' in response.headers.get('Content-Type'):
                content = response.json()
                print(content)
            else:
                content = response.text

            keywords = ["student", "winter", "2024", "Study", "WinterSemester", "wintersemester", "appointment", "booking"]
            for keyword in keywords:
                if keyword in content:
                    print("*************************************************************")
                    print("Appointment available at", time.asctime(time.localtime()))
                    print("*************************************************************")
                    playsound("alarm.mp3")
                else:
                    print("No appointment available at", time.asctime(time.localtime()))
            time.sleep(10)
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
        except ValueError:
            print("Received invalid JSON response")
            time.sleep(60)

check_appointment_availability()
