#!/bin/bash

#Coded by z3r0fy

#/Port Scanner

#akincilar.online // ajanlar.org // twitter.com/z3r0fy


clear

echo "***********************************************"
echo "   ----- Nmap Port Scanner Tool 1.0 -----      "
echo "***********************************************"
echo "
          _    _            _ _       _____  
    /\   | |  (_)          (_) |     |  __ \ 
   /  \  | | ___ _ __   ___ _| | __ _| |__) |
  / /\ \ | |/ / |  _ \ / __| | |/ _  |  _  / 
 / ____ \|   <| | | | | (__| | | (_| | | \ \ 
/_/    \_\_|\_\_|_| |_|\___|_|_|\__ _|_|  \_\ 
"
echo "                                    "  
echo "                            Coded by z3r0fy"  
echo "***********************************************"
echo "  "
echo "***********************************************"

echo -n "ip adresi: "; read z3r0fy

echo -n & curl http://api.hackertarget.com/nmap/?q=$z3r0fy

curl -n http://api.hackertarget.com/nmap/?q=$z3r0fy >> acikportlar.txt