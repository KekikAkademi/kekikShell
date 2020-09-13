# uncompyle6 version 3.6.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 19 2019, 23:36:22) 
# [GCC 9.2.1 20191008]
# Embedded file name: joomla_scanner.py
# Compiled at: 2019-06-19 13:30:05
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('apt-get install joomscan')
os.system('clear')
os.system('figlet JOOMLA SCANNER')
print '\nBu Ara\xc3\xa7 Joomla \xc4\xb0le Haz\xc4\xb1rlanm\xc4\xb1\xc5\x9f Web Sitelerde Bilgi Toplama ve G\xc3\xbcvenlik A\xc3\xa7\xc4\xb1\xc4\x9f\xc4\xb1 Tespiti Yapan JoomScan Arac\xc4\xb1n\xc4\xb1 Kullan\xc4\xb1r. \n\n'
hedef = raw_input('Hedef IP/Domain : ')
os.system('joomscan -u ' + hedef)
# okay decompiling pcdunyasi/joomla_scanner.pyc
