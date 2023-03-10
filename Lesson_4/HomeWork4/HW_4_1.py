# Даны два неупорядоченных набора
# целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

list_1 = [random.randint(1, 20) for _ in range(int(input()))]
list_2 = [random.randint(1, 20) for _ in range(int(input()))]
my_list = list(set(list_1) & set(list_2))
if my_list != []:
    my_list.sort()
    print(*my_list)
else:
    print("No common numbers")

