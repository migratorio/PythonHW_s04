# Задача 32. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

"""v1. Без создания нового списка"""
def uniq_list_v1(num_list):
    k = 0
    for i in range(len(num_list) - 1):
        x = num_list[i]
        for j in range(i + 1, len(num_list)):
            if x == num_list[j]:
                k = 1
                num_list[j] = None
            if k == 1:
                num_list[i] = None
                k = 0
    num_list = [int(x) for x in num_list if x != None]
    print(num_list)
    with open('task32_hw.txt', 'a') as f:
        f.write(' -> ')
        for el in num_list:
            f.write(str(el) + ' ')

"""v2. С созданием нового списка"""
def uniq_list_v2(num_list):
    uniq_list = []
    for i in range(len(num_list)):
        x = num_list[i]
        for j in range(len(num_list)):
            if x == num_list[j] and i != j:
                break
            elif j == len(num_list) - 1:
                uniq_list.append(int(x))
    print(uniq_list)
    with open('task32_hw.txt', 'a') as f:
        f.write(' -> ')
        for el in uniq_list:
            f.write(str(el) + ' ')

with open('task32_hw.txt', 'w') as num_str:
    num_str.write(input('Введите последовательность чисел через пробел: '))
with open('task32_hw.txt', 'r') as file:
    for num_list in file:
        print(num_list)
num_list = num_list.split()

uniq_list_v1(num_list)
#uniq_list_v2(num_list)
