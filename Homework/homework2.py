ogrenciListesi = ["Ali Kutlu", "Mert Şeker"]

def ogrenciEkleme():
    ad = input("Lütfen eklemek istediğiniz öğrencinin adınızı giriniz: ")
    soyad = input("Lütfen eklemek istediğiniz öğrencinin soyadınızı giriniz: ")
    adSoyad = ad +" "+ soyad
    ogrenciListesi.append(adSoyad)
ogrenciEkleme()
print(ogrenciListesi)


def ogrenciSilme():
    ad = input("Lütfen silmek istediğiniz öğrencinin adınızı giriniz: ")
    soyad = input("Lütfen silmek istediğiniz öğrencinin soyadınızı giriniz: ")
    adSoyad = ad +" "+ soyad
    ogrenciListesi.remove(adSoyad)
ogrenciSilme()
print(ogrenciListesi)


def cokluOgrenciEkleme():
    sayi = int(input("Lütfen eklemek istediğiniz öğrenci sayısını yazınız: "))
    for i in range(sayi):
        ogrenciEkleme()
cokluOgrenciEkleme()
print(ogrenciListesi)


def ogrenciler():
    print(ogrenciListesi)
ogrenciler()


def ogrenciNumarasi():
    NumaraAd = input("Lütfen numarasını öğrenmek istediğiniz öğrencinin adınızı giriniz: ")
    NumaraSoyad = input("Lütfen numarasını öğrenmek istediğiniz öğrencinin soyadınızı giriniz: ")
    NumaraAdSoyad = NumaraAd +" "+ NumaraSoyad
    numara = ogrenciListesi.index(NumaraAdSoyad)
    print(NumaraAd + " Öğrenicinin numarası: " + str(numara))
ogrenciNumarasi()



def CokluOgrenciSilme():
  i=0
  x=int(input("Kaç tane öğrenci silmek istiyorsunuz?: "))
  while i<x:
    Ad=input("Lütfen silmek istediğiniz öğrencinin adı ve soyadını giriniz: ")
    ogrenciListesi.remove(Ad)
    i +=1
CokluOgrenciSilme()
print(ogrenciListesi)
