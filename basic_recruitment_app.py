import time
sayac = 0
alanlar = ("Deep Learning", "Computer Vision", "NLP", "Machine Learning", "Artifical İntelligence")
alan = list()
yil = list()
deneyim = zip(alan, yil)
bolumadi = None
yeterlilik = None
controller = 0

print("*** Yapay Zeka Mühendisi İlanı ***")
isim = input("\n--> İlana başvurmadan önce lütfen isminizi giriniz: ")
print("\n--> Sayın {} aşağıdaki yeterlilikleri sağlıyorsanız sizinle çalışmak isteriz...\n".format(isim))

print("Bölümler:")
print("*NOT: İşe alım için bu bölümlerden mezun olunmalı.")
print("1-Matematik Müh.")
print("2-Bilgisayar Müh.")
print("3-Elektrik-Elektronik Müh.")
print("4-Mekatronik  Müh.")
print("5-İstatistik")
print("6- Bölümüm Listede Yok\n")

while True:
    secim1 = int(input("Mezun olduğunuz bölümü seçiniz:"))

    if secim1 < 1 or secim1 > 6:
        print("\n-->Lutfen dogru bir secim yapiniz!")
    else:
        if secim1 == 1:
            bolumadi = "Matematik Müh."
            break

        elif secim1 == 2:
            bolumadi = "Bilgisayar Müh."
            break

        elif secim1 == 3:
            bolumadi = "Elektrik-Elektronik Müh."
            break

        elif secim1 == 4:
            bolumadi = "Mekatronik  Müh."
            break

        elif secim1 == 5:
            bolumadi = "İstatistik"
            break

        else:
            bolumadi = "İlgili Bölümlerden Mezun Değil."
            break

print("\nİngilizce Yeterlilik Seviyesi:")
print("*NOT: İşe alım için gerekli ingilizce seviyesi B1-B2 veya C1-C2 olmalıdır.")
print("1-A1-A2")
print("2-B1-B2")
print("3-C1-C2")
print("4-İngilizcem Yok.\n")

while True:
    secim2 = int(input("İngilizce seviyenizi seçiniz:"))

    if secim2 < 1 or secim2 > 4:
        print("\n-->Lutfen dogru bir secim yapiniz!")
    else:

        if secim2 == 1:
            yeterlilik = "A1-A2"
            break

        elif secim2 == 2:
            yeterlilik = "B1-B2"
            break

        elif secim2 == 3:
            yeterlilik = "C1-C2"
            break

        else:
            yeterlilik = "İngilizcesi Yok."
            break

print("\nDeneyimler:")
print("*NOT: İşe alım için 1 veya daha fazla alanda alan başına en az 3 yıl deneyim istenmektedir.")
print("1-Deep Learning")
print("2-Computer Vision")
print("3-NLP")
print("4-Machine Learning")
print("5-Artifical İntelligence")

while True:
    tecrubesayisi = int(input("Bu alanların kaçında 3 veya 3 yılı aşkın bir tecrübeniz var: "))

    if tecrubesayisi < 0 or tecrubesayisi > 5:
        print("\n--> Lutfen dogru bir tecrube sayisi girin!")
    else:
        if tecrubesayisi == 0:
            alan.append(0)
            yil.append(0)
            break
        else:
            for i in range(tecrubesayisi):
                while True:
                    alansecimi = int(input("{}. alaninizi seciniz:".format(i+1)))

                    if 1 <= alansecimi <= 5:
                        if alansecimi == controller:
                            print("\n--> Aynı alan bir daha seçilemez!")
                        else:
                            controller = alansecimi
                            yilsecimi = int(input("Kac yil tecrubeniz var: "))
                            alan.append(alanlar[alansecimi - 1])
                            yil.append(yilsecimi)
                            break
                    else:
                        print("\n--> Lütfen doğru bir seçim yapınız.")
            break

print("*NOT: İşe alım için toplam tecrübenin en az 3 yıl olması gerekmektedir.")
while True:
    toplamtecrubeyili = int(input("\nSon olarak genel anlamda toplam kaç yıllık bir tecrübeye sahipsiniz:"))

    if toplamtecrubeyili < 0:
        print("--> Tecrübe sayısı negatif olamaz!")
    else:
        break

print("\n--> {} İsimli Basvuranin CV'si:".format(isim))
print("----------------------------------------------")
print("*Mezun Oldugu Bolum: {}".format(bolumadi))
print("*İngilizce Seviyesi: {}".format(yeterlilik))
for i, j in list(deneyim):
    if i == 0 and j == 0:
        print("*Belirtilen Alanlarda Tecrübe Sahibi Değil.")
    else:
        print("*{} Alanında {} Yıl Tecrübe Sahibi".format(i, j))
print("*Toplam Tecrübe Süresi: {} Yıl".format(toplamtecrubeyili))
print("----------------------------------------------")

print("\n--> CV'NİZ İNCELENİYOR", end="")
time.sleep(1.2)
print(".", end="")
time.sleep(1.2)
print(".", end="")
time.sleep(1.2)
print(".", end="")
time.sleep(1.2)

if (1 <= secim1 <= 5) and (secim2 == 2 or secim2 == 3) and (tecrubesayisi > 0) and toplamtecrubeyili >= 3:
    for i in range(tecrubesayisi):
        if yil[i] >= 3:
            sayac += 1
            if sayac == tecrubesayisi:
                print("\n--> İstenilen Tüm Kriterlere Uyuyorsunuz!")
                print("--> SONUÇ: Tebrikler, işe alındınız!")
                break
            else:
                continue
        else:
            print("\n--> İstenilen kriterlerin bazılarını veya hiçbirini sağlamıyorsunuz!")
            print("--> SONUÇ: Maalesef, işe alınmadınız!")
            break

else:
    print("\n--> İstenilen kriterlerin bazılarını veya hiçbirini sağlamıyorsunuz!")
    print("--> SONUÇ: Maalesef, işe alınmadınız!")
