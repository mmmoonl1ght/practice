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

plt.figure()
plt.boxplot(df['Значение'])
plt.title('Блок-диаграмма распределения')
plt.ylabel('Значение')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('boxplot.png')
plt.show()

# 2. Линейный график (порядок значений)
plt.figure()
plt.plot(df['Значение'], marker='.', linestyle='-', alpha=0.7)
plt.title('Линейный график значений')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('line_plot.png')
plt.show()

# 3. Круговая диаграмма (доли категорий, например, положительные/отрицательные)
positive = (df['Значение'] > 0).sum()
negative = (df['Значение'] < 0).sum()
zero = (df['Значение'] == 0).sum()
plt.figure()
plt.pie([positive, negative, zero], labels=['Положительные', 'Отрицательные', 'Ноль'], autopct='%1.1f%%')
plt.title('Доля положительных и отрицательных значений')
plt.savefig('pie_chart.png')
plt.show()
