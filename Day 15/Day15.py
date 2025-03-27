# Day 15 Debugging & logging dalam pyhton

# pergertian Debugging & logging
# debugging adalah proses menentukan dan memperbaiki kesalahan(bug) dalam kode program
#logging adalah mekanisme untuk mencatat informasi selama eksekusi program guna memantau dan menganalisa perilaku program

import logging

# 1. mengaktifkan logging
logging.basicConfig(level=logging.DEBUG, format='%(arstime)s - %(levelname)s - %(message)s')

# 2. contoh debuging dengan print
print("memulai program...")

def bagi(a, b):
    print(f"membagi {a} dengan {b}")
    return a / b

try:
    hasil = bagi(10, 0)
    print("hasil", hasil)
except ZeroDivisionError as e:
    print("Terjadi Kesalahan", e)

# 3. Debugging dengan logging
def bagi_logging(a, b):
    logging.debug(f"Membagi {a} dengan {b}")
    try:
        hasil = a / b
        logging.info(f"Hasil pembagian: {hasil}")
        return hasil
    except ZeroDivisionError:
        logging.error("Terjadi kesalahan: Pembagian dengan nol")
        return None
    
bagi_logging(10, 2)
bagi_logging(10, 0)

# 4. Menggunakan Breakpoint untuk debugging
import pdb

def hitung_faktor(x):
    pdb.set_trace()  # Breakpoint
    faktor = []
    for i in range(1, x + 1):
        if x % i == 0:
            faktor.append(i)
    return faktor

print("Faktor dari 12:", hitung_faktor(12))

# Latihan:
# 1. Tambahkan logging untuk fungsi yang menghitung faktorial suatu angka.
# 2. Gunakan pdb untuk mendebug fungsi rekursif sederhana.
# 3. Ubah level logging menjadi WARNING, lalu coba jalankan kembali kode di atas.
# 4. Simpan log ke file "app.log" dengan mode append.
# 5. Buat fungsi yang menangani error dengan logging dan mencatat jenis error yang terjadi.

# Coba selesaikan latihan di atas untuk memperdalam pemahaman debugging dan logging! 🚀