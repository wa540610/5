import os
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
os.system('clear')
print(' \x1b[38;5;46mRAJA SERVER LOADING....')


os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')
os.system('xdg-open https://youtu.be/Rx4eNsxjCbE?si=PEa1vc3uShrxG723')
os.system('xdg-open https://youtu.be/Rx4eNsxjCbE?si=PEa1vc3uShrxG723')

# --- RAJA NEON COLOR THEME ---
R = "\033[0m"
B = "\033[1m"

PURPLE = "\033[38;5;201m"
PINK   = "\033[38;5;213m"
CYAN   = "\033[38;5;51m"
BLUE   = "\033[38;5;45m"
GREEN  = "\033[38;5;46m"
GOLD   = "\033[38;5;220m"
WHITE  = "\033[38;5;255m"
RED    = "\033[38;5;196m"
GRAY   = "\033[38;5;245m"


# --- GITHUB APPROVAL SYSTEM ---
def raja_approval():
    os.system("clear")

    uuid_raw = str(os.getlogin()) + str(os.getuid())
    key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]

    github_link = "https://github.com/wa540610/5/blob/main/aprovel-73"

    print(f"""
{PURPLE}╔════════════════════════════════════════════════╗
{PURPLE}║ {CYAN}              𓆩 R.A.J.A 𓆪                 {PURPLE}     ║
{PURPLE}║ {PINK}             APPROVAL SYSTEM                {PURPLE}   ║
{PURPLE}╠════════════════════════════════════════════════╣
{PURPLE}║ {GOLD}              ⚡ PREMIUM ACCESS ⚡            {PURPLE} ║
{PURPLE}╚════════════════════════════════════════════════╝
{R}""")

    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")

    print(
        f"{WHITE}{B} YOUR KEY {GRAY}➜ "
        f"{PINK}{B}RAJA-{key}{R}"
    )

    print(f"{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")

    print(f"{GOLD}{B}              💎 TOOL PRICES{R}")
    print(f"{PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")

    print(f"{CYAN}[01] {WHITE}7 Dollars   {PURPLE}➜ {GREEN}7 Days{R}")
    print(f"{BLUE}[02] {WHITE}14 Dollars  {PURPLE}➜ {GREEN}15 Days{R}")
    print(f"{PINK}[03] {WHITE}28 Dollars  {PURPLE}➜ {GREEN}30 Days{R}")

    print(f"{PURPLE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}")

    print(
        f"{CYAN} ⚡ STATUS {WHITE}➜ "
        f"{GOLD}Checking Approval...{R}"
    )

    try:
        response = requests.get(
            github_link,
            timeout=10
        ).text

        if f"RAJA-{key}" in response:

            print(f"""
{GREEN}╔════════════════════════════════════════════════╗
{GREEN}║ {WHITE}             ✓ ACCESS GRANTED               {GREEN}   ║
{GREEN}║ {CYAN}          Welcome To RAJA TOOL ⚡            {GREEN}  ║
{GREEN}╚════════════════════════════════════════════════╝
{R}""")

            time.sleep(2)

        else:

            print(f"""
{RED}╔════════════════════════════════════════════════╗
{RED}║ {WHITE}             ✗ ACCESS DENIED                {RED}   ║
{RED}║ {GOLD}       Key Is Not Approved Yet              {RED}   ║
{RED}╚════════════════════════════════════════════════╝
{R}""")

            os.system(
                f'xdg-open "https://wa.me/+923229120975?'
                f'text=THIS IS MY KEY 🗝️ SIR👉{key}"'
            )

            sys.exit()

    except requests.RequestException:
        print(
            f"\n{RED}[!] {WHITE} Check Internet 🛜 connection.{R}"
        )
        sys.exit()


# --- START APPROVAL ---
raja_approval()
# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

import os
import random
import time
from concurrent.futures import ThreadPoolExecutor as tred

# ==================== COLOR COMBINATIONS ==================== #
C = '\033[1;36m'
G = '\033[1;32m'
Y = '\033[1;33m'
R = '\033[1;31m'
M = '\033[1;35m'
W = '\033[1;37m'
RESET = '\033[0m'

rad = R

import random

def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


sys.stdout.write('\x1b]2;𓆩【 R.A.J.A 👑 】𓆪 \x07')

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    print("""
\033[1;36m╔══════════════════════════════════════════════════╗
\033[1;35m║              𓆩  R.A.J.A 👑  𓆪                 \033[1;36m   ║
╠══════════════════════════════════════════════════╣
\033[1;32m║  ██████╗  █████╗      ██╗ █████╗               \033[1;36m  ║
\033[1;32m║  ██╔══██╗██╔══██╗     ██║██╔══██╗              \033[1;36m  ║
\033[1;32m║  ██████╔╝███████║     ██║███████║              \033[1;36m  ║
\033[1;32m║  ██╔
