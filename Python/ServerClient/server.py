#!/usr/bin python
# -*- coding: utf-8 -*-

# server.py dosyamızı oluşturalım

import socket # soket modülümüzü Import ederek çağırıyoruz.

#Socket Objemizi Yaratıyoruz
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Yeni bir soket objesi oluşturalım.

#host = '127.0.0.1'
host = socket.gethostname() # Lokal cihazımızın ismini çağıralım.
port = 12345 # Kullanacağımız portu belirtiyoruz.

#Binding to Socket
serversocket.bind(('127.0.0.1', port)) # bind metodu ile host ve portu bildiriyoruz.

#Starting TCP Listener
serversocket.listen(3) # Şimdi client üzerinden gelecek bağlantıyı beklemeye hazırız.

while True:
    #Starting the Connection
    clientsocket, address = serversocket.accept() # Gelen bağlantı isteklerini kabul eden metodumuzu çağırıyoruz.
    
    print("Bağlantı Geldi ~ %s ~" % str(address)) # Gelen bağlantı host adını ekrana yazıyoruz.
    
    message = 'Merhaba! Bağlandığın için teşekkürler..' + "\r\n"
    clientsocket.send(message.encode('utf-8')) # Client üzerine mesajımızı gönderiyoruz.
    
    clientsocket.close() # En son bağlantımızı kapatıyoruz.