# Python Notlarım

Python
* Çalıştırılabilir dosya:bir programlama dilinde kodun derlenmesiyle elde edilen,makine diline dönüştürülmüş hazır programa denir.Windows'ta uzantısı ".exe" dir.(executable)run komutuyla çalışır.
* .py uzantılı dosyayı .exe  çevirmek için PyInstalller,py2exe programları kullanılabilir.
* Python Guido van Rossum tarafından geliştirilmiş nesne tabanlı,birimsel ve etkileşimli yüksek seviyeli  bir programlama dilidir.Açık kaynaklı bir dildir.Python ile web geliştirme,oyun tasarımı,robotik uygulamalar,veri analizi gibi birçok şey geliştirilebilir.
IDLE(Integrated Development and Learning Enviroment),Tümleşik Geliştirme ve Öğrenme Ortamında Python geliştirilebilir.Verimli kod yazmaya yardımcı olan uygulama sınıfıdır.Python IDLE başlangıç seviyesi  için uygun bir araçtır.
Değişken:verinin depolanabileceği alan,yer
Değişkenlere isim verirken dikkat edilmesi gereken kurallar mevcuttur.Bir değişkenin ismi harf ya da alt çizgiyle başlamalıdır.Değiken isminin içerisinde alt çizgi hariç boşluk veya özel karakter olmamalıdır.Değişken ismi,bir Python komutu olamaz.Keyword ismi değişken ismi verilirken kullanılamaz.Değişken isimlerinde Türkçe karakter kullanılmamalıdır.!!

keyword list e ulaşmak için :
import keyword
keyword.kwlist

Python'da büyük harf ve küçük harf aynı isimli değişkenlerin farklı değişken yapar.

Değişken atama yapma örneği
iki değişken olsun:A ve B
Değişkenlerin değerlerini birbirleriyle değiştirmek için a,b=b,a ataması yapılabilir.
** üs alma operatörü
// işareti int değeri döndürür bölme işleminde

//Kod Örneği 
a=5
b=10
print(a,"+",b,"=",a+b)
//sonu. 5+10=15
 
  İşlem önceliği :parantez içi,üs alma,çarpma,bölme,mod,toplama çıkarma olarak en öncelikliden az öncelikliye göre yapılır.
  
  Temel Veri Tipleri
*int:tam sayı
*float:ondalıklı sayı
*bool:doğru ,yanlış
*str:karakter veri tipi
 Değikenin tipini öğrenmek için type(x) i kullanılır.Type'ın içine bir ifade yazıldığında bu argümanın doğruluğuna göre bir bool ifade döndürülür.

Veri tipleri birbirine dönüştürülebilir.Örneğin 9.6 değeri olan bir float ifadeyi (int)9.6 ya da int(9.6) yazarak int ifadeye dönüştürebiliriz.Bir başka veri tipini floata float(x) ya da string e de string(x) ifadelerini uygulayarak dönüştürebiliriz.Değişkenin tipini değiştirdiğimizde değişkenin orijinaldeki type ifadesinde gösterilir.Ancak değer farklı bir değişkene atanırsa o değişkenin türü değiştirdiğimiz tür olur.

Python'da yorum satırları # karakteriyle oluşturulur.

Python'da veri giriş komutu:input("İSMİNİZ:") klavyeden ismi alır.Klavyeden girilen verilerin tipi defaultta str olarak belirlenir.Bu veri tipini int e dönüştürebiliriz.
Python'da veri çıkış komutu:print()

