import numpy as np
import math

lst = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

def find_mediana(array):
    array.sort() 
    if len(array)%2==1:
        mediana = array[len(array)//2]
    else:
        mediana = (array[(len(array)-1)//2] + array[(len(array))//2]) / 2
    return mediana  

def dispersion_1(array, mediana):
    array.sort()
    sum = 0
    for i in range(len(array)):
        sum += (array[i]-mediana)**2
    return sum/len(array)

def dispersion_2(array, mediana):
    array.sort()
    sum = 0
    for i in range(len(array)):
        sum += (array[i]-mediana)**2
    return sum/(len(array)-1)



print(f'{sorted(lst)}\n')

print(f'Среднее арифметическое равно: {sum(lst)/len(lst)}')
print(f'Медиана равна: {find_mediana(lst)}')
print(f'Смещенная дисперсия равна: {dispersion_1(lst,find_mediana(lst))}')
print(f'Смещенное стандартное отклонение: {math.sqrt(dispersion_1(lst,find_mediana(lst)))}')
print(f'Несмещенная дисперсия равна: {dispersion_2(lst,find_mediana(lst))}')
print(f'Несмещенное стандартное отклонение: {math.sqrt(dispersion_2(lst,find_mediana(lst)))}')
print()
print(f'Смещенная: {np.var(lst), np.std(lst)}')
print(f'Несмещенная: {np.var(lst,ddof=1), np.std(lst,ddof=1)}')


