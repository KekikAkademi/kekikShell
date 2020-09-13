#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet SMB TARAMA")
print("""
Bu araç SMB Servisine yönelik Bilgi Toplama ve Güvenlik Açığı Analizi gerçekleştirir. NMAP tool kullanır. Bu aracın doğru şekilde çalışabilmesi için, hedefte 139,445 nolu portlar açık olmalı.

1) SMB Brute
2) System Info
3) MS17-010
4) Enum Shares
5) Enum Users
6) DoublePulsar Backdoor

""")
secim = input("Seçim : ")

if(secim=="1"):
	print("")
	print("SMB BRUTE : SMB Servisine yönelik kaba kuvvet uygulanabilir mi, sorusunun cevabını verir.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-brute -p139,445")

if(secim=="2"):
	print("")
	print("System Info : Hedef Sistem bilgisini elde etmeye çalışır.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-system-info -p139,445")

if(secim=="3"):
	print("")
	print("MS17-010 : Güvenlik açığının olup olmadığını kontrol eder.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-vuln-ms17-010 -p139,445")

if(secim=="4"):
	print("")
	print("Enum Shares : Paylaşılan dizinleri tespit etmeye çalışır.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-enum-shares -p139,445")

if(secim=="5"):
	print("")
	print("Enum Users : Kullanıcı adlarını tespit etmeye çalışır.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-enum-users -p139,445")

if(secim=="6"):
	print("")
	print("DoublePulsar Backdoor : Arka kapı varmı yok mu kontrolünü yapar.")
	print("")
	hedef = input("HEDEF IP/DOMAIN : ")
	os.system("nmap " + hedef + " --script smb-double-pulsar-backdoor -p139,445")

