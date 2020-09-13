#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Wordlist Olustur")
print("""
Wordlist Oluşturma Programına Hoş Geldiniz.
""")

minimumkarakter = raw_input("Minimum Karakter Sayısını Girin: ")
maksimumkarakter = raw_input("Maksimum Karakter Sayısını Girin: ")
karakter = raw_input("İstediğiniz Karakterleri Girin: ")
kayityeri = raw_input("Kaydedilecek Yeri Girin: ")

os.system("crunch " + minimumkarakter + " " + maksimumkarakter + " " + karakter + " -o " + kayityeri)

print("İşlem Başarıyla Tamamlandı.")
