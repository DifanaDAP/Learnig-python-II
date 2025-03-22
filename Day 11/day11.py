# Day 11 modules & Packages dalam python

# menggunakan modul yang di buat sendiri
import mymodule # buat mymodule.py

nama_user = input("Masukan Nama Anda:")
print(mymodule.sapa(nama_user))

angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("masukan angka kedua: "))
print("Hasil penjualan: ", mymodule.tambah(angka1, angka2))

# mengunakan module bawaan python
import math
angka = float(input("Masukan angka untuk dihitung akarnya: "))
print("akar kuadratnya adalah: ", math.sqrt(angka))

# menggunakan package
from mypackage import modul1, modul2 # buat package mypackage

angka3 = int(input("Masukan angka pertama: "))
angka4 = int(input("masukan angka kedua: "))
print("Hasil penjualan: ", modul1.kali(angka3, angka4))
print("Hasil pembagian: ", modul2.bagi(angka3, angka4))
