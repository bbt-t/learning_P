# from contextlib import suppress
# # from datetime import *
# a = [1, ]
#
# remove_error = suppress(IndexError)
#
# with remove_error:
#     print(a[20])


# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# list_a.extend(list_b)
# result = set()
# for item in list_a:
#     if list_a.count(item) == 2:
#         result.add(item)
# print(list(result))
#               Лучшая практика чтобы узнать перремечения 2х списков:
# result_in_gen = [a for a in list_a for b in list_b if a == b]
# print(result_in_gen)
# import itertools
# from collections import namedtuple
#
# l_list = ['math', 'bio', 'geo']
# Students = namedtuple('ST', ('name', *l_list))
# mark_s = Students('Petya', *(5, 2, 3))
# print(mark_s)
#
# print(mark_s._asdict()['geo'])

# from collections import defaultdict
#
# some_d = {'a':1,'b':2,'c':3}
#
# some_d = defaultdict(int,some_d)
# print(type(some_d['d']))


###
#      В качестве "несуществующего" ключа по-умолчанию можно использовать свой КЛАСС или функию! т.к для этого
# подходит ЛЮБОЙ коллабл обьект! (обьект, у которого реализован мегический (дандер) метод __call__) !

# from collections import namedtuple
#
# def myintdef():
#     return "такой ключ не существует!"
#
# class MyInt:
#     def __init__(self, values):
#         self.values = values
#     def setvalue(self, value):
#         self.values = value
#     def __call__(self):
#         return self.values
#
# my_exp_class = MyInt(11)
# my_exp_class.setvalue(33)

# a = {'a': 1, 'c': 2}
#
# f = defaultdict(myintdef, a)
# d = defaultdict(int, a)
# #
# print(f['h'], d['p'], f['ret'])
# print(f , d)

###
# nametuple можно добавлять в качестве включа!
# a = {'a': 1, 'c': 2}
#
# Other = namedtuple('Other', 'not_found_items')
#
# a['Other'] = Other('123')
#
# print(a)
# print(a['Other'])
# print(a['Other']._asdict()['not_found_items'])

######
#                       Бинарный поиск:

# def BinaryFind(val, l):
#     first = 0
#     last = len(l) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last) // 2
#
#         if l[mid] == val:
#             index = mid
#         else:
#             if val < l[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
#
# print(BinaryFind(20,[10,20,30,40,50,60,70,80]))
######


# Проверка записи логов и "ротации" по 10кб (rotation) в zip-архиве(compression):
#
# from loguru import logger

# logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation = '10 KB', compression = 'zip')

# for _ in range(1000):
#     logger.debug("YAHOOO! it's WORK! (debug))")

# rotation - очень гибкий инструмент ротации (сохранение текущего файла логов и создание нового)
# т.к можно указать время("10:00")/раз в неделю("1 week")/по размеру(кб/мб)

# В логуру есть встроеный декоратор чтобы "ловить"/"отслеживать" и обрабатывать EXCEPTION (ошибки):
# @logger.catch

# @logger.catch
# def ExmpLoguruDec(a,b):
#     print(a/b)


# Сортировка списка "а" в соответствии с частотой "встречи" его элементов в списке "b" :
# from collections import Counter
#
# def exp_sort(a: list, b: list) -> list:
#     a.sort(key=lambda x: b.count(x), reverse=True)
#     return a
# 2й вариант: (НАМНОГО МЕДЛЕННЕЙ варианта выше (через .sort(x)) !!!)
# def sort_by_count(a: list, b: list) -> list:
#     a.sort(key=lambda x: x in Counter(b).most_common())
#     return a

# from collections import Counter
# from datetime import timedelta, datetime
# import time

#
# my_arr_a = [1,2,3]
# my_arr_b = [1,1,1,1,2,3,3,3]

####
# #                                               КЛАСС - ДЕКОРАТОР!

# class Example_d:
#     __slots__ = ("count_method",)
#
#     def __init__(self, count_method=1):
#         self.count_method = count_method
#
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args):
#             for _ in range(self.count_method):
#                 func(*args)
#
#         return wrapper
#

