'''
УПРАВЛЕНИЕ ДОСТУПОМ К АТРИБУТАМ

Методы __getattr__ и __getattribute__перегрузки  операторов  предоставляют  иной  способ  управления  доступом  к атрибутам  классов.
Подобно  свойствам  и дескрипторам  они  позволяют  добавлять  программный код, который будет вызываться автоматически при попытках
обращения к атрибутам, эти два метода обеспечивают более обобщенные способы управления.

Операция чтения значения атрибута может быть перехвачена с помощью двух разных методов: 1) __getattr__ вызывается  при  обращении
к неопределенным атрибутам –  то есть к атрибутам, которые отсутствуют в экземпляре или в наследуемых им классах.
2) __getattribute__ вызывается  при  обращении  к любомуатрибуту,  поэтому при  его  использовании  следует  проявлять
особую  осторожность,  чтобы  не попасть  в бесконечный  цикл  рекурсивных  вызовов  этого  метода,  и переадресовать операции
чтения суперклассу.

Встроенный класс property,  которая  позволяет  определить  для  отдельных атрибутов методы чтения и записи,
такие атрибуты часто называют свойствами. Фактически  свойства  являются  ограниченной  разновидностью  дескрипторов
(упрощает процесс создания дескриптора).
Протокол дескрипторов, который позволяет организовать доступ к ОТДЕЛЬНЫМ атрибутам с помощью экземпляров классов
с произвольными методами чтения и записи.

В property прописаны методы getter, setter и deleter,  которые  присваивают  соответствующие  методы  доступа к
свойству и возвращают копию самого свойства. Мы можем использовать эти
методы,  чтобы  определить  компоненты  свойств,  декорируя  обычные  методы, однако  компонент getter обычно
устанавливается  автоматически,  в процессе создания самого свойства:
'''

'''
def__getattr__(self,name):
вызывается только при попытке обратиться к неопределенному атрибуту, поэтому он может без всякой опаски
обращаться к другим атрибутам в своём теле.
[obj.name]

Однако  методы __getattribute__и __setattr__ вызываются  при  обращении к любым атрибутам,
поэтому внутри них следует проявлять осторожность, когда возникает необходимость обратиться к другим атрибутам,
чтобы избежать повторного вызова этого же метода и попадания в бесконечный цикл рекурсивных вызовов.

def __getattribute__(self, name):
    x = self.other                 # ЦИКЛ!

def __getattribute__(self, name):
    x = object.__getattribute__(self, ‘other’)

def __setattr__(self, name, value):
    self.other = value             # ЦИКЛ!

def __setattr__(self, name, value):
    self.__dict__[‘other’] = value # С использованием словаря атрибутов


def __delattr__(self, name): Удаление любого атрибута
[del obj.name]
'''


class Person:
    def __init__(self, name):
        self._name = name

    # name = property(name)
    @property
    def name(self):
        # “property docs”
        print('fetch...')
        return self._name

    # name = name.setter(name)
    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    # name = name.deleter(name)
    @name.deleter
    def name(self):
        print('remove...')
        del self._name


bob = Person('BobSmith') # Объект bob имеет управляемый атрибут
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)

print('-' * 40)


class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):  # Только для неопределенных атрибутов
        print('get: ' + attr)  # Не attr1: наследуется от класса
        return 3  # Не attr2: хранится в экземпляре


X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-' * 40)


class GetAttribute(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):  # Вызывается всеми операциями присваивания
        print('get: ' + attr)  # Для предотвращения зацикливания
        if attr == 'attr3':  # используется суперкласс
            return 3
        else:
            return object.__getattribute__(self, attr)


Y = GetAttribute()
print(Y.attr1)
print(Y.attr2)
print(Y.attr3)