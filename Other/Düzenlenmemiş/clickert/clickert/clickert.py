# -*- coding: utf-8 -*-
#raif.py tarafından kodlandı
import os
import sys
import json  # chromedriver'ın çalışır olduğunu kontrol et
import time
import base64
import random
# Bunları inceliyorsan 6 haftalık emeğe bakıyorsun demektir . Tabiki mükemmel kodlanmadı . Elimden geleni yaptım ..
import platform
import threading
import urllib
import urllib.request as req
####
isim = os.getlogin()
platform = platform.system()
if platform == "Windows":
    chromedriver = "/chromedriver.exe"
    try:
        from win10toast import ToastNotifier
    except:
        print("\n\t\twin10toast modülü yüklü değil !\n\t\tpip kurulu ise yükleyebilirim !")
        try:
            os.system("pip install win10toast")
            from win10toast import ToastNotifier
        except:
            print("\n\t\tKurulamadı ! İletişime geçin ...")
elif platform == "Linux":
    chromedriver = "/chromedriver"
else:
    print("\tÜzgünüm işletim sistemin desteklenmiyor . Mac için ayrı düzenleme yapmam gerekiyor");sys.exit()
acik = "\n\t\tBuranın ekran görüntüsünü al ve bana yolla (@raif.py)\n\t\tGörünüşe göre bir açık yakaladın :)"
orj_json = """{"linktl": "linktl.link1 linktl.link2", "bcvc": "bcvc.link1 bcvc.link2", "trlink": "trlink.link1 trlink.link2", "adfly": "adfly.link1 adfly.link2", "api":"https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all", "user-agent": ["Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1", "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0"] , "plt_linktl": 40, "plt_bcvc": 50, "plt_trlink": 40, "plt_adfly": 40}"""
renk = random.choice(["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"])
argv = sys.argv
####
if sys.version_info.major < 3:
    print("\033[31mSadece P 3 !");sys.exit()
####
def temizle():
    if platform == "Windows":
        os.system("cls")
    else:
        os.system("clear")
####
def exit1():
    try:
        input(renk+"\n\t\tPress [Enter] to exit\t\033[0m")
    except:sys.exit()
    sys.exit()
    
####
temizle()
print(f"\t\t\033[32mHoşgeldin {renk}{isim}\033[32m Lütfen Bekle ...\033[0m")
try:
    from selenium import webdriver
    import selenium # from selenium improt webdriver     # PROXY TXTİ DEENETLE    from selenium import webdriver
except ImportError:
    print("\t\tGörünüşe göre Selenium yüklü değil :/ . \n\t\tEndişelenme Python'u doğru kurduysan yükleyebilirim ")
    kontrol = os.system("pip3 install selenium")
    if kontrol != 0:print("\t\tpip paket yöneticisi yüklü değil gibi gözüküyor o_o ....\n")
    try:
        from selenium import webdriver
        import selenium
    except ImportError:
        print("\t\tÜzgünüm dostum Selenium kurulamadı . Iletişim kurun @raif.py \n")
        exit1()
    except:
        print("\n\t\tBu sefer daha başka bir hata aldık :D");exit1()
except:
    print("\n\t\tBu nasıl bir hatadır ?\n")
    os.system("pip3 uninstall selenium")
    os.system("pip3 install seneium")
    try:
        from selenium import webdriver
        import selenium
    except:
        print("\n\t\tÜzgünüm . Düzgün kurulamadı . Gerekli 'ss'leri ulaştırın --> @raif.py | omerto12.45@gmail.com ")
        exit1()
try:
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless")
    if platform == "Windows":
            opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=os.getcwd()+chromedriver, options=opt)
    driver.quit()

except:
    print("\033[31m\n\t\tChromedriver doğru yapılandırılmamış !\n\t\tLütfen uygun olanı indirip buraya atın --> "+os.getcwd());exit1()
temizle()
#####################################################

#
def bildir(konu):
    if platform == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Clickert V5",konu)
    else:
        olamaz=os.system(f'notify-send -u critical -a "clickert v5" "{konu}"')
        if olamaz != 0:
            print("\033[31m\t\t"+konu+"\033[0m")