#
# @Example_d(1000000)
# def sort_by_count(arr1,arr2):
#     arr1.sort(key=lambda x: arr2.count(x), reverse=True)
#     return arr1
####
#               Из римских цифр в арабские и наоборот:
# import roman
# def roman_to_int(num_r:str) -> int:
#     return roman.fromRoman(num_r)
# from functools import wraps
# #Создаём декоратор
# def dec_examples(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"заворачиваем функцию {func}")
#         func(*args)
#         print("ЗАКОНЧИЛИ!")
#     return wrapper
#
# @dec_examples
# def for_my_exp(a,b):
#     '''
#     Выводит значения переданных аргументов
#     '''
#     print(f"{a}:{b}")
#
# for_my_exp(2,1)
# print(help(for_my_exp))

### Поведение слотс с приватными атрибутами (свойствами):

# class ExpForSlots:
#     __slots__ = ('x','y','__z')
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.z = x - y
#     #Пишем геттер:
#     @property
#     def z(self):
#         return self.__z
#     #Обязательно пишем сеттер:
#     @z.setter
#     def z(self,value):
#         self.__z = value
#
# some_exp_for_slots = ExpForSlots(2,3)
# some_exp_for_slots_2 = ExpForSlots(5,7)
# Спокойно можем работать с приватным атрибутом (и задавать значения для конкретного эклемпляра
# (обьекта) класса тоже!)

# some_exp_for_slots.z = 20
# print(some_exp_for_slots.z) #--> 20
# print(some_exp_for_slots_2.z) #--> -2

# Итог:
# Слотс НИКАК не влияет на приватные атрибуты потому что мы определяем для них сеттер и геттер
# которые являются методами , а на методы класса/обьекта класса слотс НЕ может повлиять!

# print(some_exp_for_slots.__slots__)

# class ChildExp(ExpForSlots):
#     __slots__ = 'u',
#
#     def __init__(self, x, y, u):
#         # super().__init__(x,y)
#         self.u = u

# child_obj = ChildExp(1,2,3)
# ОЧЕНЬ ВАЖНО быть внимательным с методами .index() и .find() !!!!
# потому что они ищут ТОЛЬКО первое вхождение искомого элемента!!!
# a = ['3','4','5','2','1']
# min_v = min(a)
# max_v = max(a)
# # print(f'минимальное - {min_v} , максимальное - {max_v}')
# # # минимальное - 1 , максимальное - 5
# # print(f"элементы по индексам min и max: {a.index(min_v), a.index(max_v)}")
# # # элементы по индексам min и max: (4, 2)
# # a[4], a[2] = a[2], a[4]
# # # элемент списка с пиндексом 4('1') и 2('5') меняются местами
# # print(''.join(a))
# # # 34125 перевели список в строку
#
#
# # a[a.index(min_v)] = a[a.index(max_v)]
# # print(f"Второе присвоение: {a}")
# # a[a.index(max_v)] = a[a.index(min_v)]
# # print(f"Первое присвоение: {a}")
# print(min_v,max_v,sep="\n")
#
# a[a.index(min_v,3)], a[a.index(max_v)] = a[a.index(max_v)], a[a.index(min_v,3)]
# #print(a) #-> ['3', '4', '1', '2', '5']
# #a[a.index(max_v)], a[a.index(min_v,3)] = a[a.index(min_v,3)], a[a.index(max_v)]
# print(a) #-> ['3', '4', '5', '2', '1']
#
# abc = [1,2,3,3,3,4,5]
# print(abc.index(3))


# from typing import Union, Iterable
#
# def example_Zam(chars):
#     def some_def(string: Union[str, Iterable[str]]):
#         if not isinstance(string,str):
#             raise ValueError("Argument must be a string")
#         return string.strip(chars)
#     return some_def
#
# s1 = example_Zam("!")
# print(s1("PrivED!"))
# for _ in s1.__closure__:
#     print(_, _.cell_contents)
#
# s2= example_Zam("?")
# print(s2("pupka?"))
# for _ in s2.__closure__:
#     print(_, _.cell_contents)
#
# s3 = example_Zam(".")
# print(s3("pu.pua"))
# for _ in s3.__closure__:
#     print(_, _.cell_contents)

