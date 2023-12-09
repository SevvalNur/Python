def kelime_bul(board):
    def dfs(satir, sutun, yol, ziyaret_edildi):
        # Eğer tahta sınırları dışına çıkılmışsa veya hücre ziyaret edilmişse, işlemi sonlandır
        if not (0 <= satir < satir_sayisi and 0 <= sutun < sutun_sayisi) or ziyaret_edildi[satir][sutun]:
            return

        # Yolu güncelle ve şu anki hücreyi ziyaret et
        yol += board[satir][sutun]
        ziyaret_edildi[satir][sutun] = True

        # Eğer bu yol, kelime listesinde varsa, bulunan kelimeler kümesine ekle
        if yol in kelime_listesi:
            bulunan_kelimeler.add(yol)

        # Yatay ve dikey yönlere göre derinlemesine arama yap
        yonler = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, ds in yonler:
            yeni_satir, yeni_sutun = satir + dr, sutun + ds
            dfs(yeni_satir, yeni_sutun, yol, ziyaret_edildi)

        # Geri dönüşte ziyaret durumunu geri al
        ziyaret_edildi[satir][sutun] = False

    # Tahta boyutlarını al
    satir_sayisi, sutun_sayisi = len(board), len(board[0])
    # Bulunan kelimeleri tutan küme
    bulunan_kelimeler = set()

    # Kullanıcıdan kelime listesini alır.
    kelime_listesi = input("Kelime listesini virgülle ayırarak girin: ")

    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            # Her bir hücre için ziyaret durumunu tutan matrisi oluştur
            ziyaret_edildi = [[False] * sutun_sayisi for _ in range(satir_sayisi)]
            # Derinlemesine arama fonksiyonunu çağır
            dfs(i, j, ziyaret_edildi)

    # Bulunan kelimeleri liste olarak döndür
    return list(bulunan_kelimeler)

# Kullanıcıdan kelime tahtasını al
def kelime_tahtasini_al():
    kelime_arama_tahtasi = []
    
    # Kullanıcıdan tahtanın satır sayısını al
    satir_sayisi = int(input("Kelime tahtasının satır sayısını girin: "))
    
    # Her bir satırı kullanıcıdan al
    for i in range(satir_sayisi):
        satir = list(input(f"{i+1}. satırı girin: "))
        kelime_arama_tahtasi.append(satir)
    
    return kelime_arama_tahtasi


# Kullanıcıdan kelime tahtasını al
kelime_arama_tahtasi = kelime_tahtasini_al()

# Kullanıcıya kelime bulmaca tahtasını göster
print("Kelime Bulmaca Tahtası:")
for row in kelime_arama_tahtasi:
    print(row)

# Kelimeleri bulan fonksiyonu çağır
bulunan_kelimeler = kelime_bul(kelime_arama_tahtasi)

# Bulunan kelimeleri ekrana yazdır
print("Bulunan kelimeler:", bulunan_kelimeler)

