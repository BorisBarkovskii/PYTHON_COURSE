# Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках
# не настолько просто, насколько
# легко он их придумывает,
# Вам стоит написать программу.

# Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова,
# если во фразе несколько слов,
# то они разделяются дефисами.

# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает
# в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке

alp = "аеёиоуыэюя"
word_sug = input().split()
vowel_letters = [word.count(char) for word in word_sug
                 for char in word if char.lower() in alp]

if len(set(vowel_letters)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

# 2 вариант

# def vowels_counter(S):
#     vowels = list('а е ё и о у ы э ю я'.split())
#     vowels_counter = list()
#     for i in S:
#         counter = 0
#         for ch in i:
#             if ch in vowels:
#                 counter += 1
#         vowels_counter.append(counter)
#     return vowels_counter

# s = list("ff ff ff".split())  # можно заменить на input().split()

# print("Парам пам-пам" if len(set(r := vowels_counter(s))) == 1 and r[0] != 0 else "Пам парам")