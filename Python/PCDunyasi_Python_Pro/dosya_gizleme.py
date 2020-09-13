# uncompyle6 version 3.6.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 19 2019, 23:36:22) 
# [GCC 9.2.1 20191008]
# Embedded file name: dosya_gizleme.py
# Compiled at: 2019-05-06 00:23:00
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('apt-get install steghide')
os.system('clear')
os.system('figlet DOSYA GIZLEME')
print '\n1) Bilgi Toplama\n2) Dosya Gizleme\n3) Dosya \xc3\x87\xc4\xb1kartma\n'
secim = raw_input('Se\xc3\xa7im : ')
if secim == '1':
    resim = raw_input('Resim : ')
    os.system('steghide info ' + resim)
if secim == '2':
    resim = raw_input('Resim : ')
    gizlenecek_dosya = raw_input('Gizlenecek Dosya : ')
    os.system('steghide embed -cf ' + resim + ' -ef ' + gizlenecek_dosya)
if secim == '3':
    resim = raw_input('Resim : ')
    os.system('steghide extract -sf ' + resim)
# okay decompiling pcdunyasi/dosya_gizleme.pyc
