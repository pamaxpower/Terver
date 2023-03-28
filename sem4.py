'''Пример теста гипотез
'''

import numpy as np
import scipy.stats as stats

x = np.array([2.5, 2.2, 2.6, 2.0, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9])
y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])
print(x, y)

# считаем среднее арифметическое каждой выборки m
m1 = np.mean(x)  # 2.290909
m2 = np.mean(y)  # 2.081818
print(m1, m2)

# считаем дисперсию d
d1 = np.var(x, ddof=1)  # 0.100909
d2 = np.var(y, ddof=1)  # 0.171636
print(d1, d2)

# считаем значение t-критерия
t = (m1 - m2) / np.sqrt((d1 / len(x)) + (d2 / len(y)))          # 1.328348
print(t)

# сравниваем это значение с таблицным. (Таблица. Двусторонний критерий Стьюдента)
# уровень значимости (по горизонтали) - 0,05 (alpha)
# степень свободы (по вертикали) - 2*(n-1)? где n-1 - степень свободы, 2-две выборки
# по таблице значение равно 2,086 сигм
# на графике: в области [-2,086;2,086] - лежит нулевая гипотеза Н-0
# так как наш показатель 1,3283 лежит внутри Н-0, то статистически значимых отличий между x и y нет
# t < табл.значения, значит гипотеза Н-0 верна

test = stats.ttest_ind(x,y)
print(test)
# Ttest_indResult(statistic=1.3283484757831463, pvalue=0.19902265798859645)
# если p-value > alpha - гипотеза Н-0 - верна
