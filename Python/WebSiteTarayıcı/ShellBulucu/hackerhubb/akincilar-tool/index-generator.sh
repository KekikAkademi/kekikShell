#!/bin/bash
 red=`echo -en "\e[31m"`
 green=`echo -en "\e[32m"`
 orange=`echo -en "\e[33m"`
 blue=`echo -en "\e[34m"`
 purple=`echo -en "\e[35m"`
 aqua=`echo -en "\e[36m"`
 gray=`echo -en "\e[37m"`
 darkgray=`echo -en "\e[90m"`
 lightred=`echo -en "\e[91m"`
 lightgreen=`echo -en "\e[92m"`
 lightyellow=`echo -en "\e[93m"`
 lightblue=`echo -en "\e[94m"`
 lightpurple=`echo -en "\e[95m"`
 lightaqua=`echo -en "\e[96m"`
 white=`echo -en "\e[97m"`
 default=`echo -en "\e[39m"`
 BLACK=`echo -en "\e[40m"`
 RED=`echo -en "\e[41m"`
 GREEN=`echo -en "\e[42m"`
 ORANGE=`echo -en "\e[43m"`
 BLUE=`echo -en "\e[44m"`
 PURPLE=`echo -en "\e[45m"`
 AQUA=`echo -en "\e[46m"`
 GRAY=`echo -en "\e[47m"`
 DARKGRAY=`echo -en "\e[100m"`
 LIGHTRED=`echo -en "\e[101m"`
 LIGHTGREEN=`echo -en "\e[102m"`
 LIGHTYELLOW=`echo -en "\e[103m"`
 LIGHTBLUE=`echo -en "\e[104m"`
 LIGHTPURPLE=`echo -en "\e[105m"`
 LIGHTAQUA=`echo -en "\e[106m"`
 WHITE=`echo -en "\e[107m"`
 DEFAULT=`echo -en "\e[49m"`
echo "${aqua}               INDEX GENERATOR V1 - POLATBEY"
echo "${purple}         Neden Boyle Birsey Yaptım Bilmiyorum amk"
echo "${red}                     Aşamaları Takip Edin."

echo ""
read -p "${green} 	</> Sayfa Baslık Ismı : " baslik

read -p "${green} 	</> Ismınız : " owend

read -p "${green} 	</> Forum Adresınız : " link

read -p "${green} 	</> Forum Hakkında Bilgi (Hâck Form vb.) : " formbilgi

read -p "${green} 	</> Mail Adresin : " mail

read -p "${green} 	</> Meta (description,keyword,author ornek. Hacked Ali) : " ornekali

read -p "${green}   </>     Youtube Sarkı ( 9_-5GpNTMW1 kısmı ) :" yt

read -p "${green} 	</> Street 1. : " dost

read -p "${green} 	</> Street 2. : " dost1

read -p "${green} 	</> Street 3. : " dost2

read -p "${green} 	</> Hangi Tasarımı Seciyorsun 1 - 2 - 3 : " ch

sleep 1

echo "\n\n	${green}[+] Deface Page Olusturuluyor"

sleep 1

case "$ch" in
1) echo "	[+] Sayfa Tasarımı Yapılıyor"
sleep 1

	

cat >deface.html <<EOF
<html> 
<head> 
<title>$baslik</title> 
  <meta name="description" content="$ornekali">
  <meta name="keyword" content="$ornekali">
  <meta name="author" content="$ornekali">
<link href="http://fonts.googleapis.com/css?family=Iceland" rel="stylesheet" type="text/css"></script>
</head>
<body oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;" style="background-image: url(''); background-repeat: repeat; background-position: center; background-attachment: fixed;" bgcolor="black">
<center><h1><font size="7" face="Iceland" color="white"><b><font size="3" color=white> ≺/≻ </font><font color=#ffff00>$owend</font> <font size="3"color=white> ≺/≻ </font></font></font></h1>
<img src="https://i.ebayimg.com/images/g/ZDcAAOSwkNFcdxqj/s-l300.jpg" style="width:350px;height:300px;"> </center>
 <center><font size="6" face="Iceland" color="grey"><br>#0W3ND <font color=#ffff00>$owend</font><br> <center><font size="6" face="Iceland" color="white">$forum <font color=grey>$formbilgi</font><center><font size="4" face="Iceland" color="red">#Email : <font color=grey>$mail</font><br> <center>
