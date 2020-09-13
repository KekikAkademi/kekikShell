#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Guvenlik Duvari Tespit")
print("""
Güvenlik Duvarı Tespit Etme Programına Hoş Geldiniz.
""")

site = raw_input("Site Adresini Girin: ")
os.system("wafw00f " + site)
