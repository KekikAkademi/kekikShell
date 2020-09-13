"""

uzun bi süre once kalı lınuxla ılk tanıştıgım donemlerde yaptıgım bi araç
şu an kullanım sorunları olan varsa alıp kullansın aracı sorun bulursanız soyleyın upgrade edeyim

"""
import os
from os import system
from time import sleep
import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

green = ("\033[92m")
blue = ("\033[94m")
yellow =  ("\033[93m")
red = ("\033[91m")
def dpkgClear():
    system("xterm -e sudo rm -rf  /var/lib/dpkg/lock")
    system("clear")
    system("xterm -e sudo dpkg --configure -a")
    system("clear")
def list():
    file = open("/etc/apt/sources.list", "w")
    file.write("""deb http://http.kali.org/kali kali-rolling main contrib non-free""")
    file.close()
    print(green+"[+]Source list güncellendi.")
def logo():
    print (green+"*******************************")
    print (green+"*"+red+"    www.cyber-warrior.org    "+green+"*")
    print (green+"*"+red+"      Kali Linux Destek      "+green+"*")
    print (green+"*"+red+"     coding:'ZeRRoN-HACK'    "+green+"*")
    print(green+"""*******************************
* YENİ BAŞLAYANLAR İÇİN LİNUX * 
*       YARDIM UYGULAMASI     *
* 1. Tarayıcı Uygulamaları    *
* 2. Grafik Uygulamaları      *
* 3. Bug ve sorun gidermeler  *
* 4. Arayüz Özelleştirme      *
* 0. Ana Menü                 *
* 99. çıkmak için  yazınız    *
*******************************""")
    sleep(0.5)
try:
    list()
    system("clear")
    sleep(2)
    while True:
        dpkgClear()
        logo()
        scm = int(input(red+"Bir Seçim Yapınız:"+green))
        if (scm == 1):
            system("clear")
            print("""
******************
*1. Google Chrome* 
*2. Firefox-ESR  *
*3. Opera browser*
******************""")
            sleep(0.3)
            scmt = int(input(red+"Bir Seçim Yapınız:"+green))
            if (scmt == 1):
                print("Google Chrome Yükleniyor...")
                dpkgClear()
                system("xterm -e sudo apt-get install google-chrome-stable")
                print("Kurulum Tamamlandı.")
                system("clear")
                continue
            elif (scmt == 2):
                print("Firefox-esr kuruluyor...")
                dpkgClear()
                system("xterm -e sudo apt-get install firefox-esr")
                print("Kurulum Tamamlandı...")
                system("clear")
                continue
            elif (scmt == 3):
                print("opera browser indiriliyor...")
                system('xterm -e wget "http://download3.operacdn.com/pub/opera/desktop/49.0.2725.39/linux/opera-stable_49.0.2725.39_amd64.deb"')
                dpkgClear()
                print("dosya indirildi..")
                system("sudo dpkg -i *.deb")
                print("indirildi ve kuruldu.")
                system("clear")
                continue
            else:
                print("Lütfen Geçerli Bir Secim Yapınız...")
                continue
        elif (scm == 2):
            print("""
*************
*1. Pitivi  *
*2. Kdenlive*
*3. Krita   *
*************""")
            scmg = int(input(red+"Bir Seçim Yapınız:"+green))

            if (scmg == 1):
                print("Pitivi Yükleniyor...")
                dpkgClear()
                system("xterm -e sudo apt-get install pitivi")
                print("Pitivi Yüklendi")
                system("clear")
                continue
            elif (scmg == 2):
                print("Kdenlive Yükleniyor...")
                dpkgClear()
                system("sudo apt-get install kdenlive")
                print("Kdenlive Kuruldu.")
                system("clear")
                continue
            elif (scmg == 3):
                print("Krita Kuruluyor...")
                dpkgClear()
                system("sudo apt-get install krita")
                print("Krita Kuruldu.")
                system("clear")
                continue
            else:
                print("Lüften Geçerli Bir Seçim Yapınız")
                system("clear")
                continue
        elif (scm == 3):
            print("""
******************************************
*1. Google chrome root olarak çalıştırma.*
*2. Source.list güncelleme               *
*3. Dpkg paket yükleyicisi sorunları     *
******************************************""")
            scmc = int(input(red+"Lütfen Seçim Yapınız:"+green))
            if (scmc == 1):
                print("google chrome root olarak çalıştırmak için ayarlanıyor...")
                system('echo "--no-sandbox">> /opt/google/chrome/google-chrome')
                print("Google Chrome işlemi başarılı...")
                system("clear")
                continue
            elif (scmc == 2):
                print("Source List Güncelleniyor(bu işlem için root yetkisi ile çalıştırın)")
                file = open("/etc/apt/sources.list", "w")
                file.write("""deb http://http.kali.org/kali kali-rolling main contrib non-free""")
                file.close()
                print("Source list güncellendi.")
                system("clear")
                continue
            else:
                print("Lütfen Geçerli Bir Seçim Yapınız.")
                continue
        elif (scm == 4):
            print("""
***************************
*1.Terminale Nick  Ekleme *
*2.Klavye Işıgı Açma      *
****************************""")
            a = int(input(red+"işlem seçiniz:"+green))
            if (a == 1):
                system("xterm -e sudo rm -rf  /var/lib/dpkg/lock")
                system("xterm -e sudo dpkg --configure -a")
                system("xterm -e apt-get install toilet")
                file = open("/etc/bash.bashrc", "a", encoding="utf-8")
                sleep(0.5)
                m_e = input(red+"Girilecek Nickname:"+green)
                metin = ("\ntoilet -f mono9 -F metal {}".format(m_e))
                file.write(metin)
                sleep(0.5)
                print(red+"Metin ekleme Başarılı terminali yeniden başlatin"+green)
                file.close()
                system("clear")
                continue
            elif (a == 2):
                print("""
*****************
*KLAVYE LED AÇMA*
*1. aç/on       *  
*2. kapat/off   *
*****************""")
                a = int(input("Seçim yapınız:"))

                if (a == 1):
                    system("xset led 3")
                    print("ışık açıldı.")
                elif (a == 2):
                    system("xset -led 3")
                    print("ışık kapatıldı.")
                else:
                    print("Geçerli işlem şeciniz")
            else:
                print("Geçerli işlem seçiniz")
