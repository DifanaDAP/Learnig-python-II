# Latihan:
import numpy as np

# 1. Buat array 3x3 berisi angka acak dari 1 hingga 20.
array3 = np.random.randint(1, 21, size=(3, 3))
print("\nArray 3x3:")
print(array3)

# 2. Hitung rata-rata dan standar deviasi dari array tersebut.
print("\nStandar deviasi array:", np.std(array3))
print("\nRata-rata array:", np.mean(array3))

# 3. Buat matriks 2x2 dan lakukan perkalian matriks dengan matriks lain.
matriks1 = np.array([[1, 3], [2, 4]])
matriks2 = np.array([[5, 7], [6, 8]])
print("\nperkalian matriks:")
print(np.dot(matriks1, matriks2))
# 4. Lakukan operasi slicing pada array 2D.
print("\nSlice baris ke 2 array:")
print(array3[1])
print("Slice kolom ke 3 array :")
print(array3[:, 2])
# Selamat mencoba! 🚀