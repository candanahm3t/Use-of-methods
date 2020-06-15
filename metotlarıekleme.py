import time 

class Yazılımcı():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara 
        self.maas = maas
        self.diller = diller
    
    def bilgilerigoster(self):
        print("""
        Yazılımcı Objesinin Özellikleri

        İsim : {}

        Soyisim : {}

        Numara: {}

        Maas : {}

        Bildiği Diller : {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))


    def numara_degis(self,yeni_numara):
        
        self.numara=yeni_numara

    def zam_yap(self,zam_miktarı):
      
        self.maas+=zam_miktarı

    def dil_ekle(self,yeni_dil):
        
        self.diller.append(yeni_dil)


yazilimci = Yazılımcı("Ahmet","Candan","181816062",12500,["C","Python","Java"])

while True:
    print(""" Çalışan Bilgi Sistemine Hoşgeldiniz

    **************************************************
    1) Mevcut Çalışan Bilgisini Görmek İçin 1'i
    2) Çalışan Numara Değişikliği İçin 2'yi
    3) Çalışana Zam Yapmak İçin 3'ü 
    4) Yeni Yazılım Dili Eklemek İçin 4'ü
    5) Çıkmak İçin q'yu Tuşlayınız
    **************************************************
    """)

    secim = input("Seçiminizi Girin:")

    if secim == "1":
        yazilimci.bilgilerigoster()
        secim2=input("Devam etmek için herhangi bir tuşa çıkmak için q'ya basınız.")
        if(secim2=="q"):
            break

    elif secim == "2":
        numara=input("Yeni Numarayı Girin")
        yazilimci.numara_degis(numara)

        print("Numara Değiştiriliyor..")
        time.sleep(1)

        yazilimci.bilgilerigoster()
        secim2=input("Devam etmek için herhangi bir tuşa çıkmak için q'ya basınız.")
        
        if(secim2=="q"):
            break
    
    elif secim == "3":

        zam = int(input("Kaç TL zam yapılacak:"))
        yazilimci.zam_yap(zam)

        print("Zam yapılıyor..")
        time.sleep(1)

        yazilimci.bilgilerigoster()
        secim2=input("Devam etmek için herhangi bir tuşa çıkmak için q'ya basınız.")
        
        if(secim2=="q"):
            break

    elif secim == "4":

        dil = input("Eklenecek yazılım dilini girin:")
        yazilimci.dil_ekle(dil)

        print("Dil ekleniyor..")
        time.sleep(1)

        yazilimci.bilgilerigoster()
        secim2=input("Devam etmek için herhangi bir tuşa çıkmak için q'ya basınız.")
        
        if(secim2=="q"):
            break

    elif secim == "q":
        print("Çıkış yapılıyor")
        break
