# Задача 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
poly_temp = []
k = int(input('Введите натуральное число, соответствующее степени многочлена: '))
if k == 0:
    print('0 = 0')
    exit()
for i in range(k, -1, -1):
    q = random.randint(1, 100)
    if q == 0 and i != 0:
        continue
    elif i > 1:
        poly_temp.append(str(q) + '*x**' + str(i))
    elif i == 1:
        poly_temp.append(str(q) + '*x')
    elif i == 0 and q != 0:
        poly_temp.append(str(q))
polynom = ''
for i in range(len(poly_temp) - 1):
    polynom += poly_temp[i] + ' + '
polynom += poly_temp[len(poly_temp) - 1] + ' = 0'

file = open("creat_polynom.txt", "w")
file.write(polynom)
