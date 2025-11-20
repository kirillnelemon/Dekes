# print("Hello")
# #Функция которая выводит текст в консоль
# Name = input("Введите ваше имя:")
# Age = int(input("Введите ваш возраст:"))
# water = 4.5
# print(type(Age), type(Name), type(water))
# print("Привет,", Name, "тебе" , Age , "лет")
# print('Я пью', water , 'литра воды')
# #format - Форматирования строки и # вставка переменных напрямую
# Age = int(input('Возраст:'))
# Name = input('Имя:')
# s_name =input('Фамилия:')
# date = input('Дата рождения:')
# print(f'Ваши переданные данные:')
#     f"1.Возраст:{Age} n\"
#     f"2.Имя:{Name} n\"
#     f"3.Фамилия:{s_name} n\"
#     f"4.Дата рождения:{date} n\"
#
#
#
# print("Я сегодня встал рано на пары.", "Мне очень хочется спать."
#        "Но я пересилил себя и пошёл получать знания.",
#       sep="^^^", end= '@'
#       )
# print('Успешного дня')
# ```
# Ариф. Операция
# + - * /
# ** - операция возведения в степень
# print(2**2) #4
# // - деление целочисленное
# print(2//4)# DIV 0
# % - деление по остатку
# print(5%2) # 1
# sum() - сумма переданных элементов
# min() - минимальный элемент
# max() - максимальный элемент

# Как не делить
# 1. Деление на ноль
# 2. Деление целого числа на ноль
# 3. Нахождения остатка от деления на ноль
#
# РЕР-8 Руководство по коду на Python
# 1) Имена функций, переменных, классов, должны состоять из маленьких букв, а слово разделяется
# символами подчёркивания - это необходимо, чтобы их было легче прочитать(fun, my_fun)
# 2)Нельзя давать имена, которые зарегистрированы в самом Python: int, False, True, None, if, in, from. return, list, float,...

# my_var = 100
# my_var = my_var + 200 + 300
# my_var += 200 + 300
# print(my_var)



#Практика 2
# Задание 1
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# sum_number = a + b + c
# pro_number = a * b * c
# print(sum_number)
# print(pro_number)

#Задание 2
# Month = int(input('Введите зп за месяц'))
# credit = int(input('Введите сумму кредита в банке за месяц'))
# Communal_services = int(input('Введите задолженность за коммунальные услуги'))
# raz_number = Month - credit - Communal_services
# print(raz_number)

#Задание 3
# d1 = int(input("Введите длину диагонали: "))
# d2 = int(input("Введите длину диагонали: "))
# S_Romb = (d1 * d2) / 2
# print(S_Romb)

#Задание 4
#print("To be\nor not\nto be")

#Задание 5
#print("Life is what happens\n                      when\n                            you're busy making other plans\"\n                                                             Jonh Lennon")

#Практика 1
#Задание 1
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# sum_number = a + b + c
# pro_number = a * b * c
# Change = int(input('Выберете действие'))
# if Change == 1:
#     print(sum_number)
# if Change == 2:
#     print(pro_number)

#Задание 2
# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
# Arifm = (a + b + c) / 3
# Change = int(input('Выберете действие'))
# if Change == 1:
#     print(max)
# if Change == 2:
#     print(min)
# if Change == 3:
#     print(Arifm)

#Практика 2

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))


# n = int(input())
# if n % != 0:
#     print('Делится на 7')
# n = 957
# print(n % 10)# посл цифра
# print(n // 10)# отсекает последнюю цифру

# n = int(input('Enter number:'))
#
# a = n % 10
# n = n // 10
# b = n % 10
# n = n // 10
# c = n % 10
# print(a + b + c)



#Блок 1 задание 2

# a = int(input('Введите число'))
# b = (a % 10)
# if b < a:
#     print('Первое число меньше')
# else:
#     print('Первое число больше')



#Блок 2 задание 1

# r = int(input('Введите число'))
# S = 3.14 * r ** 2
# C = 2 * 3.14 * r
# print(S)
# print(C)


#блок 2 задание 2
# year = int(input('Введите возраст'))
# if year > 18 or year = 18:
#     print('Пропуск в стрипуху разрешён')
# else:
#     print('Пропуск запрещён! Гуляй малолетка')

#блок 2 задание 3

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
#
# if a >= b  and a >= c:
#     print(a)
# if b >= a and b >= c:
#     print(b)
# if c >= a and c >= b:
#     print(c)