def down(indirme,api="https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"):
    if not api:
        print("\t\tGörünüşe göre api kısmını boş bırakmışsın . Orjinal api ile devam ediliyor!")
        api="https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    if not indirme:
        print("\t\tApi kaynağından güncel liste indiriliyor")
        try:
            req.urlretrieve(api,"proxy.txt")
        except:
            print("\n\t\tProxy listesi indirilirken hata ile karşılaşıldı . Tekrar deneniyor")
            time.sleep(3)
            try:
                req.urlretrieve(api,"proxy.txt")
            except:print("\n\t\tProxy listesi indirilirken hata ile karşılaşıldı !")
    elif indirme:
        print("\t\t-no_download yada -indirme_yapma parametresi açık . Indirme yapılmayacaktır")
#
###########----------------------------##############
def exit0(mesaj):
    # exit 'ı çağır çıkış yaptır . Aslan
    print(f"\n\t\t\033[31m{mesaj}\033[0m")
    threading.Thread(target=bildir(mesaj))
    try:
        thread._stop
        thread._delete
    except:pass
    sys.exit()
#####################################################
def linktl(agents,page_load_timeout=40):
    while True:
        link = random.choice(settings[sec].split())
        while True:    
            try:
                with open("proxy.txt") as liste:
                    liste = liste.read().split("\n")
                    liste = random.choice(liste)
                    if not liste:
                        print("\t\tProxy boş geldi . Yeniden deneniyor !")
                    else:
                        break
            except:
                try:
                    time.sleep(3)
                    with open("proxy.txt") as liste:
                        liste = liste.read().split("\n")
                        liste = random.choice(liste)
                        if not liste:
                            print("\t\tProxy boş . Tekrar deneniyor")
                        else:
                            break
                except:
                    print("\n\t\tProxy.txt bulunamadı . Api kaynağından indiriliyor !")
                    down(indirme,api)      ######PROXY.txt YOK NE YAPACAĞIZ ?
        
        agent = random.choice(agents)
        print("""\t\t\033[36m-\033[0mProxy : {} User-Agent : {}\033[36m-\033[0m""".format(liste,agent[13:35]))

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument('--proxy-server={}'.format(liste))
        chrome_options.add_argument("--user-agent={}".format(agent))
        chrome_options.add_argument("--headless")
        if platform == "Windows":
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromedriver1 = os.getcwd()+chromedriver
        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)            
        except selenium.common.exceptions.WebDriverException:
            try:
                print("\n\t\t[Doğrulanıyor]\n")
                time.sleep(3)
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:
                print("\t\tPls install & unzip chromedriver this location -> {}   link = https://chromedriver.chromium.org/".format(os.getcwd()));exit()
        except:
            try:
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:sys.exit()
        driver.set_page_load_timeout(int(page_load_timeout))
        try:
            driver.get(link)
            if driver.title == "lnkload.com":print("( Bad Proxy )\n");sys.exit()
            if driver.title == 'Just a moment...':
                print("\t\tCloudFlare Protection .. We will waiting 5 seconds ..")
                time.sleep(5)
            konum = driver.current_window_handle
            time.sleep(15)
            driver.find_element_by_id('get_link_btn').click()
            driver.switch_to.window(konum)
            time.sleep(1)
            driver.find_element_by_id('get_link_btn').click()
            driver.switch_to.window(konum)
            time.sleep(3)
            #powered by raif.py
            print("\t\t\033[36m**Başarılı !** --->  \033[0m"+liste+"")
            driver.quit()
        except:
            driver.quit()
        try:
            driver.quit()
        except:pass
