'''
iterable - просто итерируемый объект (перечисляемый), эти контейнеры поддерживают функцию len
iter, next - итератор, генерирует значения по требованию, а не все сразу. итераторы не знают сколько
в них элементов (что за значекние будет следующее)

В Python (и не только в нем) есть два понятия, которые звучат практически одинаково, но обозначают разные вещи, — iterator и iterable.
Первое — это объект, который реализует описанный выше интерфейс, а второе — контейнер, который может служить источником данных для итератора.

Итерируемый объект - воспроизводит по одному результату за раз в контексте инструментов выполнения итераций (к примеру цикла for).

В самом начале цикл for получает итератор из итерируемого объекта, передавая его встроенной функции iter,
которая возвращает объект, имеющий требуемый метод __next__. Это станет более очевидным, если посмотреть, на то,
как внутренние механизмы циклов for обрабатывают такие встроенные типы последовательностей, как списки.
'''

L = [1, 2, 3] # у листа не прописна метод next, но его функция итер возвращает объект у которого он есть
# конечно объект листа и объект итератора листа это разные вещи
'''
Действительно, по list’у можно итерироваться, но сам по себе list никак не следит, где там мы остановились в проходе по нему.
А следит объект по имени listiterator, который list возвращается методом iter() и используется, скажем, циклом for или вызовом map().
Когда объекты в перебираемой коллекции кончаются, возбуждается исключение StopIteration.
Списки и многие другие встроенные объекты не имеют собственных итераторов (т.е. они не являются итераторами),
потому что они поддерживают возможность участия сразу в нескольких итерациях.
Чтобы начать итерации по таким объектам, необходимо предварительно вызвать функцию iter (которая и вернёт их итератор,
с помощью которого мы и пройдёмся по последовательности):
'''
I = iter(L) # таких итераторов можно сделать хуеву тучу раз у одного L

print(iter(L))
print(iter(L) is L)

print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__())
print('-' * 40)

# Итерируемые объекты возвращают элементы не в виде списка, а по одному элементу за раз.
R = range(5)
print(R)
I = iter(R)
print(I is R)
print(next(I))
print(list(range(5)))
print('-' * 40)

'''
У объектов файлов есть своя функц некст.
Рекомендуемый в настоящее время способ чтения строк из текстового файла – не читать файл явно вообще. Вместо этого предлагается открыть файл
в итерационном контексте, например в цикле for или в генераторе списков и позволить итерационному инструменту на каждой итерации автоматиче-
ски извлекать по одной строке из файла с помощью метода __next__. Такой подход считается более оптимальным в смысле простоты программирова-
ния, скорости выполнения и использования памяти.
'''
f = open('test-open-file.txt')

print(iter(f) is f)

print(f.__next__().rstrip())
print(f.__next__().rstrip())
print('-' * 40)

'''
list comprehension - способ создания нового списка (генератор списка).
Более того, генераторы списков могут выполняться значительно быстрее (зачастую почти в два раза), чем
инструкции циклов for, потому что итерации выполняются со скоростью языка C, а не со скоростью программного
кода на языке Python. Такое преимущество в скорости особенно важно для больших объемов данных.
'''
lines = [line.rstrip() for line in open('test-open-file.txt')]
print(lines)
lines = [('shit' in line, line) for line in open('test-open-file.txt')]
print(lines)
lines = [line.rstrip() for line in open('test-open-file.txt') if 'shit' in line]
print(lines)
print([x + y for x in 'abc' for y in 'lmn'])
print('-' * 40)

'''
Если файл открыть внутри выражения, генератор списков автоматически будет использовать итерационный протокол,
с которым мы познакомились выше в этой главе. То есть он будет читать из файла по одной строке за раз – вызовом
метода __next__ файла, пропускать строку через функцию rstrip и добавлять результат в список.
И снова мы получаем именно то, что запрашиваем – результат работы метода rstrip для каждой строки в файле.
'''

# iterators
map_iter_obj = map(str.upper, open('test-open-file.txt'))
print(map_iter_obj, list(map_iter_obj))

enum_iter_obj = enumerate(open('test-open-file.txt'))
print(enum_iter_obj, list(enum_iter_obj))

X = (1, 2)
Y = (3, 4)
Z = (5, 6, 7)
zip_iter_obj = zip(X, Y, Z)
print(zip_iter_obj, list(zip_iter_obj))
print('-' * 40)

'''
Создаём из итерируемых объектов кортежи, множества и словари
'''
print(tuple(open('test-open-file.txt')))
print(set(open('test-open-file.txt')))
a, *b = open('test-open-file.txt')
print(a, b, sep='') # a have \n
print('-' * 40)

'''
Генераторы кортежей, множеств и словарей
'''
print({line for line in open('test-open-file.txt')})
print({key: value for key, value in enumerate(open('test-open-file.txt'))})

'''
У словарей keys, values, items - это итерируемые объекты (но они не поддерживают функцию len), их метод итер возвращает их итераторы.
У обычного объекта словаря работает также как и кийс (по сути нет необходимости в dict.keys()).
'''