#блок 2 задание 4

# a = int(input('Введите сторону треугольника'))
# b = int(input('Введите сторону треугольника'))
# c = int(input('Введите сторону треугольника'))
#
# if (b + c > a) and (c + a > b) and (b + a > c):
#     print('Такой треугольник существует')
# else:
#     print('Такого трегольника не существует')


# Week_day = int('Введите число')
# if Week_day == 1:
#     print('Понедельник')
# elif Week_day == 2:
#     print('Вторник')
# elif Week_day == 3:
#     print('Среда')
# elif Week_day == 4:
#     print('Четверг')
# elif Week_day == 5:
#     print('Пятница')
# elif Week_day == 6:
#     print('Суббота')
# elif Week_day == 7:
#     print('Воскресенье')


# Mouth = int(input('Введите номер месяца'))
# if Mouth == 1:
#     print('Январь')
# elif Mouth == 2:
#     print('Февраль')
# elif Mouth == 3:
#     print('Март')
# elif Mouth == 4:
#     print('Апрель')
# elif Mouth == 5:
#     print('Май')
# elif Mouth == 6:
#     print('Июнь')
# elif Mouth == 7:
#     print('Июль')
# elif Mouth == 8:
#     print('Август')
# elif Mouth == 9:
#     print('Сентябрь')
# elif Mouth == 10:
#     print('Октябрь')
# elif Mouth == 11:
#     print('Ноябрь')
# elif Mouth == 12:
#     print('Декабрь')

# a = int(input('Введите число'))
# if a > 0:
#     print('Number is positive')
# if a < 0:
#     print('Number is negative')
# if a == 0:
#     print('Number is equal to zero')

# a = int(input('Введите число'))
# b = int(input('Введите число'))
#
# if a == b:
#     print('А всё')
# elif a < b:
#     print(a,b)
# elif a > b:
#     print(b,a)

# a = int(input('Введите число'))
# if 1 <= a <= 100:
#     if a % 3 == 0:
#         print('Fizz')
#     elif a % 5 == 0:
#         print('Buzz')

#     elif a % 5 == 0 and a % 3 == 0:

#     elif a % 5 == 0 and a % == 0:

#         print('Fizz Buzz')
#     else:
#         print(a)
#
# else:
#     print('Неверно')


# user_string = input("Введите ариф. выражение:")
# result = ''
# value1 = ''
# value2 = ''
# letter = ''
# letter_index = 0
# for i in range (0,len(user_string)):
#     if user_string[i] in '+-*/':
#         letter = user_string[i]
#         letter_index = i
# #поиск первого числа
# for i in range(0, letter_index):
#     value1 += user_string[i]
# #поиск второго
# for i in range(letter_index + 1, len(user_string)):
#     value2 += user_string[i]
# value1 = int(value1)
# value2 = int(value2)
# if letter == '+':
#     result = value1 + value2

#Практика 2 Задание 1

# a = int(input('Введите число'))
# b = int(input('Введите число'))
# c = int(input('Введите число'))
#
# sum_numbers = a + b + c
# pro_result = a * b * c
# print(sum_numbers, pro_result)
#Задание 2
# a = int(input('Введите зарплату'))
# b = int(input('Введите кредит в банке'))
# c = int(input('Введите задолженность'))
#
# razn_number = a-b-c
# print(razn_number)

#Задание 3
# d1 = float(input('Введите длину диагонали'))
# d2 = float(input('Введите длину диагонали'))
#
# area = (d1 * d2) / 2
#
# print('Площадь ромба:', area)


#Задание 4
#print('To be', 'or not', 'to be', sep = '\n')

#  for i in range(0, 10): #условие цикла
#   выполнение внутреннего кода
# for i in range(10, 0, -1):
#     print('Hello', i)
#while(условие)
#while True:
#    print('*')
# value_user = 1
# sum_user = 0
# while value_user != 0: #Пока выполняется условие
#     value_user = int(input('Введите число суммирования'))
#     sum_user = sum_user + value_user
# print('Сумма числа пользователя:', sum_user)
# for i in range(0, 6):
#     print('*' * i)
#Пользователь вводит строку
#необходимо её проверить на палиндроме
#кок, а буду я у дуба.
# user_string = input('Введите строку для проверки на Палиндром: ')

# counter_letter = len(user_string)#фунция подсчёта кол-во элементов

# counter_letter = len(user_string)#функция подсчёта кол-во элементов

