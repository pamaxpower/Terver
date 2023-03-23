import numpy as np
import pandas as pd
#z = np.array([1,2,4,1,1,5,7,2,3,5,7,8])
z = np.arange(1, 11)
z = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
def find_perc(array):
    array.sort() 
    print(array)
    print(len(array))

    if len(array)%2==1:
        mediana = array[len(array)//2]
        arr1 = array[:len(array)//2+1]
        if len(arr1)%2==1:
            q1 = arr1[len(arr1)//2]
        else:
            q1 = (arr1[(len(arr1)-1)//2] + arr1[(len(arr1))//2]) / 2
        arr2 = array[len(array)//2:]
        
        if len(arr2)%2==1:
            q3 = arr2[len(arr2)//2]
        else:
            q3 = (arr2[(len(arr2)-1)//2] + arr2[(len(arr2))//2]) / 2

    else:
        mediana = (array[(len(array)-1)//2] + array[(len(array))//2]) / 2
        arr1 = array[:len(array)//2]
        if len(arr1)%2==1:
            q1 = arr1[len(arr1)//2]
        else:
            q1 = (arr1[(len(arr1)-1)//2] + arr1[(len(arr1))//2]) / 2
        arr2 = array[len(array)//2:]
        if len(arr2)%2==1:
            q3 = arr2[len(arr2)//2]
        else:
            q3 = (arr2[(len(arr2)-1)//2] + arr2[(len(arr2))//2]) / 2
    

    print(f'Первая квартиль равен: {q1}')
    print(f'Мидиана равна: {mediana}')
    print(f'Третья квартиль равен: {q3}')
    print(f'Межквартильное расстояние равно: {q3-q1}')

find_perc(z)
print(f'Среднее арифметическое: {sum(z)/len(z)}')

print(np.quantile(z, 0.25))
print(np.median(z))
print(np.quantile(z, 0.75))

print(np.std(z))            # смещенное стандартное отклонение
print(np.var(z))            # смещенная дисперсия

print(np.std(z,ddof=1))     # несмещенное стандартное отклонение
print(np.var(z,ddof=1))     # несмещенная дисперсия
print(np.sqrt(np.var(z,ddof=1)))    # несмещенное стандартное отклонение



