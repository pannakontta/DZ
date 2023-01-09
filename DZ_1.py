
#Задание 2 (исправленное)
# name = input('Ваше имя: ')
# surname = input('Ваша фамилия: ')
# dish = input('Укажите Ваше любимое блюдо: ')
# print('Пользователь', name, surname, 'любит есть', dish + '.')
# print('Порадуемся за него!')

'''
#Задание 3
dpoint = input('Укажите Ваш пункт отправления: ')
apoint = input('Укажите Ваш пункт прибытия: ')
print(dpoint, '-',apoint)
'''
'''
#Задание 4
a = input('First word: ') 
b = input('Second word: ') 
print(a, b) 
c = a
a = b
b = c
print(a, b)
'''
'''
#Задание 5
a = int(input('Введите первое число: ')) 
b = int(input('Введите второе число: '))
ra = a%10
rb = b%10
print('Ответ:', ra + rb)
'''

'''
#Green Red Blue RedRedGreen BlueGreen Green

#Задание 1
r = 'Red' 
g = 'Green' 
b = 'Blue' 
print(g, r, b, r + r + g, b + g, g) 
'''

#Задание 6
# a = int(input('Введите четырёхзначное число: '))
# ua = a%10
# ta = a%100
# tta = int((ta - ua)/10)
# ha = a%1000
# hha = int((ha - ta)/100)
# tha = a//1000
# print('Обратное число: ', ua, tta, hha, tha)

# на занятии
a = 1234
b = a
num4 = a % 10 #4
a //= 10 #123
num3 = a % 10
a //= 10 #12
num2 = a % 10
a //= 10 #1
num1 = a % 10
a = b
print(num4, num3, num2, num1)
print(int(str(num4)+str(num3)+str(num2)+str(num1)))

#
res = 0
res = res * 10 + num4
res = res * 10 + num3
res = res * 10 + num2
res = res * 10 + num1
print(res)

#Задание 6 (исправленное)
# a = int(input('Введите четырёхзначное число: '))
# ua = a%10
# ta = a%100
# tta = int((ta - ua)/10)
# ha = a%1000
# hha = int((ha - ta)/100)
# tha = a//1000
# a = str(ua)+str(tta)+str(hha)+str(tha)
# a = int(a)
# print('Обратное число: ', a)