# value_user = True #Переменнная для проверки палиндромов
# for letter_begin in range(0, counter_letter):
#     for letter_end in range(counter_letter, 0, -1):
#         print('Проверяется буква:',user_string[letter_begin])
#         print('Проверяется буква:',user_string[letter_end])
#         if letter_end != letter_end:
#             break
#     if value_user == False:
#         print('Слово не является палиндромом')
#         break


# elif letter == '-':
#     result = value1 - value2
#
# elif letter == '*':
#     result = value1 * value2
#
# elif letter == '/':
#     result = value1 / value2
# print('Вычисление равно:', result)

# user_input = input('Введите строку: ')
# reversed_string = user_input[: : -1]
# print('Результат:', reversed_string)


#Практика 2
#задание 1
# week = int(input("Ввести номер дня недели: "))
# if week == 1:
#     print("Понедельник")
# if week == 2:
#     print("Вторник")
# if week == 3:
#     print("Среда")
# if week == 4:
#     print("Четверг")
# if week == 5:
#     print("Пятница")
# if week == 6:
#     print("Суббота")
# if week == 7:
#     print("Воскресенье")
#задание 2
# month = int(input("Введите месяц: "))
# if month == 1:
#     print("Январь")
# if month == 2:
#     print("Февраль")
# if month == 3:
#     print("Март")
# if month == 4:
#     print("Апрель")
# if month == 5:
#     print("Май")
# if month == 6:
#     print("Июнь")
# if month == 7:
#     print("Июль")
# if month == 8:
#     print("Август")
# if month == 9:
#     print("Сентябрь")
# if month == 10:
#     print("Октябрь")
# if month == 11:
#     print("Ноябрь")
# if month == 12:
#     print("Декабрь")
#задание 3
# a = int(input("Введите число: "))
# if a > 0:
#     print("Number is positive")
# if a < 0:
#     print("Number is negative")
# if a == 0:
#     print("Number is zero")
# срез - подстрока или подмассив извлечённый из основного можно состоять из 1-n символов или элементов
# 1. взятие одного символа
# 2. Срез в двумя параметрами
# print(string[0:6])
# #[a:b] - интервал символов
# #find and rfind
# #нужны для поиска подстроки в строке
# print(string.find('l')) #Вернёт индекс элемента
# #Если элемента не, то -1
# print(string.rfind('l'))
# #find - ищет с лева направо
# #rfind - щет справа на лево
# #METHOD REPLACE - замена одной стр на другую
# print(string.replace('l'))
# #METHOD COUNT - считает кол-во вхождений символа в строку
# print(string.count('l'))
# # Список (массив) - послед элементов
# #пронумер от 0, как символы в строке
# Primes = [2, 3, 5, 7, 11, 13]
# print(Primes)
# print(Primes.count(3))
# print(type(Primes))
# Rainbow = ['red' , 'orange' , 'yellow' , 'green' , 'blue' , 'purple']
# print(f'кол-во цветов радуги: {len(Rainbow)} ')
# for i in Rainbow:
#     print(i, end=' ')
# print()
# # добавление и удаление элементов списка
# my_list = []
# count_list = int(input('Введите кол-во элементов: '))
# for i in range(count_list):
#     print(f"Введите элемент {i}")
#     new_element = int(input("->:"))
#     my_list.append(new_element)#Добавление нового
# print(my_list)
# print(my_list.pop())# удаление посл элемента
# #Методы join и split
# # 1 2 3
# user_str = input()
# user_list = user_str.split()
# print(string.split('l'))
# for i in range (len(user_list)):
#     user_list[i] = int(user_list[i])#Преобр типа
#
# print(''.join(Rainbow))# объединение строк
# #генератор списков
#
# n = 5
# #способ 1
# list_gen1 = []
# for i in range(n):
#     list_gen1.append(i*n)
# print(f"Первый способ {list_gen1}")
# #способ 2
# list_gen2 = [i*n for i in range(0, n)]
# print(f"Второй способ {list_gen2}")
#
# #Практика
# #Задание 1
# from random import randint
# list1 = []
# for i in range(len(list1)):
#     list1[i] = randint(0, 10)
# print(f"Вывод списка {list1}")
# from time import time
# x = [5] * 1_000_000_000
# start = time()
# x.append(0, 999)
# stop = time()
# print(stop - start)
# x = [100, 222, 5454, 7777]
# print(x[3])
# x.append(5)
# x.append(999)
# print(x)
# x.insert(2, 999)
# print(x)
# x.pop(2)

