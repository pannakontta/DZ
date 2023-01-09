#Задача №1

# s1 = input('Введите первую строку: ')
# s2 = input('Введите вторую строку: ')
# if len(s1) < 2 or len(s2) < 2:
#     print('Error')
# elif s1 > s2:
#     print(s1)
# else:
#     print (s2)

#Задача №2

# s = input('Введите четное количество символов: ')
# l = int(len(s) / 2)
# if l % 2 > 0:
#     print(s[:l:2] + s[l::2])
# else:
#     print(s[:l:2] + s[l+1::2])



#Задача №3
# e = input('Your e-mail: ')
# if e[0] == '.'or e[0] == '-' or e[0] == '_' or e[0] == '@' or \
#     e.count('.') == 0 or e.count('@') == 0 or e.count('@') > 1 or e.count('.@') >> 0 or e.count('@.') >> 0 or\
#     e[-1] == '.'or e[-1] == '-' or e[-1] == '_' or e[-1] == '@' or\
#     len(e) >> 32:
#     print('Unavailable e-mail')
# else:
#     print('Correct')


#Задача №4

# s = input('Введите несколько слов через пробел: ')
# print('Количество введенных слов:', len(s.split()))

# print(s.strip().count(' ') + 1)


#Задача №5


# s = input('Введите строку: ')
# print('Сколько раз встречается ch:', s.count('ch'))


i = 5
while i > 0:
    print(i)
    i -= 1
