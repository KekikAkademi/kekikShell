from selenium import webdriver # selenium modülümüzü import edip içindeki fonksiyonları kullanacağımızı söyledik.

def whatsapp():

    tarayiciyol = "C:/Users/erkan/Desktop/chromedriver_win32/chromedriver" # Selenium İçin Chrome veya firefox direverlerini indirip yolunu
                                                                        # Gösterdik Linkleri Formda bulabilirsiniz.

    tarayici = webdriver.Chrome(executable_path=tarayiciyol) # Selenium modülüne hangi driveri kullanacağımızı belirttik.
    tarayici.get("https://web.whatsapp.com/") # Requeset modülünden hatırlayacağınız üzere get metodu ile url'imizi belirttik.


    isim = input("Flood Atmak İstediğiniz Kişiyi Yazınız: ") # Gerekli Bilgilerin girilmesi için input oluşturduk.
    flood = input("Flood Mesajı Giriniz: ")
    sayi = int(input("Flood Sayısını Belirtiniz: ")) # İnt olarak belirterek sadece sayıları tanımasını söyledik aksi halde çalışmamasını belirttik.


    input("[*] İşlemin Başlaması İçin Herhangi Tuşa Basınız! 'Enter'") # İşlemin direkt başlamaması için burda bir aralık bıraktık. 
                                                                    # Bizim komutuz ile başlamasını sağladık.

    kisi = tarayici.find_element_by_xpath("//span[@title = '{}']".format(isim))# kisi adlı değişken oluşturarak sayfanın kaynak kodunda formdaki 
                                                                            # Resimde göreceğiniz üzere span'nin içerisinde bulunan  title etiketini
                                                                            # find_element_by_xpath Fonksiyonu yardımı ile ve en son olarak .format
                                                                            # Parametresi ile kime flood attack gerçekleştirecek isek belirtiktik.

    kisi.click() # Click fonksiyonu ile tıklama işlemi gerçekleştirdik.

    mesajblok = tarayici.find_element_by_class_name("_13mgZ") # mesajblok adlı değişken oluşturarak find_element_by_class_name fonksiyonu yardımı ile 
                                                            # Sayfanın kaynak kodundan mesaj yazdığımız text dosyasının class ismini alıp belirttik.

    for i in range(sayi): # for döngüsü sayesinde sayi adlı inputa girilen sayı kadar döndürmesini,
        mesajblok.send_keys(flood) # send_keys fonksiyonu yardımı ile flood adlı inputa girilen mesajı göndermesini,
        buton = tarayici.find_element_by_class_name("_3M-N-") # Sayfa kaynağından gönderme butonunun class ismin ögrenip belirterek,
        buton.click() # En son olarak click fonksiyonunu çağırarak  girilen bütün işlemleri for döngüsü ile döndürüp göndermesini söyledik.

    # Relativo Hornet ...


whatsapp()