#print(123)

# from time import time
#
# x = [5] * 1_000_000
# start = time()
# for i in range(5):
#     x.pop(0)
#
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.pop()
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.append(999)
# #x.insert(0, 999)
# stop = time()
# print(stop - start)
#
# start = time()
# for i in range(5):
#     x.insert(0, 999)
# stop = time()
# print(stop - start)

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num)

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
#
# # 1. Все числа диапазона
# print("\n1. Все числа диапазона:")
# for num in range(start, end + 1):
#     print(num, end=" ")
#
# # 2. Все числа диапазона в убывающем порядке
# print("\n\n2. Все числа диапазона в убывающем порядке:")
# for num in range(end, start - 1, -1):
#     print(num, end=" ")
#
# # 3. Все числа, кратные 7
# print("\n\n3. Все числа, кратные 7:")
# for num in range(start, end + 1):
#     if num % 7 == 0:
#         print(num, end=" ")
#
# # 4. Количество чисел, кратных 5
# print("\n\n4. Количество чисел, кратных 5:")
# count = 0
# for num in range(start, end + 1):
#     if num % 5 == 0:
#         count += 1
# print(count)



#Практика 2 списки

# Задание 1: Произведение элементов списка
# def multiply_list(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result

# Задание 2: Поиск минимума без встроенных функций
# def find_min(numbers):
#     if not numbers:
#         return None
#     min_val = numbers[0]
#     for num in numbers:
#         if num < min_val:
#             min_val = num
#     return min_val

# Задание 3
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(numbers):
#     count = 0
#     for num in numbers:
#         if is_prime(num):
#             count += 1
#     return count

# Задание 4
# def remove_number(numbers, target):
#     initial_len = len(numbers)
#     numbers[:] = [x for x in numbers if x != target]
#     return initial_len - len(numbers)



#append(5)
#insert(0, 5)
#pop()
#pop(0)

# s = "gfhcv"
# A = set(s)
# print(A)
# if len(A) == len(s):
#     print("Все символы уникальны")
# else:
#     print("есть повторения")
#
# x = 5
# y = 0
# if x > 1 or x / y == 2:
#     print(1)
# else:
#     print(2)

# A = {1, 2, 3, 4, 5}
# if 20 in A:
#     print('Yes')
# else:
#     print('No')



# s = input('Введите пароль')
# A = set(s)
# if len(A) == len(s):
#     print("Все символы уникальны")
# else:
#     print("есть повторения")

# cities = ['Москва', 'Владивосток', 'Казань', 'Сочи', 'Омск', 'Питер', 'Омск','Владивосток']
# a = set(cities)
# print(a)
# if 'Пермь' in a:
#     print('Пермь есть')
# else:
#     print('Пермь нет')

# math_failers = {'Быстров', 'Исаев', 'Силизнёв', 'Черемных', 'Алиев'}
# rus_failers = {'Войтович', 'Кириллов', 'Гущин', 'Быстров'}
# inf_failers = {'Войтович', 'Силизнёв', 'Гущин', 'Самойлов'}
# print(rus_failers | math_failers | inf_failers)
#
# print(rus_failers & inf_failers)
#
# print(rus_failers - math_failers - inf_failers)
# print(math_failers - rus_failers - inf_failers)
# print(inf_failers - math_failers - rus_failers)
#
# print(math_failers & rus_failers & inf_failers)


#площадь круга
# def calculate_circle_area(radius):
#     area = 3.14 * radius * radius
#     return area
# print(calculate_circle_area(10))
# #площадь прямоугольника
# def get_rectangle_area(a, b):
#     a = int(input('введите длинну: '))
#     b = int(input('введите ширину: '))
#     area = a * b
#     print('площадь прямоугольника', area)
#
# # длинна окружности
# def get_circle_len(radius):
#     circle_len = 2 * 3.14 * radius
#     return circle_len
# 
#
# print('1. ассчитать площадь круга')
# print('2. ассчитать площадь треугольника')
# print('3. ассчитать длинна круга')
# print('0. выход')
# menu_choice = input('Введите пункт меню:')
#
# if menu_choice == "1":
#     pass#что-то делаем
# if menu_choice == "2":
#     get_rectangle_area()
# if menu_choice == "3":
#     pass# get_circle_len()
# if menu_choice == "0":
#     pass# что-то делаем