Kod Örneği:
print('b','t','k',sep=',')aralara virgül ile ayırıyor.
print("btk"*3) 3 kere boşluksuz btk yazar çünkü str olarak algılar.
Ekrana çıktı yazdırmak için format() komutunu kullanabiliriz.Örneğin:
a=5
print("a={0}".format(a))
çıktı:a=5 olur.
print(f"a={a})
çıktı :a=5

 **print("/\n<>\n \") ters taksim işareti tek kalamaz.Hata 
verir.**

Koşul İfadeleri:
if:tek koşula bağlı işlemler için kullanılır.
if else:çift koşula bağlı işlemler için kullanılır.
if elif else:çoklu koşula bağlı işlemler için kullanılır.

Mantıksal Operatörler :and, or, not. 

Koşul kod örneği:
if 5==5:
  print("doğru")

Döngü yapıları for ve while olarak ikiye ayrılır.For döngüsünde tekrar sayısı belliyken while da dögü  koşula bağlı olarak çalışır.
Liste:sıralı eleman dizisdir.Birden fazla değer barındırabilir.Python'da string bir listedir.
Liste örneği:
liste=["ali","ahmet"]
print(liste)

Listede eleman aramak için 
if isim in liste:
  print("rezervasyonunuz var")
  Listede olmayan eleman varsa bir işlem gerçekleştirmek için not operatörü kullanılır.

  Range fonksiyonu:İstenen aralıkta sayı dizisi üretmek için kullanılır.
  Ör:
  range(1,10,2) #1 den 10 a kadar olan sayıları ikişer ikişer artacak şekilde ekrana yazar.
  Ör:
  for a in range(0,5):
    print(a)
    0 dan 4 e kadar sayıları yazdırır.

  Break ve continue komutu:Break komutunu sonsuz döngüden çıkmak için kullanabiliriz.Contunie döngüden çıkmadığımız fakat belli bir değerde işlem yapmadığımız yerlerde kullanılır.

  Fonksiyon:programın belli işlevini yerine getiren program parçaları.
  fonksiyon tanımlama ör:
  def topla():
   print("toplama işlemi yapar")
parametreli fonksiyon ör:
def selamlama(isim):
  print("sayın",isim,"hoşgeldin")

Ad=input("ismin nedir?")
selamlama(Ad)

Yerel değişen sadece fonksiyon içinde kullanılır.Global değişkeni ise tüm programda kullanırız.Fonksiyonun içinde global değişken olarak tanımlayabilirsin.

Lambda fonksiyon:tek satırlık fonksiyon tanımlamak için kullanılır.
ör:
dolar=lambda Tl:Tl/18

Özyinelemeli fonksiyon:Bir fonksiyon içerisinde aynı fonksiyonu çağırma işlemi yaparsak bu özyinelemeli fonksiyondur.

String işlemleri:(String bir karakter dizisdir.)
İndisleri sayarken boşluklar sayılır.İndisi  değiştirmeye Python izin vermiyor farklı bir şekilde yapılır bu uygulama.
String ifadeler + ile birleştirilir.
String dilimlemek için değişkenismi[:] ifadesi kullanılır.
[0:3] 0'dan 3'e kadar olan indsilerin değerini alır.
[1:5]1 (dahil) ile 5 arasındaki değerleri alır.
[1:2:2]1 den başayark 2 şer atlayarak indisleri alır.
[::-1]Stringi tersten yazdırır.
",".join(reversed(stringismi)):ters 

Stringi değiştirmek için replace i kullanabilirz.
ör:
adres="konuralp"
adres=adres.replace("konuralp","merkez")

String ifadeyi  silmek için ör:
yazi="python"
print(yazi)
for x in range(1,6):
 print(yazi[:-x])
pytho
pyth
pyt
py
p

Stringe For Döngüsü ile Erişme
for d in "sevval":
 print(d):
 if d==3:
   a=d
  s+=1
print(a)

Split() komutuyla stringi listeye dönüştürebilir.
String uzunluğu bulmak için len(string ismi)
Count ta belirli karakterin sayısını döndürür.
stringadı[ilk indis:son indis:adım miktarı]
.upper=stringi büyük karakterle yazar.
.swapcase=ilk String büyük sonrası küçük(kelime bazında)
at in "talat" var mı yok mu kontrol eder içinde at Stringi

Diziler Python'da liste olarak kullanılır.Dizinin elemanına indis numarasını yazarak ulaşılabilir.Listedeki elemanın indisine .index() ile ulaşılabilir.Liste [:] ifadesi ile bölünebilir.Listeye eleman eklemek için .append(indexno) kullanılır.Bir elemanın değerini belirli bir indise yerleştirmek için insert(indis,eleman) kullanılır.

Listenin uzunluğunu bulmak için len(listeismi)
listeismi.count("ta") kaç tane ta elemanı var onu sayar.
İki listeyi birleştirmek için  print(list1+list2) yapılabilir.Liste1 e liste2 yi eklemek için ayrıca liste1.extend(liste2) kullanılabilir.(sondan ekler)
Listeyi ters çevirmek için listeismi.reverse() kullanılır.
Listenin en büyük elemanını bulmak için max(listeismi)  min(listeismi) minimumu bulur.
Stringi karakter dizisine dönüştürmek için listeismi=list(stringkelime)
Listeden eleman silmek için remove(eleman ismi) kullanılır.
Listenin tamamını boşaltmak için listeismi.clear() kullanılır.
Bir indisteki elemanı silmek için .pop(indisno)  kullanılır.
Listede eleman aramak için ör:
l in Listeismi

Liste elemanlarını sıralamak için listeismi.sort() kullanılır.

Enumarete fonksiyonu:listeni elemanlarını numaralandırmak için kullanılır.

Yığın (stack):eleman ekleme ve çıkarmanın son elemandan gerçekleştiği yapıdır.(FIFO)
Kuyruk:eleman eklemenin sondan ve çıkarmanın listenin başından gerçekleştiği yapıdır.(LIFO)

Sözlük yapısı dizi gibi tanımlanır farkı ikişerli olarak tanımlanır.(dictionary)Olustumak için l=dict{["a:1","b=2"]}
Dict fonksiyonları:s.get() anahtarın value değerini gösterir.
s.keys() anahtarları verir
s.values  value ları verir

Küme tanımlamak için k={1,2,23} işlemi yapılabilir.k nin tipi burada set tir.İki kümeyi birleştirmek için küme1ismi|küme2ismi kullanılır.Ortak elemanları 1 defa yazılır.k1&k2 birleşimleri elde edilir.k1-k2 fark kümesi gösterilir.

Demet(tuple) listeyle aynıdır fakat farklılığı birinde [] kullanırken tuple de () işaret kullanılır.Tuple elemanı değiştirilemez.Sözlüklerde key olarak kullanılabilirler.

Sınıf tanımlanırken class ifadesi kullanılır.Sınıf içinde tanımlanan metotlar self işaretçisini alırlar

Self:nesneyi direkt göstermek için kullanılır.
Nesneler sınıftan türetilirler.Nesne oluşturmak için ör:
class araba():
 pass

 taksi=araba() 

 nesneadı=sınıfadı() şeklinde nesne tanımlanır.

 Nesnenin içindeki değerlere initial atamak için ör:
  class araba():
    def __init__(self,model,marka,renk):
    self.model=model
    self.marka=marka
    self.renk=renk

Taksi=araba(2020,"fiat",mavi) direkt değerleri atar.

Görevi biten nesneler otomatik silinir Python'da.
init metodunda başlangıç değerleri koyulur ve return alamaz.
dir(nesneismi) fonksiyonu:nesnenin özellik ve metotları öğrenilir.
Kalıtım: Sınıf içerisinde sınıf oluşturabiliriz.Bir sınıf başka bir sınıftan miras alarak özelliklerini kullanabilir.
Modül import ile modül eklenebilir.Sistem dosyasında hazır modüller var.Ayrıca kendi oluşturduklarımızı import edebiliriz.

from math import sqrt
import random
print(sqrt(100))
abs mutlak değer alır.
round yuvarlar.
max max ı bulur
pow üs alır.
hex hexadecimal değeri döndürür.
sum toplama yapar
 rastgele sayı üretmek için random modülünü ekleyip özelliklerini kullanabiliriz.
 random.randit(2,9)
 random.uniform(10,11) arasında değer üretir.
 listenin içinde random bir şey seçmek için random.choice(liste)
 Turtle ile çizim yapılabilir.Bir modüldür.

 Grafik koordinat sistemi 
 .position() 0 a 0 dan başlar.
 .goto(koordinatlar)  nereye gitmek istiyorsan oranın koordinatı
 .setpos()

 ileri gitmek için forward()
 geri gitmek için backward()
 sola gitmek için left(derecedeğeri)
 sğa gitmek için .rt()

 turtle.getshapes() 
 turtle.shape("turtle") simgeyi kaplumbağa yaptı
 
 Renk komutları:
 ör:

from turtle import *
color(red,brown)
pensize(30)
begin_fill()
ucgen()
end_fill()

eğer spesifik renk istersen rgb değerini yazabilirsin
fillcolor()
