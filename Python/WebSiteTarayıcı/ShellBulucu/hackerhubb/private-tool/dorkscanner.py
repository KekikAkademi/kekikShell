#!/usr/bin/python

import urllib2
import re

def unique(seq):
  seen = set()
  return [seen.add(x) or x for x in seq if x not in seen]

def bing_joomla_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + s + "+index.php?option=com&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                jmnoclean = findwebs[i]
                findjm = re.findall('(.*?)index.php', jmnoclean)
                lista.extend(findjm)
            page += 50
        except:
            pass

    final = unique(lista)
    return final


def bing_wordpress_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + s + "+?page_id=&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                wpnoclean = findwebs[i]
                findwp = re.findall('(.*?)\?page_id=', wpnoclean)
                lista.extend(findwp)

            page += 50
        except:
            pass
    final = unique(lista)
    return final

def main():
	jms = []
	wps = []
	print ('  ')
	print (' Joomla , WordPress Dork Scanner ')
	print ('  ')
	print ('     instagram.com/murrez.sec ')
	print ('  ')
	print ('  ')	
	ipsfile = raw_input(' Dork List :  ')
	ips = open(ipsfile, 'r').read().split()
	for ip in ips :
		jms.extend(bing_joomla_grabber(ip))
		wps.extend(bing_wordpress_grabber(ip))

	jmfile = open('joomla.txt', 'a')
	wpfile = open('wordpress.txt', 'a')

	for jm in jms :
		jmfile.write(jm)
		jmfile.write('\n')

	for wp in wps :
		wpfile.write(wp)
		wpfile.write('\n')

	jmfile.close()
	wpfile.close()

if __name__ == '__main__' :
	main()