def bcvc(agents,page_load_timeout=40):
    while True:
        link = random.choice(settings[sec].split())
        while True:
            try:
                with open("proxy.txt") as liste:
                    liste = liste.read().split("\n")
                    liste = random.choice(liste)
                    if not liste:
                        print("\t\tProxy boş geldi . Yeniden deneniyor !")
                    else:
                        break
            except:
                try:
                    time.sleep(3)
                    with open("proxy.txt") as liste:
                        liste = liste.read().split("\n")
                        liste = random.choice(liste)
                        if not liste:
                            print("\t\tProxy boş geldi . Yeniden deneniyor !")
                        else:
                            break
                except:print("\n\t\tProxy.txt bulunamadı . Api kaynağından indiriliyor !");down(indirme,api) 
        
        agent = random.choice(agents)
        print("""\t\t\033[36m-\033[0mProxy : {} User-Agent : {}\033[36m-\033[0m""".format(liste,agent[13:35]))

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--proxy-server={}'.format(liste))
        chrome_options.add_argument("--user-agent={}".format(agent))
        chrome_options.add_argument("--headless")
        if platform == "Windows":
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromedriver1 = os.getcwd()+chromedriver
        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)            
        except selenium.common.exceptions.WebDriverException:
            try:
                print("\t\t[Doğrulanıyor]")
                time.sleep(3)
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:
                print("\t\tPls install & unzip chromium this location -> {}   link = https://chromedriver.chromium.org/".format(os.getcwd()));exit()
        except:
            try:
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:sys.exit()
                
        driver.set_page_load_timeout(page_load_timeout)
        try:
            driver.get(link)
            if driver.title == "bc.vc":
                sys.exit()
            time.sleep(7)
            handler = driver.current_window_handle
            tikla = driver.find_element_by_id("getLink").click()
            time.sleep(7)
            try:
                driver.switch_to.window(handler)
            except:
                pass
            try:
                tikla = driver.find_element_by_id("getLink").click()
            except:
                pass
            time.sleep(5)
            #powered by raif.py
            print("\t\t\033[36m**Başarılı !** --->  \033[0m"+liste+"")
        except:
            driver.quit()
        try:
            driver.quit()
        except:pass
def adfly(agents,page_load_timeout=40):
    while True:
        link = random.choice(settings[sec].split())
        while True:
            try:
                with open("proxy.txt") as liste:
                    liste = liste.read().split("\n")
                    liste = random.choice(liste)
                    if not liste:
                        print("\t\tProxy boş geldi . Yeniden deneniyor !")
                    else:
                        break
            except:
                try:
                    time.sleep(3)
                    with open("proxy.txt") as liste:
                        liste = liste.read().split("\n")
                        liste = random.choice(liste)
                        if not liste:
                            print("\t\tProxy boş geldi . Yeniden deneniyor !")
                        else:
                            break
                except:print("\n\t\tProxy.txt bulunamadı . Api kaynağından indiriliyor !");down(indirme,api)
        
        agent = random.choice(agents)
        print("""\t\t\033[36m-\033[0mProxy : {} User-Agent : {}\033[36m-\033[0m""".format(liste,agent[13:35]))

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument('--proxy-server={}'.format(liste))
        chrome_options.add_argument("--user-agent={}".format(agent))
        chrome_options.add_argument("--headless")
        if platform == "Windows":
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromedriver1 = os.getcwd()+chromedriver
        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)            
        except selenium.common.exceptions.WebDriverException:
            try:
                print("\t\t[Doğrulanıyor]")
                time.sleep(3)
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:
                print("\t\tPls install & unzip chromedriver this location -> {}   link = https://chromedriver.chromium.org/".format(os.getcwd()));exit()
        except:
            try:
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:sys.exit()
                
        driver.set_page_load_timeout(page_load_timeout)
        try:
            driver.get(link)
            if driver.title == "libittarc.com":print("( Bad Proxy )\n");sys.exit()
            if driver.title == 'Just a moment...':
                print("\t\tCloudFlare Protection .. We will waiting 5 seconds ..")
                time.sleep(6)
            time.sleep(7)
            tikla = driver.find_element_by_class_name("mwButton").click()
            time.sleep(3)
            try:
                tabs = driver.window_handles
                driver.switch_to.window(tabs[0])
                
                tikla = driver.find_element_by_class_name("mwButton").click()
            except:pass
            #powered by raif.py
            print("\t\t\033[36m**Başarılı !** --->  \033[0m"+liste+"")
            
        except:
            driver.quit()
        try:
            driver.quit()
        except:pass
