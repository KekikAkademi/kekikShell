"""

wifi adaptorunuzu monitor moda ve managed moda alma işlemini hızlandırmak için
yazdıgım basit tool eklenmesini istediginiz bişey varsa yorumlarda belirtirseniz sevinirim.

"""

import os
red = ("\033[31m")
colorRest = ("\033[0m")
def monitor(adName=""):
    os.system(f"ifconfig {adName} down")
    os.system(f"airmon-ng start {adName}")
    os.system(f"ifconfig {adName}mon up")
    os.system(f'iwconfig {adName}mon | grep "Mode"')
def disableMonitor(adName=""):
    os.system(f"ifconfig {adName}mon down")
    os.system(f"airmon-ng stop {adName}mon")
    os.system(f"ifconfig {adName} up")
    os.system(f'iwconfig {adName} | grep "Mode"')
def aygıtlar():
    os.system("ifconfig | grep wlan")



aygıtlar()
adNameWrite = input(red+"adaptor name:"+colorRest)
monitor(adName=adNameWrite)
kapat = input(red+"monitor modu kapatmak için  E/H:"+colorRest)
if kapat == "E" or kapat == "e":
    disableMonitor(adName=adNameWrite)
elif kapat == "H" or kapat == "h":
    print("kapatmak işlemi iptal edildi.")
else:
    print("geçersiz işlem.")