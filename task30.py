# Задача 30. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N > 3: '))
temp_list = []
mult_list = []
for i in range(2, n):
    if n % i == 0:
        if i == 2:
            mult_list.append(i)
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                if j == i - 1:
                    mult_list.append(i)
print(mult_list)

with open('simple_multipliers.txt', 'w') as f:
    for el in mult_list:
        f.write(str(el) + ', ')
