#!/usr/bin/env python

import socket
import urllib2
import re 

def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

def BingAllGrabber(s, numpages):
    lista = []
    page = 1
    while page <= numpages:
    #    try:
            bing = "http://www.bing.com/search?q="+s+"+&count=50&first="+str(page)
            openbing  = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
            #print findwebs
            for i in range(len(findwebs)):
                    allnoclean = findwebs[i]
                    findall1 = re.findall('http://(.*?)/', allnoclean)
                    for idx, item in enumerate(findall1):
                                    if 'www' not in item:
                                                    findall1[idx]  = 'http://www.' + item + '/'
                                    else:	
                                            findall1[idx]  = 'http://' + item + '/'
                    lista.extend(findall1)

            page = page + 50
     #   except:
      #      pass

    final =  unique(lista)
    return final

def Clean(s):
	domainlist = []
	for domain in domains:
		if 'http://' in domain:
			domain = domain.lstrip('http://')
		if domain[-1] == '/':
			domain = domain.rstrip('/')
		domainlist.append(domain)
	return domainlist


def GetIp(s):
	iplist = []
	for domain in s:
		try:
			ip = socket.gethostbyname(domain)
			iplist.append(ip)
		except socket.gaierror:
			pass
	iplist = unique(iplist)
	return iplist

if __name__ == '__main__':
        print('  ')
        print(' Instagram.com/murrez.sec ')
        print('  ')
        print('  WordPress Dork Scanner ')
        print('  ')		
	dork = raw_input('Enter Dork >>> ')
	dork = dork.replace(' ', '+')
	numpages = int(raw_input('Enter Number Pages >>> '))

	numpages = numpages * 50

	domains = BingAllGrabber(dork, numpages)
	print '[*] Grabbed %i Domains' % len(domains)

	# Extracting Websites Ips

	resp = raw_input('Would You Like To Save Grabbed Domains [Y/n] : ')
	if resp.lower() == 'y':
		wheretosave = raw_input('Where Would You Like To Save : ')
		savedomains = open(wheretosave, 'w')
		for domain in domains:
			savedomains.write(domain)
			if domain != domains[-1]:
				savedomains.write('\n')

	resp1 = raw_input('Would You Like To Grab IPs [Y/n] : ')

	if resp1.lower() == 'y':
		domains = Clean(domains)
		ips = GetIp(domains)
		print '[*] Grabbed %i IPs' % len(ips)
		resp3 = raw_input('Would You Like To Save Grabbed IPs [Y/n] : ')
		if resp3.lower() == 'y':
			wheretosave = raw_input('Where Would You Like To Save : ')
			saveips = open(wheretosave, 'w')
			for ip in ips:
				saveips.write(ip)
				if ip != ips[-1]:
					saveips.write('\n')
	else:
		exit()