# import random
# N = 10
# list_booble = []
# for i in range(N):
#     list_booble.append(random.randint(-10, 10))
# print(f"Начальный список: {list_booble}")
#
# for i in range (N):
#     for j in range(N - 1 - i):
#         if list_booble[j] > list_booble[j + 1]:
#             list_booble[j], list_booble[j + 1] = list_booble[j+1], list_booble[j]
# print(f"финальный список: {list_booble}")

# import random
# N = 20
# list_booble = []
# for i in range(N):
#     list_booble.append(random.randint(-10, 10))
# print(f"Начальный список: {list_booble}")
#
# for i in range (N//2):
#     for j in range(N//2 - 1 - i):
#         if list_booble[j] < list_booble[j + 1]:
#             list_booble[j], list_booble[j + 1] = list_booble[j+1], list_booble[j]
#
# for i in range (N//2):
#     for j in range(N//2, N - 1):
#         if list_booble[j] > list_booble[j + 1]:
#             list_booble[j], list_booble[j + 1] = list_booble[j+1], list_booble[j]
#
# print(f"финальный список: {list_booble}")

#Кортежи(tuple) - это неизменяемая структура данных, кот. по своему подобию похожа на список.
# list = [1, 2, 3]
# list.append(2)
# list.pop()
# del list
# tupleB = tuple(4, 5, 6)
# tupleA = (1, 2, 3)
# print(type(tupleA))
# print(tupleA)
# #tupleA[1] = 20 #TypeError
# #Удаление кортежей
# del tupleB
# print(tupleB)

#Преобразование типа
# list = [1, 2, 3, 4, 5]
# print(type(list), list)
# tpl = tuple(list)
# print(type(list), tpl)
#
# #Словари = это неупорядочная структура данных, позволяет хранить пары "Ключ - значение"
# dictionari = {
#                 "Персона": "Человек",
#                 "Марафон": "Гонка беунов длинной около 26 миль",
#                 "Противостояние": "Оставаться сильным, несмотря на сложность"
#                 "Бежать": "Даигаться быстрее"
#
#               }
# gender_dict = {0: "Жен", 1: "Муж"}
# story_count = {"Сто": 100, "Девяносто":90,"Десять":10,  "Пять": 5}
# '''
# dict = { (1, 2, 3) :"Кортеж может быть ключём",
#         "Бежать":"Строка тоже",
#         ['носок', 1, 2]:"списки не могут"
#         1.0: "Дробный тип нем могут"
#         }
# Изм. типы данных в качестве ключа выступать не могут(HEXЭШИРУЕТСЯ)
# int(1) = float(1.0) = True
#
#
# '''
# d = {}
# d = {"dict_key":1, "dictionary":2}
# print(d)
# d = dict( [(1,1), (2,1)] )
# d_str = (  ("ab", "cd")  )
# d = dict.fromkeys(['a','b'])
# print(d)
# key_list = ['marvel', 'dc']
# value_list = ['Spiderman', 'Flash']
# superhero_dict = dict(zip(key_list, value_list))
# print(superhero_dict)
# d = {a : a**2 for a in range(7)}
# print(d)
# #Добавление пар
# d['туфля'] = 'обувь'
# print(d)
# #Удаление пар
# del d['туфля']
# superhero_dict.clear() #Очистка словаря
# b = d.copy() #Копирование словаря
# print(d.get(1))
# #d.update('ключ': 'значение', 'ключНовый':'ЗначениеНовогоключа'
# #d.values()
# #d.items()
# #d.keys()
# for key, value in story_count.items():
#     print(key, value)
# for key in story_count.keys():
#     print(key)
# #Множество - set
# sets = {0,1,2,3,4}
# fset = frozenset({2,3,4})
# lists = [1,2,3,4]
# tuples = (7,8,9)
# new_set = sets.union(lists, tuples, fset)
# #set.intersection()
# #set.difference()
# #set.symmotrie_difference()
# #set.copy()
# #set.update()
# #set.intersection_update()
# #set.symmetrie_difference_update()
# #set.add()
# set.remove

# import random
#
# # Задание 1
# print("ЗАДАНИЕ 1")
# print("=" * 50)
#
# # Создаем список из 20 случайных элементов от -10 до 10
# original_list_1 = [random.randint(-10, 10) for _ in range(20)]
# print(f"Начальный список: {original_list_1}")
#
# # Находим середину списка
# mid = len(original_list_1) // 2
#
# # Сортируем левую половину по возрастанию, правую - по убыванию
# left_sorted = sorted(original_list_1[:mid])
# right_sorted = sorted(original_list_1[mid:], reverse=True)
#
# # Объединяем обе половины
# result_1 = left_sorted + right_sorted
# print(f"Результат: {result_1}")


