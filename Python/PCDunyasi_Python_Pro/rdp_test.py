# uncompyle6 version 3.6.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 19 2019, 23:36:22) 
# [GCC 9.2.1 20191008]
# Embedded file name: rdp_bf_test.py
# Compiled at: 2019-05-04 12:46:56
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('figlet RDP BF TEST')
print '\nBu Ara\xc3\xa7 Kendi RDP Servislerinizin Parola G\xc3\xbcvenli\xc4\x9fi \xc4\xb0\xc3\xa7in Geli\xc5\x9ftirilmi\xc5\x9ftir. Ama\xc3\xa7 D\xc4\xb1\xc5\x9f\xc4\xb1 Kullan\xc4\xb1m Yasakt\xc4\xb1r. T\xc3\xbcm Sorumluluk Arac\xc4\xb1 Kullanan Ki\xc5\x9fiye Aittir.\n\n1) RDP Servis Kontrol\n2) Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1 Tespiti\n3) Wordlist Olu\xc5\x9ftur\n4) RDP BF Test\n'
secim = raw_input('Se\xc3\xa7im : ')
if secim == '1':
    hedef_ip = raw_input('Hedef IP : ')
    os.system('nmap -O -p 3389 ' + hedef_ip)
if secim == '2':
    print 'Kod : enablecredsspsupport:i:0'
if secim == '3':
    kullanilacak_karakterler = raw_input('Kullan\xc4\xb1lacak Karakterler : ')
    minimum_karakter = raw_input('Minimum Karakter : ')
    maksimum_karakter = raw_input('Maksimum Karakter : ')
    os.system('crunch ' + minimum_karakter + ' ' + maksimum_karakter + ' ' + kullanilacak_karakterler + ' -o wordlist.txt')
if secim == '4':
    hedef_ip = raw_input('Hedef IP : ')
    kullanici_adi = raw_input('Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1 : ')
    wordlist = raw_input('Wordlist : ')
    os.system('patator rdp_login host=' + hedef_ip + " user='" + kullanici_adi + "' password=FILE0 0=" + wordlist + ' -x free=host:code=0')
# okay decompiling pcdunyasi/rdp_test.pyc