<div id=bar style="position: fixed; width: 100%; bottom: 0px; font-family: TSa height: 20px; color: white; font-size: 13px; left: 0px; border-top: 1px solid #000; padding: 5px; background-color: #000"> 
<CENTEr><a href="https://wm4code.org/" style="color: white;">$dost &#9679; $dost2 &#9679; $dost3 &#9679; #$owend </CENTER></div>
<iframe width="1" height="1" src="https://www.youtube.com/embed/$yt?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen=""></iframe>

</html>
EOF
# Dosya olusturma kısmı
sleep 1
echo "	[+] Deface Page Olusturuluyor"
sleep 1
echo "\n	Deface-Page-Generator Kullandıgınız Icın EYW - Ctrl c cek"
sleep 5
firefox deface1.html
	;;



2)
echo "	[+] Sayfa Tasarımı Yapılıyor"	
sleep 1
cat >deface2.html <<EOF
<!DOCTYPE html>
<html><head>
<script type='text/javascript'>
//<![CDATA[
msg = "$baslik";
msg = "" + msg;pos = 0;
function scrollMSG()
{document.title = msg.substring(pos, msg.length) + msg.substring(0, pos); pos++;
if (pos > msg.length) pos = 0
window.setTimeout("scrollMSG()",150);}
scrollMSG();
//]]>
</script>
<link rel="shortcut icon" href=""><link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"><script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
  <meta name="description" content="$ornekali">
  <meta name="keyword" content="$ornekali">
  <meta name="author" content="$ornekali">
<link href="https://fonts.googleapis.com/css?family=Dosis:200" rel="stylesheet">
</head><body oncontextmenu="return false;" onkeydown="return false;" onmousedown="return false;">
<script type="text/javascript">
function clickIE() {if (document.all) {(message);return false;}}
function clickNS(e) {if
(document.layers||(document.getElementById&&!document.all)) {
if (e.which==2||e.which==3) {(message);return false;}}}
if (document.layers)
{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}
document.oncontextmenu=new Function("return false")
</script>
<style>
/* width */
::-webkit-scrollbar {
  width: 15px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #000000;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #FF0000;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #FF0000;
}
</style>
<style type="text/css">
body {
background-color:#000000;
   -webkit-background-size: 100% 100%;
   -moz-background-size: 100% 100%;
   -o-background-size: 100% 100%;
   background-size: 100% 100%;
   margin: 0px auto;
}
</style>


<style>
body {
    background-image: url("https://66.media.tumblr.com/4f813ac81466fc48413132dfb0f105cb/tumblr_pmd6e6Ol7y1runoqyo5_r1_500.gif");

background-size: cover;
</style>
<br><br><br><center><img src="https://www.resimag.com/p1/d745bd31d83.png" border="" width="250px" height=""</center>
<center><b><p><font face="Dosis" size="10" color="red">Hacked By $owend</font></p></b></center>
<br>
<center><b><p><font face="Dosis" size="5" color="gold">$link ~ $formbilgi</font></p></b></center>
<br>
<center><b><p><font face="Dosis" size="4" color="white">Greetz To : $dost | $dost1 | $dost2 /font></p></b></center>
 <footer>
 <br>
 <a href="https://$link" link="red" alink="red" vlink="red" color="red">$owend</a>
 <br>
<center><div style="background:url(https://i.hizliresim.com/Lb5boG.gif) repeat; width: 300px; height: 20px;" class="style31"><b><p><font face="Dosis" size="3" color="red">Copyright © ∞ 2019 - $owend</font></p></b></center></div>
<br>
</center></body></html>
<iframe width="1" height="1" src="https://www.youtube.com/embed/$yt?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen=""></iframe>
<div style = "display: none;">?>

EOF
sleep 1
echo "	[+] Deface Page Sorunsuz Olusturuldu"
sleep 1
echo "\n	Deface-Page-Generator Kullandıgınız Icın EYW - Ctrl c cek"
sleep 5
firefox deface2.html
	;;
3) echo "	[+] Sayfa Tasarımı Yapılıyor"	
sleep 1
cat >deface3.html <<EOF
<html>
<title>$baslik</title>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="description" content="test">
  <meta name="keyword" content="test">
  <meta name="author" content="test">

