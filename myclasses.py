
class MyFerstClassHuman:
    gender_man = "male"
    gender_woman = "female"

    def __init__(self, name, birth_day, height, color_hair, location):
        self.name = name
        self.birth_day = birth_day
        self.height = height
        self.color_hair = color_hair
        self.location = location

    def age(self):
        import datetime
        return datetime.datetime.now().year - self.birth_day

    @property
    def sity(self):
        print("ВОУ! Москвич!" if self.location == "Moscow" else "Переферийник....")

    @classmethod
    def dfltcolor(cls, name, birth_day, height, location):
        return cls(name, birth_day, height, "black", location)

    @classmethod
    def dflth(cls, name, birth_day, color_hair, location):
        return cls(name, birth_day, 180, color_hair, location)


class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self._balance = balance

    def add(self, sum):
        self._balance += sum

    def withdraw(self, sum):
        self._balance -= sum

    def getbalance(self):
        return self._balance if self._balance != 0 else "ur BALANCE = 0 !"


class Shape:
    def __init__(self):
        print('Shape object created')

    def draw(self):
        print('Drawing shape')

    def area(self):
        print('Calc area')

    def perimeter(self):
        print('Calc perimeter')


class Rect(Shape):
    pass

    # Домашнее задание по классам!!!


class DomZ:
    # условие на приём аргументов при создании обьекта класса:
    def set(self, text, somedig):
        if type(somedig) == int:
            self.sd = somedig
        else:
            self.sd = 0
        if type(somedig) == str:
            self.txt = text + somedig
        else:
            self.txt = text

    # init с уловиями метода SET :
    def __init__(self, text, somedig=0):
        self.set(text, somedig)

    # Вывод параметров обьекта класса:
    def display(self):
        print(self.txt, self.sd)

    # Документация через метод:
    def __doc__(self):
        return "Это домашнее задание по классам."


# Материнский класс(родительский)
class TestParentClass:
    def __init__(self, age):
        self.age = age
        print("Это вывод из материнского класса")


# Наследование
class TestchClass(TestParentClass):
    def __init__(self, age, name):
        # TestParentClass.__init__(self,age,name) #необходимо чтобы у наследника были атрибуты родительского класса
        # после переобределения конструктора (__init__) , иначе будет ошибка при попытке вызова age/name.
        self.name = name
        super().__init__(age)  # ЛУЧШЕ ИСПОЛЬЗОВАТЬ функцию "super()" ! чем вызывать __init__ из родительского
        # класса! При этом указывать self не нужно т.к он и так вызывается автоматически при вызове функции.
        # Также с помощью функции super() можно бращаться к любому методу родительского класса и если не находит нужного
        # то ищет его по всему "дереву" наследования!!! ЭТО ОЧЕНЬ ВАЖНО !
        # Положение функции super() имеет значение!!!(ДО self.name = name или ПОСЛЕ)

        print("Это вывод из наследника")


class Test_123:
    def set(self, n):
        if n == 0:
            self.num = 300
        else:
            self.num = n

    def get(self):
        print("Значение", self.num)

    def __init__(self, n=0):
        self.set(n)
        print("Создан обьект класса.")
        self.get()


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# Самостоялка

class AccountInBank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # при вызове print(обьект класса) будет заданная строка:
    def __str__(self):
        return f"Владелец счета {self.owner} \nБаланс {self.balance}"

    ###
    def deposit(self, sum):
        self.balance += sum
        print(f"Внесение {sum} выполнено.")

    def withdraw(self, sum):
        if sum >= self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= sum
            print(f"Снятие {sum} выполнено.")


###Область видимости для класса
# name = 'Popka'
#
# class Pac:
#     name = 'Ivan'
#     def print_name():
#         print(name)
# p = Pac()
# print(p.name) #===>> Ivan
# p.print_name()#===>> Popka
# ###

class Person_exap:
    def __init__(self, name):
        self._name = name

    # Перенаправление обращения к _name
    def get_name(self):
        print('From get')
        return self._name

    def set_name(self, value):
        print('From set')
        self._name = value

    #
    name = property(fget=get_name, fset=set_name)
    # ИЛИ: (абсолютно то же самое)
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)


