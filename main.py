import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# load dataset
df = sns.load_dataset('titanic')

print(df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

# Biểu đồ 1 - countplot tỉ lệ sống sót
sns.countplot(x = 'survived', hue = 'sex', data = df)
plt.title('Tỉ lệ sống sót theo giới tính')
plt.xlabel('Sống sót')
plt.ylabel('Số lượng')
plt.show()
plt.close()

# Biểu đồ 2 - histogram phân phối tuổi
sns.histplot(df['age'].dropna(), bins = 30, kde = True)
plt.title('Phân phối tuổi của hành khách')
plt.xlabel('Tuổi')
plt.ylabel('Số lượng')
plt.show()
plt.close()

# Biểu đồ 3 - boxplot tuổi theo hạng vé
sns.boxplot(x = 'pclass', y = 'fare', data = df)
plt.title('Giá vé theo hạng vé')
plt.xlabel('Hạng vé')
plt.ylabel('Giá vé')
plt.show()
plt.close()

# Biểu đồ 4 - heatmap tương quan giữa các biến số
sns.heatmap(df.corr(numeric_only = True), annot = True, cmap = 'coolwarm')
plt.title('Bản đồ nhiệt tương quan giữa các biến số')
plt.show()
plt.close()

# Biểu đồ 5 - barplot tỉ lệ sống sót theo giới tính
sns.barplot(x = 'sex', y = 'survived', data = df)
plt.title('Tỉ lệ sống sót theo giới tính')
plt.xlabel('Giới tính')
plt.ylabel('Tỉ lệ sống sót')
plt.show()
plt.close()

# Biểu đồ 6 - pairplot tổng quan
sns.pairplot(df.dropna(), hue = 'survived', vars = ['age', 'fare', 'pclass'])
plt.show()
plt.close()