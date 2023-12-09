class TuşluTelefon:
    def __init__(self):
        self.phonenumberdigits = {
            "1": ["1"],
            "2": ["a", "b", "c","2"],
            "3": ["d", "e", "f","3"],
            "4": ["g", "h", "ı","4"],
            "5": ["j", "k", "l","5"],
            "6": ["m", "n", "o","6"],
            "7": ["p", "q", "r", "s","7"],
            "8": ["t", "u", "v","8"],
            "9": ["w", "x", "y", "z","9"],
            "0": ["0"]
        }

    def harfleri_tuşlara_dönüştür(self, kelime):
        indisler = []

        for harf in kelime:
            if harf == ' ':
                indisler.append('')
                continue

            harf_bulundu = False
            tuş_bilgisi = []
            for tuş, harfler in self.phonenumberdigits.items():
                if harf.lower() in harfler:
                    tuş_bilgisi = [tuş] * (harfler.index(harf.lower()) + 1)
                    harf_bulundu = True
                    break

            if harf_bulundu:
                indisler.append(tuş_bilgisi)
            else:
                indisler.append(["Geçersiz"])

        return indisler

if __name__ == "__main__":
    tuşlu_telefon = TuşluTelefon()
    metin = input("Metni giriniz: ")
    indisler = tuşlu_telefon.harfleri_tuşlara_dönüştür(metin)

    print("\nTuşların sırayla basıldığı array:")
    print(indisler)
