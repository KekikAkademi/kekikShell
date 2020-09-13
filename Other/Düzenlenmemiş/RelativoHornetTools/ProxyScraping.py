from selenium import webdriver
import time

class proxy_scraping:
    def __init__(self):
        self.link = input("Site Link Giriniz: ")
        self.driver = webdriver.Chrome("C:/Users/erkan/Desktop/chromedriver_win32/chromedriver")
        # Link için input oluşturduk.
        # Tarayıcı İçin driverimizi belirttik.

    def tarayici_kapat(self):
        self.driver.close()

        # Bu fonksiyonu çağırdığımızda tarayıcı kapansın.
    def site(self):
        tarayici = self.driver
        tarayici.get(self.link)
        time.sleep(4) # Tarayici değişkenini çağırdığımızda bizim motorumuzu açmasını söyledik ve input değerini burada kullanacağımızı söyldik.
        etiket = tarayici.find_element_by_tag_name("tbody")
        etiket_iki = etiket.find_elements_by_tag_name("tr") # Burada Çekeceğimiz kısmı sırası ile belirttik.
        # şimdi verileri çekmesi için for döngüsüne sokalım.
        for i in etiket_iki:
            i = i.text.split(" ")
            print(i[0]+":"+i[1], i[2]) # 0 1 2. indexleri çekmesini söyledik. Bu sayede blokları önümüze getirecek.
# nesne oluşturalım.

proxy = proxy_scraping()
proxy.site()
proxy.tarayici_kapat()

# Tool hazır bakalım. :)

    