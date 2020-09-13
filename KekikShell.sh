#!/bin/bash
#Code:keyiflerolsun
#instagram: @keyiflerolsun

#Renk Şeması // https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
	renkreset='\e[0m'
	mavi='\e[1;94m'
	cyan='\e[1;96m'
	yesil='\e[1;92m'
	kirmizi='\e[1;91m'
	beyaz='\e[1;77m'
	sari='\e[1;93m'

#Genel Değişken Tanımları
KurulumTamamlandi() {
	sleep 1
	printf "$beyaz[$renkreset$kirmizi ~ $renkreset$beyaz]$renkreset$kirmizi KURULUM BİTTİ!$renkreset"
	sleep 2
}

HataliIslem() {
	printf "$sari[$renkreset$beyaz!$renkreset$sari] HATALI İŞLEM!$renkreset"
	sleep 1.5
	clear
}

#Banner // http://patorjk.com/software/taag/#p=display&c=bash&f=Stop&t=Kekik%20Shell
banner() {
	clear
	printf "$yesil _    _      _     _ _      $renkreset$beyaz     _    _           _ _ $renkreset\n"
	printf "$yesil| |  / )    | |   (_) |     $renkreset$beyaz    | |  | |         | | |$renkreset\n"
	printf "$yesil| | / / ____| |  _ _| |  _  $renkreset$beyaz     \ \ | | _   ____| | |$renkreset\n"
	printf "$yesil| |< < / _  ) | / ) | | / ) $renkreset$beyaz      \ \| || \ / _  ) | |$renkreset\n"
	printf "$yesil| | \ ( (/ /| |< (| | |< (  $renkreset$beyaz  _____) ) | | ( (/ /| | |$renkreset\n"
	printf "$yesil|_|  \_)____)_| \_)_|_| \_) $renkreset$beyaz (______/|_| |_|\____)_|_|$renkreset\n"
	printf " $beyaz v4.2 coded by github.com/KekikAkademi/KekikShell$renkreset \n"
	printf "\n"
}

#Ana_Menu
Ana_Menu() {
	banner
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$renkreset$sari Genel Kurulumlar$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$renkreset$sari Termux Kurulumlar$renkreset\n"
	printf "$yesil[$renkreset$beyaz 03 $renkreset$yesil]$renkreset$sari The Linux Choice$renkreset\n"
	printf "$yesil[$renkreset$beyaz 04 $renkreset$yesil]$renkreset$sari BruteForce$renkreset\n"
	printf "$yesil[$renkreset$beyaz 05 $renkreset$yesil]$renkreset$sari Botnet$renkreset\n"
	printf "$yesil[$renkreset$beyaz 06 $renkreset$yesil]$renkreset$sari Other$renkreset\n"
	printf "$yesil[$renkreset$beyaz 07 $renkreset$yesil]$renkreset$sari Python$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Çıkış$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem:\e[0m\e[1;77m ' islem

#GenelKurulumlar
if [[ $islem == 1 || $islem == 01 ]]; then
	GenelKurulumlar

#TermuxKurulumlar
elif [[ $islem == 2 || $islem == 02 ]]; then
	TermuxKurulumlar

#TheLinuxChoice
elif [[ $islem == 3 || $islem == 03 ]]; then
	TheLinuxChoice

#BruteForce
elif [[ $islem == 4 || $islem == 04 ]]; then
	BruteForce

#Botnet
elif [[ $islem == 5 || $islem == 05 ]]; then
	Botnet

#Other
elif [[ $islem == 6 || $islem == 06 ]]; then
	Other

#Python
elif [[ $islem == 7 || $islem == 07 ]]; then
	Python

#Çıkış
elif [[ $islem  == 99 ]]; then
	exit 1

else
	HataliIslem
	Ana_Menu

fi

}