# # Задание 1
# def print_quote():
#     print("\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"")
#     print("\nBill Gates")
#
#
# # Задание 2
# def print_even_numbers(start, end):
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             print(num, end=' ')
#     print()
#
#
# # Задание 3
# def draw_square(side_length, char, filled):
#     for i in range(side_length):
#         if filled or i == 0 or i == side_length - 1:
#             print(char * side_length)
#         else:
#             print(char + ' ' * (side_length - 2) + char)
#
#
#
#     print("Задание 1:")
#     print_quote()
#
#     print("\nЗадание 2:")
#     print_even_numbers(3, 11)
#
#     print("\nЗадание 3 (пустой квадрат):")
#     draw_square(5, '*', False)
#
#     print("\nЗадание 3 (заполненный квадрат):")
#     draw_square(5, '*', True)
#ПРАКТИКА 1
# import random
# class Number:
#     def __init__(self, list1):
#         self.list1 = list1
#         self.count = len(self.list1)
#         self.drob = int(self.count*0.66)
#
#     def print(self):
#         print("Текущий список:", list1)
#     def mysort(self):
#         srsum = 0
#         for i in self.list1:
#             srsum += 1
#         srsum = srsum/self.count
#         if srsum > 0:
#             for i in range(self.drob):
#                 for j in range(self.drob-1-i):
#                     if self.list1[j] > self.list1[j+1]:
#                         self.list1[j], self.list1[j+1] = self.list1[j+1], self.list1[j]
#             self.printf()
#         else:
#             for i in range(self.count - self.drob):
#                 for j in range(self.count - self.drob-1-i):
#                     if self.list1[j] > self.list1[j+1]:
#                         self.list1[j], self.list1[j+1] = self.list1[j+1], self.list1[j]
#             self.printf()

# list1 = [random.randint(-10, 10) for i in range(10)]
# number = Number(list1)
# number.printf()
# number.mysort()

#ПРАКТИКА 2
# class Student:
#     def __init__(self, grades):
#         self.grades = grades
#         self.count = len(grades)
#
#     def printf(self):
#         print("Оценки студента:", self.grades)
#
#     def resit_exam(self):
#         try:
#             index = int(input("Введите номер оценки (от 1 до 12): ")) - 1
#             if 0 <= index < self.count:
#                 new_grade = int(input("Введите новую оценку (1-12): "))
#                 if 1 <= new_grade <= 12:
#                     self.grades[index] = new_grade
#                     print("Оценка изменена.")
#                 else:
#                     print("Ошибка: оценка должна быть от 1 до 12.")
#             else:
#                 print("Ошибка: неправильный номер.")
#         except ValueError:
#             print("Ошибка ввода.")
#
#     def check_scholarship(self):
#         avg = sum(self.grades) / self.count
#         print(f"Средний балл: {round(avg, 2)}")
#         if avg >= 10.7:
#             print("Студент получает стипендию.")
#         else:
#             print("Студент не получает стипендию.")
#
#     def sort_grades(self):
#         choice = input("Сортировать по возрастанию (введите +) или по убыванию (введите -): ")
#         if choice == "+":
#             for i in range(self.count - 1):
#                 for j in range(self.count - i - 1):
#                     if self.grades[j] > self.grades[j + 1]:
#                         self.grades[j], self.grades[j + 1] = self.grades[j + 1], self.grades[j]
#         elif choice == "-":
#             for i in range(self.count - 1):
#                 for j in range(self.count - i - 1):
#                     if self.grades[j] < self.grades[j + 1]:
#                         self.grades[j], self.grades[j + 1] = self.grades[j + 1], self.grades[j]
#         else:
#             print("Ошибка: неизвестный выбор.")
#         self.printf()
#
#
# grades = []
#
# print("Введите 10 оценок (от 1 до 12):")
# for i in range(10):
#     while True:
#         try:
#             n = int(input(f"Оценка {i + 1}: "))
#             if 1 <= n <= 12:
#                 grades.append(n)
#                 break
#             else:
#                 print("Оценка должна быть от 1 до 12.")
#         except ValueError:
#             print("Введите число!")
#
# student = Student(grades)
# while True:
#     print("\nМеню:")
#     print("1 - Вывести оценки")
#     print("2 - Пересдать экзамен")
#     print("3 - Проверить, выходит ли стипендия")
#     print("4 - Отсортировать список")
#     print("0 - Выход")
#
#     choice = input("Выберите пункт меню: ")
#
#     if choice == "1":
#         student.printf()
#     elif choice == "2":
#         student.resit_exam()
#     elif choice == "3":
#         student.check_scholarship()
#     elif choice == "4":
#         student.sort_grades()
#     elif choice == "0":
#         print("Выход из программы.")
#         break
#     else:
#         print("Неверный выбор.")