<link rel="shortcut icon" href="http://i.hizliresim.com/52EbZD.png">

<style>

* { margin: 0; padding: 0; }

html {

background: url(http://i.hizliresim.com/a08mkg.jpg) no-repeat center center fixed;

-webkit-background-size: cover;

-moz-background-size: cover;

-o-background-size: cover;

background-size: cover;

</style>

</br>

</br>

<center><img src="https://i.hizliresim.com/rOyQ93.gif" width="300" height="250"></a></center>

</br>

<center><img src="http://i.hizliresim.com/WE8mBP.png" width="757" height="7"></center>

</br>

<center><b><font size="10" face="Aldrich" color="#000000">HACKED BY $owend</font></b></center>
<center><img src="http://i.hizliresim.com/WE8mBP.png" width="757" height="7"></center>

</br>

<center><img src="http://i.hizliresim.com/WE8mBP.png" width="100" height="5">&nbsp;&nbsp;<b><font size="4" face="Aldrich">$link &#9679 $formbilgi</font></b>&nbsp;&nbsp;<img src="http://i.hizliresim.com/WE8mBP.png" width="100" height="5"></center>
<center><img src="http://i.hizliresim.com/WE8mBP.png" width="100" height="5">&nbsp;&nbsp;<b><font size="4" face="Aldrich">$dost &#9679; $dost2 &#9679; $dost3</font></b>&nbsp;&nbsp;<img src="http://i.hizliresim.com/WE8mBP.png" width="100" height="5"></center>

</br>

</br>

<center><img src="https://i.hizliresim.com/VMRvVZ.png" width="100" height="100"></center>  

<body oncontextmenu="return false" onselectstart="return false" ondragstart="return false"></body>

<link href='https://fonts.googleapis.com/css?family=Aldrich' rel='stylesheet' type='text/css'>

<script language="javascript" src="http://is.sitekodlari.com/sagtusengelleme1.js"></script>

<body oncontextmenu="return false" onselectstart="return false" ondragstart="return false"></body> 

<script type="text/javascript"> 

//form tags to omit in NS6+: 

var omitformtags=["input", "textarea", "select"] 

omitformtags=omitformtags.join("|") 

function disableselect(e){ 

if (omitformtags.indexOf(e.target.tagName.toLowerCase())==-1) 

return false 

} 


function reEnable(){ 

return true 

} 



if (typeof document.onselectstart!="undefined") 

document.onselectstart=new Function ("return false") 

else{ 

document.onmousedown=disableselect 

document.onmouseup=reEnable 

} 

</script> 

<iframe width="0" height="0" src="https://www.youtube-nocookie.com/embed/$yt?&amp;autoplay=1 " frameborder="0" allowfullscreen>

<body onkeydown="return false">                

</html>
EOF
# File Written Successfully
sleep 1
echo "	[+] Deface Page Sorunsuz Olusturuldu !"
sleep 1
echo "\n	Deface-Page-Generator Kullandıgınız Icın EYW - Ctrl c cek"
sleep 5
echo "\n\n"
firefox deface3.html

	;;
*) echo "	[-] Bir Hata Olustu ! "
	;;

esac

exit