def trlink(agent,page_load_timeout=40):
    while True:
        link = random.choice(settings[sec].split())
        while True:
            try:
                with open("proxy.txt") as liste:
                    liste = liste.read().split("\n")
                    liste = random.choice(liste)
                    if not liste:
                        print("\t\tProxy boş geldi . Yeniden deneniyor !")
                    else:
                        break
            except:
                try:
                    time.sleep(3)
                    with open("proxy.txt") as liste:
                        liste = liste.read().split("\n")
                        liste = random.choice(liste)
                        if not liste:
                            print("\t\tProxy boş geldi . Yeniden deneniyor !")
                        else:
                            break
                except:print("\n\t\tProxy.txt bulunamadı . Api kaynağından indiriliyor !");down(indirme,api)
        
        agent = random.choice(agents)
        print("""\t\t\033[36m-\033[0mProxy : {} User-Agent : {}\033[36m-\033[0m""".format(liste,agent[13:35]))

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument('--proxy-server={}'.format(liste))
        chrome_options.add_argument("--user-agent={}".format(agent))
        chrome_options.add_argument("--headless")
        if platform == "Windows":
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chromedriver1 = os.getcwd()+chromedriver
        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)            
        except selenium.common.exceptions.WebDriverException:
            try:
                print("\t\t[Doğrulanıyor]")
                time.sleep(3)
                driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver1)
            except:
                print("\t\tPls install & unzip chromedriver this location -> {}   link = https://chromedriver.chromium.org/".format(os.getcwd()));exit()

                
        driver.set_page_load_timeout(page_load_timeout)
        try:
            driver.get(link)
            if driver.title == 'tr.link':
                sys.exit()
            if driver.title == 'Attention Required! | Cloudflare':
                sys.exit()
            elif driver.title == "安全检查! | 百度云加速":
                print("\t\t\t\033[31mUYGUR TÜRKLERİNE ÖZGÜRLÜK !\033[0m");sys.exit()
            time.sleep(2)
            try:
                uyari = driver.find_element_by_class_name("cancel").click()
            except:
                try:
                    time.sleep(3)
                    uyari = driver.find_element_by_class_name("cancel").click()
                except:pass
            sekmeler = driver.window_handles
            while True:
                driver.switch_to.window(random.choice(sekmeler))
                if driver.title == "TRLink - Link Kısalt, Para Kazan - Shorten Link, earn money":
                    break
            time.sleep(5)
            #driver.switch_to.window(orj_tabs)
            #print("Bu bir hata değil sorun yok !")
            tik = driver.find_element_by_xpath('//*[@id="dinami"]/font/span/main/button').click()
            sekmeler = driver.window_handles
            while True:
                driver.switch_to.window(random.choice(sekmeler))
                if driver.title == "TRLink - Link Kısalt, Para Kazan - Shorten Link, earn money":
                    break
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div[1]/main/div/a').click()
            #asd-dsa
            sekmeler = driver.window_handles
            while True:
                driver.switch_to.window(random.choice(sekmeler))
                if driver.title == "TRLink - Link Kısalt, Para Kazan - Shorten Link, earn money":
                    break
            try:tik = driver.find_element_by_xpath('/html/body/div/div[1]/main/div/a').click()
            except:pass
            time.sleep(3)
            sekmeler = driver.window_handles
            while True:
                driver.switch_to.window(random.choice(sekmeler))
                if driver.title == "TRLink - Link Kısalt, Para Kazan - Shorten Link, earn money":
                    break
            tik1 = driver.find_element_by_class_name("skip-ad").click()
            time.sleep(2)
            #sys.agrv(raifs.text).rawput("NONES","!")
            print("\t\t\033[36m**Başarılı !** --->  \033[0m"+liste+"")
            driver.quit()
        except:
            driver.quit()
        try:driver.quit()
        except:pass
####################################
def json_error():
    print("\n\t\tJson dosya biçemi bozuk gibi gözüküyor . Default ayarlar ile değiştiriliyor lütfen kendi ayarlarınızı yapınız !\n")
    with open("settings.json","w") as settings:
        settings.write(orj_json)
    try:settings = json.loads(orj_json)
    except:print("\t\tjson_error'da bilinmeyen bir hata alındı .\n\t\tsettings.json'u silip programı baştan açınız");exit1() 
    time.sleep(3)
    try:
        agents = settings["user-agent"]
        api = settings["api"]
    except KeyError:print("\t\tjson_error'KeyError Hatası alındı . settings ayarları hatalı !");exit1()
    except:print("\t\tjson_error'da bilinmeyen bir hata alındı .\n\t\tsettings.json'u silip programı baştan açınız");exit1()
######################################################
try:
    with open("settings.json") as settings:
        settings = settings.read()
        settings = json.loads(settings)
        agents = settings["user-agent"]
        api = settings["api"]
except FileNotFoundError:
    print("\n\t\t'settings.json' ayar dosyası bulunamadı ! Oluşturuluyor . Lütfen gerekli ayarları yapınız !\n")
    with open("settings.json","w") as settings:
        settings.write(orj_json)
    settings = json.loads(orj_json)
    agents = settings["user-agent"]
    api = settings["api"]
    time.sleep(3)
