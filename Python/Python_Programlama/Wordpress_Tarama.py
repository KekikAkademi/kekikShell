#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""
Wordpress Tarama Programına Hoş Geldiniz. 

1) Hızlı Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanıcı Adı Tarama
""")

islemno = raw_input("İşlem Numarasını Girin: ")

if(islemno=="1"):
	site = raw_input("Site Adresi Girin: ")
	os.system("wpscan --url " + site)

elif(islemno == "2"):
	site = raw_input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate p")

elif(islemno == "3"):
	site = raw_input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate t")

elif(islemno == "4"):
	site = raw_input("Site Adresi Girin: ")
	os.system("wpscan --url " + site + " --enumerate u")

else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
