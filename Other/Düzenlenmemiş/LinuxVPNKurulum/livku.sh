#!/bin/bash
apt-get update -y
apt-get -y install pptpd
echo "ms-dns 8.8.8.8" >> /etc/ppp/pptpd-options
echo "ms-dns 8.8.4.4" >> /etc/ppp/pptpd-options
ip=`ifconfig eth0 | grep 'inet addr' | awk {'print $2'} | sed s/.*://`
echo "localip $ip" >> /etc/pptpd.conf
echo "remoteip 10.1.0.1-100" >> /etc/pptpd.conf
clear
echo "###################################"
echo "Yeni kullanici bilgilerini giriniz"
echo "###################################"
echo "Yeni kullanici adi: "
read kullanici
echo "Yeni sifre: "
read sifre
echo "$kullanici    pptpd   $sifre  *" >> /etc/ppp/chap-secrets
service pptpd restart
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables-save
clear
echo 
echo !!!!!!!!!!!!!!!!!!!!!!!!
echo !! Kurulum tamamlandi.!!
echo !!!!!!!!!!!!!!!!!!!!!!!!
echo
echo
echo "############################"
echo "VPN bilgileri"
echo "############################"
echo "VPN iP Adresi: " $ip
echo "Kullanici adi: " $kullanici
echo "Sifre: "         $sifre
echo "############################"

exit
