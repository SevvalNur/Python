import numpy as np

def numpy_fonksiyon_ornekleri():

# Matrisin transpozunu alma
   transpoz_matris = np.transpose(matris)

# Matris determinantını bulma
    matris_det = np.linalg.det(matris)

 # Matrisin tersini alma
    matris_ters = np.linalg.inv(matris)

# İki matrisi çarpma
    matris_2 = np.array([[2, 0, 1], [1, 2, 3], [4, 5, 6]])
    matris_carpim = np.dot(matris, matris_2)


    zeros_array = np.zeros((3, 4))
    print("Zeros Array (Sıfırlar Matrisi):")
    print(zeros_array)

    
    ones_array = np.ones((2, 3))
    print("\nOnes Array (Birler Matrisi):")
    print(ones_array)

    arange_array = np.arange(0, 10, 2)
    print("\nArange Array (Arange Fonksiyonu):")
    print(arange_array)

    
    linspace_array = np.linspace(0, 1, 5)
    print("\nLinspace Array (Linspace Fonksiyonu):")
    print(linspace_array)

    
    random_array = np.random.random((2, 2))
    print("\nRandom Array (Rastgele Sayılar Matrisi):")
    print(random_array)

    # Max fonksiyonu ile random_array içindeki en büyük değeri bulma
    max_value = np.max(random_array)
    print("\nMax Value (Maksimum Değer):", max_value)

if __name__ == "__main__":
    numpy_fonksiyon_ornekleri()
