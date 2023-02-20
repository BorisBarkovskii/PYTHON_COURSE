# Найдите сумму цифр трехзначного числа.

num = int(input("Введите трехзначное число: "))
num_sum = 0

while num:
    num_sum += num % 10
    num //= 10

print(f"Сумма равна: {num_sum}")
