import requests
import re
import io
import os
import string
#------------------------sqlerr.txt------------------------------
file = io.open('sqlerr.txt' , 'r')
err_list = file.readlines()
file.close()
print(' ______________________________________')
print('|                                      |')
print('|  Parser dork from                    |')
print('|      _                               |')
print('|     |_) o ._   _     _  _  ._ _      |')
print('|     |_) | | | (_| o (_ (_) | | |     |')
print('|                _|                    |')
print('|                                      |')
print('|                v.2.1                 |')
print('|                           famgor(c)  |')
print('|______________________________________|')
print
#--------------------------------------------------------------
file = io.open('url_pars.txt', 'w')
file.close()
#------------------Dorks list----------------------------------
dorks = io.open('dorks.txt' , 'r', encoding='utf8')
dorks_list = dorks.readlines()
dorks.close()
#--------------------------------------------------------------
pages = int(input('Sayfanin giris sayisi : '))*10
print('Dork Sayisi : '+str(len(dorks_list)))
for i in range(len(dorks_list)):
    search = dorks_list[i].strip()
    count = 1
    while (count < pages):
        req = ('http://www.bing.com/search?q=' + search + '&first='+str(count))
        try:	
            response = requests.get(req)
        except:
            print('Error get bing.com')
        req = ''	
        try:
            link = re.findall('<h2><a href="(.+?)"', response.text, re.DOTALL)
            for i in range(len(link)):
                print(link[i])
                if link[i].find('http://bs.yandex.ru'):
                    open('url_pars.txt', 'a+').write(link[i] +'\'' + '\n')
        except:
            print('Error parsing url')
        count = count+10
#---------------------Delete duplicates-------------------------
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]
print('Removing duplicates...')
input = io.open('url_pars.txt', 'r')
output = io.open('url.txt', 'w')
linesarray = input.readlines()
input.close()
seen = []
seen = f7(linesarray)
for i in range(len(seen)):
    output.write(seen[i])
os.remove('url_pars.txt')
output.close()
print('Complete')
print('Checking error...')
#-------------------------url.txt--------------------------------
file = io.open('url.txt' , 'r')
url_list = file.readlines()
file.close()
#------------------------Proverka--------------------------------
err_page = 0
good_page = 0
for i in range(len(url_list)):
    page = url_list[i].strip()
    try:
        response = requests.get(page)
    except:
        err_page = err_page+1
        print('Error while get page.')
    for i in range(len(err_list)):
        err = str(err_list[i])
        err = err.strip()			
        if response.text.find(err)>0:
            print('FIND "'+err+'" in '+page)
            io.open('good.txt', 'a+').write(page + '\n')
            good_page = good_page + 1
        else:
            pass
#-------------------------------------------------------------------
print('Good pages: '+str(good_page))
print('404,403 pages: '+str(err_page))
print('Complete. Press any key...')
