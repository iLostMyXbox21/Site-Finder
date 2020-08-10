import time
import colorama
import urllib.request
import os

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from colorama import Fore, init

init()

def clear():
    os.system('cls')
def mainmenu():
    print(f"""{Fore.CYAN} 
  ______   ______  ________  ________        ________  ______  __    __  _______   ________  _______  
 /      \ /      |/        |/        |      /        |/      |/  \  /  |/       \ /        |/       \ 
/$$$$$$  |$$$$$$/ $$$$$$$$/ $$$$$$$$/       $$$$$$$$/ $$$$$$/ $$  \ $$ |$$$$$$$  |$$$$$$$$/ $$$$$$$  |
$$ \__$$/   $$ |     $$ |   $$ |__          $$ |__      $$ |  $$$  \$$ |$$ |  $$ |$$ |__    $$ |__$$ |
$$      \   $$ |     $$ |   $$    |         $$    |     $$ |  $$$$  $$ |$$ |  $$ |$$    |   $$    $$< 
 $$$$$$  |  $$ |     $$ |   $$$$$/          $$$$$/      $$ |  $$ $$ $$ |$$ |  $$ |$$$$$/    $$$$$$$  |
/  \__$$ | _$$ |_    $$ |   $$ |_____       $$ |       _$$ |_ $$ |$$$$ |$$ |__$$ |$$ |_____ $$ |  $$ |
$$    $$/ / $$   |   $$ |   $$       |      $$ |      / $$   |$$ | $$$ |$$    $$/ $$       |$$ |  $$ |
 $$$$$$/  $$$$$$/    $$/    $$$$$$$$/       $$/       $$$$$$/ $$/   $$/ $$$$$$$/  $$$$$$$$/ $$/   $$/                                                                                          {Fore.RESET}""")
mainmenu()
while True:
    domains = ['.com', '.net', '.org', '.edu', '.gov', '.cc', '.pub', '.xyz', '.wtf']
    site = input('> ')
    if site.upper() == '!CLEAR': 
        clear()
        mainmenu()
    elif site.upper() == '!EXT':
        for i in domains:
            print(i)
    else:
        for i in domains:
            weburl = f'{site}{i}'
            print(f'{Fore.CYAN}{weburl}')
            req = Request(f'https://www.{weburl}')
            try:
                response = urlopen(req)
            except HTTPError as e:
                print(f'{Fore.RED}Could not reach {weburl}: {e.code}{Fore.RESET}')
            except URLError as e:
                print(f'{Fore.RED}Failed to reach a server: {e.reason}{Fore.RESET}')
            else:
                print(f'{Fore.GREEN}https://{weburl} is running{Fore.RESET}')
            time.sleep(1)