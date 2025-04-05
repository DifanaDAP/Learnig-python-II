# Latihan:
import sqlite3

db = sqlite3.connect("Latihan.db")
cursor = db.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nama TEXT NOT NULL,
               usia INTEGER NOT NULL)
               ''')
cursor.execute("INSERT INTO users (nama, usia) VALUES( ?, ?)", ('Alice', 20))
cursor.execute("INSERT INTO users (nama, usia) VALUES (?, ?)", ('Bob', 30))

# 1. Tambahkan 3 data pengguna baru.
pengguna_baru =[
    ("Charlie", 22),
    ("David", 36),
    ("Edward", 24)
]
cursor.executemany("INSERT INTO users (nama, usia) VALUES (?, ?)", pengguna_baru)
db.commit()

# menampilkan semua data pengguna
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
for row in data:
    print(row)

# 2. Tampilkan hanya pengguna dengan usia > 25.
cursor.execute("SELECT * FROM users WHERE usia > 25")
print("\nPengguna dengan usia > 25:")
for row in cursor.fetchall():
    print(row)

# 3. Buat tabel baru bernama 'produk' dengan kolom id, nama_produk, harga.
cursor.execute('''
               CREATE TABLE IF NOT EXISTS produk(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nama_produk TEXT NOT NULL,
               harga REAL NOT NULL)
               ''')

# 4. Tambahkan 2 produk, lalu tampilkan seluruh isi tabel produk.
produk = [
    ("Laptop", 15000000), 
    ("Smartphone", 5000000)
]
cursor.executemany("INSERT INTO produk (nama_produk, harga) VALUES (?, ?)", produk)
db.commit()

cursor.execute("SELECT * FROM produk")
print("\nData produk:")
for row in cursor.fetchall():
    print(row)

# tutup koneksi
db.close()