import random


'Задача 1'

'1 variant'

# N = int(input('Введите длину стороны квадрата: '))
# CH = input('Введите символ: ')
# print((CH + ' ') * N)
# for i in range(N-2):
#     print(CH + ((N * 2 - 3) * ' ') + CH)
# print((CH + ' ') * N)

'2 variant'

# N = int(input('Введите длину стороны квадрата: '))
# CH = input('Введите символ: ')
# # for i in range(N):
# #     print((CH + ' ') * N)

# print((((f'{CH} ' *  N) + '\n') * N)[:-1])


'Задача 2'

'1 variant'

# lst = [random.randint(0, 100) for _ in range(5)]
# print(lst)
# i = 0
# while i < 5:
#     if lst[i] > 50:
#         i += 1
#     else:
#         print(False)
#         break
# if i == 5:
#     print(True)

'2 variant'

# lst = [random.randint(0, 100) for _ in range(5)]
# print(lst)
# for i in lst:
#     if i > 50:
#         if i == lst[4]:
#             print(True)
#     else:
#         print(False)
#         break



# lst = [random.randint(0, 100) for _ in range(5)]
#     flag = True
#     for i in lst:
#         if i < 50:
#             flag = False
#             break
#     print(lst)
#     print(flag)


# def foo():
#     for i in lst:
#         if i < 50:
#             return False
#     return True


# if min(lst) < 50:
#     print(False)
# else:
#     print(True)







'Задача 3'

# lst = []
# dad_lst = ['молоко', 'огурцы', 'пиво', 'рыбка']
# gmom_lst = ['чай', 'сахар', 'сухарики']
# lst = dad_lst + gmom_lst
# lst.remove('пиво')
# lst.remove('рыбка')
# items = 0
# for i in lst:
#     print(i)
#     items += 1
# print(f'В списке покупок {items} пунктов')


# lst = []
# lst.append('молоко')
# lst.append('огурцы')
# lst.append('пиво')
# lst.append('рыбка')
# lst.append('чай')
# lst.append('сахар')
# lst.append('сухарики')

# lst += ['молоко', 'огурцы', 'пиво', 'рыбка']
# lst += ['чай', 'сахар', 'сухарики']
# lst.extend(['чай', 'сахар', 'сухарики'])


'Задача 4'

# lst = [random.randint(1, 10) for _ in range(10)]
# num = int(input('Введите число: '))
# print(lst)
# find_num = 0
# for i in lst:
#     if i == num:
#         find_num = i
# if find_num == num:
#     print('Такое число в списке есть')
# else:
#     print('Такого числа в списке нет')

# lst = [random.randint(1, 10) for _ in range(10)]
# num = int(input('Введите число: '))
# print(lst)
# if num in lst: 
#     print(True)
# else:
#     print(False)




'Задача 5'

# lst = [random.randint(1, 10) for _ in range(10)]
# num = int(input('Введите число: '))
# print(lst)
# count_num = 0
# for i in lst:
#     if i == num:
#         count_num += 1
# print(f'Число {num} встречается в списке {count_num} раз(a)')



# lst = [random.randint(1, 10) for _ in range(10)]
# num = int(input('Введите число: '))
# print(lst)
# print(lst.count(num))