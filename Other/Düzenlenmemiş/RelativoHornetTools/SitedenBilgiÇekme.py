import requests

from bs4 import BeautifulSoup

def veri():

    while True:
        try:
            url = input("Verilerini Çekmek İstediğiniz Site Adresinizi Giriniz: ")
            etiket_bir = input("Etiket İsmini Giriniz: ")
            etiket_iki = input("Diğer Etiket İsmini Giriniz: ")
            etiket_üc = input("Sitede Bulunan Etiket İsmini Giriniz: ")


            r = requests.get(url)

            soup = BeautifulSoup(r.content,"html.parser")

            ele_gecirilen_veriler = soup.find_all(etiket_bir,{etiket_iki:etiket_üc})


            print(ele_gecirilen_veriler)
            print("-"*20,"İşlem Sayısı","-"*20)
            print("=>",len(ele_gecirilen_veriler))

        except:
            print("Girilen Site Bilgileri Yanlış.")
            cikis = input("Çıkış Yapmak İstiyor musunuz ? 'E' 'H' : ")
            if cikis == "E":
                print("Çıkış Yapıldı.")
                break

veri()