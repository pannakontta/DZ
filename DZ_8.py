# dict = {}
# words = input('Введите строку: ').replace(',', '').replace('.', '')
# list_w = words.lower().split()
# print(list_w)
# dict[list_w[0]] = 0
# for i in list_w:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)


s = '''Когда Антон прочитал "Войну и мир", ему стало интересно, 
сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, 
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и 
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз'''

def prepare_string (s: str):
    return s.replace('"', '').replace('(', '').replace(')', '').replace(',', '').replace('.', '').lower()

s = prepare_string(s)
d = {}
for w in s.split():
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

# for key in d:
#     print(f'{key} {d[key]}')

'''Подсчет букв и их процентное содержание'''

for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

# for key in d:
#     print(f'{key} {d[key] / len(s) * 100}'[0:7])


d = sorted(d.items()) #получаются кортежи
for key, val in d:
    print (f'{key} {round(val / len(s) * 100, 3)}')

'''Другой споосб подсчета букв'''

sorted_keys = sorted(d)
for key in sorted_keys:
    print(key, d[key])