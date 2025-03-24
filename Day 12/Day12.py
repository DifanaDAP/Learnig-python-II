# Day 12: Virtual Environment dalam Python

# Apa itu Virtual Environment?
# Virtual Environment (venv) adalah fitur Python yang memungkinkan kita untuk membuat lingkungan Python terisolasi,
# sehingga paket-paket yang diinstal tidak akan mempengaruhi sistem utama atau proyek lainnya.

# 1. Membuat Virtual Environment
# Untuk membuat virtual environment, jalankan perintah berikut di terminal atau command prompt:
# Windows:
#   python -m venv myenv
# macOS/Linux:
#   python3 -m venv myenv

# 2. Mengaktifkan Virtual Environment
# Windows:
#   myenv\Scripts\activate
# macOS/Linux:
#   source myenv/bin/activate

# 3. Memeriksa Virtual Environment Aktif
# Setelah diaktifkan, prompt terminal akan berubah dan menunjukkan nama virtual environment di awal.
# Untuk memeriksa Python yang digunakan:
#   python --version
#   which python (Linux/macOS) atau where python (Windows)

# 4. Menginstal Paket di Virtual Environment
# Setelah mengaktifkan environment, kita bisa menginstal paket menggunakan pip:
#   pip install numpy pandas matplotlib
# Untuk menyimpan daftar paket yang terinstal:
#   pip freeze > requirements.txt

# 5. Menonaktifkan Virtual Environment
# Untuk keluar dari virtual environment, cukup jalankan perintah berikut:
#   deactivate

# 6. Menggunakan requirements.txt untuk Menginstal Paket
# Jika bekerja dalam tim, kita bisa membagikan file requirements.txt agar orang lain dapat menginstal paket yang sama:
#   pip install -r requirements.txt

# Latihan
# 1. Buat virtual environment baru dan aktifkan.
# 2. Instal beberapa paket seperti numpy, pandas, dan matplotlib di dalamnya.
# 3. Simpan daftar paket ke dalam file requirements.txt.
# 4. Coba nonaktifkan dan aktifkan kembali virtual environment.
