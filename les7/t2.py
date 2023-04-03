import numpy as np
import scipy.stats as stats 

# создание двух массивов данных
group1 = [1000,1380,1200]


x1 = [1000,1380,1200]
x2 = [1400,1600,1180,1220]

res = [] # Создаем пустой массив для хранения результата
sum = 0 # Создаем переменную для хранения суммы рангов


for i in range(len(x1)):
    res = [1400,1600,1180,1220]
    res.insert(0, x1[i]) # Берем первый элемент из x1 и ставим его в начало x2
    print(res)
    rslt = np.argsort(res)
    print(rslt)
    sum += rslt[0] # Берем из массива рангов первое значение и вычитаем из этого значения 1
    print(sum)

"""
# объединение двух массивов
all_values = np.concatenate((group1, group2))

# ранжирование значений
ranked_values = np.argsort(all_values)
# print(all_values)
# print(np.sort(all_values))
# print(ranked_values)

# расчет суммы рангов для каждой из групп
ranks_group1 = ranked_values[:len(group1)].sum()
ranks_group2 = ranked_values[len(group1):].sum()
R = max(ranks_group1, ranks_group2)
print(R)

# расчет U-статистики
n1 = len(group1)
n2 = len(group2)
if R == ranks_group1:
    nt = (n1*(n1+1)) / 2
else:
    nt = (n2*(n2+1)) / 2

print(nt)
U1 = n1 * n2 + n1 * (n1 + 1) / 2 - ranks_group1
U2 = n1 * n2 + n2 * (n2 + 1) / 2 - ranks_group2
print(n1*n2)
print(n1 * (n1 + 1) / 2)
print(n1 / (n1 + n2))
print (U1, U2)
U = max(U1, U2)

# U = R - nt
# print(U)



# определение p-value
p = 2 * (1 - (U / (n1 * n2)))

print("Статистика U = %.2f, p-value = %.3f" % (U, p))
"""
print(stats.mannwhitneyu(group1, group2))