##GenelKurulumlar
GenelKurulumlar() {
	sleep 0.5
	apt update && apt upgrade -y
	apt-get install python -y
	apt-get install python2 -y
	apt-get install python-pip -y
		pip install wordlist -y
	apt-get install sudo -y
	apt-get install tsu -y
	apt-get install proot -y
	apt-get install pv -y
	apt-get install ruby -y
	apt-get install cat -y
	apt-get install screenfetch -y
	apt-get install cowsay -y
	apt-get install toilet -y
	apt-get install figlet -y
	apt-get install php -y
	apt-get install perl -y
	apt-get install nmap -y
	apt-get install bash -y
	apt-get install nano -y
	apt-get install curl -y
	apt-get install tar -y
	apt-get install zip -y
	apt-get install fish -y
	apt-get install unzip -y
	apt-get install wget -y
	apt-get install cmatrix -y
	apt-get install openssl -y
	apt-get install openssh -y
	apt-get install ngrok -y
	apt-get install wget -y
	apt-get install curl -y
	pip install grip #Markdown Okumaya Yarar // grip -b *.md
	pip3 install pysocks bs4 scapy-python3 #Hibernet Botnet requirements
	apt-get install nmap hydra medusa ncrack #Brutedum requirements
		#One-Lin3r
		pkg install nano -y
		pkg install git -y
		pkg install perl -y
		pkg install python -y
		pkg install python2 -y
		pip install --upgrade pip
		python3 -m pip install --upgrade pip
		pip3 install one-lin3r
		#One-Lin3r
	KurulumTamamlandi
	Ana_Menu
}

##TermuxKurulumlar
TermuxKurulumlar() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ Termux Kurulumlar ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$sari Ekstra Tuşlar$renkreset		$yesil[$renkreset$beyaz 03 $renkreset$yesil]$sari Tema-Ayar$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$sari Termux Repolar$renkreset		$yesil[$renkreset$beyaz 04 $renkreset$yesil]$sari Metasploit$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' Termux_Islem

###Ekstra Tuşlar
if [[ $Termux_Islem == "1" || $Termux_Islem == "01" ]]; then
	sleep 0.5
	termux-setup-storage
	sleep 1
	mkdir $HOME/.termux/ ;echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" >> $HOME/.termux/termux.properties; termux-reload-properties;
	KurulumTamamlandi
	TermuxKurulumlar

###TermuxRepolar
elif [[ $Termux_Islem == "2" || $Termux_Islem == "02" ]]; then
	sleep 0.5
	pkg install unstable-repo -y
	pkg install root-repo -y
	pkg install python python2 -y
	pkg install python3 -y
	pkg install pip pip2 -y
	KurulumTamamlandi
	TermuxKurulumlar

###Tema Ayar
elif [[ $Termux_Islem == "3" || $Termux_Islem == "03" ]]; then
	TemaAyar() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ Tema Ayar ~" | pv -qL 75
		printf "$renkreset"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$renkreset$sari OhMyZSH$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$renkreset$sari Termux-Style$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' Tema_Islem
		
		####OhMyZSH
		if [[ $Tema_Islem == "1" || $Tema_Islem == "01" ]]; then
			sleep 0.5
			cd $HOME
			pkg install -y libcurl curl
			sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"
			KurulumTamamlandi
			TemaAyar
			
		####Termux-Style
		elif [[ $Tema_Islem == "2" || $Tema_Islem == "02" ]]; then
			sleep 0.5
			cd $HOME
			git clone https://github.com/adi1090x/termux-style.git
			sleep 1
			cd $HOME/termux-style/
			chmod +x *
			./setup

		#Geri
		elif [[ $Tema_Islem == "99" ]]; then
			TermuxKurulumlar

		else
			HataliIslem
			TemaAyar

		fi
		}
		TemaAyar

###Metasploit
elif [[ $Termux_Islem == "4" || $Termux_Islem == "04"  ]]; then
	sleep 0.5
	pkg install unstable-repo -y
	pkg install metasploit -y
	KurulumTamamlandi
	TermuxKurulumlar

###Geri
elif [[ $Termux_Islem == "99" ]]; then
	Ana_Menu

else
	HataliIslem
	TermuxKurulumlar

fi
}