except json.decoder.JSONDecodeError:json_error()
except KeyError:json_error()
except KeyboardInterrupt:exit1()
except:print("\033[31m\t\tBilinmeyen bir hata ile karşılaşıldı !\033[0m");exit1()
###############

                 
#####################################################
print(renk+r"""
                                __   _,--="=--,_   __
                               /  \."    .-.    "./  \
                              /  ,/  _   : :   _  \/` \
                              \  `| /o\  :_:  /o\ |\__/
                               `-'| :="~` _ `~"=: |
                                  \`     (_)     `/
                           .-"-.   \      |      /   .-"-.
                .---------{     }--|  /,.-'-.,\  |--{     }---------.
                 )        (_)_)_)  \_/`~-===-~`\_/  (_(_(_)        (
                (        _ _      _             _           ____    )
                 )   ___| (_) ___| | _____ _ __| |_  __   _| ___|  (
                (   / __| | |/ __| |/ / _ \ '__| __| \ \ / /___ \   )
                 ) | (__| | | (__|   <  __/ |  | |_   \ V / ___) | (
                (   \___|_|_|\___|_|\_\___|_|   \__|   \_/ |____/   )
                 )                                                 (
                '---------------------------------------------------"""+"\033[0m\n\t\t\t\t[Premium Edition {}|{}|\033[0m]".format(renk,isim))

if len(argv) > 1:
    if "-no_download" in argv:
        indirme = True
        print("\n\t\t[ Program çalıştığı süre boyunca proxy güncellemesi yapmayacak ! ]")
    elif "-indirme_yapma" in argv:
        indirme = True
        print("\n\t\t[ Program çalıştığı süre boyunca proxy güncellemesi yapmayacak ! ]")

    else:
        indirme = False
        for i in ["-i","i","info","-info","--info","-v","--version","version","-version","help","hakkında","bilgi"]:
            if i in argv:
                print("""\n\t\t{}Merhabalar\033[0m ;\n\n\t\tBurayı bulduğun için çok müteşekkiriz .\n\t\tKısaca ne işe yarar bu program özetleyelim\n\n\t\t{}Nasıl Çalışır\033[0m :\n\n\t\t- Internetten çekilmiş proxy listesine bağlanarak tek tek linkleri geçer\n\t\t  böylece tıklama kazanırsınız\n\n\t\t- Lakin çalışması için mutlaka Chrome/Mium yüklü olmalıdır\n\n\t\t- Gerekli ayarları yaptıktan sonra kaç sekme açılsın sorusuna\n\t\t  ne kadar fazla rakam verirseniz o kadar hızlı tıklanma kazanacaksınız\n\n\t\t- Arkaplanda çalıştırıp günlük işlerinize devam etmek istiyorsanız\n\t\t  15-20 sizin için ideal olacaktır\n\n\t\t- Bilgisayarı sadece tıklama kazanmak amaçlı açacaksanız (ram|cpu miktarı'na göre)\n\t\t  40-50 arası tavsiyedir\n\n\t\t{}Riski Var mı\033[0m ?\n\n\t\tNasıl olsa bu bot programı dostum , tabiki riski var\n\n\t\tSize birkaç önerimiz var:\n\n\t\t- Zaten kullanılan link üzerinde çalıştırmanız\n\t\t- Kısa linkleri fazla tutmanız\n\t\t- Kendi referansınız ile sahte hesaplar açarak oradan da kasmanız"\n\t\t- Premium proxy listesi kullanmak [iletişim kur @raif.py]\n\n\t\t{}Full Sürüm\033[0m :\n\n\t\tFull sürümü alarak aslında tam olarak ne almış olacaksınız ;\n\n\t\t- Sınırsız kullanım (ücretsiz sürümde sınırlama vardır [mecburen])\n\n\t\t- Tam erişim (ücretsiz sürümde tam kontrol sağlayamazsınız)\n\n\t\t- Dışa bağımlılığı yok (ücretsiz sürümde web adresime bağlanmak zorundadır)\n\n\t\t- Uzak bilgisayar desteği (uzak bilgisayarınız var ise 7/24 çalıştırabilirsiniz)\n\n\t\t- Kişisel ayarlamalar (full sürümü satın alırsanız size özel ayarlar yapabiliriz)\n\n\t\t- [En önemlisi] Lise'ye giden gençlere maddi/manevi destek olmak\n\n\t\t\033[31mVIP\033[0m :\n\n\t\tVip alarak aslında tam olarak ne almış olacaksınız ;\n\n\t\t- Sınırsız kullanım (ücretsiz sürümde sınırlama vardır)\n\n\t\t- Tam erişim (ücretsiz sürümde tam kontrol sağlayamazsınız)\n\n\t\t- Dışa bağımlılığı yok (ücretsiz sürümde web adresime bağlanmak zorundadır)\n\n\t\t- Uzak bilgisayar bizden ! (Tarafımızca sağlanacak uzak bilgisayar desteği !)\n\n\t\t- Tamamen Özelleştirilebilir (vip sürümü satın alırsanız programı baştan bile yazabilirim :)\n\n\t\t- [En önemlisi] Lise'ye giden gençlere maddi/manevi destek olmak\n\n\t\t\033[31mÜcretsiz sürümden kazancınız ne ise desteğimiz ile 3/4 katına çıkacağını garanti ederiz :)\033[0m\n\n\t\t{}Biz Kimiz\033[0m :\n\n\t\tKendimizi gizleme ihtiyacı duymuyoruz . Yasadışı değiliz :\n\n\t\t- [Tarafından yazıldı]      Ömer Raif Tekin @raif.py\n\t\t- [Tarafından ortaklaşarak] Celal Gülsar    @celalgulsar.py\n\t\t- [Tarafından ortaklaşarak] Başar Girginer  @basarg.x64\n\n\t\t\033[31mSatın Alma Işlemleri Için\033[0m --> \033[32m@raif.py \ omerto12.45@gmail.com\033[0m\n\n\t\tSaygılarla . Clickert Takımı @clickert.py\n\n\n\t\tSon güncelleme : hosting shell açığını bildirdiğim için tüm hesaplarımı engelledi . Sabrım kalmadı artık . Prjeyi opensource yapıyorum .\n\t\tFixlenene kadar kullanabilirsiniz ...""".format(renk,renk,renk,renk,renk));exit1()