# Использование обьекта класса в качестве ключа в словаре:
# class Exmp_Hash:
#     def __init__(self,value):
#         self._value = value
#     @property
#     def value(self):
#         return self._value
#     def __hash__(self):
#         return True#hash(self.value)
#     def __eq__(self, exmp_obj):
#         return isinstance(exmp_obj,Exmp_Hash) and self.value == exmp_obj.value
#
# some_key = Exmp_Hash(["12"])


# ДЕСКРИПТОРЫ многократно уменьшают обьём кода (так же как и миксины)!!! класс-дескриптор (Decrit_Exempl) можно
# использовать многократно для разных классов с похожим поведением атрибутов. В них реализовываются методы SET,GET
# или (ещё есть setname) DELETE (или все вместе) :
class Exmp_For_Description:
    def __init__(self, name, surname):
        self._name = Decrit_Exempl(name)
        self._surname = Decrit_Exempl(surname)

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname


class Decrit_Exempl:
    def __init__(self, value=None):
        if value:  # если значение вообще пришло
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


# Пример № 2: Игры с рандомом
from random import choice


class Choice_descrp:
    def __init__(self, *mychoice):
        self._mychoice = mychoice

    def __get__(self, obj, owner):
        return choice(self._mychoice)


class Game:
    dice = Choice_descrp(1, 2, 3, 4, 5, 6)
    flip = Choice_descrp('Орёл', 'Решка')
    rock_paper = Choice_descrp('rock', 'paper', 'sci')


# Пример № 3: Показывает время в данный момент (в секундах)
from time import time


class Ep:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    ep = Ep()


class str_exp:
    def __init__(self, some_str):
        self.some_str = some_str

    def __str__(self):
        return self.some_str.upper()

    def __len__(self):
        return len(self.some_str) + 15


class My_Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        del_item = self.array.pop()
        return del_item

    def __iter__(self):
        self.index = len(self.array) - 1
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        result = self.array[self.index]
        self.index -= 1
        return result


# свой класс для ошибок:
# class BadError(Exception):
#     pass

# def sub(a, b):
#     try:
#         print(a/b)
#     except BadError:
#         print("Bad Zero Division Error")
#     #except ZeroDivisionError:
#         #print("Zero Division Error")
#
# sub(10, 0) # Zero Division Error
from typing import Optional, List


class Character_Exp_Hints:

    def __init__(self, armor: Optional[int], powers: List[int]):
        self.powers = powers
        self.armor = armor
        self.health = 100

    def hit(self, damage: int):
        self.health -= damage

    def is_allowed(self):
        return self.health > 0

#обьявление абстрактного метода / класса :
#from abc import *

# class Cars_exp(metaclass=ABCMeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         print(self.name, self.age)

#class OloExp:
#     static_attributes = [1, 2]
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#     #Статикметод полностью изолирован от класса и обьектов каласса! потому как ему ничего не передается
#     #(ни cls(класс) ни self) , он не имеет ниначто ссылок!
#     @staticmethod
#     def pow_i(val):
#         return f"Передано аргументом значение: {val}"
#     #Имеет доступ только к атрибутам класса в том числа и к статикметодам.
#     @classmethod
#     def exp_i(cls,val):
#         cls.static_attributes.append(val)
#         return cls.static_attributes
#
# some_obj_cl = OloExp(10,5)
#
# print(some_obj_cl.pow_i(3))
# print(OloExp.exp_i(19))
# print(some_obj_cl.static_attributes)
# print(some_obj_cl.exp_i(99))
# print(some_obj_cl.static_attributes)

class MyDict(dict):
    def __missing__(self, key):
        self[key] = rval = []
        return rval

    def __str__(self):
        return super().__str__()

    __doc__ = ("Переобределили метод __missing__ в словарях, у несуществующего "
               "ключа будет всегда знананениче [] (пустой список)")