# Day 14: Regular Expression (Regex) dalam Python

# Pengertian Regular Expression
# Regular Expression (disingkat Regex) adalah pola teks yang digunakan untuk mencocokkan, mencari, dan memanipulasi string.
# Regex sangat berguna untuk validasi data, pencarian teks, dan pengolahan data dalam berbagai aplikasi.

import re

# 1. Pencocokan Pola Dasar
text = "Hari ini tanggal 14 Maret 2025. Besok tanggal 15."
pattern = r'\d{1,2} Maret \d{4}'  # Mencari pola tanggal
match = re.search(pattern, text)
if match:
    print("Tanggal ditemukan:", match.group())

# 2. Mencari Semua Kecocokan dalam Teks
pattern = r'\d{1,2}'  # Mencari angka dalam teks
matches = re.findall(pattern, text)
print("Angka yang ditemukan:", matches)

# 3. Mengganti Pola dalam String
pattern = r'Maret'
replaced_text = re.sub(pattern, 'April', text)
print("Teks setelah penggantian:", replaced_text)

# 4. Validasi Format Email
email = "user@example.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if re.match(pattern, email):
    print("Email valid")
else:
    print("Email tidak valid")

# 5. Ekstraksi Kata dari Kalimat
text = "Python adalah bahasa yang kuat dan fleksibel!"
pattern = r'\b\w+\b'  # Mencari kata dalam teks
words = re.findall(pattern, text)
print("Kata-kata dalam teks:", words)

# Latihan:
# 1. Buat regex untuk mencocokkan nomor telepon dengan format (XXX) XXX-XXXX.
# 2. Gunakan regex untuk mengekstrak semua alamat email dari sebuah paragraf.
# 3. Cari semua kata yang dimulai dengan huruf kapital dalam sebuah teks panjang.
# 4. Gantilah semua angka dalam teks dengan tanda '#'.
# 5. Validasi apakah sebuah string adalah password yang kuat (minimal 8 karakter, ada huruf besar, kecil, angka, dan simbol).

# Coba selesaikan latihan di atas untuk memperdalam pemahaman regex! 🚀