else:indirme = False
while True:
    ######
    while True:
        try:
            ilk_secim = int(input("""
                -----------------------

                {}Çalıştırmak istediğiniz :\033[0m
            
                1 - linktl 
                2 - bcvc   
                3 - adfly  
                4 - trlink 
                
                5 - \033[31mÇıkış\033[0m

                A: """.format(renk)))
            if ilk_secim == 5:
                exit1()
            elif ilk_secim in [1,2,3,4]:
                break
            else:
                temizle()
                print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")
        except KeyboardInterrupt:
            exit1()
        except KeyError:
            temizle()
            print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")
        except ValueError:
            temizle()
            print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")
    ######
    if ilk_secim == 1:
        sec = "linktl"
    elif ilk_secim == 2:
        sec = "bcvc"
    elif ilk_secim == 3:
        sec = "adfly"
    elif ilk_secim == 4:
        sec = "trlink"
    try:
        plt = settings["plt_"+sec]
        link = settings[sec].split()
    except:
        json_error()
    while True:
        try:
            ikinci_secim = int(input("""
                {}-----------------------\033[0m
                
                Kaynak   =  {}
                Linkinz  =  {} [{}] 
                Timeout  =  {}

                {}-----------------------\033[0m

                1 - Çalıştır
                2 - Link'i değiştir
                3 - Timeout'u değiştir
                
                4 - \033[31mÇıkış\033[0m
                
                A: """.format(renk,sec,len(link),link[0],plt,renk)))
            if ikinci_secim == 4:exit1()
            elif ikinci_secim in [1,2,3]:break
            else:
                temizle()
                print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")
        except KeyboardInterrupt:exit1()
        except KeyError:
            temizle()
            print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")
        except ValueError:
            temizle()
            print(renk+"\n\t\tLütfen doğru seçeneği işaretleyin !\033[0m")


    #####################################################3
    if ikinci_secim == 2:
        try:
            deg_link = input("\n\t\tBoşluk bırakarak istediğiniz kadar link ekleyebilirsiniz !\n\t\tA: linkadresi1.com lakinadres.com/blmemne [sonsuz]\n\n\t\tLink giriniz : ")
            if not deg_link:
                temizle()
                print("\n\n\t\tBoş geçildi . Değişmeyecek ! \n")
            elif deg_link:
                with open("settings.json","w") as dosya:
                    settings[sec]=deg_link
                    dosya.write(json.dumps(settings))
        except KeyboardInterrupt:exit1()
        except:print("\n\t\tBilinmeyen hata !");exit1()
        
    elif ikinci_secim == 3:
        while True:
            try:
                deg_plt = int(input("\t\tTimeout değerini girin :"))
                settings["plt_"+sec] = deg_plt
                with open("settings.json","w") as dosya:
                    dosya.write(json.dumps(settings))
                break
            except KeyboardInterrupt:exit1()
            except KeyError:
                print("\n\t\tLütfen doğru seçeneği işaretleyin !\n")
            except ValueError:
                print("\n\t\tLütfen doğru seçeneği işaretleyin !\n")

    elif ikinci_secim == 1:
        while True:
            try:
                deger = int(input("""
                {}Kaç defa açılsın ?\033[0m 
                
                A: """.format(renk)))
                if deger < 1:temizle();print("\n\t\tBu miktarı nasıl açabilirim ?!")
                else:break
            except KeyboardInterrupt:exit1()
            except KeyError:
                temizle()
                print("\n\t\tLütfen doğru seçeneği işaretleyin !\n")
            except ValueError:
                temizle()
                print("\n\t\tLütfen doğru seçeneği işaretleyin !\n")
        temizle()
        print(renk+"""
\t          _ _      _             _        
\t      ___| (_) ___| | _____ _ __| |_      
\t     / __| | |/ __| |/ / _ \ '__| __|     
\t    | (__| | | (__|   <  __/ |  | |_      
\t     \___|_|_|\___|_|\_\___|_|   \__| 
\t        \033[0mv5 opensource |by raif.py
""")    
        down(indirme,api)
        if not indirme:
            print("\n\t\tOtomatik güncelleme\033[32m [aktif]\033[0m\n")
        elif indirme:
            print("\n\t\tOtomatik güncelleme\33[31m [pasif]\033[0m\n")
        time.sleep(3)
        sifir = 0
        if ilk_secim == 1:
            while sifir < deger:
                try:
                    thread=threading.Thread(target=linktl,args=(agents,plt))
                    thread.daemon=True
                    thread.start()
                    sifir += 1
                except:
                    print("\t\tKarşılaşılmayan hata !")
                    sys.exit()
        elif ilk_secim == 2:
            while sifir < deger:
                try:
                    thread=threading.Thread(target=bcvc,args=(agents,plt))
                    thread.daemon=True
                    thread.start()
                    sifir += 1
                except:
                    print("\t\tKarşılaşılmayan hata !")
                    sys.exit()
        elif ilk_secim == 3:
            while sifir < deger:
                try:
                    thread=threading.Thread(target=adfly,args=(agents,plt))
                    thread.daemon=True
                    thread.start()
                    sifir += 1
                except:
                    print("\t\tKarşılaşılmayan hata !")
                    sys.exit()
        elif ilk_secim == 4:
            while sifir < deger:
                try:
                    thread=threading.Thread(target=trlink,args=(agents,plt))
                    thread.daemon=True
                    thread.start()
                    sifir += 1
                except:
                    print("\t\tKarşılaşılmayan hata !")
                    sys.exit()
        else:
            print(acik)
            exit1()
        kontrol = 0
        kontrol1 = 0  
        while True:
                try:
                    time.sleep(50) #50 olarak düzelt 
                    zaman = time.localtime().tm_min
                    if zaman in [00,20,40]:
                        down(indirme,api)
                
                
                
                except SystemExit:
                    threading.Thread(target=bildir("Sunucu çıkışı tetikledi . Bir problem olmuş olabilir"))
                    thread._stop
                    thread._delete
                    print("\n\t\t\033[31mSunucu çıkış'ı tetikledi . Bir problem olmuş olabilir\033[0m")
                    sys.exit()
                except:
                    threading.Thread(target=bildir("Çıkış tetiklendi !"))
                    thread._stop
                    thread._delete
                    print("\n\t\tÇıkış tetiklendi . Çıkılıyor !\n\t\tArkaplanda açık kalan chrome'ları kapatabilirsiniz\a")
                    sys.exit()