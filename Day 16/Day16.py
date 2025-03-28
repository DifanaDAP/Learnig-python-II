# Day 16 pandas dasar

import pandas as pd

# 1. membuat dataframe dari dictionary
data = {
    'nama' : ['Alya', 'Budi', 'Citra', 'Dedi'],
    'usia' : [23, 25, 22, 24],
    'kota' : ['Jakarta', 'Bandung', 'Surabaya', 'Medan']
}
df = pd.DataFrame(data)
print("Data Frame:")
print(df)

# 2. Membaca data dari file csv
# df_csv = pd.read_csv('data.csv')
# print(df_csv.head())

# 3.Menampilkan informasi data
print("\nInfo Data:")
print(df.info)

print("\nStatistik Deskriptif")
print(df.describe)

# 4. Mengakses Data
print("\nMengakses kolom nama:")
print(df['nama'])

print("\nMengakses baris pertama:")
print(df.iloc[0])

#5. menambah kolom baru
df['Gaji'] = (5000000, 6000000, 5500000, 5800000)
print("\nData frame setelah menambah kolom Gaji")
print(df)

# 6. menghapus kolom
df = df.drop(columns=['kota'])
print("\nData frame setelah menghapus kolom kota:")
print(df)

# 7. Menyaring data
print("\nDAta usia di atas 23 tahun")
print(df[df['usia'] > 23 ])

# 8 menyimpan data ke file csv
df.to_csv('output.csv', index=False)


# Latihan:
# 1. Buat DataFrame baru dengan 5 kolom dan minimal 5 baris data.
# 2. Tambahkan kolom baru berdasarkan perhitungan dari kolom lain.
# 3. Filter data berdasarkan kondisi tertentu.
# 4. Simpan hasilnya ke dalam file CSV.

# Coba eksplorasi Pandas lebih lanjut! 🚀