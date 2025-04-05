# Latihan:
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 1. Buat line chart dari fungsi cos(x)
x_cos = np.linspace(0, 10, 100)
y_cos = np.cos(x_cos)
plt.plot(x_cos, y_cos, label='cos(x)', color='green')
plt.title("line chart: Cos(x)")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True)
plt.legend()
plt.show()

# 2. Buat scatter plot dengan warna berbeda tiap titik berdasarkan kategori
kategori = np.random.choice(['x', 'y', 'z'], size= 50)
df_scatter = pd.DataFrame({
    'x' : np.random.rand(50),
    'y' : np.random.rand(50),
    'kategori' : kategori
})
plt.figure(figsize=(6,4))
sns.scatterplot(data=df_scatter, x='x', y='y', hue='kategori')
plt.title('Scatter plot berdasarkan kategori')
plt.show()

# 3. Buat histogram dari data acak normal dengan 50 bins
hist_data = np.random.randn(1000)
plt.hist(hist_data, bins=50, color='orange', alpha=0.8)
plt.title('Histogram normal distriburion')
plt.xlabel('nilai')
plt.ylabel('frekuensi')
plt.show()

# 4. Buat seaborn barplot dari DataFrame yang kamu buat sendiri
df_bar = pd.DataFrame({
    'kelompok' : ['A', 'B', 'C', 'D'],
    'jumlah' : [ 23, 45, 12, 77]
})
plt.figure(figsize=(6,4))
sns.barplot(x='kelompok', y='jumlah', data=df_bar, palette='pastel')
plt.title('barplot dari Dataframe')
plt.show()
# Selamat visualisasi data! 🚀