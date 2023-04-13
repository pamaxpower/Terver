"""
Метод построения математическое регрессии. Математические формулы.
"""
import numpy as np
s = np.array([27,37,42,48,57,56,77,80])             # площадь квартиры
p = np.array([1.2,1.6,1.8,1.8,2.5,2.6,3,3.3])       # стоимость

n = len(s)

b1 = (n*np.sum(p*s) - np.sum(s) * np.sum(p)) / (n*np.sum(s**2) - np.sum(s)**2)  # 1 способ
print(b1)       # 0.03875

# b1 = (np.mean(p*s) - np.mean(s) * np.mean(p)) / (np.mean(s**2) - np.mean(s)**2) # 2 способ
# print(b1)       # 0.03875

b0 = np.mean(p) - b1*np.mean(s)
print(b0)           # 0.01715

y_pred = b0 + b1 * s
print(f'y-предсказанная: {y_pred}') 

mse = ((p-y_pred)**2).sum() / n
print(f'Средняя квадратичная ошибка: {mse: .4f}')