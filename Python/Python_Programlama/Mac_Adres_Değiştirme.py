#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC Degistirme")
print("""
MAC Adres Değiştirme Programına Hoş Geldiniz. 

1) MAC Adresi Random Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orijinale Döndür
""")

islemno = raw_input("İşlem No Girin: ")

if(islemno=="1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Random Belirlendi.")


if(islemno=="2"):
	macadres = raw_input("Yeni MAC Adres Girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Elle Belirlendi.")

if(islemno=="3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adresi Orijinale Döndürüldü.")