# a = not bool('False')
# print(a +1)


# a = [5,4,10]
#
# b = [x == 10 for x in a]
#
# print(any(b))
#
# gg = 11
#
# if 10 < gg < 12:
#     print("YAHOOO!")
# name = 'Dim'
# class TaskP:
#     name = "Ivan"
#     def addx(self):
#         return name
#     @staticmethod
#     def powx(val):
#         return val**2
#     @classmethod
#     def clm(cls):
#         return cls.name
#
# gg_x = TaskP()

# print(gg_x.addx())
# print(gg_x.clm())
# print(gg_x.powx(2))
# print(type(gg_x.powx))
# print(type(gg_x.addx))
# print(type(gg_x.clm))

###########
# import datetime
# import pytz

# time_now = datetime.datetime.now() # это "наивное" время, т.к не знает зону.Лучше не использовать!
# timezone = datetime.datetime.now(pytz.utc)
# time_z_b = datetime.datetime.now(pytz.timezone("Europe/Berlin"))
# print(time_now,timezone,time_z_b, sep='\n')
#
#Лучше всего писать так:
# timezone = pytz.timezone('Europe/Moscow')
# time_now = timezone.localize(datetime.datetime.now()) # это,так называемое, "осведомлённое"
# время (знает зону)
#
# print(time_now)
#
# class ParentClass:
#     def __str__(self):
#         return "Вызыван из ParentClass"
#
# class FatherClass(ParentClass):
#     def __str__(self):
#         return "Вызван из Father"
#
# class MotherClass(ParentClass):
#     def __str__(self):
#         return "Вызван из Mother"
#
# class SonClass(FatherClass,MotherClass):
#     # def __str__(self):
#     #     return 'Вызван из Son'
#     pass
#
# print(SonClass.mro())
#
# Petya = SonClass()
# print(Petya)


# from functools import wraps
# def taboo_agrs(func):
#     """
#     Декоратор для проверки входящего аргумента
#     :param func: с 1 рагументом
#     :return: ничего - если аргумент str, TypeError - если аргумент не str
#     """
#     @wraps(func)
#     def is_inst(string):
#         if not isinstance(string, str):
#             raise TypeError('Argument is not a string')
#         else:
#             return func(string)
#     return is_inst
#
# @taboo_agrs
# def func_for_upper(a):
#     return a.upper()
#
# print(func_for_upper())

