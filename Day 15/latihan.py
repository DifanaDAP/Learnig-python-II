# Latihan:
# 1. Tambahkan logging untuk fungsi yang menghitung faktorial suatu angka.
import logging

def faktorial(n):
    logging.debug(f"Menghitung faktorial dari {n}")
    if n == 0 or  n == 1:
        return 1
    else:
        return n * faktorial(n -1)
print("faktorial 5:" ,faktorial(5))

# 2. Gunakan pdb untuk mendebug fungsi rekursif sederhana.
import pdb

def hitung_pangkat(x, y):
    pdb.set_trace()  #breakpoint
    if y == 0:
        return 1
    return x * hitung_pangkat(x, y - 1)
print("2 pangkat 3: ", hitung_pangkat( 2, 3))
# 3. Ubah level logging menjadi WARNING, lalu coba jalankan kembali kode di atas.
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(messege)s')

# 4. Simpan log ke file "app.log" dengan mode append.
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 5. Buat fungsi yang menangani error dengan logging dan mencatat jenis error yang terjadi.
def bagi_dengan_logging(a, b):
    try:
        hasil = a / b
        logging.info(f"Hasil: {hasil}")
        return hasil
    except ZeroDivisionError as e:
        logging.error(f"Kesalahan: {e}")
        return None
    except Exception as e:
        logging.critical(f"Kesalahan tidak terduga: {e}")
        return None
print("Pembagian aman:", bagi_dengan_logging(10, 0))

# Coba selesaikan latihan di atas untuk memperdalam pemahaman debugging dan logging! 🚀