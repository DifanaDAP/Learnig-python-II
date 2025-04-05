# Day 18 matplotlib & seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# data untuk visualisasi
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 1. line plot dengan matplotlib
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='sin(x)', color='blue')
plt.title('Line plot: sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# 2. scatter plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, c=colors,cmap='viridis')
plt.title('scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# 3 histogram
data_hist = np.random.randn(1000)
plt.hist(data_hist, bins= 30, color = 'purple', alpha = 0.7)
plt.title("histograf data acak")
plt.xlabel("nilai")
plt.ylabel("frekuensi")
plt.show()

# 4. visualisasi dengan seaborn
# Membuat dataframe untuk seaborn
df = pd.DataFrame({
    'kategori': np.random.choice(['A', 'B', 'C'], size=100),
    'nilai': np.random.randn(100)
})

#boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x='kategori', y='nilai', data=df)
plt.title('Boxplot kategori')
plt.show()

# 5. heatmap
data_headmap = np.random.rand(5, 5)
sns.heatmap(data_headmap, annot=True, cmap='coolwarm')
plt.title('headmap')
plt.show()

# Latihan:
# 1. Buat line chart dari fungsi cos(x)
# 2. Buat scatter plot dengan warna berbeda tiap titik berdasarkan kategori
# 3. Buat histogram dari data acak normal dengan 50 bins
# 4. Buat seaborn barplot dari DataFrame yang kamu buat sendiri

# Selamat visualisasi data! 🚀