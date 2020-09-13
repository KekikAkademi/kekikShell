#!/usr/bin/perl 
# FCKeditor Grabber , Coded by CrashBandicot FUck ALl Haters , Noob , Lamers , Nationalist , Zionist , Leecher
# Fuck All Noobs Copying my script :3
# Gr33tz All Staff Exploit4arab , M-A , xmjhad , danzo & all friend
# FUcking Serveur .il
# This Beta

use HTTP::Request;
use LWP::Simple;
use LWP::UserAgent;


if ($^O =~ /MSWin32/) {system("cls"); system("color a");
}else { system("clear"); }
print "\n\t                          FCKeditor Grabber\n";
print "\t                        result in connector.txt";
print "\n\t                   .Usage : perl $0  list.txt.\n\n";

open(tarrget,"<$ARGV[0]") or die "$!";
while(<tarrget>){
chomp($_); 
$target = $_;
if($target !~ /http:\/\//)
{
$target = "http://$target";
}
$websss = $target."FCKeditor/editor/filemanager/connectors/asp/";
$website = $target."FCKeditor/editor/filemanager/connectors/asp/connector.asp";
$nigga = "$target/FCKeditor/editor/filemanager/browser/default/browser.html?connector=$website";
$req=HTTP::Request->new(GET=>$websss);
$ua=LWP::UserAgent->new();
$ua->timeout(30);
$response=$ua->request($req);
if($response->status_line=~ /403/ )

 {
print "\n[+]$target => FCK & Connector Detected \n";
open (TEXT, '>>connector.txt');
print TEXT "=================\n$nigga\n";
close (TEXT);
}
else{
print "\n[+]$target => Try Other Path of FCK...\n";
$wbs1 = $target."FCKeditor/editor/filemanager/browser/default/connectors/asp/";
$fuckaa = "$target/FCKeditor/editor/filemanager/browser/default/browser.html?connector=connectors/asp/connector.asp";
$reqq=HTTP::Request->new(GET=>$wbs1);
$uaa=LWP::UserAgent->new();
$uaa->timeout(30);
$responsee=$uaa->request($reqq);
if($responsee->status_line=~ /403/  ) {  

print "\n[+]$target => Path 2: FCK & Connector Detected \n";
open (TEXTt, '>>connector.txt');
print TEXTt "=================\n$fuckaa\n";
close (TEXTt);


	}else { print "\n [+]$target => 404 Not Found\n";}


}
}