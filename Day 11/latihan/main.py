# latihan 3

import math_operations
from text_utils import vokal_konsonan

angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))
print("hasil pangkat: ", math_operations.pangkat(angka1, angka2))
print("Hasil modulus: ", math_operations.modulus(angka1, angka2))

teks = input("Masukan teks: ")
vokal, konsonan = vokal_konsonan.hitung_vokal_konsonan(teks)
print(f"Jumlah huruf vokal: {vokal}, jumlah huruf konsonan: {konsonan}")