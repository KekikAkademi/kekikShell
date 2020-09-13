from urllib import urlopen as o
import sys 
from termcolor import colored, cprint 

print u"  "
print u"\u001b[35m Priv8 Web Server Scanner Exploit \u001b[35m"
print u" "
print u"\u001b[32m Created Murrez \u001b[32m"
print u"  "
print u" \u001b[33mInstagram : murrez.sec \u001b[37m"
print u"  "
lists = open(raw_input(' Site List : '), 'r').read().split('\n')
for ip in lists:
    print u'\u001b[31m [+] Vuln Success -> ', ip
    grab = 'null'
    try:
        grab = o('https://api.hackertarget.com/reverseiplookup/?q=' + ip).read()
    except:
        continue
    if 'error check' in grab:
        print 'Check ip format in input file'
        continue
    if 'No records' in grab:
        print 'No reverse IP record available'
        continue
    grab = grab.split('\n')
    for domain in grab:
        open('vulnlist.txt', 'a+').write(domain + '\n')
