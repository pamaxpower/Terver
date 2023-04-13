"""
Встроенная функция для построения линейной регрессии
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

model = LinearRegression()  # задаем мат.модель

s = np.array([27,37,42,48,57,56,77,80])             # площадь квартиры
p = np.array([1.2,1.6,1.8,1.8,2.5,2.6,3,3.3])       # стоимость

s = s.reshape((-1,1))    # создаем матрицу 8 строк, 1 столбец на основании массива s
print(s)

regres = model.fit(s,p) # подбираем коэффициенты

print(regres.intercept_)    # выводим интерсепт
print(regres.coef_)         # выводим коэффициенты

y_pred = model.predict(s)   # считаем предиктовые значения p
print(y_pred)

plt.scatter(s,p)
plt.plot(s, 0.1715 + 0.0387*s)
plt.show



