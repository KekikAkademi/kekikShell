from selenium import webdriver

#Incognito
option = webdriver.ChromeOptions()
option.add_argument('-incognito')
browser = webdriver.Chrome(chrome_options=option)

#
f = open('Proxy_list.txt', 'w')

#URL
browser.get("https://free-proxy-list.net/")

#Show 80 Proxies
browser.find_element_by_xpath("//select[@name='proxylisttable_length']/option[text()='80']").click()

#Just for sorting
browser.find_element_by_xpath("//th[@aria-label='Port: activate to sort column ascending']").click()
browser.find_element_by_xpath("//th[@aria-label='Port: activate to sort column descending']").click()

#Extract IP & Port
def get_list():
	rows = browser.find_elements_by_xpath("//tbody/tr[@role='row']")
	for r in rows:
		datas = r.find_elements_by_tag_name('td')
		ip = datas[0].text
		port = datas[1].text
		print(ip+":"+port)
		f.write(ip+":"+port+"\n")
get_list() #Get first list

#Rest lists
while True:
	browser.find_element_by_xpath("//li[@class='fg-button ui-button ui-state-default next']/a").click()
	get_list()	
	if len(browser.find_elements_by_xpath("//li[@class='fg-button ui-button ui-state-default next disabled']/a")) != 0:
		break
print('------------------Completed-------------------')
f.write('----------------------------Thanks for watching-----------------------------')
f.close()

