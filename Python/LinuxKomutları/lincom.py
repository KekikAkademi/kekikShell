# -*- coding: utf-8 -*-
#!/usr/bin/python
#Linux Tanıtım Aracı Beta Sürüm

import webbrowser
import os
import subprocess
import time
import random

varsayilan="\033[0m"
mavi="\033[96m"
kirmizi="\033[91m"
yesil="\033[92m"
mor="\033[95m"
turuncu="\033[93m"
lacivert="\033[94m"

renkler_sü=(mavi,kirmizi,yesil,mor,turuncu,lacivert)

try:
    sec = random.randint(0,5)
    print(renkler_sü[sec]+"\n")
    print("     ________|----|_______")
    print("    /                     \_____________                 ____________")
    print("   /          KB           _____________| * * * *       <____________|********")
    print("  |     KernelBlog.org     |__                           Kernel Panic")
    print("  | __________________________\ ")
    print("  |/                           \ ")
    print("  |   O      O      O      O    |              Yazar: Yunus Emre ÖZTÜRK      ")
    print("   \___________________________/     Linux Komutları İçin Yazılan İnteraktif Araçtır.\n")
    print("Linux Komutları Tanıtım Aracına Hoşgeldiniz.")
    print("Bu Aracı Tam Ekran Kullanmanız Önerilir.\n")
    print("1- Temel Linux Komutları Öğreticisi")
    print("2- Hakkımızda")
    print("3- KernelBlog.org")
    print("4- Linux Komutları #2 Makalesi\n")
    while True:
        girdi=input(mavi+"komut> "+varsayilan)
        if girdi=="1":
            print(yesil+"\nÖğretici Başlatılıyor...\n"+varsayilan)
            time.sleep(2)
            print(mavi+"      'ls' Komutu")
            print("-----------------------")
            print("\nİlk komutumuz 'ls'. 'ls' komutu bize olduğumuz dizindeki dosya ve dizinleri listeler. Aşağıdaki deneme bölümünden 'ls' komutunu deneyiniz.\n")
            while True:
                komut=input("Lütfen komut giriniz> ")
                if komut=="ls":
                    ls = subprocess.check_output("ls")
                    print("\n",ls.decode("utf-8"),"\n")
                    break
                else:
                    print("Lütfen doğru komutu giriniz.\n")
            print("Gördüğünüz gibi 'ls' komutu bize olduğumuz dizindeki dosyaları listeledi. İsterseniz bir terminal açıp terminalden 'ls' komutunu deneyebilirsiniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(kirmizi+"      'cd' Komutu")
            print("-----------------------\n")
            print("Gelelim 'cd' adlı komutumuza\n")
            print("'cd' komtumuz bize dizinler arası geçişi sağlar.\n")
            print("'cd geçilecek_dizin' olarak kullanabilirsiniz. Örnek olarak bir terminal açıp öncelikle 'ls' komutu ile dizini listeleyin ve 'cd' komutu ile de seçtiğiniz bir dizine geçin."+varsayilan,"\n")
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mor+"     'pwd' Komutu")
            print("-----------------------\n")
            print("'pwd' (Print Working Directory) adlı komutumuz ise adından da anlaşıldığı gibi olduğumuz dizini bize söylüyor. Aşağıdaki deneme bölümünden 'pwd' komutunu deneyiniz.\n")
            while True:
                komut=input("Lütfen komut giriniz> ")
                if komut=="pwd":
                    pwd = subprocess.check_output("pwd")
                    print("\n",pwd.decode("utf-8"))
                    break
                else:
                    print("Lütfen doğru komutu giriniz.\n")
            print("Şu an siz bu dizindesiniz demektir. İsterseniz bir terminal açıp 'pwd' komutunu deneyerek hangi dizinde olduğunuzu görebilirsiniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(turuncu+"    'mkdir' Komutu")
            print("-----------------------\n")
            print("'mkdir' (Make Directory) komutumuz bizim bir dizin oluşturmamızı sağlıyor. 'mkdir OLUŞTURULACAK DİZİN' şeklinde kullanabilirsiz. Gelin bir örnek yapalım. 'mkdir dizin' komutu ile bir dizin oluşturunuz ve sonra 'ls' komutunu kullanarak oluşup oluşmadığını kontrol ediniz.\n")
            while True:
                komut=input(turuncu+"Lütfen komut giriniz> ")
                komutkont=komut.find("mkdir ")
                if komutkont!=-1:
                    rmdeg=komut[6:]
                    os.system(komut)
                    print("Dizin başarıyla oluşturuldu.\n")
                    while True:
                        komut=input(turuncu+"Lütfen komut giriniz> ")
                        if komut=="ls":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("'ls' çıktısında da görüldüğü gibi dizin başarıyla oluştu.\n"+varsayilan)
                            break
                        else:
                            print(turuncu+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                            pass
                    break
                else:
                    print(turuncu+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(lacivert+"      'rm' Komutu")
            print("-----------------------\n")
            print("Geldik 'rm' adlı komutumuza. 'rm' (Remove) komutumuz bir dosyayı veya dizini silmeye yarıyor. Dosya silmek için: 'rm dosya adı'. Dizin silmek için ise 'rm -r dizin adı' şeklinde kullanabilirsiniz. Şimdi gelin örneğe geçelim. Az önce oluşturduğumuz dizini 'rm -r' komutu ile silelim. Ve 'ls' ile silindiğini de görelim.\n")
            while True:
                komut=input(lacivert+"Lütfen komut giriniz> ")
                komutkont=komut.find("rm -r "+rmdeg)
                if komutkont!=-1:
                    os.system(komut)
                    print("Dizin başarıyla silindi.\n")
                    while True:
                        komut=input(lacivert+"Lütfen komut giriniz> ")
                        if komut=="ls":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("Terminale 'ls' komutunu yazarak dizinin silindiğini görebilirisniz.\n"+varsayilan)
                            break
                        else:
                            print(lacivert+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                            pass
                    break
                else:
                    print(lacivert+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mavi+"      'cp' Komutu")
            print("-----------------------\n")
            print("Sırada cp (Copy) adlı komutumuz var. cp bize bir dosyanın içerisindekini diğer dosyaya kopyalamayı veya bir dosyayı yada dizini bir yerden bir yere kopyalamayı sağlar. Dosya kopyalamak için: 'cp 1.dosya 2.dosya'. Dosya veya dizini kopyalamak için: 'cp kopyalanacak_dosya_yada_dizin kopyalanacak_yeni_yer'.\n")
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(kirmizi+"      'mv' Komutu")
            print("-----------------------\n")
            print("'mv' komutumuz ise bir dosyayı bir dosyaya taşımaızı, bir dosya yada dizini bir yerden bir yere taşımamızı veya bir dosyanın yada dizinin ismini değiştirmemizi sağlıyor. Dosyayı dosyaya taşımak için: 'mv 1.dosya 2.dosya'. Dosya veya dizini bir yerden bir yere taşımak için: 'mv taşınacak_dosya_veya_dizin taşınacak_dizin'. İsmini değiştirmek için: 'mv ismi_değiştirilecek_dosya yeni_isim'\n")
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mor+"      'wc' Komutu")
            print("-----------------------\n")
            print("Sırada 'wc' adlı komutumuz var. 'wc' komutu belirtilen bir dosyanın sırasıyla satır, kelime ve karakter sayısını göstermek için kullanılır. Aşağıdaki deneme bölümünden Linux Tanıtım Aracının olduğu dizindeki dosya adlı dosya ile 'wc' komutunu deneyiniz.\n")
            while True:
                komut=input(mor+"Lütfen komut giriniz (wc dosya)> ")
                if komut=="wc dosya":
                    print("\n")
                    wc = os.system("wc dosya")
                    print("\nHata Sayısı:",wc,"\n")
                    print("Gördüğünüz gibi sırasıyla satır, kelime ve karakter sayısını yazdırdı.\n"+varsayilan)
                    break
                else:
                    print("Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(turuncu+"      'ln' Komutu")
            print("-----------------------\n")
            print("'ln' komutu kısa yol oluşturmamızı sağlar. 'ln' komutunun iki farklı parametresi var. 'ln dosya_adı bağlanacak_kısa_yol_adı' bu kullanımı Windows'daki kısa yol gibi düşünebilirsiniz ana dosya silindiğinde kısayol da işe yaramaz hale gelir.\n")
            print("2. kullanım ise 'ln -s dosya_adı bağlanacak_kısa_yol_adı' bu kullanımda fark ana dosyayı sildiğinizde kısa yol hala duracaktır. Yani bir tip kopyası gibi düşünebilirsiniz ama birisinde yaptığınız değişiklik diğerine de geçer\n")
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(lacivert+"    'touch' Komutu")
            print("-----------------------\n")
            print("'touch' komutu yeni boş bir dosya oluşturmamızı sağlar. 'touch oluşturulacak_dosya_adı' şeklinde kullanabilirsiniz. Aşağıdaki deneme bölümünden 'touch' komutunu deneyiniz. Ardından 'ls' komutunu deneyerek dosyanın oluşup oluşmadığına bakınız.\n")
            while True:
                komut=input(lacivert+"Lütfen komut giriniz> ")
                komutkont=komut.find("touch ")
                if komutkont!=-1:
                    touchdosya=komut[6:]
                    os.system(komut)
                    print("Dosya başarıyla oluşturuldu.\n")
                    while True:
                        komut=input(lacivert+"Lütfen komut giriniz> ")
                        if komut=="ls":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("Terminale 'ls' komutunu yazarak dosyanın oluştuğunu görebilirsiniz.\n"+varsayilan)
                            break
                        else:
                            print(lacivert+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                            pass
                    break
                else:
                    print(lacivert+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mavi+"     'cat' Komutu")
            print("-----------------------\n")
            print("'cat' komutu dosyanın içeriğini görüntülemeye yarar. 'cat dosya_adı' şeklinde kullanabilirsiniz. Aşağıdaki deneme bölümünden Linux Tanıtım Aracının olduğu dizindeki dosya adlı dosya ile 'cat' komutunu deneyiniz.\n")
            while True:
                komut=input(mavi+"Lütfen komut giriniz (cat dosya)> ")
                if komut=="cat dosya":
                    print("\n")
                    cat = os.system("cat dosya")
                    print("\nHata Sayısı:",cat,"\n")
                    print("Gördüğünüz gibi 'cat' komutu bize dosyanın içeriğini görüntüledi.\n"+varsayilan)
                    break
                else:
                    print(mavi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(kirmizi+"     'more' Komutu")
            print("-----------------------\n")
            print("'more' komutu belirtilen dosyanın içeriğini sayfalayarak gösterir. Yani sayfa sayfa. 'more dosya_adı' şeklinde kullanabiirsiniz. 'more' komutundan çıkmak için 'q' ya basmak gerekmektedir. Aşağıdaki deneme bölümünden Linux Tanıtım Aracının olduğu dizindeki dosya adlı dosya ile 'more' komutunu deneyiniz.\n")
            while True:
                komut=input(kirmizi+"Lütfen komut giriniz (more dosya)> ")
                if komut=="more dosya":
                    print("\n")
                    more = os.system(komut)
                    print("\nHata sayısı:",more,"\n")
                    print("'more' komutu bize görüldüğü gibi dosyayı sayfa sayfa gösterdi.\n"+varsayilan)
                    break
                else:
                    print(kirmizi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mor+"     'head' Komutu")
            print("-----------------------\n")
            print("'head' komutu belirtilen dosyanın içeriğini ilk 10 satırını gösterir. 'head dosya_adı' şeklinde kullanabiirsiniz. Aşağıdaki deneme bölümünden Linux Tanıtım Aracının olduğu dizindeki dosya adlı dosya ile 'head' komutunu deneyiniz.\n")
            while True:
                komut=input(mor+"Lütfen komut giriniz (head dosya)> ")
                if komut=="head dosya":
                    print("\n")
                    head = os.system(komut)
                    print("\nHata sayısı:",head,"\n")
                    print("Gördüğünüz gibi 'head' komutu dosya içeriğinin ilk 10 satırını gösterdi.\n"+varsayilan)
                    break
                else:
                    print(mor+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(turuncu+"     'tail' Komutu")
            print("-----------------------\n")
            print("'tail' komutu belirtilen dosyanın içeriğini son 10 satırını gösterir. 'tail dosya_adı' şeklinde kullanabiirsiniz. Aşağıdaki deneme bölümünden Linux Tanıtım Aracının olduğu dizindeki dosya adlı dosya ile 'tail' komutunu deneyiniz.\n")
            while True:
                komut=input(turuncu+"Lütfen komut giriniz (tail dosya)> ")
                if komut=="tail dosya":
                    print("\n")
                    tail = os.system(komut)
                    print("\nHata sayısı:",tail,"\n")
                    print("Gördüğünüz gibi 'tail' komutu dosya içeriğinin son 10 satırını gösterdi.\n"+varsayilan)
                    break
                else:
                    print(turuncu+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(lacivert+"    'chmod' Komutu")
            print("-----------------------\n")
            print("'chmod' komutu bizim bir dosya veya klasörün iznini değiştirmemizi sağlar. 'chmod +verilecek_izin dosya' şeklinde kullanabilirsiniz. Örnek: 'chmod +x dosya'. İzin olarak 3 farklı izin vardır. r (Read - Okuma), w (Write - Yazma), x (Execute - Çalıştırma). Aşağıdaki deneme bölümünden 'touch' komutunda oluşturduğunuz dosyayı kullanarak 'chmod' komutunu deneyiniz (dosyaya çalıştırma izni veriniz) ardından 'ls -l' komutnunu kullanarak dosyanın izinlerine göz atınız.\n")
            print("Not: 'ls -l' komutu 'ls' komutunun '-l' parametresini ifade eder. '-l' parametresi bize o dizindeki dosyaların geniş çaplı bilgilerini verir. Oluşturulma tarihinden izinlerine kadar. 'ls -l' koutunu verdiğinizde en sol kısımda kalan bölüm izinleri temsil eder.\n")
            while True:
                komut=input(lacivert+"Lütfen komut giriniz> ")
                if komut=="chmod +x "+touchdosya:
                    chmod = os.system(komut)
                    print("İzin başarıyla verildi\n")
                    while True:
                        komut=input(lacivert+"Lütfen komut giriniz> ")
                        if komut=="ls -l":
                            print("\n")
                            ls=os.system("ls -l")
                            print("Hata Sayısı:",ls,"\n")
                            print("En sol kısma baktığınızda x işaretinin oraya eklendiğini görebilirsiniz.\n"+varsayilan)
                            break
                        else:
                            print(mavi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                    break
                elif komut=="ls -l":
                    print("\n")
                    ls=os.system("ls -l")
                    print("Hata Sayısı:",ls)
                else:
                    print(lacivert+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mavi+"     'gzip' Komutu")
            print("-----------------------\n")
            print("Sıra geldi 'gzip' komutumuza. 'gzip' komutu bir dosyayı sıkıştırmamızı sağlar. 'gzip dosya' şeklinde kullanabilirsiniz. Aşağıdaki deneme bölümünden 'touch' komutunda oluşturduğunuz dosyayı 'gzip' komutu ile sıkıştırınız sonra 'ls' komutu ile dosyanın sıkışıp sıkışmadığını kontrol ediniz.\n")
            while True:
                komut=input(mavi+"Lütfen komut giriniz> ")
                if komut=="gzip "+touchdosya:
                    gzip = os.system(komut)
                    print("Dosya başarıyla sıkıştırıldı\n")
                    while True:
                        komut=input(mavi+"Lütfen komut giriniz> ")
                        if komut=="ls":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("Görüldüğü gibi dosya gz uzantısı ile sıkıştırılmış durumda.\n"+varsayilan)
                            break
                        else:
                            print(mavi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                    break
                elif komut=="ls":
                    ls = subprocess.check_output("ls")
                    print("\n",ls.decode("utf-8"),"\n")
                else:
                    print(mavi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(kirmizi+"   'gunzip' Komutu")
            print("-----------------------\n")
            print("Gelelim 'gunzip komutuna'. 'gunzip' komutu sıkıştırılmış bir dosyayı açmayı sağlar. 'gunzip dosya' şeklinde kullanabilirsiniz. Aşağıdaki deneme bölümünden 'gzip' komutunda sıkıştırdığınız dosyayı 'gunzip' komutu ile açınız sonra 'ls' komutu ile dosyanın açılıp açılmadığını kontrol ediniz.\n")
            while True:
                komut=input(kirmizi+"Lütfen komut giriniz> ")
                if komut=="gunzip "+touchdosya:
                    gunzip = os.system(komut)
                    print("Dosya başarıyla açıldı\n")
                    while True:
                        komut=input(kirmizi+"Lütfen komut giriniz> ")
                        if komut=="ls":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("Görüldüğü gibi dosya tekrar açılmış durumda.\n"+varsayilan)
                            break
                        else:
                            print(kirmizi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                    break
                elif komut=="ls":
                    ls = subprocess.check_output("ls")
                    print("\n",ls.decode("utf-8"),"\n")
                else:
                    print(kirmizi+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            siradakikomut=input(yesil+"Sıradaki Komuta Geçmek İçin Entera Basınız.\n"+varsayilan)
            print(mor+"    'alias' Komutu")
            print("-----------------------\n")
            print("'alias' komutu sistemde var olan komutların adlarını değiştirmeye yarar. Komut adları yerine takma ad kullanmamızı sağlar yani. 'alias takma_ad=komut' şeklinde kullanabilirsiniz. Aşağıdaki deneme bölümünden 'alias' komutunu 'ls' komutunu kullanarak deneyiniz. 'ls' komutunun ismini 'dosyalist' ile değiştiriniz. Sonra 'dosyalist' komutunu deneyiniz.\n")
            while True:
                komut=input(mor+"Lütfen komut giriniz> ")
                if komut=="alias dosyalist=ls":
                    print("İsim başarıyla değiştirildi.\n")
                    while True:
                        komut=input(mor+"Lütfen komut giriniz> ")
                        if komut=="dosyalist":
                            ls = subprocess.check_output("ls")
                            print("\n",ls.decode("utf-8"),"\n")
                            print("'ls' komutunun ismi 'dosyalist' değişmiş durumda.\n"+varsayilan)
                            break
                        else:
                            print(mor+"Lütfen doğru komutu giriniz.\n"+varsayilan)
                    break
                elif komut=="ls":
                    ls = subprocess.check_output("ls")
                    print("\n",ls.decode("utf-8"),"\n")
                else:
                    print(mor+"Lütfen doğru komutu giriniz.\n"+varsayilan)
            time.sleep(3)
            print(mavi+"Temel Linux Komutları Öğreticisini Başarı İle Tamamladınız. Tebrikler Ve İyi Çalışmalar...\n")
            os.system("rm "+touchdosya)
            ogreticiyikapat=input("Öğreticiden Ve Araçtan Çıkmak İçin Entera Basınız\n"+varsayilan)
            break
        elif girdi=="2":
            webbrowser.open("https://kernelblog.org/hakkimizda")
        elif girdi=="3":
            webbrowser.open("https://kernelblog.org")
        elif girdi=="4":
            webbrowser.open("https://kernelblog.org/2018/04/temel-linux-komutlari-2/")
except KeyboardInterrupt as e:
    print(mavi+"\nLinux Komutlarını Tanıtan Aracımızı Kullandığınız İçin Teşekkür Ederiz İyi Çalışmalar...")
else:
    pass
