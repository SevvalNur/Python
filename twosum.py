from typing import List

class Sol:
    def TwoSum(self, numbers: List[int], target: int) -> List[int]:
        store = dict()

        for i in range(len(numbers)):
            difference = target - numbers[i]
            #aradığım değerden indisin değerini yeni bir değişkene atadım ve bu da bana listedeki ikinci aradığım indisi verecek.
            # eğer difference dic
            if difference not in store:
                store[numbers[i]] = i
            else:
                # If found, return the indices
                return [store[difference], i]

# Kullanıcıdan girişleri al
try:
    nums = list(map(int, input("Sayıları virgülle ayırarak girin: ").split(',')))
    print("numbers:",nums)
    target = int(input("Hedef değeri girin: "))

    # Sol sınıfından bir örnek oluştur
    sol = Sol()

    # TwoSum fonksiyonunu çağır ve sonucu yazdır
    result = sol.TwoSum(nums, target)
    print("Sonuç:", result,"iki indisin toplamıdır.")

except ValueError:
    print("Hatalı giriş. Lütfen sayıları doğru formatta girin.")


                
    
