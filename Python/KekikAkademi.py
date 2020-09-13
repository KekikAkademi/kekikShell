# uncompyle6 version 3.6.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Oct 19 2019, 23:36:22) 
# [GCC 9.2.1 20191008]
# Embedded file name: BTH_PRO.py
# Compiled at: 2019-05-23 12:41:31
import os
os.system('apt-get install figlet')
os.system('clear')
os.system('figlet BTH PRO V1.5')
yesil = '\x1b[32m'

print("""
Bu Araç BirkanTekkan'ın Takipçileri İçin Hazırladığı PenTest Araçlarını Barındıran Bir Projedir.
    Bu Proje Kendi Sistemlerinize PenTest Uygulamanız İçin Geliştirilmiştir.

~Amaç Dışı Kullanımdan Doğacak Olan Sorumluluk Tamamen Kullanıcıya Aittir.


        1) Bilgi Toplama [4]
        2) Güvenlik Açığı Analizi [1]
        3) Güvenlik Açığı İstismarı [0]
        4) İstismar Sonrası [2]
        5) Parola Saldırıları [2]
        6) Koklama & Sızdırma [0]
        7) DoS/DDoS Saldırıları [1]
        8) Akıllı Telefon Pentest [0]
        9) Kablosuz Ağ Pentest [0]
        10) Ekstra Araçlar [2]
        11) Araç Ekle
        12) Sorun Bildir

""")

secim = input('Seçim : ')

