# Latihan:
import pandas as pd

# 1. Buat DataFrame baru dengan 5 kolom dan minimal 5 baris data.
data ={
    'nama': ['Alif', 'budi', 'citra', 'dhea', 'Didit'],
    'usia' : [27, 25, 26, 23, 24],
    'asal' : ['Bali', 'Jogyakarta', 'Bandung', 'Tanggerang', 'Bandung'],
    'status' : ['menikah', 'menikah', 'lajang', 'lajang', 'lajang'],
    'Pekerjaan' : ['wirausaha', 'Kantoran', 'freelance', 'kantoran', 'wirausaha']
}
df = pd.DataFrame(data)
print("Data Frame:")
print(df)

# 2. Tambahkan kolom baru berdasarkan perhitungan dari kolom lain.
df['Gaji'] = [10000000, 4500000, 3000000, 5000000, 15000000]
print("\nData Frame ditambah gaji:")
print(df)

# 3. Filter data berdasarkan kondisi tertentu.
print("\nData usia di atas 23:")
print(df[df['usia'] > 23])
# 4. Simpan hasilnya ke dalam file CSV.
df.to_csv('latihan.csv', index=False)

# Coba eksplorasi Pandas lebih lanjut! 🚀