#destek ve öneri alanı guvenlık amacı ile askıya alınmıştır..                
        elif (pass):
            try:

                print("""
******************
*Destek Ve Öneri *
******************""")
                sleep(0.5)
                print("Destek ve önerileriniz dikkate alınıp uygulama güncellenecektir.")
                sleep(0.5)
                gm = input("Gmail Adresinizi Giriniz.")
                kş = input("Gmail şifrenizi giriniz")
                hm = pass
                mb = "Uygulama öneri"
                gmail = input("Gönderilecek önerinizi Mesaj Olarak Yazınız:")

                mesaj = MIMEMultipart()
                mesaj["from"] = "{}".format(gm)
                mesaj["to"] = "{}".format(hm)
                mesaj["subject"] = "{}".format(mb)
                yazi = "{}".format(gmail)

                mesajgovdesi = MIMEText(yazi, "plain")
                mesaj.attach(mesajgovdesi)

                mail = smtplib.SMTP("smtp.gmail.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login(gm, kş)
                mail.sendmail(mesaj["from"], mesaj["to"], mesaj.as_string())
                mail.close()
                print("Mesajınız Başarıyla Alındı destek oldugunuz için Teşekkür ederim.")

            except:
                print(
                    "Mail atmak için 'https://myaccount.google.com/lesssecureapps' linke tıklayıp izin vermeniz gerekmektedir")
        elif (scm == 99):
            print("çıkış yapılıyor...")
            break
        elif (scm == "0"):
            continue
        else:
            print("Lütfen Geçerli Bir Seçim Yapınız...")
except PermissionError:
    print(red+"""
 [x]Lütfen root yetkileri alarak başlatın
 uygulamanın bir çok işleminde root izini 
 gerekiyor bir kerelik root yetkisi hiç 
 bir sorun yaşamadan gerekli işlemler
 yapılacaktır...""")

