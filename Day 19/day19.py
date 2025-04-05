# Day 19 basic sql with sqlite

import sqlite3

# 1. membuat koneksi dan kursor
db = sqlite3.connect("contoh.db")
cursor = db.cursor()

# 2. membuat tabel
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nama TEXT NOT NULL,
               usia INTERGER NOT NULL)
               ''')

# 3. menambahkan data
cursor.execute("INSERT INTO users (nama, usia ) VALUES( ?, ?)", ('Alice', 20))
cursor.execute("INSERT INTO users (nama, usia) VALUES (?, ?)", ('Bob', 30))
db.commit()

# 4. menampilkan data
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
print("Data pengguna:")
for row in data:
    print(row)

# 5. update data
cursor.execute("UPDATE users SET usia = ? WHERE nama = ?", (28, "Alice"))
db.commit()

# 6. Delete data
cursor.execute("DELETE FROM users WHERE nama = ?", ("Bob",))
db.commit()

# 7 Tampilkan data setelah perubahan
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
print("\nData Setelah perubahan:")
for row in data:
    print(row)

# Tutup koneksi
db.close()

# Latihan:
# 1. Tambahkan 3 data pengguna baru.
# 2. Tampilkan hanya pengguna dengan usia > 25.
# 3. Buat tabel baru bernama 'produk' dengan kolom id, nama_produk, harga.
# 4. Tambahkan 2 produk, lalu tampilkan seluruh isi tabel produk.