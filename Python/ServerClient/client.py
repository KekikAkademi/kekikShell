#!/usr/bin python
# -*- coding: utf-8 -*-

# client.py dosyamızı oluşturalım.

import socket # soket modülümüzü Import ederek çağırıyoruz.

#Socket Objemizi Yaratıyoruz
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Yeni bir soket objesi oluşturalım.

#host = '127.0.0.1'
host = socket.gethostname() # Lokal cihazımızın ismini çağıralım.
port = 12345 # Kullanacağımız portu belirtiyoruz.

clientsocket.connect(('127.0.0.1', port)) # Bağlantı isteğimizi gönderiyoruz.
message = clientsocket.recv(1024) # Server gelen mesajını ekrana yazıyoruz.

clientsocket.close()

print(message.decode('utf-8'))