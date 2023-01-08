import os, re, random, string, time, sys, base64, httpx
from colorama import Fore
from colorama import Style
from random import randint
from lxml.html import fromstring
from threading import Thread
from httpx_socks import SyncProxyTransport



# cleaner
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



# title
def title():
  print(Fore.RED + """ ______     ______     ______   ______     ______     ______     ______     __  __    
/\  __ \   /\  ___\   /\__  _\ /\  == \   /\  __ \   /\  ___\   /\  ___\   /\_\_\_\   
\ \  __ \  \ \___  \  \/_/\ \/ \ \  __<   \ \ \/\ \  \ \___  \  \ \  __\   \/_/\_\/_  
 \ \_\ \_\  \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_____\   /\_\/\_\ 
  \/_/\/_/   \/_____/     \/_/   \/_/ /_/   \/_____/   \/_____/   \/_____/   \/_/\/_/  ~2Loop#6969""")



#menu
def menu():
    cls()
    title()
    print(Fore.RED + " ")
    print("-- Ez Proxy Scraper&Checker  ------------------------------")
    print(" ")
    print("[1] Proxy Scraper")
    print("[2] Proxy Checker")
    print(" ")
    print("-----------------------------------------------------------")
    
    while True:
        menuinput = input("[?] Input > ")
        print(" ")

        try:
            menuinput = int(menuinput)
            break
        except (ValueError, TypeError, NameError):
            menu()
    
    menuinput = int(menuinput)
    if str(menuinput) == "1":
        scraper()
    elif str(menuinput) == "2":
        checker()
    else:
        menu()


#proxy scraper
def scraper():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print(" ")
    print("-- Ez Proxy Scraper ---------------------------------------")
    print(" ")
    print("[\] Scraping")
    http = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=http&ssl=yes','https://api.proxyscrape.com/?request=displayproxies&proxytype=https&ssl=yes','https://sheesh.rip/new.txt','https://www.proxy-list.download/api/v1/get?type=https','https://www.proxy-list.download/api/v1/get?type=http','https://spys.me/proxy.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt','https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt','https://raw.githubusercontent.com/almroot/proxylist/master/list.txt']
    s4 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks4','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt']
    s5 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks5','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt']
    try:
        os.remove('http.txt')
        os.remove('socks4.txt')
        os.remove('socks5.txt')
    except:
        pass
    for src in http:
        r = httpx.get(src)
        with open("http.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print(" ")
    print('[!] HTTP Scraped')
    for src in s4:
        r = httpx.get(src)
        with open("socks4.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('[!] SOCKS4 Scraped')
    for src in s5:
        r = httpx.get(src)
        with open("socks5.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('[!] SOCKS5 Scraped')
    time.sleep(0.5)
    print(" ")
    print('[+] Done')
    time.sleep(2)
    menu()


#proxy checker
def checker():
    os.system('cls' if os.name == 'nt' else 'clear')
    def check(PROXY,url,prxtype):
        if prxtype == 'http':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownHTTP]','accept-language': 'en'},follow_redirects=True,proxies='http://'+PROXY)
        elif prxtype == 'socks4':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS4]','accept-language': 'en'},follow_redirects=True,transport=SyncProxyTransport.from_url('socks4://'+PROXY))
        elif prxtype == 'socks5':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS5]','accept-language': 'en'},follow_redirects=True,proxies='socks5://'+PROXY)

        with HxClient as client:
            try:
                    req = client.get(url)
                    if req.status_code == 200 and "GET" in req.text:
                        print (Fore.GREEN + '[+] Valid - ' + PROXY + ' ' + str(req.status_code))
                        with open(f'{prxtype}_valid.txt', 'a') as xX:
                            xX.write(PROXY + '\n')
                    elif req.status_code != 200 or not "GET" in req.text:
                        print (Fore.YELLOW + '[!] Invalid - ' + PROXY + ' ' + str(req.status_code))
                    else:
                        print(Fore.RED + '[-] Bad - ' + PROXY + ' ' + str(req.status_code))
            except httpx.HTTPError as exc:
                pass
            except:
                pass
    def proxer():
        try:
            prxtype = input('[?] http / socks4 / socks5 > ')
        except:
            print('[!] Invalid')
            menu()
        try:
            fileproxy = input('[?] Proxy file > ')
        except:
            print('[!] Invalid')
            menu()
        domain = 'https://httpbin.org/anything'
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(fileproxy, 'r') as x:
            prox = x.read().splitlines()
        Threads = []
        for proxy in prox:
            t = Thread(target=check, args=(proxy,domain,prxtype),daemon=True)
            t.start()
            Threads.append(t)
        for i in Threads:
            i.join()
        print(" ")
        print('[!] Done')
        time.sleep(3)
        menu()
    proxer()
    menu()



menu()