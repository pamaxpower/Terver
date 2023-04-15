"""
"""

import numpy as np
import scipy.stats as st

y1 = np.array([70, 50, 65, 60, 75, 67, 74])
y2 = np.array([80, 74, 90, 70, 75, 65, 85])
y3 = np.array([148, 142, 140, 150, 160, 170, 155])

k = 3   # кол-во групп
n = len(y1) * 3     # число всех элементов во всех группах

ym1 = np.mean(y1)
ym2 = np.mean(y2)
ym3 = np.mean(y3)
print(f'Средние для каждой выборки:\ny1={ym1},\ny2={ym2},\ny3={ym3}')

total = np.array([y1, y2, y3])
print(total)
ymt = np.mean(total)
print(f'Среднее по всех значениям групп: {ymt}')

# Сумма квадратов отклонений от общего среднего
s = np.sum((total - ymt)**2)
print(f'Сумма квадратов отклонений от общего среднего: {s}')

# Сумма квадратов отклонений средних групповых от общего среднего
sf = np.sum((ym1-ymt)**2)*len(y1) + np.sum((ym2-ymt)**2)*len(y2) + np.sum((ym3-ymt)**2)*len(y3)
print(f'Сумма квадратов отклонений средних групповых от общего среднего: {sf}')

# Остаточная сумма  квадратов отклонений
so = np.sum((y1-ym1)**2) + np.sum((y2-ym2)**2) + np.sum((y3-ym3)**2)
print(f'Остаточная сумма отклонений: {so}')

Df = sf / (k-1)
print(f'Факторная дисперсия равна: {Df}')

Do = so / (n-k)
print(f'Остаточная дисперсия равна: {Do}')

Fn = Df/Do
print(f'\nНаблюдаемый критерий Фишера: {Fn}\n')

f =st.f_oneway(y1,y2,y3)
print(f)

# Вывод: Fn > f, значит, есть статистичеки значимые различия: принимаем H1.

