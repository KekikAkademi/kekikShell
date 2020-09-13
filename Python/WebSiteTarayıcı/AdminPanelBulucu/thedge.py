#!/usr/bin/python3
# Code by PosiX

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from queue import Queue, Empty
import threading
import argparse
import time, datetime
import sys

found = []
error = []
user_agent = "Mozilla/5.0 (Macintosh; U; U; PPC Mac OS X 10_6_7 rv:6.0; en-US) AppleWebKit/532.23.3 (KHTML, like Gecko) Version/4.0.2 Safari/532.23.3"

class ThreadScan(threading.Thread):
    """ thread untuk admin page """
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """ check jika admin page ada """
        while True:
            try:
                try:
                    site = self.queue.get(False)
                except Empty:
                    break
                try:
                    req = Request(site, headers={"User-Agent": user_agent})
                    connection = urlopen(req)
                    found.append(site)
                    self.queue.task_done()
                    # jika tugas selesai rilis status
                        
                except HTTPError:
                    error.append(site)
                    #print("\033[91m[-]\033[0m", site)
                    self.queue.task_done()
                except Exception as e:
                    self.queue.task_done()
            except KeyboardInterrupt as e:
                print("\n\033[36m[?] \033[0mCTRL+C Detected...")
                
def admin_scan():
    """
    buat antrian dan rangkaian
    untuk memindai admin page
    """
    # parsing command line
    parser = argparse.ArgumentParser(description="TheEdge a admin page scan with multi-threading")
    parser.add_argument("-u", "--url", dest="url", help="url target scan")
    parser.add_argument("-t", "--thread", dest="thread", help="thread max 20")
    
    args = parser.parse_args()
    if not args.url:
        sys.exit("\033[97merror argument: your usage this a tool with argument\npython TheEdge.py --help")
    if not args.thread:
        sys.exit("\033[97merror argument: your usage this a tool with argument\npython TheEdge.py --help")
        
    # handle url site
    site = args.url
    if not site.startswith("http://"):
        site = "http://"+site
    if not site.endswith("/"):
        site = site+"/"
        
    numb_thread = args.thread
    if not numb_thread:
        numb_thread = 20
    else:
        pass
    # baca file
    try:
        f = open("jembod.txt", "r")
        path = f.readlines()
    except FileNotFoundError as e:
        print("\033[91mFile not found!")
    finally:
        try:
            f.close()
        except:
            print("\033[91mCan\'t close file!")
                
    now = datetime.datetime.now()
    print ("\033[97m[\033[96m>\033[97m] Starting at \033[93m" +str (now.hour) +":" +str (now.minute) +":" + str (now.second))
    time.sleep(2)
    print("\033[97m[\033[96m>\033[97m] Wordlist total \033[93m"+ str(len(path)), "\n")
    
    queue = Queue()
    threadList = []
    for line in path:
        # hapus \n diakhir baris
        line = line.replace("\n", "")
        link = site+line
        queue.put(link)
    for i in range(0, int(numb_thread)):
        thread = ThreadScan(queue)
        threadList.append(thread)
        #thread.setDaemon(True)
        thread.start()
    # menunggu thread semuanya selesai
    queue.join()

def progress_bar(total, progress):
    """
    Original Source: https://stackoverflow.com/a/15860757/1391441
    """
    
    barLength, status = 25, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r\033[97m[\033[96m>\033[97m] Processed: \033[91m[\033[97m{}\033[91m] \033[93m{:.0f}% {}".format( "#" * block + "-" * (barLength - block), round(progress * 100, 0), status)
    sys.stdout.write(text)
    sys.stdout.flush()
    
def result():
    """
    hasil scan
    if: not found
    else: found
    """
    # ambil result dari error eksekusi with progressbar
    runs = len(error)
    save = open("result.txt", "w+")
    for run_num in range(runs):
        time.sleep(0.1)
        progress_bar(runs, run_num + 1)
    
    print("\n\033[97m[\033[96m>\033[97m] Scan finised")
    if len(found) == 0:
        print("\033[97m[\033[91m-\033[97m] Congratulations! Admin page it was not found!!!")
    else:
        for site in found:
            print("\033[97m[\033[92m+\033[97m] Found!", site)
            
def info():
    """ banner display """
    psx = """\033[91m
 ________  __                        ________        __                     
/        |/  |                      /        |      /  |                    
$$$$$$$$/ $$ |____    ______        $$$$$$$$/   ____$$ |  ______    ______  
   $$ |   $$      \  /      \       $$ |__     /    $$ | /      \  /      \ 
   $$ |   $$$$$$$  |/$$$$$$  |      $$    |   /$$$$$$$ |/$$$$$$  |/$$$$$$  |
   $$ |   $$ |  $$ |$$    $$ |      $$$$$/    $$ |  $$ |$$ |  $$ |$$    $$ |
   $$ |   $$ |  $$ |$$$$$$$$/       $$ |_____ $$ \__$$ |$$ \__$$ |$$$$$$$$/ 
   $$ |   $$ |  $$ |$$       |      $$       |$$    $$ |$$    $$ |$$       |
   $$/    $$/   $$/  $$$$$$$/       $$$$$$$$/  $$$$$$$/  $$$$$$$ | $$$$$$$/ 
                                                        /  \__$$ |          
   \033[92m# https://maqlo-heker.blogspot.com\033[91m                   $$    $$/           
   \033[92m# Code by PosiX\033[91m                                      $$$$$$/         
          """
    print(psx)
    
if __name__ == '__main__':
   info()
   admin_scan()
   result()