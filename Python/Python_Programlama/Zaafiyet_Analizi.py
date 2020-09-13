#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zaafiyet Analiz")
print("""
Zaafiyet Analizi Programına Hoş Geldiniz.
""")

os.system("lynis audit system")

print("""

DETAYLI AÇIKLAMA BURAYA YAPILABİLİR.

""")
	
