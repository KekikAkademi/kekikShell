# Clickert
Çeşitli link kısaltma sitelerinin tıklama bot'u . [http-https | socks4 | socks5]
----------------------------------------------
Windows için .exe indirmek için :

    https://github.com/raif-py/clickert.exe


Kullanım : 
----------


İşletim sisteminize Python3 'u ve "pip paket yöneticisini" kurduktan sonra başlatabilirsiniz 

Linux :

     python3 clickert.py
     
Windows :

    clickert.py 'ye çift tık (python3 launcher ile başlatacak)
---------------------------------------    
Gereklilikler [herşey doğru giderse kendisi yüklenecektir] :

   Linux:
    
        selenium
    
   Windows:
    
        selenium
        win10soup

-------------------------------------
Alabileceğiniz olası hatalar :

   Chromedriver doğru yapılandırılmamış . indirip bu konuma atın [konum]:
   
    işletim sisteminize ve chrome sürümüne uygun chromedriver'ı buradan yükleyin https://chromedriver.chromium.org/
    zip'den çıkartıp clickert.py'nin olduğu yere kopyalayın içeriğini
    
    
    
----------------------------------------
Çalıştığı süre boyunca belli sürelerde proxy güncellemesi yapacaktır .
Kendi listesinizi kullancaksanız ; [manuel liste ile devam edecekseniz]

    python clickert.py -indirme_yapma
ile çalıştırın ..

------------------------------------
Hangisini Açmalıyım :
----
    clickert.py'yi açarak http\https proxyler kullanacak ve listeniz proxy.txt olacaktır
    
    clickert_socks4.py'yi açarak socks4 proxyler kullanacak ve listeniz socks4.txt olacaktır
    
    clickert_socks5.py'yi açarak socks5 proxyler kullancak ve listeniz socks5.txt olacaktır
Bunlar ne bilmiyorsan clickert.py'yi kullanabilirsin .

------------------------------------

 Sorumluluk kabul edilmeyecektir !
 
 
 *Powered by raif.py*
 