## 1) Bilgi Toplama
if secim == '1' or secim == '01':
    os.system('clear')
    os.system('figlet Bilgi Toplama')
    print("""
        1) Port Tarama (NMAP)
        2) SSH Enumerate (ssh_enum.py)
        3) İçerik Yönetim Sistemi(CMS) Tespit (CMSEEK)
        4) Drupal Enumerate (DRUPWN, DROOPESCAN)

        99) Ana Menü
	""")
    btsecim = input('BTSeçim : ')
    
    ## 1.1) Port Tarama
    if btsecim == '1' or btsecim == '01':
        os.system('apt-get install nmap')
        os.system('clear')
        os.system('figlet Port Tarama')
        print("""

Bu Adımda NMAP Aracı Kullanılarak Port Taraması Gerçekleştirilir
ve Elde Edilen Bütün Sonuçlar TXT Dosyalarına Kaydedilir.
Sizden İsteden Sadece "Hedef IP/Domain" Bilgisidir.

~Amaç Dışı Kullanmak Yasaktır. Sadece Kendi Sistemlerinizde Test Edin.  

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 02:00

        1) Hızlı Tarama
        2) TCP/UDP Tarama
        3) Tüm Portlar Tarama
        4) İşletim Sistemi Tespiti
        5) Agresif Tarama 
        6) Ayrıntılı Tarama
        7) Belirli Porta Ayrıntılı Tarama
		""")
        ptsecim = input('PTSeçim : ')
        
        ## 1.1.1) Hızlı Tarama
        if ptsecim == '1':
            hthedefip = input('Hedef IP/Domain : ')
            os.system('nmap -T4 -p 1-65535 -oN hizli_tarama_' + hthedefip + '.txt ' + hthedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.2) TCP/UDP Tarama
        elif ptsecim == '2':
            tuthedefip = input('Hedef IP/Domain : ')
            os.system('nmap -sS -sU -PN -oN tcp_udp_tarama_' + tuthedefip + '.txt ' + tuthedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.3) Tüm Portlar Tarama
        elif ptsecim == '3':
            tpthedefip = input('Hedef IP/Domain : ')
            os.system('nmap -sS -sV -sU -PN -p 1-65535 -oN tum_port_tarama_' + tpthedefip + '.txt ' + tpthedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.4) İşletim Sistemi Tespiti
        elif ptsecim == '4':
            ishedefip = input('Hedef IP/Domain : ')
            os.system('nmap -O -oN isletim_sistemi_tarama_' + ishedefip + '.txt ' + ishedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.5) Agresif Tarama
        elif ptsecim == '5':
            athedefip = input('Hedef IP/Domain : ')
            os.system('nmap -T4 -A -oN agresif_tarama_' + athedefip + '.txt ' + athedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.6) Ayrıntılı Tarama
        elif ptsecim == '6':
            ahedefip = input('Hedef IP/Domain : ')
            os.system('nmap -T4 -A -v -oN ayrintili_tarama_' + ahedefip + '.txt ' + ahedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
        
        ## 1.1.7) Belirli Porta Ayrıntılı Tarama
        elif ptsecim == '7':
            bphedefip = input('Hedef IP/Domain : ')
            port = input('Hedef Port : ')
            os.system('nmap -A -v -sS -sV -p ' + port + ' -oN belirli_port_tarama_' + bphedefip + ' ' + bphedefip)
            print('')
            print(yesil + 'Sonuçlar Kaydedildi.')
            print('')
    
    ## 1.2) SSH Enumerate
    elif btsecim == '2' or btsecim == '02':
        os.system('wget https://www.exploit-db.com/download/45233')
        os.system('clear')
        os.system('mv 45233 ssh_enum.py')
        os.system('figlet SSH ENUM')
        print('')
        print("""
Bu Adımda 'SSH Enumerate' Gerçekleştirilerek Verilen Wordlistteki Kelimeler Kontrol Edilir
ve Hedef'e Uygun Olan Kullanıcı Adı Tespit Edilir.
Sonuçlar TXT Dosyasına Kaydedilir.
İşlem Sonrasında 'sonuc.txt' Dosyası İncelenir
'is a valid user!' Aranır.

        Bu Adımda Hedef IP/Port ve Wordlist Bilgilerine İhtiyaç Duyulur.

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 19:35

		""")
        hedef_ip = input('Hedef IP : ')
        hedef_port = input('Hedef Port : ')
        wordlist = input('Wordlist : ')
        os.system('python ssh_enum.py --port ' + hedef_port + ' --userList ' + wordlist + ' --outputFile sonuc.txt ' + hedef_ip)
        os.system('clear')
        print('')
        print(yesil + "Sonuçlar Kaydedildi. 'sonuc.txt' ")
        print('')
    
    ## 1.3) İçerik Yönetim Sistemi(CMS) Tespit
    elif btsecim == '3' or btsecim == '03':
        os.system('git clone https://github.com/Tuhinshubhra/CMSeeK')
        os.system('pip3 install -r CMSeeK/requirements.txt')
        os.system('clear')
        os.system('figlet CMS TESPIT')
        print("""
Bu Adımda (CMSEEK) Aracı Kullanılarak
Hedef Sitenin Kullanmış Olduğu İçerik Yönetim Sistemi(CMS) Tespit Edilir. 

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 11:05

		""")
        hedef_ip = input('Hedef IP/Domain : ')
        os.system('python3 CMSeeK/cmseek.py -u ' + hedef_ip)
    
    ## 1.4) Drupal Enumerate
    elif btsecim == '4' or btsecim == '04':
        os.system('git clone https://github.com/immunIT/drupwn')
        os.system('python3 drupwn/setup.py install')
        os.system('pip3 install -r drupwn/requirements.txt')
        os.system('pip install droopescan')
        os.system('clear')
        os.system('figlet DRUPAL ENUM')
        print("""
Bu Adımda 'DRUPWN ve DROOPESCAN' Aracı Kullanılarak
Drupal Kullanan Sitelere Enumeration Yapılır.

        Bu Adımda Hedef IP/Domain Bilgisi Girerken Başına http:// veya https:// da Ekleyin. 

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 12:11

		""")
        hedef_ip = input('Hedef IP/Domain : ')
        os.system('drupwn --users --themes --modules --dfiles --nodes enum ' + hedef_ip)
        os.system('figlet DROOPESCAN')
        os.system('droopescan scan -u ' + hedef_ip)

## 2) Güvenlik Açığı Analizi
elif secim == '2' or secim == '02':
    os.system('clear')
    os.system('figlet GUVENLIK ACIGI ANALIZ')
    print("""
	1) Otomatik Pentest (SNIPER)
	""")
    gasecim = input('GASecim : ')
    
    ## 2.1) Otomatik Pentest (SNIPER)
    if gasecim == '1' or gasecim == '01':
        os.system('clear')
        os.system('figlet SNIPER')
        os.system('git clone https://github.com/1N3/Sn1per.git')
        os.system('cd Sn1per/ && ./install.sh')
        os.system('clear')
        os.system('figlet SNIPER')
        print("""
Bu Adımda "Sniper" İsimli Araç Kullanılarak
Otomatik Penetrasyon Test İşlemi Başlar.

    Bu Aracın Ücretli Versiyonuda Vardır. Bu Adımda Ücretsiz Versiyon Kullanılmaktadır. 
		""")
        os.system('rm -rf Sn1per')
        hedef_ip = input('Hedef IP/Domain : ')
        os.system('sniper -t ' + hedef_ip)

## 4) İstismar Sonrası
elif secim == '4' or secim == '04':
    os.system('clear')
    os.system('figlet ISTISMAR SONRASI')
    print("""
	1) Linux Exploit Kontrol
	2) SimpleHttpServer
	""")
    issecim = input('ISSecim : ')
    
    ## 4.1) Linux Exploit Kontrol
    if issecim == '1' or issecim == '01':
        os.system('git clone https://github.com/mzet-/linux-exploit-suggester')
        os.system('mv linux-exploit-suggester/linux-exploit-suggester.sh ./les.sh')
        os.system('rm -rf linux-exploit-suggester.sh')
        os.system('clear')
        os.system('figlet LINUX EXPLOIT KONTROL')
        print("""
Bu Adımda 'Linux Exploit Suggester' İsimli Araç İndirilir
ve Masaüstüne 'les.sh' Olarak Kaydedilir.

        Hedef Sunucuda Bu Araç Çalıştırılarak Hedef'e Uygun Exploit Olup Olmadığı Kontrol Edilir.

		Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
		Dakika : 11:05

		""")
        
    ## 4.2) SimpleHttpServer
    if issecim == '2' or issecim == '02':
        os.system('git clone https://github.com/zqqf16/SimpleHTTPServer')
        os.system('mv SimpleHTTPServer/http.py ./server.py')
        os.system('rm -rf SimpleHTTPServer')
        os.system('clear')
        os.system('figlet HTTP SERVER')
        print("""
Bu Adımda HTTP SERVER Başlatılır.
Bulunduğu Dizine Başka Bilgisayarlardan Bağlanılabilir
Dosya Upload/Download Yapılabilir.

        IP : Local/Dış - Port : 8000

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 27:14

		""")
        print('Dış IP')
        os.system('curl icanhazip.com')
        print('')
        os.system('python server.py')

## 5) Parola Saldırıları
elif secim == '5' or secim == '05':
    os.system('clear')
    os.system('figlet PAROLA SALDIRI')
    print("""
	1) SSH Brute (HYDRA)
	2) Wordlist Oluştur (CEWL)
	""")
    pssecim = input('PSSecim : ')
    
    ## 5.1) SSH Brute
    if pssecim == '1' or pssecim == '01':
        os.system('apt-get install hydra')
        os.system('clear')
        os.system('figlet SSH BRUTE')
        print("""
Bu Adımda HYDRA Aracı Kullanılarak
SSH Servisine Yönelik Kaba Kuvvet Saldırısı Gerçekleştirilir.

        Bu Adımda Hedef IP/Kullanıcı Adı/Wordlist Bilgilerine İhtiyaç Duyulur.
~Amaç Dışı Kullanmak Yasaktır. Tüm Sorumluluk Kullanan Kişiye Aittir.

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 23:15

		""")
        hedef_ip = input('Hedef IP : ')
        kullanici_adi = input('Kullanıcı Adı : ')
        wordlist = input('Wordlist : ')
        os.system('hydra -V -l ' + kullanici_adi + ' -P ' + wordlist + ' ' + hedef_ip + ' ssh')
    
    ## 5.2) Wordlist Oluştur
    elif pssecim == '2' or pssecim == '02':
        os.system('apt-get install cewl')
        os.system('clear')
        os.system('figlet WORDLIST OLUSTUR')
        print("""
Bu Adımda CEWL Aracı Kullanılarak
Hedef Web Sitesindeki Kelimeler Toplanılarak Wordlist Oluşturulur.
Oluşturulan Wordlist KullanıcıAdı/Parola Olarak Kullanılabilir.

        Bu Adımda Hedef IP/Domain Bilgisi Yeterlidir.
        Sonuçlar 'cewl_wordlist.txt' olarak kaydedilir.

    Kullanım Videsu : https://youtu.be/3tVSS02eQ4E
    Dakika : 16:21

		""")
        hedef_domain = input('Hedef IP/Domain : ')
        os.system('cewl -d 2 ' + hedef_domain + ' -w ' + hedef_domain + '_wordlist.txt')
        os.system('clear')
        print('')
        print(yesil + 'Sonuçlar Kaydedildi. ' + hedef_domain + '_wordlist')
        print('')

## 7) DoS/DDoS Saldırıları 
elif secim == '7' or secim == '07':
    os.system('clear')
    os.system('figlet DOS/DDOS SALDIRILARI')
    print("""
	1) Hibernet
	""")
    dssecim = input('DSSeçim : ')
    
    ## 7.1)Hibernet
    if dssecim == '1' or dssecim == '01':
        os.system('clear')
        os.system('figlet HIBERNET')
        print("""
Bu Adımda "HIBERNET" Aracı Kullanılarak
DoS/DDoS Saldırıları Gerçekleştirilmektedir.

    Bu Araç Proxy Desteklidir Farklı IP Adreslerinden Saldırılıyormuş Gibi Etki Yaratabilir. 
		""")
        secim = input('Hedef IP/Domain : ')
        os.system('git clone https://github.com/All3xJ/Hibernet.git')
        os.system('pip3 install pysocks bs4 scapy-python3')
        os.system('python3 Hibernet/HiberProxy.py')
        os.system('python3 Hibernet/HibernetV2.2.py')

## 10) Ekstra Araçlar
elif secim == '10':
    os.system('clear')
    os.system('figlet EKSTRA ARACLAR')
    print("""
	1) Uzak Komut Satırı Bağlantısı (TTYD)
	2) Ağ İzleme (ETHERAPE)
	""")
    easecim = input('EASecim : ')
    
    ## 10.1) Uzak Komut Satırı Bağlantısı
    if easecim == '1' or easecim == '01':
        os.system('clear')
        os.system('figlet TTYD')
        print("""
Bu Adımda 'TTYD' Aracı Kullanılarak
Başka Bir Browser'den Bu Komut Satırına Erişim Sağlanabilir.

        Dış Ağdan Bu Komut Satırına Bağlanmak İçin Modem den Port Açmanız Gerekir.
        Bu Aracın Kullandığı Port : 7681 

    Kullanım Videosu : https://youtu.be/4O_p9ZQHaN0


        1) Servis Başlatılsın

		""")
        ttydsecim = input('TTYD Seçim : ')
        if ttydsecim == '1':
            os.system('rm -rf ttyd')
            os.system('apt-get install cmake g++ pkg-config git vim-common libwebsockets-dev libjson-c-dev libssl-dev')
            os.system('git clone https://github.com/tsl0922/ttyd.git')
            os.system('clear')
            os.system('figlet TTYD')
            os.system('cd ttyd && mkdir build && cd build && cmake .. && make && make install && ./ttyd bash')
    
    ## 10.2) Ağ İzleme
    elif easecim == '2' or easecim == '02':
        os.system('apt-get install etherape')
        os.system('clear')
        os.system('figlet AG ANALIZ')
        print("""
Bu Adımda "ETHERAPE" Aracı Kullanılarak
Ağ İzleme Yapılır.

Görsel Arayüzlü Bu Araç Sayesinde
Ağa Gelen/Giden Paketleri Anlık Olarak İzleyebilirsiniz.
		""")
        os.system('etherape')

## 11) Araç Ekle
elif secim == '11':
    print("""

Bu Projeye Araç Ekleme İsteğinde Bulunabilirsiniz.
Aşağıdaki Forma Gerekli Bilgileri Doldurmanız Yeterli.

    İsteğiniz İncelenir ve Araç Bu Projeye Dahil Edilir.

        https://forms.gle/iZUrrwSd7dVhRLoL8

	""")

## 12) Sorun Bildir
elif secim == '12':
    print("""
Bu Projede Karşılaştığınız Sorunları Aşağıdaki Formu Kullanarak Bize Bildirebilirsiniz.

    https://forms.gle/jHtN2kJZxroXiXBcA

	""")
# okay decompiling pcdunyasi/BTH_PRO_V1.5_Sniper.pyc