'''
# 1. Как в программе представлены дни рождения?
Ответ: В программе дни рождения представлены как числа от 1 до 365, где каждое число соответствует дню в году
(1 = 1 января, 365 = 31 декабря). Это позволяет эффективно сравнивать совпадения.

# 2
# Было:
if not (1 <= num_bdays <= 100):
# Заменить на:
if num_bdays < 1:

# 3
TypeError: 'str' cannot be interpreted as an integer

# 4
months = ["January", "February", ..., "December"]

# 5
# Было:
if i % 10000 == 0:
    print(f"{i} simulations run...")
# Замените на:
if i % 1000 == 0:
    print(f"{i} simulations run...")


'''


# class ListProcessor:
#     def __init__(self):
#         self.lists = []
#         self.combined_list = []
#
#     def input_lists(self):
#         print("Введите четыре списка целых чисел:")
#         for i in range(4):
#             while True:
#                 try:
#                     user_input = input(f"Список {i + 1} (через пробел): ")
#                     numbers = list(map(int, user_input.split()))
#                     self.lists.append(numbers)
#                     break
#                 except ValueError:
#                     print("Ошибка! Введите целые числа через пробел.")
#
#     def combine_lists(self):
#         """Объединение всех списков"""
#         self.combined_list = []
#         for lst in self.lists:
#             self.combined_list.extend(lst)
#         return self.combined_list
#
#     def combine_unique_lists(self):
#         """Объединение только уникальных элементов"""
#         self.combined_list = []
#
#         # Создаем множества для каждого списка
#         sets = [set(lst) for lst in self.lists]
#
#         # Находим элементы, которые уникальны для каждого списка
#         for i, current_set in enumerate(sets):
#             other_sets = sets[:i] + sets[i + 1:]  # Все множества кроме текущего
#
#             for element in current_set:
#                 # Проверяем, что элемент отсутствует во всех других списках
#                 is_unique = True
#                 for other_set in other_sets:
#                     if element in other_set:
#                         is_unique = False
#                         break
#
#                 if is_unique:
#                     self.combined_list.append(element)
#
#         return self.combined_list
#
#     def sort_list(self, order='asc'):
#         """Сортировка списка"""
#         if order == 'asc':
#             self.combined_list.sort()
#         elif order == 'desc':
#             self.combined_list.sort(reverse=True)
#         return self.combined_list
#
#     def linear_search(self, target):
#         """Линейный поиск"""
#         for i, value in enumerate(self.combined_list):
#             if value == target:
#                 return i
#         return -1
#
#     def binary_search(self, target):
#         """Бинарный поиск (требует отсортированный список)"""
#         left, right = 0, len(self.combined_list) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#             if self.combined_list[mid] == target:
#                 return mid
#             elif self.combined_list[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         return -1
#
#     def display_lists(self):
#         """Отображение всех списков"""
#         print("\nВведенные списки:")
#         for i, lst in enumerate(self.lists, 1):
#             print(f"Список {i}: {lst}")
#
#     def display_result(self):
#         """Отображение результата"""
#         print(f"Объединенный список: {self.combined_list}")
#
#
# def main():
#     processor = ListProcessor()
#
#     while True:
#         print("\n" + "=" * 50)
#         print("=" * 50)
#         print("1. Объединение всех элементов")
#         print("2. Объединение уникальных элементов")
#         print("3. Выйти")
#
#         choice = input("Выберите задание (1-3): ")
#
#         if choice == '3':
#             print("Выход из программы.")
#             break
#
#         if choice not in ['1', '2']:
#             print("Неверный выбор! Попробуйте снова.")
#             continue
#
#         # Ввод списков
#         processor.input_lists()
#         processor.display_lists()
#
#         if choice == '1':
#             # Задание 1
#             processor.combine_lists()
#             print("\n--- Задание 1 ---")
#             print("Все списки объединены.")
#
#         elif choice == '2':
#             # Задание 2
#             processor.combine_unique_lists()
#             print("\n--- Задание 2 ---")
#             print("Объединены только уникальные элементы.")
#
#         processor.display_result()
#
#         # Сортировка
#         sort_choice = input("\nВыберите сортировку (1 - по возрастанию, 2 - по убыванию): ")
#         if sort_choice == '1':
#             processor.sort_list('asc')
#             print("Список отсортирован по возрастанию.")
#         elif sort_choice == '2':
#             processor.sort_list('desc')
#             print("Список отсортирован по убыванию.")
#         else:
#             print("Сортировка не выполнена.")
#
#         processor.display_result()
#
#         # Поиск
#         try:
#             search_value = int(input("\nВведите значение для поиска: "))
#
#             if choice == '1':
#                 # Линейный поиск для Задания 1
#                 index = processor.linear_search(search_value)
#                 if index != -1:
#                     print(f"Значение {search_value} найдено на позиции {index}")
#                 else:
#                     print(f"Значение {search_value} не найдено")
#
#             elif choice == '2':
#                 # Бинарный поиск для Задания 2
#                 index = processor.binary_search(search_value)
#                 if index != -1:
#                     print(f"Значение {search_value} найдено на позиции {index}")
#                 else:
#                     print(f"Значение {search_value} не найдено")
#
#         except ValueError:
#             print("Ошибка! Введите целое число для поиска.")
#
#
# if __name__ == "__main__":
#     main()

