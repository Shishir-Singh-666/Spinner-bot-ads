import requests
import time
from termcolor import colored
import pyfiglet

# Base 
url = "https://api.timboo.pro/adsgram"
headers = {
    "authority": "api.timboo.pro",
    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://app.spinnercoin.org",
    "referer": "https://app.spinnercoin.org/",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

# Simple banner
def display_banner():
    ascii_banner = pyfiglet.figlet_format("FoketCrypto", font="slant")
    print(colored(ascii_banner, "cyan"))
    print(colored("Telegram: https://t.me/foketcrypto", "green"))
    print(colored("YouTube: https://youtube.com/@foketcrypto", "red"))


display_banner()


init_data = input(colored("\nEnter your qurey id (paste it here): ", "yellow"))
while not init_data.strip():
    print(colored("[!] qurey id  cannot be empty. Please try again.", "red"))
    init_data = input(colored("\nEnter your init_data (paste it here): ", "yellow"))

delay_time = input(colored("\nEnter delay time in seconds (default is 5): ", "yellow"))
try:
    delay_time = int(delay_time) if delay_time.strip() else 5
except ValueError:
    print(colored("[!] Invalid input. Using default delay time of 5 seconds.", "red"))
    delay_time = 5

print(colored(f"[INFO] Script started with delay time: {delay_time} seconds", "cyan"))

# Infinite loop
while True:
    try:
        
        data_step1 = {"initData": init_data}
        response_step1 = requests.post(url, headers=headers, json=data_step1)

        if response_step1.status_code == 200:
            hash_code = response_step1.json().get("hash")  
            if hash_code:
                print(colored(f"[+] Extracted Hash Code: {hash_code}", "green"))

                
                data_step2 = {
                    "initData": init_data,
                    "hash": hash_code,
                }

                response_step2 = requests.post(url, headers=headers, json=data_step2)

                
                if response_step2.status_code == 200:
                    print(colored(f"[+] Final Response: {response_step2.json()}", "green"))
                else:
                    print(colored(f"[!] Request failed in Step 2 with status code: {response_step2.status_code}", "red"))
                    print(colored(f"[!] Response: {response_step2.text}", "yellow"))
            else:
                print(colored("[!] Hash code not found in the first response.", "red"))
        else:
            print(colored(f"[!] Request failed in Step 1 with status code: {response_step1.status_code}", "red"))
            print(colored(f"[!] Response: {response_step1.text}", "yellow"))

       
        print(colored(f"[INFO] Sleeping for {delay_time} seconds...", "cyan"))
        time.sleep(delay_time)

    except KeyboardInterrupt:
        print(colored("[!] Script interrupted by user. Exiting...", "red"))
        break
    except Exception as e:
        print(colored(f"[!] An error occurred: {e}", "red"))