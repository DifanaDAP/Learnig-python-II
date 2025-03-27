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
paragraf = "Silahkan hubungi kami di support@website.com atau admin@domain.org"
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
emails = re.findall(pattern, paragraf)
print("Email yang ditemukan", emails)

# 3. Cari semua kata yang dimulai dengan huruf kapital dalam sebuah teks panjang.
teks_panjang = "Saya belajar Python di kampus universitas"
pattern= r'\b[A-Z][a-z]*\b'
capital_words = re.findall(pattern, teks_panjang)
print("kata-kata dengan huruf kapital:", capital_words)

# 4. Gantilah semua angka dalam teks dengan tanda '#'.
teks_angka = "Hari ini adalah 5 maret 2025, besok 6 maret"
pattern = r'\d'
teks_hasil = re.sub(pattern, "#", teks_angka)
print("Teks setelah penggantian angka:", teks_hasil)

# 5. Validasi apakah sebuah string adalah password yang kuat (minimal 8 karakter, ada huruf besar, kecil, angka, dan simbol).
password = "Str0ngP@ssword!"
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
if re.match(pattern, password):
    print("password kuat")
else:
    print("password lemah")