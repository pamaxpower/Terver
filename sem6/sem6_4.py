"""
Найдите 95% доверительные интервалы для долей больных, которые чувствовали боли
при включенном и выключенном приборе. 
Можно ли по этим интервалам оценить статистическую значимость различий?
********** - прибор включен - прибор выключен
Боли нет            24              3     
Боли есть           6               17
"""

import numpy as np
import scipy.stats as stats
from math import factorial as fact
from math import pow

m1 = 24
n1 = 30
m2 = 3
n2 = 20
p1 = m1/n1
p2 = m2/n2

def comb (n,k):
    return fact(n) / (fact(k) * fact(n-k))

def check(m, n):
    p = m/n
    if n*p>5 and n*(1-p)>5:
        print('Проверка пройдена. Ищите через стандартную ошибку')
        SE = np.sqrt(p*(1-p) / n)
        print(SE)
        L = np.around(p - np.abs(stats.norm.ppf(0.05/2)) * SE, decimals=2)
        U = np.around(p + np.abs(stats.norm.ppf(0.05/2)) * SE, decimals=2)
        print((L, U))
    else:
        print('Проверка не пройдена. Используйте формулу Бернулли')
        result = 0
        for i in range(n+1):
            c = comb(n,i)
            result = c * pow(i/n, i) * pow(1-i/n, n-i)

            print(i/n, result)
            #if result > 0.95:
                #print(m/n)
        # смотрим картинку и считаем вероятность
        # итог будет [0.04, 0.39]
    
#check(m1, n1)
check(1, 5)

# Вывод интервалы не пересекаются - имеется статитстически значимое различие