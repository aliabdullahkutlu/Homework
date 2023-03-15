#PYTHON SELENIUM KURSU 1. HAFTA ÖDEV

#1- Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

"Metinsel verileri saklamak istediğimiz zaman “String” veri tipine ihtiyaç duyarız."

string ="Python Yazılım Kursu"
print(string)

print("Sayısal veri kullanmak istediğimizde sayının durumuna göre int, float, complex veri tiplerinden birini kullanırız.")
int=6 # Tam sayılar 
float=7.5 # Ondalıklı sayılar 
complex=4j # Gerçek ve sanal kısımdan oluşan kompleks sayılar

print("Boolean değer tipi false yada true değerleri tutmak için kullanılır.")
boolean=True or False

print("Dizi halinde tutulan veriler list, tuple, set, dictionary olarak ayrılır")
list=["p","y","t","h","o","n"] # List; sıralı ve elemanları değiştirilebilir bir dizidir. Dizi elemanlarının tekrarlamasına izin verir. Aynı elemandan aynı dizide birden fazla olabilir.
print(list)

tuple=("y","a","z","ı","l","ı","m") # Tuple; sıralı ve elemanları değiştirilemeyen bir dizidir. Dizi elemanlarının tekrarlamasına izin verir. Aynı elemandan aynı dizide birden fazla olabilir.
print(tuple)

set = {"c", "python", "html", "css"} # Set; sırasız ve indexlenmemiş bir dizidir. Dizi elemanlarının tekrarlamasına izin vermez. Bir elemandan bir dizide bir tane olur.
print(set)

dictionary = {"Dil" : "Pyhton" , "Konu" : "If Conditional" } #Dictionary; sırasız, elemanları değiştirilebilir ve indexlenmiş bir dizidir. Dizi elemanlarının tekrarlamasına izin vermez. Bir elemandan dizide bir tane olur.
print(dictionary)


#2- Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

#Kodlama io sayfasında Kurslarım,Tüm kurslar,Kariyer gibi titlelar string ifadelerdir.
#Kategori ve Eğitmen titleları list ifadelerdir.
#%10 tamamlandı sayaçları '10' integerdir.


#3- Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

#Örneğin kursun içeriğine erişmek için üyelik girişi yapılıp yapılmadığını şart blokları ile kontrol edebiliriz.


eposta=input("E-mail")
sifre=input("Password")
#input() fonksiyonu kullanıcıdan bilgi almak için kullanılır.

if eposta==("kodlama.io@gmail.com") and sifre ==("kodlama"):
    print ("Giriş Başarılı")
elif eposta==("") and sifre ==(""):
    print ("Bu alanlar boş bırakılamaz.")
else:
    print("E-posta veya şifre yanlış tekrar deneyin")
    
