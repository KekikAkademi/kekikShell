from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import time
#Incognito
option = webdriver.ChromeOptions()
option.add_argument('-incognito')
browser = webdriver.Chrome(chrome_options=option)

#
f = open('hidemyna.csv', 'w')
headers = ('Ip , Port , Country, Type, Anonymity\n') # Creat header
f.write(headers)

#URL
browser.get("https://hidemyna.me/en/proxy-list/")
time.sleep(6)

def get_list():
	#tbody is unique. so that easy
	#All tr tag inside tbody just inclue IP_Port list, so just find_elements
	rows = browser.find_elements_by_xpath("//table[@class='proxy__t']//tbody/tr")
	#1st td is IP
	#2nd td is Port
	#3rd td is Country
	#4th i dont need
	#5th is Type
	#6th Anonymity
	for r in rows:
		datas = r.find_elements_by_tag_name('td')
		ip = datas[0].text
		port = datas[1].text
		Country = datas[2].text
		Type = datas[4].text
		Anonymity = datas[5].text
		print(ip+','+port+','+Country+','+Type+','+Anonymity)
		f.write(ip+','+port+','+Country+','+Type+','+Anonymity+"\n")
get_list() #Get first list

#Rest lists
#you should use unique class,id or tag name 
while True:
	to_click = browser.find_element_by_xpath("//div[@class='proxy__pagination']/ul/li[@class='arrow__right']/a")
	browser.execute_script("arguments[0].click();", to_click)
	get_list()	#get it
	if len(browser.find_elements_by_xpath("//div[@class='proxy__pagination']/ul/li[@class='arrow__right']")) == 0: #No more list
		break
print('------------------Completed-------------------')
f.close()

