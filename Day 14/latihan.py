# Latihan:
import re

# 1. Buat regex untuk mencocokkan nomor telepon dengan format (XXX) XXX-XXXX.
nomor_hp = "(021) 456-7890"
pattern = r'\(\d{3}\) \d{3}-\d{4}'
if re.match(pattern, nomor_hp):
    print("Nomor hp valid")
else:
    print("NOmor hp tidak valid")
# 2. Gunakan regex untuk mengekstrak semua alamat email dari sebuah paragraf.
# 3. Cari semua kata yang dimulai dengan huruf kapital dalam sebuah teks panjang.
# 4. Gantilah semua angka dalam teks dengan tanda '#'.
# 5. Validasi apakah sebuah string adalah password yang kuat (minimal 8 karakter, ada huruf besar, kecil, angka, dan simbol).