##TheLinuxChoice
TheLinuxChoice() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ The Linux Choice ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$renkreset$sari Fotoğraf Al$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$renkreset$sari Konum Al $renkreset$mavi(NROK Link Vermiyor)$renkreset\n"
	printf "$yesil[$renkreset$beyaz 03 $renkreset$yesil]$renkreset$sari Panoda Kopyalanan İçeriği Al$renkreset\n"
	printf "$yesil[$renkreset$beyaz 04 $renkreset$yesil]$renkreset$sari Ses Al$renkreset\n"
	printf "$yesil[$renkreset$beyaz 05 $renkreset$yesil]$renkreset$sari Pardon $renkreset$mavi(Yalnızca Serveo // Çalışmıyor)$renkreset\n"
	printf "$yesil[$renkreset$beyaz 06 $renkreset$yesil]$renkreset$sari Printer Spam $renkreset$mavi(Yalnızca Serveo // Çalışmıyor)$renkreset\n"
	printf "$yesil[$renkreset$beyaz 07 $renkreset$yesil]$renkreset$sari Kullanıcı Adı Araştır$renkreset\n"
	printf "$yesil[$renkreset$beyaz 08 $renkreset$yesil]$renkreset$sari Sahte Login Ekranı Oluştur$renkreset\n"
	printf "$yesil[$renkreset$beyaz 09 $renkreset$yesil]$renkreset$sari .lnk BackDoor Oluştur $renkreset$mavi(Yalnızca Serveo // Çalışmıyor)$renkreset\n"
	printf "$yesil[$renkreset$beyaz 10 $renkreset$yesil]$renkreset$sari SSH Brute Force$renkreset\n"
	printf "$yesil[$renkreset$beyaz 11 $renkreset$yesil]$renkreset$sari SMS Bomber (v1 // Çalışmıyor)$renkreset\n"
	printf "$yesil[$renkreset$beyaz 12 $renkreset$yesil]$renkreset$sari PythonRAT$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem:\e[0m\e[1;77m ' TheLinuxChoice_Islem