####
#        Валидатор: Дескриптор
class ValidSting:
    def __set_name__(self, owner, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        print('Вызван __set__()')
        if not isinstance(value, str):
            raise ValueError(f"self.property_name must be a string")
        # key = f"_{self.property_name}"
        # setattr(instance, key, value)
        #2 строчки выше и 1 нижу равны по функционалу (заменяют друг друга) ,
        # оба варианта записывают значение в локальный словарь и добавляют _ .
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        print("Вызван get()")
        if isinstance is None:
            return self
        # key = f"_{self.property_name}"
        # return getattr(instance, key, None)#None - значение по умолчанию
        #2 строчки выше и 1 нижу равны по функционалу (заменяют друг друга) ,
        # оба варианта показывают значение из лок.словаря. #None - значение по умолчанию
        return instance.__dict__.get(self.property_name, None)


class ExampleValid:
    name = ValidSting()
    other_name = ValidSting()

a = ExampleValid()
a.name = 'Ivat'
print(a.__dict__)
print(a.name)
########
##      ДАТАКЛАСС
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
# (order=True) - нужно указывать чтобы иметь возможность отсортировать (sorted()) или сравнивать несолько экземпляров
# класса. Сортировка будет по значению первого атрибута (если они равны, то по 2му)
# frozen=True означает что мы запрещаем изменение атлибутов класса (становятся "только для чтения") для экземпляров
# класса. Т.е по сути это аналог звщищённого атрибута _x/_y/_z
class MyDataClass:
    #то что ниже это __init__ ! т.еатрибуты динамические, а не статические!
    y: list = field(compare=False) #не будет участвовать в сортировке
    z: int = field(repr=False)#запрет на вывод атрибута z в репр (при принте)
    x: int = field(default=1) # можно указывать значение по умолчанию

    def __post_init__(self): #здесь можно делать что угодно!
        #self.gen = self.y.append((self.x + self.z)) - не работает с frozen=True !
        pass


# datac_obj = MyDataClass([1, 4, 6], 8)
# print(datac_obj) # c __post_init__ уже будет "MyDataClass(x=2, y=[1, 4, 6, 10])"
#
# datac_obj_2 = MyDataClass([1, 4, 6], 21)
# print(datac_obj_2 > datac_obj) #-> True т. будет 21,1 > 8,1

#datac_obj.x = 33 --> dataclasses.FrozenInstanceError: cannot assign to field 'x'




# def check_syntax(string: str) -> bool:
#     """
#     Проверка синтаксиса, попытался ограничить передаваемое в eval() через ASCII
#     :param string: армиф. выражение
#     :return: True если всё норм
#     """
#     try:
#         return all(ord(x) < 97 for x in string) and isinstance(eval(string), (int, float))
#
#     except:
#         return False
#
# print(check_syntax("1 + -22"))

# Ограчинение выполняемых функций eval():
# print(eval('abs(1-1)',{'__builtins__': None},{'print':print,'abs':abs})

def join_digits(num: int) -> str:
    """
    Переводит число в строку поцифренно(10 -> '1','0')
    :param num: целочисленное значение
    :return: строка с добавлением '-' между элементами
    """
    return '-'.join(''.join(str(x) for x in range(1, num + 1)))


# from typing import NamedTuple
# class For_Exp_NT(NamedTuple):
#     x: int
#     y: int

# a = []
# a.append(For_Exp_NT(33,20))
# b = For_Exp_NT.x
# print(a)
# print(type(b))


############
# import string
#
# a = "'![Prii? v"
# b = (x for x in a if x not in string.punctuation and not x.isspace())
# print(''.join(b))
# b = a.translate(str.maketrans('','',string.punctuation))
# print(b)
#
# trans_t = str.maketrans({'о':'и'})
# print('кот'.translate(trans_t))
###########



# def who_won_BADFUNC(sc_player_1: list, sc_player_2: list) -> str:
#     """
#     Тоже самое что и функция ниже,только тут придётся добавлять новых игроков вручную!
#     :param sc_player_1: список 1го игрока
#     :param sc_player_2: список 2го игрока
#     :return: чья команда выиграла
#     """
#     VALUE_LST = [1, 2, 5, 10]
#
#     def resilt_score(score):
#         return sum(x * y for x, y in zip(VALUE_LST, score))
#
#     player_1 = resilt_score(sc_player_1)
#     player_2 = resilt_score(sc_player_2)
#
#     if player_1 != player_2:
#         return f"Команда{1 if player_1 > player_2 else 2} победила"
#     else:
#         return "Ничья"

# def who_won_NICEFUNC(*args: list, count_t:int = 0) -> str:
#     """
#     Сопоставляет с константой и выдаёт "выигрывшую" команду (по очереди входа аргументов)
#     :param count_t: не задавать значение! используется при подсчёте команд
#     :param args: списки с кол.составом команд
#     :return: какая команда (по номеру) выиграла
#     """
#     VALUE_LST: tuple = (1, 2, 5, 10)
#     score_lst: dict = {}
#
#     for items in (x for x in args):
#         score_lst[str(count_t := count_t + 1)] = sum(x * y for x, y in zip(VALUE_LST, items))
#
#     return ('Ничья' if count_t == 2 and score_lst['1'] == score_lst['2']
#             else f'Команда{max(score_lst, key=score_lst.get)} выиграла')
#
# print(who_won_NICEFUNC([6, 4, 3, 1], [12, 0, 0, 1]))


# a = [x for x in range(10) if not x % 2]
# print(a)

# def func(x):
#     def inner_func(y):
#         return x * y
#     return inner_func
# print(func(3)(2))


# HTTP HTTPS
# датаклассы


