"""
На препарате A положительный результат лечения наблюдается у 17 пациентов из 32, 
а на препарате B у 9 из 22. Построить 95% доверительный интервал для разности долей.
Обнаружены ли статистические значимые различия?
Решить через тестирование гипотезы!
"""
# Выдвигаем гипотезы:
# H0: z = z(т)
# H1: z != z(т)

import numpy as np

n1 = 32
m1 = 17
n2 = 22
m2 = 9
p1 = m1/n1
print(f'Доля 1: {p1: .2}')
p2 = m2/n2
print(f'Доля 2: {p2: .2}')
p = (m1+m2) / (n1+n2)
print(f'Общая доля: {p: .2}')

SE = np.sqrt(p * (1 - p) * ((1 / n1) + (1 / n2)))
print(f'Стандартная ошибка разности долей: {SE: .3}')

Z = ((p1-p2) - 0.5 * ((1 / n1) + (1 / n2)))/ SE
print(f'Набледаемое значение Z = {Z: .2}')

# Наблюдаемое значение Z меньше табличного, значит, статистической значимости нет (нулевая гипотеза верна)