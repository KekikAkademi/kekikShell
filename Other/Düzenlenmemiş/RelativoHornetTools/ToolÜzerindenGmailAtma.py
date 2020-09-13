import smtplib

def maill():
    print("[*] En Fazla 500 Mail Gönderebilirisiniz.")
    print("[*] Gmail Giriş Bilgilerinizi Giriniz")
    kullanici = input("Gmail Adresinizi Giriniz: ")
    sifre = input("Şifrenizi Giriniz: ")
    giden = input("Mailin Kimden Gideceğini Belirtiniz: ")
    alan = input("Kime Gideceğini Belirtiniz: ")
    mesaj = (input("Lütfen Mesajınızı Giriniz: "))

    try:
        sunucu = smtplib.SMTP("smtp.gmail.com",587)
        sunucu.ehlo() # Bulunduğumuz Konumdan Mail Göndereceğimizi Belirttik.
        sunucu.starttls() # Bilgileri Gizleyerek Göndermesini Söyledik.
        sunucu.login(kullanici,sifre)
        sunucu.sendmail(giden,alan,mesaj.encode('utf-8')) # Mail Atan kişi, Maili alan kişi ve gireceğimiz mesajımızı burada belirttik.
        print("[+] İşlem Başarılı.") # Herşey Tamam ise İşlem'in Gerçekleştiğine dair mesaj vermesini söyledik.

    except smtplib.SMTPAuthenticationError:
        print("[-] Girilen Bilgiler Hatalı İşlem Başarısız.") 
        # Eğer işlem başarısız ise hata mesajını bizim yönledirmemiz ile sonlandırmasını Söyledik.


        # Relati Hornet ...

maill()