"""
Логистическая регрессия
"""
import math
import numpy as np
import pandas as pd
from scipy.special import expit


# x1 = np.array([100,40,50,70,50,80,75])
# x2 = np.array([30,20,20,40,30,70,25])
# x3 = np.array([1,0,1,2,0,3,4])
# y = np.array([1,0,1,1,0,1,1])

# df = pd.DataFrame(({'Зарплата': x1, 'Трата на продукты': x2, 'Поездки': x3, 'Возврат кредита': y}))
# print(df)

x1 = np.array([68,72,120])
x2 = np.array([27,40,40])
x3 = np.array([2,0,1])


# modl = -0.18839 + 0.01115 * x1 - 0.00279 * x2 + 0.16286 * x3

for i in range(3):
    print(x1[i], x2[i], x3[i])
    modl = -0.18839 + 0.01115 * x1[i] - 0.00279 * x2[i] + 0.16286 * x3[i]
    sigmoid = expit(modl) # сигмоидная функция 
    #
    print(f'Клиент_{i}: {modl:.4f}, {sigmoid:.4f}')
