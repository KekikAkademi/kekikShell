#tutorial : https://www.youtube.com/watch?v=qdmmSM0bF5U&t=99s
#!/usr/bin/env python
#py -m pip install bs4
#py -m pip install requests
#Coded By : AfeezRenz
#http://www.instagram.com/_ezrenz
#http://www.facebook.com/r3xb0yz
#respectcoders
#majulah malaysiaku !!

import requests
import requests,re
from bs4 import BeautifulSoup
import time
import socket
import os
import sys
import string
from urllib import parse
#url

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print (" ")
print ("\t+------------------------------------------+\t")
print (" \t \t") 
print ("                    [ Dork Auto Find SQLI V2 ]                             ")
print ("                [ Author: AfeezRenz |  @_ezrenz ]                       ")
print ('              [   Example :   inurl:".asp?id=8"   ]                       ')
print (" \t \t")
print ("\t+------------------------------------------+\t")
print (" ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
dork=input('Dork:')
page=input('Total Pages: ')
file=input('File Output [Ex:result.txt] : ')
engine=input('Search Engine [google/bing]:')
payloader=input('Payload [ G For Google / B for Bing]: ')
print ('\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#searchengine
url='http://www.' + engine + '.com/search'
f= open(file, "w+")
#if google:search,else :search bing
if payloader.strip() in "g G".split():
	#payloadgoogle
	print ('[ $ ] Please Wait, Adding Some Coffee....')
	print ('\n')
	payload={'q':dork,'start':'0', 'num' : int(page)*10}
else:
	#payloadbing
	print ('[ $ ] Please Wait, Adding Some Coffee....')
	print ('\n')
	my_headers={'User-agent':'Mozilla/11.0'}
	payload={'q':dork,'first':'0', 'count' : int(page)*10+1}
	#startsearchbing
	r=requests.get(url,params=payload,headers=my_headers)
	soup=BeautifulSoup(r.text,'html.parser')
	litags=soup.find_all('h2')
	for linex in litags:
		line2=linex.find_all('a')
		for link in line2:
			result=link.get('href')
			print ('[ # ]   ' + parse.unquote(result))
			f.write(parse.unquote(result) + "\n")
#payloadgoogleasal={'q':dork,'start':'0', 'num' : int(page)}
#Setting User-Agent
my_headers={'User-agent':'Mozilla/11.0'}
#Get Data from search url
r=requests.get(url,params=payload,headers=my_headers)
#readalldataresult
soup=BeautifulSoup(r.text,'html.parser')
#get h3 tag with rclass
h3tags=soup.find_all('h3',class_='r')

#caripakai regex.
#If found : Print,else : exit
for h3 in h3tags:
	try:
		#startsearchgoogle
		res = (re.search('url\?q=(.+?)\&sa',h3.a['href']).group(1))
		print ('[ # ]   ' + parse.unquote(res))
		f.write(parse.unquote(res) + "\n")
	except:
		continue
f.close()
print ('\n')
print ('[ $ ] Saved In %s File' % (file))
print ('[ $ ] Search Finished on page %s using %s search' % (page,engine))
print ('[ $ ] Exit at %s' % time.strftime("%X"))
#habis
#print ('Search Doned In %' % int(calt))
#