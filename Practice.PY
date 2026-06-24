import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(-10000, 10001, 200)

df = pd.DataFrame(data, columns=['Значение'])

print("Первые 5 строк:")
print(df.head())

print("\nИнформация о данных:")


print("\nСтатистики:")
print(f"Среднее: {df['Значение'].mean():.2f}")
print(f"Медиана: {df['Значение'].median()}")
print(f"Минимальное: {df['Значение'].min()}")
print(f"Максимальное: {df['Значение'].max()}")
print(f"Сумма: {df['Значение'].sum()}")

plt.hist(df['Значение'], bins=20, edgecolor='black', alpha=0.7)
plt.title('Гистограмма распределения случайных чисел')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig('histogram.png')
plt.show()

