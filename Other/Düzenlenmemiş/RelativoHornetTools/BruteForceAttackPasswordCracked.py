import time

liste = ["a","b","c","d","e","f","g","h","i","j","k","m","n","l","o","p","q","r","s","t","u","v","w","x","y","z"]
ilk = input("Password Girin: ") 
harf = str() 
zaman = time.time() 

def atak(harf,ilk): 
    try: 
        if harf == ilk: 
            print("[*] Şifre Kırıldı => ",harf) 
            print("Kırma Esnasında Geçen Zaman =>",zaman)
    except KeyboardInterrupt:                                                                
        print("Hata!")

def brute_force_atak(): 
    for cw in liste: 
        harf = cw 
        
        atak(harf,ilk) 

        for cw2 in liste: 
            harf = cw + cw2 
            atak(harf,ilk) 

            for cw3 in liste:
                harf = cw + cw2 + cw3
                atak(harf,liste)

                for cw4 in liste:
                    harf = cw + cw2 + cw3 + cw4             
                    atak(harf,ilk)                     

                    for cw5 in liste:
                        harf = cw + cw2 + cw3 + cw4 + cw5
                        atak(harf,ilk)
                        
                        for cw6 in liste:
                            harf = cw + cw2 + cw3 + cw4 + cw5 + cw6
                            atak(harf,ilk)

                            for cw7 in liste:
                                harf = cw + cw2 + cw3 + cw4 + cw5 + cw6 + cw7
                                atak(harf,ilk)
                                break       

brute_force_atak() 

# Relativo Hornet...