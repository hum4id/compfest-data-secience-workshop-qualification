import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("https://drive.google.com/uc?id=1vooChEw-U_GiiSIbNEogGjpOkIFsZ22a")

# Calculate mean score for each company
rerata_skor_company = df.groupby('company')['score'].mean().sort_values(ascending=False).head(20).reset_index()

# Create bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x='score', y='company', data=rerata_skor_company, palette='crest')

# Annotate bars with the mean score values
# note: matplotlib.pyplot.text(x, y, s, fontdict=None, **kwargs)
for index, value in enumerate(rerata_skor_company['score']):
    plt.text(value, index, f'{value:.2f}', va='center')

plt.title('Top 20 Companies Berdasarkan Rerata Skor', fontsize=20)
plt.xlabel('Rerata Skor', fontsize=16)
plt.ylabel('Company', fontsize=16)
plt.text(0.58, 0.02, 'By Abu Abdirrahman Humaid Al-Atsary', ha='center', va='center', fontsize=14, color='gray', alpha=0.9, transform=plt.gcf().transFigure)
plt.show()
