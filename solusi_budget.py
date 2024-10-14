import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Membaca dataset
df = pd.read_csv("https://drive.google.com/uc?id=1vooChEw-U_GiiSIbNEogGjpOkIFsZ22a")

# Pembersihan Data: Menghapus baris dengan nilai budget atau year yang hilang
df = df.dropna(subset=['budget', 'year'])

# Mengonversi kolom 'year' menjadi integer dan 'budget' menjadi numeric
df['year'] = df['year'].astype(int)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')

# Menghapus baris dengan budget yang tidak valid setelah konversi
df = df.dropna(subset=['budget'])

# Mengelompokkan data berdasarkan tahun dan menghitung rata-rata budget per tahun
average_budget_per_year = df.groupby('year')['budget'].mean().reset_index()

# Membuat plot tren rata-rata budget per tahun
plt.figure(figsize=(12, 6))
sns.lineplot(data=average_budget_per_year, x='year', y='budget', marker='o')

# Menyesuaikan format sumbu y
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x)))

plt.title('Tren Rata-rata Budget Film per Tahun', fontsize=20)
plt.xlabel('Tahun', fontsize=16)
plt.ylabel('Rata-rata Budget', fontsize=16)
plt.grid(True)
plt.text(0.58, 0.02, 'By Abu Abdirrahman Humaid Al-Atsary', ha='center', va='center', fontsize=14, color='gray', alpha=0.9, transform=plt.gcf().transFigure)
plt.show()
