# day 17 numpy dasar

import numpy as np

# 1. membuat array 1d
array1 = np.array([1, 2, 3, 4, 5])
print("Array 1D:", array1)

# 2. membuat array 2d
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray 2d:")
print(array2)

# 3. membuat array dengan arange dan reshape
array3 = np.arange(1, 13).reshape(3, 4)
print("\nArray dengan arange dan reshape:")
print(array3)

# 4. operasi matematika
print("\nPenjumlahan array :", array1 + 10)
print("pengurangan array :", array1 - 2)
print("perkalian array: ", array1 * 3)
print("pembagian array:", array1 / 2)

# 5. operasi statistik
print("\nRAta-rata array: ", np.mean(array1))
print("median : ", np.median(array1))
print("Standar deviasi:", np.std(array1))

# 6. indexing dan slicing
print("\nElemen pertama array1:", array1[0])
print("Elemen terakhir array1:", array1[-1])
print("Slide array1 [1:4]:", array1[1:4])

# 7. operasi matriks
matriks1 = np.array([[1, 2], [3, 4]])
matriks2 = np.array([[5, 6], [7, 8]])
print("\nPenjumlahan matriks:")
print(matriks1 + matriks2)
print("perkalian matriks:")
print(np.dot(matriks1, matriks2))

# Latihan:
# 1. Buat array 3x3 berisi angka acak dari 1 hingga 20.
# 2. Hitung rata-rata dan standar deviasi dari array tersebut.
# 3. Buat matriks 2x2 dan lakukan perkalian matriks dengan matriks lain.
# 4. Lakukan operasi slicing pada array 2D.

# Selamat mencoba! 🚀