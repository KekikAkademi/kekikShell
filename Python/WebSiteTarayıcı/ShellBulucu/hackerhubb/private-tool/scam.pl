#!/usr/bin/perl
# M-A_labz
# Modules
use HTTP::Request;
use strict;
use Win32::Console::ANSI;
use warnings;
use LWP::Simple;
use Term::ANSIColor;
if($^O =~ /Win/){
 
   system("cls");
   system("title Mass Scripts Grabber 0.1");
}else{
   system("clear");
}
$|=1;
print color("red"), '
 ____________________________________________________________________
|                                                                    |
|               Mass Scripts Grabber (bing supported)                |
|                          By Mr_AnarShi-T                           |
|                                                      v 0.1         |
|____________________________________________________________________|
';
print color 'reset';

        print color("yellow"), "\n\n[+] Enter List File Ips  : ";
                                print color 'reset';
        my $host=<STDIN>;
        chomp($host);
        open (SITE, "<$host") || die "[-] Can't open the List of site file !";
        my @SITE = <SITE>;
        close SITE;
        foreach my $xp (@SITE) {
        chomp $xp;
        my $ip = $xp;
        chomp ($ip);
        my %group;


        if ( $ip !~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/ ) {
                print color("bold white"), "# Skiping $ip\n";
                                print color 'reset';

        }

        my $page = 0;
		print color("green"), "Working on $ip\n";
		print color 'reset';
        print color("bold white"), "[#] Begin Reserving !";
        print color 'reset';
        while (1) {

                my $content = get("http://www.bing.com/search?q=ip:$ip&first=$page&FORM=PERE") or

die("Error getting output\n");
                my $status = keys %group;
                while ( $content =~ /<cite>[:\/\/]*([\w\.\-]+)[\w+\/\.\-_:\?=]*<\/cite>/g) {
                        $group{$1} = undef;
                }
                last if ($status == keys %group);
                $page = $page + 10;
        }

        print color("bold white"),  "\n# OUTPUT for $ip\n";
                print color 'reset';
        open (IN,">reverse-$ip.txt");
        foreach my $host (keys %group) {
        print IN "$host\n";
        }
        close(IN);

open (F, "<reverse-$ip.txt") || die "[-] Can't open the List Of Domains Names!";
my @DOMAINS = <F>;
close F;
foreach my $D (@DOMAINS) {
chomp $D;

# Wordpress Grabbing !!

my $wp = "http://".$D."/wp-login.php/";
my $reqwp=HTTP::Request->new(GET=>$wp);
my $uawp=LWP::UserAgent->new();
$uawp->timeout(0);
my $responsewp=$uawp->request($reqwp);

my $wp2 = "http://".$D."/wp/wp-login.php/";
my $sitewp2 = "http://".$D."/wp/";
my $reqwp2=HTTP::Request->new(GET=>$wp2);
my $uawp2=LWP::UserAgent->new();
$uawp2->timeout(0);
my $responsewp2=$uawp2->request($reqwp2);

my $wp1 = "http://".$D."/cms/wp-login.php/";
my $sitewp1 = "http://".$D."/cms/";
my $reqwp1=HTTP::Request->new(GET=>$wp1);
my $uawp1=LWP::UserAgent->new();
$uawp1->timeout(0);
my $responsewp1=$uawp1->request($reqwp1);

my $wp3 = "http://".$D."/portal/wp-login.php/";
my $sitewp3 = "http://".$D."/portal/";
my $reqwp3=HTTP::Request->new(GET=>$wp3);
my $uawp3=LWP::UserAgent->new();
$uawp3->timeout(0);
my $responsewp3=$uawp3->request($reqwp3);

# Joomla Grabbing !!

my $joom = "http://".$D."/administrator/";
my $reqjoom=HTTP::Request->new(GET=>$joom);
my $uajoom=LWP::UserAgent->new();
$uajoom->timeout(0);
my $responsejoom=$uajoom->request($reqjoom);

my $joom2 = "http://".$D."/joomla/administrator/";
my $site2 = "http://".$D."/jooma/";
my $reqjoom2=HTTP::Request->new(GET=>$joom2);
my $uajoom2=LWP::UserAgent->new();
$uajoom2->timeout(0);
my $responsejoom2=$uajoom2->request($reqjoom2);

my $joom1 = "http://".$D."/cms/administrator/";
my $site1 = "http://".$D."/cms/";
my $reqjoom1=HTTP::Request->new(GET=>$joom1);
my $uajoom1=LWP::UserAgent->new();
$uajoom1->timeout(0);
my $responsejoom1=$uajoom1->request($reqjoom1);

my $joom3 = "http://".$D."/portal/administrator/";
my $site3 = "http://".$D."/portal/";
my $reqjoom3=HTTP::Request->new(GET=>$joom3);
my $uajoom3=LWP::UserAgent->new();
$uajoom3->timeout(0);
my $responsejoom3=$uajoom3->request($reqjoom3);

# Vbulletin Grabbing !!

my $vb1 = "http://".$D."/vb/clientscript/vbulletin_global.js";
my $sitevb1 = "http://".$D."/core/";
my $reqvb1=HTTP::Request->new(GET=>$vb1);
my $uavb1=LWP::UserAgent->new();
$uavb1->timeout(0);
my $responsevb1=$uavb1->request($reqvb1);

my $vb2 = "http://".$D."/clientscript/vbulletin_global.js";
my $sitevb2 = "http://".$D."/";
my $reqvb2=HTTP::Request->new(GET=>$vb2);
my $uavb2=LWP::UserAgent->new();
$uavb2->timeout(0);
my $responsevb2=$uavb2->request($reqvb2);

my $vb3 = "http://".$D."/cc/clientscript/vbulletin_global.js";
my $sitevb3 = "http://".$D."/";
my $reqvb3=HTTP::Request->new(GET=>$vb3);
my $uavb3=LWP::UserAgent->new();
$uavb3->timeout(0);
my $responsevb3=$uavb3->request($reqvb3);

# whmcs grabbing !!

my $whm = "http://".$D."/clients/includes/jscript/jquery.js";
my $sitewhm = "http://".$D."/clients/";
my $reqwhm=HTTP::Request->new(GET=>$whm);
my $uawhm=LWP::UserAgent->new();
$uawhm->timeout(0);
my $responsewhm=$uawhm->request($reqwhm);

my $whm2 = "http://".$D."/whmcs/includes/jscript/jquery.js";
my $sitewhm2 = "http://".$D."/whmcs/";
my $reqwhm2=HTTP::Request->new(GET=>$whm2);
my $uawhm2=LWP::UserAgent->new();
$uawhm2->timeout(0);
my $responsewhm2=$uawhm2->request($reqwhm2);

my $whm3 = "http://".$D."/billing/includes/jscript/jquery.js";
my $sitewhm3 = "http://".$D."/billing";
my $reqwhm3=HTTP::Request->new(GET=>$whm3);
my $uawhm3=LWP::UserAgent->new();
$uawhm3->timeout(0);
my $responsewhm3=$uawhm3->request($reqwhm3);

my $whm4 = "http://".$D."/support/includes/jscript/jquery.js";
my $sitewhm4 = "http://".$D."/support/";
my $reqwhm4=HTTP::Request->new(GET=>$whm4);
my $uawhm4=LWP::UserAgent->new();
$uawhm4->timeout(0);
my $responsewhm4=$uawhm4->request($reqwhm4);

# Zen Cart grabbing !!

my $zen = "http://".$D."/store/admin/login.php?zenAdminID";
my $sitezen = "http://".$D."/";
my $reqzen=HTTP::Request->new(GET=>$zen);
my $uazen=LWP::UserAgent->new();
$uazen->timeout(0);
my $responsezen=$uazen->request($reqzen);

my $zen2 = "http://".$D."/admin/login.php?zenAdminID";
my $sitezen2 = "http://".$D."/";
my $reqzen2=HTTP::Request->new(GET=>$zen2);
my $uazen2=LWP::UserAgent->new();
$uazen2->timeout(0);
my $responsezen2=$uazen2->request($reqzen2);

my $zen3 = "http://".$D."/products/admin/login.php?zenAdminID";
my $sitezen3  = "http://".$D."/";
my $reqzen3 =HTTP::Request->new(GET=>$zen3);
my $uazen3 =LWP::UserAgent->new();
$uazen3 ->timeout(0);
my $responsezen3 =$uazen3 ->request($reqzen3 );

my $zen4 = "http://".$D."/shop/admin/login.php?zenAdminID";
my $sitezen4  = "http://".$D."/";
my $reqzen4 =HTTP::Request->new(GET=>$zen4 );
my $uazen4 =LWP::UserAgent->new();
$uazen4 ->timeout(0);
my $responsezen4 =$uazen4 ->request($reqzen4 );
###############################################################################################
# Checking Wordpress Websites !!
if ($responsewp->content=~ /<body class="login">/){print color("green"), "[+] $D :[WordPress]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$D is wordpress\n";
close(TN);
}
else {if ($responsewp1->content=~ /<body class="login">/){print color("green"), "[+] $D :[WordPress]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site1 is wordpress\n";
close(TN);
}
else{ if ($responsewp2->content=~ /<body class="login">/){print color("green"), "[+] $D :[WordPress]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site2 is wordpress\n";
close(TN);
}
else{ if ($responsewp3->content=~ /<body class="login">/){print color("green"), "[+] $D :[WordPress]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site3 is wordpress\n";
close(TN);
}

# Checking Joomla Websites !!

if ($responsejoom->content=~ /Joomla!/){print color("green"), "[+] $D :[Joomla]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$D is joomla\n";
close(TN);
}
else {if ($responsejoom1->content=~ /Joomla!/){print color("green"), "[+] $D :[Joomla]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site1 is joomla\n";
close(TN);
}
else{ if ($responsejoom2->content=~ /Joomla!/){print color("green"), "[+] $D :[Joomla]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site2 is joomla\n";
close(TN);
}
else{ if ($responsejoom3->content=~ /Joomla!/){print color("green"), "[+] $D :[Joomla]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site3 is joomla\n";
close(TN);
}

# Vbulletin Checking Websites !!

else{ if ($responsevb1->is_success && $responsevb1->content=~/!window.console/){print color("green"), "[+] $D :[Vbulttein]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site3 is vb\n";
close(TN);
}
else{ if ($responsevb2->is_success && $responsevb1->content=~/!window.console/){print color("green"), "[+] $D :[Vbulttein]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site3 is vb\n";
close(TN);
}
else{ if ($responsevb3->is_success && $responsevb1->content=~/!window.console/){print color("green"), "[+] $D :[Vbulttein]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$site3 is vb\n";
close(TN);
}

# Checking Whmcs Websites !!

else{ if ($responsewhm->is_success && $responsewhm->content=~/jQuery/){print color("green"), "[+] $D:[Whmcs]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitewhm is whmcs\n";
close(TN);
}
else{ if ($responsewhm2->is_success && $responsewhm2->content=~/jQuery/){print color("green"), "[+] $D :[Whmcs]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitewhm2 is whmcs\n";
close(TN);
}
else{ if ($responsewhm3->is_success && $responsewhm3->content=~/jQuery/){print color("green"), "[+] $D :[Whmcs]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitewhm3 is whmcs\n";
close(TN);
}
else{ if ($responsewhm4->is_success && $responsewhm4->content=~/jQuery/){print color("green"), "[+] $D :[Whmcs]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitewhm4 is whmcs\n";
close(TN);
}

# Checking Zen Cart Websites

else{ if ($responsezen->is_success && $responsezen->content=~/zenAdminID/){print color("green"), "[+] $D :[Zen Cart]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitezen is Zen Cart\n";
close(TN);
}
else{ if ($responsezen2->is_success && $responsezen2->content=~/zenAdminID/){print color("green"), "[+] $D :[Zen Cart]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitezen2 is Zen Cart\n";
close(TN);
}
else{ if ($responsezen3->is_success && $responsezen3->content=~/zenAdminID/){print color("green"), "[+] $D :[Zen Cart]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitezen3 is Zen Cart\n";
close(TN);
}
else{ if ($responsezen4->is_success && $responsezen4->content=~/zenAdminID/){print color("green"), "[+] $D :[Zen Cart]\n";
print color 'reset';
open(TN,">>$ip-scripts.txt");
print TN "$sitezen4 is Zen Cart\n";
close(TN);
}
else {
print color("bold white"), "[-] $D :[Unknown] \n";
print color 'reset';
}}}}}}}}}}}}}}}}}}}}