###FotoAl
if [[ $TheLinuxChoice_Islem == "1" || $TheLinuxChoice_Islem == "01" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/FotoAl/
	chmod +x *
	./saycheese.sh

###KonumAl
elif [[ $TheLinuxChoice_Islem == "2" || $TheLinuxChoice_Islem == "02" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/KonumAl/
	chmod +x *
	./locator.sh

###PanoAl
elif [[ $TheLinuxChoice_Islem == "3" || $TheLinuxChoice_Islem == "03" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/PanoAl/
	chmod +x *
	./clipboardme.sh
	
###SesAl
elif [[ $TheLinuxChoice_Islem == "4" || $TheLinuxChoice_Islem == "04" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/SesAl/
	chmod +x *
	./sayhello.sh

###Pardon
elif [[ $TheLinuxChoice_Islem == "5" || $TheLinuxChoice_Islem == "05" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/Pardon/
	chmod +x *
	./excuseme.sh
	
###PrinterSpam
elif [[ $TheLinuxChoice_Islem == "6" || $TheLinuxChoice_Islem == "06" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/PrinterSpam/
	chmod +x *
	./helloprinter.sh

###KullaniciBul
elif [[ $TheLinuxChoice_Islem == "7" || $TheLinuxChoice_Islem == "07" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/KullaniciBul/
	chmod +x *
	./userrecon.sh

###SahteLogin
elif [[ $TheLinuxChoice_Islem == "8" || $TheLinuxChoice_Islem == "08" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/SahteLogin/
	chmod +x *
	./shellphish.sh

###LinkBackDoor
elif [[ $TheLinuxChoice_Islem == "9" || $TheLinuxChoice_Islem == "09" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/LinkBackDoor/
	chmod +x *
	./badlnk.sh

###SSHZorla
elif [[ $TheLinuxChoice_Islem == "10" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/SSHZorla/
	chmod +x *
	./fastssh.sh
	
###SMSBomb
elif [[ $TheLinuxChoice_Islem == "11" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/SMSBomb/
	chmod +x *
	python smsbomber.py

###PythonRAT
elif [[ $TheLinuxChoice_Islem == "12" ]]; then
	printf "\n"
	sleep 0.5
	cd TheLinuxChoice/PythonRAT/
	chmod +x *
	./install.sh
	./pyrat.sh

###Geri
elif [[ $TheLinuxChoice_Islem == "99" || $TheLinuxChoice_Islem == "99" ]]; then
	Ana_Menu

else
	HataliIslem
	TheLinuxChoice

fi
}

##BruteForce
BruteForce() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ BruteForce ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$sari BruteDum$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' BruteForce_Islem

###BruteDum
if [[ $BruteForce_Islem == "1" || $BruteForce_Islem == "01" ]]; then
	printf "\n"
	sleep 0.5
	cd BruteForce/BruteDum/
	chmod +x *
	python brutedum.py

###Geri
elif [[ $BruteForce_Islem  == 99 ]]; then
	Ana_Menu

else
	HataliIslem
	BruteForce

fi
}

##Botnet
Botnet() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ Botnet ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$sari Bomb-Botnet$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$sari Hibernet$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' Botnet_Islem

###Bomb-Botnet
if [[ $Botnet_Islem == "1" || $Botnet_Islem == "01" ]]; then
	printf "\n"
	sleep 0.5
	cd Botnet/Bomb-Botnet/
	chmod +x *
	python Bomb-Botnet.py

###Hibernet
elif [[ $Botnet_Islem == "2" || $Botnet_Islem == "02" ]]; then
	printf "\n"
	sleep 0.5
	cd Botnet/Hibernet/
	chmod +x *
	python HiberProxy.py
	python HiberSOCKS.py
	python HibernetV2.2.py

###Geri
elif [[ $Botnet_Islem  == 99 ]]; then
	Ana_Menu

else
	HataliIslem
	Botnet

fi
}

##Other
Other() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ Other ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$sari EasySploit$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$sari hacktronian$renkreset\n"
	printf "$yesil[$renkreset$beyaz 03 $renkreset$yesil]$sari FudPayload$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' Other_Islem

###EasySploit
if [[ $Other_Islem == "1" || $Other_Islem == "01" ]]; then
	printf "\n"
	sleep 0.5
	cd Other/EasySploit/
	chmod +x *
	./installer.sh
	./easysploit
	
###hacktronian
elif [[ $Other_Islem == "2" || $Other_Islem == "02" ]]; then
	printf "\n"
	sleep 0.5
	cd Other/hacktronian/
	chmod +x *
	./installer.sh
	python hacktronian.py

###FudPayload
elif [[ $Other_Islem == "3" || $Other_Islem == "03" ]]; then
	printf "\n"
	sleep 0.5
	cd Other/FudPayload/
	chmod +x *
	./zirikatu.sh

###Geri
elif [[ $Other_Islem  == 99 ]]; then
	Ana_Menu

else
	HataliIslem
	Other

fi
}

##Python
Python() {
	clear
	banner
		printf "$cyan"
		figlet -w 50 -c -f digital "~ Python ~" | pv -qL 75
		printf "$renkreset"
	printf "\n"
	printf "$yesil[$renkreset$beyaz 01 $renkreset$yesil]$sari KekikAkademi$renkreset\n"
	printf "$yesil[$renkreset$beyaz 02 $renkreset$yesil]$sari PCDunyasi_Python_Pro$renkreset\n"
	printf "$yesil[$renkreset$beyaz 03 $renkreset$yesil]$sari Python_Programlama$renkreset\n"
	printf "$yesil[$renkreset$beyaz 04 $renkreset$yesil]$sari ServerClient$renkreset\n"
	printf "$yesil[$renkreset$beyaz 05 $renkreset$yesil]$sari WebSiteTarayıcı$renkreset\n"
	printf "\n"
	printf "$sari[$renkreset$beyaz 99 $renkreset$sari]$renkreset$beyaz Geri$renkreset\n"
	printf "\n"
	read -p $'\e[1;92m[ * ] İşlem: \e[0m' Python_Islem

###KekikAkademi
if [[ $Python_Islem == "1" || $Python_Islem == "01" ]]; then
	printf "\n"
	sleep 0.5
	cd Python/
	chmod +x *
	ls
	pwd
	sleep 3
	python KekikAkademi.py

###PCDunyasi_Python_Pro
elif [[ $Python_Islem == "2" || $Python_Islem == "02" ]]; then
	printf "\n"
	sleep 0.5
	cd Python/PCDunyasi_Python_Pro/
	chmod +x *
	pwd
	ls

###Python_Programlama
elif [[ $Python_Islem == "3" || $Python_Islem == "03" ]]; then
	printf "\n"
	sleep 0.5
	cd Python/Python_Programlama/
	chmod +x *
	pwd
	ls

###ServerClient
elif [[ $Python_Islem == "4" || $Python_Islem == "04" ]]; then
	printf "\n"
	sleep 0.5
	cd Python/ServerClient/
	chmod +x *
	pwd
	ls

###WebSiteTarayıcı
elif [[ $Python_Islem == "5" || $Python_Islem == "05" ]]; then
	printf "\n"
	sleep 0.5
	cd Python/WebSiteTarayıcı/
	chmod +x *
	pwd
	ls

###Geri
elif [[ $Python_Islem  == 99 ]]; then
	Ana_Menu

else
	HataliIslem
	Python

fi
}

Ana_Menu