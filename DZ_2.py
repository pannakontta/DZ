#Задание 1

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# res = int(input('Введите предполагаемый результат: '))
# if a * b == res:
#     print ('Верно')
# else:
#     print('Неверно')

#Задача 2

# day = int(input('Введите номер интересующего дня недели: '))
# if day == 1:
#     print('4 пара: Свойства биополимеров')
#     print('5 пара: Анализ биополимеров')
# elif day == 2:
#     print('4 пара: Информационные технологии')
#     print('5 пара: Генаая инженерия')
#     print('6 пара: Английский')
#     print('7 пара: Английский')
# elif day == 3:
#     print('6 пара: Python')
# elif day == 4:
#     print('3 пара: Биостатистика')
#     print('4 пара: Биостатистика')
#     print('5 пара: Основы геномики')
#     print('6 пара: Биокатализ')
# elif day == 5 or day == 6 or day == 7:
#     print('В выбранный день пар нет')
# else: 
    # print "ошибка"

#Задача 4

# a = int(input('Введите число: '))
# b = a / 100
# if 0.1 <= b < 1 or -1 < b <= -0.1:
#     print('Число двузначное')
# else:
#     print('Число не двузначное')


# a = int(input('Введите число: '))
# if -99 <= a <= -10 or 10 <= a <= 99:
#     print('Число двузначное')
# else:
#     print('Число не двузначное')



#Задача 5

# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))
# z = int(input('Введите третье число: '))
# if x >= y and x >= z:
#     print(x)
# elif y >= z:
#     print(y)
# else:
#     print(z)




#Задача 6

# x = int(input('Введите первое число: '))
# o = input('Введите вид математической операции: ')
# y = int(input('Введите второе число: '))
# if y == 0 and o == '/':
#     print('Такая операция недопустима')
# elif o == '*':
#     print('Результат:', x * y)
# elif o == '/':
#     print('Результат:', x / y)
# elif o == '+':
#     print('Результат:', x + y)
# elif o == '-':
#     print('Результат:', x - y)
# elif o == 'mod':
#     print('Результат:', x % y)
# elif o == 'div':
#     print('Результат:', x // y)
# elif o == 'pow':
#     print('Результат:', x ** y)

#Задача 7

# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if b != 0 and a % b == 0:
# #     print('не делится')
# if a != 0 b % a == 0:
# #     print('не делится')
# if a % b > 0:
#     print('Число a не делится нацело на b')
# else:
#     print('Число a делится нацело на b: a/b =', a/b)
# if b % a > 0:
#     print('Число b не делится нацело на a')
# else:
#     print('Число b делится нацело на a: b/a =', b/a)

#Задача 8

# a = int(input('Введите трёхзначное число: '))
# x = a // 100
# y = (a / 10) % 10
y = a // 10 % 10
# z = a % 10
# if x == y or x == z or y == z:
#     print('В числе есть одинаковые цифры')
# else:
#     print('Одинаковых цифр в числе нет')


#Задача 3

# x = 5
# y = 10
# if y > x * x or y >= 2 * x and x < y:
#     print('y > x * x or y >= 2 * x and x < y - True')
# else:
#     print('y > x * x or y >= 2 * x and x < y - False')

"""
1. y >= 2 * x - True (10 >= 5*2)
2. x < y - True (5 < 10)
3. Тогда 1 and 2 - True
4. y > x * x - False (10 < 5*5)
5. Тогда 4 or 3 - True
"""