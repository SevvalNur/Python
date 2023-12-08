from typing import List

class Sol:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Liste sıralanır

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue  # Aynı olan elemanlardan kaçınmak için yazıldı.

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]

                if three_sum > 0:
                    # toplam 0 dan  büyükse sağ pointerı arttırır.
                    right -= 1
                elif three_sum < 0:
                    # toplam 0 dan küçükse sol pointerı arttırır.
                    left += 1
                else:
                    #toplam 0 a eşitse olası indisleri ekler.
                    result.append([a, nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        # tekrarlanandan kurtulmak için yazıldı.
                        left += 1

        return result

try:
    user_input = input("Sayıları boşlukla ayırarak girin: ")
    nums = list(map(int, user_input.split()))

    # Sol sınıfından bir örnek oluştur
    sol = Sol()

    # ThreeSum fonksiyonunu çağırır ve sonucu yazdırır.
    result = sol.threeSum(nums)
    
    if result:
        print("Bulunan üç sayı grupları:")
        for triplet in result:
            print(triplet)
    else:
        print("Sıfıra toplamı olan üç sayı grubu bulunamadı.")

except ValueError:
    print("Hatalı giriş. Lütfen sayıları doğru formatta girin.")
