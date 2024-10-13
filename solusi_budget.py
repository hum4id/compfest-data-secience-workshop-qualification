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


"""
Tentu! Fungsi plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x))) digunakan untuk menyesuaikan format tampilan angka pada sumbu y di plot matplotlib. Mari kita uraikan bagian-bagiannya:

Penjelasan Detail:
plt.gca():

plt.gca() adalah singkatan dari "Get Current Axes". Fungsi ini mengembalikan objek Axes yang saat ini aktif pada plot. Objek Axes ini adalah bagian dari plot di mana sumbu x dan sumbu y berada.
Dengan menggunakan plt.gca(), kita dapat mengakses berbagai properti dari sumbu, seperti format angka, label, dan lain-lain.
yaxis:

yaxis adalah atribut dari objek Axes yang mewakili sumbu y pada plot. Ini memungkinkan kita untuk mengakses dan memodifikasi pengaturan yang terkait dengan sumbu y, termasuk format angka, label, dan ticks.
set_major_formatter:

set_major_formatter adalah metode dari objek yaxis yang digunakan untuk mengatur format tampilan utama (major format) dari sumbu. Format utama adalah format yang digunakan untuk menampilkan nilai-nilai di sumbu utama.
ticker.FuncFormatter:

ticker.FuncFormatter adalah kelas dari modul matplotlib.ticker yang memungkinkan kita untuk menentukan format angka di sumbu dengan menggunakan fungsi khusus.
FuncFormatter menerima sebuah fungsi sebagai argumen. Fungsi ini menentukan bagaimana setiap nilai di sumbu harus diformat.
lambda x, pos: '${:,.0f}'.format(x):

Ini adalah fungsi lambda yang didefinisikan secara inline untuk memformat nilai-nilai pada sumbu.
x: Parameter ini mewakili nilai saat ini pada sumbu yang sedang diformat.
pos: Parameter ini adalah posisi tick pada sumbu dan umumnya tidak digunakan dalam fungsi format ini, tapi disertakan agar fungsi lambda sesuai dengan signature yang diperlukan FuncFormatter.
'${:,.0f}'.format(x): Ini adalah format string Python yang digunakan untuk memformat nilai x.
'${:,.0f}': Format string ini berarti:
$: Menambahkan simbol dolar di depan angka.
{:,.0f}: Menyediakan format angka dengan pemisah ribuan (koma) dan tanpa desimal (0 desimal).
.format(x): Mengganti placeholder {} dengan nilai x yang telah diformat sesuai dengan string format yang diberikan.
Contoh
Jika x bernilai 1234567.89, maka '{:,.0f}'.format(x) akan menghasilkan '1,234,568', dan dengan menambahkan simbol dolar di depannya, hasil akhirnya adalah $1,234,568.

Tujuan Penggunaan
Dengan menggunakan ticker.FuncFormatter, kita memastikan bahwa angka-angka pada sumbu y ditampilkan dalam format yang lebih informatif dan mudah dibaca, seperti mata uang, dengan pemisah ribuan dan tanpa desimal jika relevan. Ini sangat membantu terutama ketika angka-angka besar perlu ditampilkan dengan cara yang lebih mudah dipahami oleh pengguna.
"""






"""
SOLUSI AWAL

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset
url = "https://drive.google.com/uc?id=1vooChEw-U_GiiSIbNEogGjpOkIFsZ22a"
df = pd.read_csv(url)

# Menampilkan beberapa baris pertama dari dataset untuk memahami strukturnya
print(df.head())

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
plt.title('Tren Rata-rata Budget Film per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata Budget (dalam juta USD)')
plt.grid(True)
plt.show()
 """