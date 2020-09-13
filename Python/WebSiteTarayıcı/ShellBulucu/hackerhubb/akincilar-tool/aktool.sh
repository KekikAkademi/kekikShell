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
  ./aktool.sh
}

portscan()
{
    clear
chmod +x port.sh
./port.sh 
echo " "
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

kcshell()
{
    clear
chmod +x shellupload.sh
./shellupload.sh
echo " "
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

reviplook()
{
    clear
echo -e "${YELLOW}      ____     ___ __ __    ___  ____    _____   ___ "
echo -e "${YELLOW}     |    \   /  _]  T  |  /  _]|    \  / ___/  /  _]"
echo -e "${YELLOW}     |  D  ) /  [_|  |  | /  [_ |  D  )(   \_  /  [_ "
echo -e "${YELLOW}    |    / Y    _]  |  |Y    _]|    /  \__  TY    _]"
echo -e "${YELLOW}    |    \ |   [_l  :  !|   [_ |    \  /  \ ||   [_ "
echo -e "${YELLOW}    |  .  Y|     T\   / |     T|  .  Y \    ||     T"
echo -e "${YELLOW}    l__j\_jl_____j \_/  l_____jl__j\_j  \___jl_____j"
echo "                                                "
chmod +x revip.py
python revip.py
echo " "
echo " Siteler Grabbed.txt Dosyasindadir. "
echo " cat grabbed.txt "
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

md5cras()
{
    clear
chmod +x md5-cracker.py
echo -e "${GREEN}                       888 888888888   "                         
echo -e "${GREEN}                       888 888           "                       
echo -e "${GREEN}                       888 888            "                      
echo -e "${GREEN}    88888b.d88b.   .d88888 8888888b.       "                     
echo -e "${GREEN}    888  888  88b d88  888       Y88b         "                  
echo -e "${GREEN}    888  888  888 888  888        888           "                
echo -e "${GREEN}    888  888  888 Y88b 888 Y88b  d88P             "              
echo -e "${GREEN}    888  888  888   Y88888   Y8888P                 "       
echo -e "${YELLOW}                                      888               "        
echo -e "${YELLOW}                                      888                       "
echo -e "${YELLOW}                                      888                       "
echo -e "${YELLOW}     .d8888b 888d888 8888b.   .d8888b 888  888  .d88b.  888d888 "
echo -e "${YELLOW}    d88P     888P        88b d88P     888 .88P d8P  Y8b 888P    "
echo -e "${YELLOW}    888      888    .d888888 888      888888K  88888888 888     "
echo -e "${YELLOW}    Y88b.    888    888  888 Y88b.    888  88b Y8b.     888     "
echo -e "${YELLOW}      Y8888P 888     Y888888   Y8888P 888  888   Y8888  888     "                                                                                                                                                             
echo " "
echo -e " MD5 [Orn : 21232F297A57A5A743894A0E4A801FC3] : "
read md5
python md5-cracker.py $md5
echo " "
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

cloudbypass()
{
    clear
echo " "
echo -e "${GREEN}   ######  ########    ########  ##    ## ########     ###     ######   ######  "
echo -e "${GREEN} ##    ## ##          ##     ##  ##  ##  ##     ##   ## ##   ##    ## ##    ## "
echo -e "${GREEN} ##       ##          ##     ##   ####   ##     ##  ##   ##  ##       ##       "
echo -e "${GREEN} ##       ######      ########     ##    ########  ##     ##  ######   ######  "
echo -e "${GREEN} ##       ##          ##     ##    ##    ##        #########       ##       ## "
echo -e "${GREEN} ##    ## ##          ##     ##    ##    ##        ##     ## ##    ## ##    ## "
echo -e "${GREEN}  ######  ##          ########     ##    ##        ##     ##  ######   ######   "
echo -e "${WHITE} "
chmod +x cloulflarebypass.py
python cloulflarebypass.py
echo " " 
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

adminpanel()
{
    clear
chmod +x admin_panel_finder.py
python admin_panel_finder.py
echo " " 
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

zoneh()
{
    clear
chmod +x zone-h.pl
echo -e "${GREEN}   ╔═╗╔═╗╔╗╔╔═╗  ╦ ╦  ╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗"
echo -e "${GREEN}   ╔═╝║ ║║║║║╣───╠═╣  ╠═╝║ ║╚═╗ ║ ║╣ ╠╦╝"
echo -e "${GREEN}   ╚═╝╚═╝╝╚╝╚═╝  ╩ ╩  ╩  ╚═╝╚═╝ ╩ ╚═╝╩╚═${WHITE}"
echo " "
echo -e " Site List [Orn site.txt] : "
read site
echo -e " Defacer [Murrez] : "
read defacer
perl zone-h.pl $site $defacer
echo " " 
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

autodorksql()
{
    clear
chmod +x sql.py
python sql.py 
echo " " 
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
}

defacepage()
{
    clear
chmod +x index-generator.sh
./index-generator.sh

}

ddos()
{
    clear
chmod +x ddos.sh
./ddos.sh

}

vulnerability()
{
    clear
chmod +x vulnerability.sh
./vulnerability.sh

}

modul()
{
    clear
echo " "
echo " Modulleri Indermekte Kararli Iseniz Enter'a Basiniz.  "
read enter		
sudo pip install BeautifulSoup4
sudo pip3 install BeautifulSoup4
sudo pip install fake-useragent
sudo pip3 install fake-useragent
sudo pip install requests
sudo pip3 install requests	
sudo pip install bs4
sudo pip3 install bs4
sudo pip install parse
sudo pip3 install parse
sudo pip install python-whois
sudo pip install lxml
sudo pip3 install lxml
sudo apt-get install python-lxml
echo " "
echo -e "${YELLOW} Indirme Islemi Bitti.   ${WHITE}"
echo " Enter'a Basarak Devam Edebilirsiniz . . .  "
read enter
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
echo -e "   ${WHITE}   ▄████████    ▄█   ▄█▄ "
echo -e "   ${LIGHTGREEN}  ███    ███   ███ ▄███▀     ████████╗ ██████╗  ██████╗ ██╗     ███████╗"
echo -e "   ${LIGHTBLUE}  ███    ███   ███▐██▀       ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝"
echo -e "   ${YELLOW}  ███    ███  ▄█████▀           ██║   ██║   ██║██║   ██║██║     ███████╗"
echo -e "   ${CYAN}▀███████████ ▀▀█████▄           ██║   ██║   ██║██║   ██║██║     ╚════██║"
echo -e "   ${GREEN}  ███    ███   ███▐██▄          ██║   ╚██████╔╝╚██████╔╝███████╗███████║"
echo -e "   ${RED}  ███    ███   ███ ▀███▄        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"
echo -e "   ${LIGHTBLUE}  ███    █▀    ███   ▀█▀ "
echo -e "${WHITE}  "
    echo -e "${WHITE}    Created BY Murrez ${CYAN}AKINCILAR.ONLINE"
	echo " "
    echo -e "${LIGHTBLUE}   ==================== Script ==================== "	
    echo -e "${WHITE}   [1] ${WHITE}Port Scan ${LIGHTRED}[Bash]"
    echo -e "${WHITE}   [2] ${WHITE}KC Shell Upload${LIGHTRED}[Bash]"
	echo -e "${WHITE}   [3] ${WHITE}Reverse Ip Lookup ${LIGHTRED}[Python]"
	echo -e "${WHITE}   [4] ${WHITE}MD5 Cracker ${LIGHTRED}[Python]"
	echo -e "${WHITE}   [5] ${WHITE}CloudFlare Bypass ${LIGHTRED}[Python]"
	echo -e "${WHITE}   [6] ${WHITE}Admin Panel Finder ${LIGHTRED}[Python]"
	echo -e "${WHITE}   [7] ${WHITE}Zone-H Mass Poster$ ${LIGHTRED}[Perl]"	
	echo -e "${WHITE}   [8] ${WHITE}Auto SQL Dork Scanner ${LIGHTRED}[Python]"	
	echo -e "${WHITE}   [9] ${WHITE}Deface Page Generator ${LIGHTRED}[Bash]"		
    echo -e "${LIGHTBLUE}   ===================== Menu ===================== "
	echo -e "${WHITE}   [10] ${WHITE}DDOS Menu${LIGHTBLUE}"
	echo -e "${WHITE}   [11] ${WHITE}Vulnerability Menu${LIGHTBLUE}"	
    echo -e "${LIGHTBLUE}   =================== Dowlands =================== "	
	echo -e "${WHITE}   [99] ${WHITE}Modulleri Indirin${LIGHTBLUE}"	
	echo " "
    echo -n -e "${RED}root@MURREZ${WHITE}:${LIGHTBLUE}~/Desktop/aktool${WHITE}# "
    read yourch
    case $yourch in
      1) portscan ;;
      2) kcshell ;;
	  3) reviplook ;;
	  4) md5cras ;;
	  5) cloudbypass ;;
	  6) adminpanel ;;
	  7) zoneh ;;
	  8) autodorksql ;;
	  9) defacepage ;;
	  10) ddos ;;
	  11) vulnerability ;;
	  99) modul ;;
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