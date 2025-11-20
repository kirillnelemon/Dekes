# Выполнил: студент группы РПО-5 Самойлов Максим
# Лабораторная работа №1, вариант №12

import math

# Процедура для работы с вещественными числами
def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

# 1. Создаем значения аргумента x и функций y1, y2 по формулам
x = [i for i in frange(-5.0, -0.0, 0.5)]  # Диапазон от -5 до -0.5 с шагом 0.5
y1 = [2 * math.log(1 + i**2) for i in x]
y2 = [(1 + math.cos(i)**2) ** (3/5) for i in x]

# 2. Создание файла data.txt для записи данных в столбцы
filename = 'data.txt'
with open(filename, 'w') as outfile:
    outfile.write('# значения x, y1 и y2\n')
    for xi, y1i, y2i in zip(x, y1, y2):
        outfile.write('%10.5f %10.5f %10.5f\n' % (xi, y1i, y2i))

# 3. Находим сумму функций y = y1 + y2
y = []
for i in range(len(y1)):
    y.append(y1[i] + y2[i])

# Сортировка суммы по возрастанию
y_sorted = sorted(y)

# 4. Добавление результатов x и отсортированной суммы в файл
with open(filename, 'a') as outfile:
    outfile.write('\n# Результат задания (x и отсортированная сумма)\n')
    for xi, yi in zip(x, y_sorted):
        outfile.write('%10.5f %10.5f\n' % (xi, yi))

# Сравнение min(y1) и min(y2)
min_y1 = min(y1)
min_y2 = min(y2)
print(f"min(y1) = {min_y1:.5f}")
print(f"min(y2) = {min_y2:.5f}")
if min_y1 < min_y2:
    print("min(y1) < min(y2)")
elif min_y1 > min_y2:
    print("min(y1) > min(y2)")
else:
    print("min(y1) = min(y2)")