# import pygame
# import random
# from py2048_classes import Board
# from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)
#
# TEXT_DARK = pygame.Color(119,118,100)
# TEXT_LIGHT = pygame.Color(255, 255, 255)
# BACKGROUND = pygame.Color(188, 173, 159)
# EMPTY = pygame.Color(286, 192, 178)
# TITLE_MAX = pygame.Color(18,91, 146)
# CELL_STYLES = {
# 0: {"font": TEXT_DARK, "fill": EMPTY},
# 1: {"font": TEXT_DARK, "fill": pygame.Color(239,229,218)},
# 2: {"font": TEXT_DARK, "fill": pygame.Color(238,225,199)},
# 3: {"font": TEXT_DARK, "fill": pygame.Color(242,177,121)},
# 4: {"font": TEXT_LIGHT, "fill": pygame.Color(245,149,99)},
# 5: {"font": TEXT_LIGHT, "fill": pygame.Color(247,127,96)},
# 6: {"font": TEXT_LIGHT, "fill": pygame.Color(246,94,59)},
# 7: {"font": TEXT_LIGHT, "fill": pygame.Color(241,219,147)},
# 8: {"font": TEXT_LIGHT, "fill": pygame.Color(237,204,97)},
# 9: {"font": TEXT_LIGHT, "fill": pygame.Color(235,193,57)},
# 10: {"font": TEXT_LIGHT, "fill": pygame.Color(231,181,23)},
# 11: {"font": TEXT_DARK, "fill": pygame.Color(192,154,16)},
# 12: {"font": TEXT_LIGHT, "fill": pygame.Color(94,218,146)},
# 13: {"font": TEXT_LIGHT, "fill": pygame.Color(37,187,100)},
# 14: {"font": TEXT_LIGHT, "fill": pygame.Color(35,140,81)},
# 15: {"font": TEXT_LIGHT, "fill": pygame.Color(113,180,213)},
# 16: {"font": TEXT_LIGHT, "fill": pygame.Color(25,130,205)}
#
# }
# BORDER_WIDTH = 10
# TILE_SIZE = 100
# NUMBER_OF_ROWS = NUMBER_OF_COLUMNS = 4
# SCREEN_WIDTH = SCREEN_HEIGHT = ((NUMBER_OF_ROWS + 1)*BORDER_WIDTH) + (NUMBER_OF_ROWS*TILE_SIZE)
# FONT_SIZE = 24
#
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, row, column, value=None):
#         super(Tile, self). __init__()
#         self.font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
#         self.x_pos = BORDER_WIDTH + (row * (BORDER_WIDTH + TILE_SIZE))
#         self.y_pos = BORDER_WIDTH + (column * (BORDER_WIDTH + TILE_SIZE))
#         self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
#         self.value = value
#         self.update(value)
#     def update(self, value):
#         self.change_fill(value)
#         self.change_text(value)
#         self.value = value
#     def change_fill(self, value):
#     def change_text(self, value):
#         if value:


