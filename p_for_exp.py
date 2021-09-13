from myclasses import *
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

################

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
#     """
#     Пример проверки входящего аругмента на соответствие с ожидаемым типом с помощью функции
#     ininstance() и модуля typing (Union, Iterable)
#     :param chars: строка
#     :return: строка
#     """
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

#################

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

###########

#        Валидатор: Дескриптор
#import collections
#import itertools
import string

import let as let


# class ValidSting:
#     def __set_name__(self, owner, property_name):
#         self.property_name = property_name
#
#     def __set__(self, instance, value):
#         print('Вызван __set__()')
#         if not isinstance(value, str):
#             raise ValueError(f"self.property_name must be a string")
#         # key = f"_{self.property_name}"
#         # setattr(instance, key, value)
#         #2 строчки выше и 1 нижу равны по функционалу (заменяют друг друга) ,
#         # оба варианта записывают значение в локальный словарь и добавляют _ .
#         instance.__dict__[self.property_name] = value
#
#     def __get__(self, instance, owner):
#         print("Вызван get()")
#         if isinstance is None:
#             return self
#         # key = f"_{self.property_name}"
#         # return getattr(instance, key, None)#None - значение по умолчанию
#         #2 строчки выше и 1 нижу равны по функционалу (заменяют друг друга) ,
#         # оба варианта показывают значение из лок.словаря. #None - значение по умолчанию
#         return instance.__dict__.get(self.property_name, None)
#
#
# class ExampleValid:
#     name = ValidSting()
#     other_name = ValidSting()
#
# a = ExampleValid()
# a.name = 'Ivat'
# print(a.__dict__)
# print(a.name)
########
##      ДАТАКЛАСС
# from dataclasses import dataclass, field
#
# @dataclass(order=True, frozen=True)
# # (order=True) - нужно указывать чтобы иметь возможность отсортировать (sorted()) или сравнивать несолько экземпляров
# # класса. Сортировка будет по значению первого атрибута (если они равны, то по 2му)
# # frozen=True означает что мы запрещаем изменение атлибутов класса (становятся "только для чтения") для экземпляров
# # класса. Т.е по сути это аналог звщищённого атрибута _x/_y/_z
# class MyDataClass:
#     #то что ниже это __init__ ! т.еатрибуты динамические, а не статические!
#     y: list = field(compare=False) #не будет участвовать в сортировке
#     z: int = field(repr=False)#запрет на вывод атрибута z в репр (при принте)
#     x: int = field(default=1) # можно указывать значение по умолчанию
#
#     def __post_init__(self): #здесь можно делать что угодно!
#         #self.gen = self.y.append((self.x + self.z)) - не работает с frozen=True !
#         pass


# datac_obj = MyDataClass([1, 4, 6], 8)
# print(datac_obj) # c __post_init__ уже будет "MyDataClass(x=2, y=[1, 4, 6, 10])"
#
# datac_obj_2 = MyDataClass([1, 4, 6], 21)
# print(datac_obj_2 > datac_obj) #-> True т. будет 21,1 > 8,1

#datac_obj.x = 33 --> dataclasses.FrozenInstanceError: cannot assign to field 'x'


###########

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

##########

# Ограчинение выполняемых функций eval(): ОЧЕНЬ ВАЖНО ИСПОЛЬЗОВАТЬ!
# print(eval('abs(1-1)',{'__builtins__': None},{'print':print,'abs':abs})

##########
# def join_digits(num: int) -> str:
#     """
#     Переводит число в строку поцифренно(10 -> '1','0')
#     :param num: целочисленное значение
#     :return: строка с добавлением '-' между элементами
#     """
#     return '-'.join(''.join(str(x) for x in range(1, num + 1)))

############

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

#############

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

#############

# Альтернатив проверки на чётность / не чётность через Bool-выражение:
# a = [x for x in range(10) if not x % 2]
# print(a)

#############

# def func(x):
#     """
#     Функцию можно вызывать,передав 2 раза аргумент
#     :param x: (х)-1й аргумент и  сразу за ним (у) - второй для влож.функции
#     :return: результат вложеной функции
#     """
#     def inner_func(y):
#         return x * y
#     return inner_func
# print(func(3)(2))

#############

# def to_readable(num: int, d_str='день') -> str:
#     """
#     Перевод секунд в дни/часы/минуты/секунды
#     :param d_str: нужен если выводить строку по-русски
#     :param num: целочисланное значение (секунды)
#     :return: дни/часы/минуты/секунды
#     """
#     days: int = num // 3600 // 24
#     hours: int = num // 3600 - days * 24
#     minutes: int = num // 60 - (hours + days * 24) * 60
#     sec: int = num - (minutes + (hours + days * 24) * 60) * 60
#
#     if 1 < days <= 4: d_str = 'дня'
#     if days > 4:      d_str = 'дней'
#
#     #или
#     # if 1 < days < 5:
#     #     d_ru = 'дня'
#     # if days > 4:
#     #     d_ru = 'дней'
#
#     return f"{days} {d_str}, {hours}:{minutes}:{sec}"
#     # return f"{days} {'дня(ей)' if days > 1 else 'день'}, {hours}:{minutes}:{sec}"
#
# print(to_readable(224930))

####################

# def string_to_lst(string: str) -> list:
#     """
#     Создание списка из строки с сохранением пунктуации и без пробелов
#     :param string: строка
#     :return: список
#     """
#     return re.split(',', ''.join([x for x in string if not x.isspace()]))

####################

# # Создание словаря:
# a = dict(
#         [(1,1),
#         (2,2),
#         (3,3)]
#         )

#################

#разделение для лучшей читаемости
#print(3_000_000) -> 3000000

#################

# ВАЖНО ПОМНИТЬ ЧТО lambda ЭТО ФУНКЦИЯ!
# def mult(x):
#     return x ** m
# lst = range(6)
# m = 2
# # каждый элемент из 0,1,2,3,4,5 (range(6) взводится в степень m (2)
# map_res = map(lambda x: x**m,lst) # -> 0, 1, 4, 9, 16, 25
# # Не забываем что лябмда - это всё-таки ФУНКЦИЯ! и поведение у неё соответствующее!
# #map_res = map(mult,lst) # -> 0, 1, 4, 9, 16, 25
# lst = [1,2,3,6,9]
# m = 1
# #т.к map - это по сути генератор, он сохранил ранее ссылку на первое значение lst
# print(*[x for x in map_res]) # -> 0 1 2 3 4 5

##################

# Сначала max потом min и далее среднее значение:
# a,b,c = (input() for x in range(3))
# print(*sorted((a,b,c))[::-2],sorted((a,b,c))[1], sep= "\n")
###

# Пример как можно добалять несоклько if в вывод:
# n = input()
# print(f"{n} программист{'а' if 1 < int(n[-1]) < 5 else ('' if n[-1] == '1' else 'ов')}")

################

# Особенности оператора возведения в степень:
# a,b = 2,3
# c = a**b**a -->> # a** (b**a)
# print(c) #--> 512

################

# def to_one_dimension_list(lst: list) -> list:
#     from collections.abc import Iterable
#     """
#     Прекрасссный вариант для перевода многомерного списка в одномерный!
#     Реализуем генератор через цикл и yield:
#     Для значений в входном списке:
#         если значение является iterable obj,то берём(возвращаем) вызов функции с этим значением в качестве
#         аргумента и дажее по той же схеме.
#         если значение НЕ итерабл, то возвращаем его.
#     :param lst: список любой вложенности
#     :return: одномерный список
#     """
#     def to_one():
#         for sublist in lst:
#             if isinstance(sublist, Iterable) and not isinstance(sublist, str):
#                 yield from to_one_dimension_list(sublist)
#             else:
#                 yield sublist
#     return list(to_one())

###############

# def to_one_dimension_list_2(lst: list) -> list:
#     from collections.abc import Iterable
#     """
#     Ещё вариант для перевода многомерного списка в одномерный.
#     Рекурсия (по возможности не использовать!)
#     :param lst: многомерный список
#     :return: одномерный список
#     """
#     if isinstance(lst, collections.abc.Iterable):
#         return [x for sublist in lst for x in to_one_dimension_list(sublist)]
#     else:
#         return [lst]

##############

# def to_one_dimension_list_3(lst):
#     from collections.abc import Iterable
#     """
#     Не рекурсивный вариант перевода списка в одномерный.
#     :param lst: многомерный список (с Tuple тоже будет работать!)
#     :return: одномерный список
#     """
#     lst = list(lst)
#     def to_one():
#         while lst:
#             while lst and isinstance(lst[0], Iterable):
#                 lst[0:1] = lst[0]
#             if lst:
#                 yield lst.pop(0)
#     return list(to_one())

############

# Фрагмент таблицы умножения для всех чисел отрезка [a,b] на все числа отрезка [c,d].
# Числа a, b, c и d являются натуральными и не превосходят 10, a<=b, c<=d.

# from collections.abc import Iterable
# # #
# a, b, c, d = (int(input()) for i in range(4))
# #lst_a = [x for x in range(a, b + 1)]
# #lst_b = [x for x in range(c, d + 1)]
#
# print(*(lst_a := [x for x in range(a, b + 1)]))
# for _ in zip(lst_b := [x for x in range(c, d + 1)], [[i * j for j in lst_a] for i in lst_b]):
#     for l in _:
#         if isinstance(l, Iterable):
#             print(*l)
#         else:
#             print(l, end=' ')

#pp = [[i * j for j in a] for i in b]
#result = zip(b,pp)

##################

# Пример важности срезов:
# a = [1,2,3]
# b = a
# print(b==a,a is b, sep='\n')
# b = a[:]
# print(b is a) #-> False !

# C неизменяемыми типами (str,tuple) совсем иначе! :
# arr1 = 'simple string'
# arr2 = arr1[:]
# print(id(arr1), id(arr2))
# print(arr1 is arr2) #-> True !

# ОЧЕНЬ ВАЖНО!
# a = 'hello'
# b = 'hell'+'o'
# print(a is b) #--> True

##############

# a = [1,2,3]
# a.reverse() # как и reversed() НЕ изменяет существущий список, возвращает итератор!

##############

# def to_pairs(lst: list, fill_char: int = None) -> list:
#     """
#     Разбиение по парам (2) списка.
#     :param lst: одномерный список
#     :param fill_char: не обязательный параметр, добавляет заданное число если нечётное кол-во элементов
#     :return: двумерный список
#     """
#     inner_l: list = lst[:]
#
#     if len(lst) % 2:
#         inner_l.append(fill_char)
#     return [inner_l[v:v + 2] for v in range(0, len(inner_l), 2)]

 #ИЛИ: блок if здесь уже не нужен ! т.к используется zip() !
    # inner_l= lst[:] + [fill_char]
    # return [list(x) for x in zip(inner_l[::2], inner_l[1::2])]
    # или с моржом:
    # return [list(x) for x in zip((inner_l:= lst[:] + [fill_char])[::2], inner_l[1::2])]

############

# def rot(text: str, offset=13) -> str:
#     """
#     Шифр ROT13 относится к сокращенной форме Поворот на 13 мест . Это особый случай Цезаря Шифра, в котором сдвиг
#     всегда равен 13 (по умолчанию). Каждая буква сдвигается на 13 мест, чтобы зашифровать сообщение.
#     Расшифровка через отрицательное значение offset. Необходим импорт string.
#     :param text: строка
#     :param offset: сдвиг
#     :return: зашифрованная/расшифрованная строка
#     """
#     str_ascii = string.ascii_letters
#     return text.translate(str.maketrans(str_ascii, str_ascii[offset:] + str_ascii[:offset]))

#####################

# def permutations(string:str):
#     """
#     Выдаёт все возможные комбинации элементов. Необходим импорт itertools
#     :param string: строка
#     :return: список строк с комбирациями
#     """
#     from itertools import permutations
#
#     return [''.join(x) for x in permutations(string, r= None)]


# def custom_permutations(string: str) -> list:
#     """
#     Выдаёт все возможные комбинации элементов. (альтернатива itertools permutations)
#     Необходим импорт random
#     :param string: строка
#     :return: список строк с комбирациями
#     """
#     from random import shuffle

#     lst_s = [x for x in string]
#     res_l = []
#     for _ in range(len(string) ** len(string)):
#         shuffle(lst_s)
#         res_l.append(''.join(lst_s))
#     return list(set(res_l))

#################

# def gimme_the_letters(span_let: str) -> str:
#     """
#     Строка из всех букв англиского алф. нужного диапазона. Необходим импорт string.
#     :param span_let: строка,диапазон букв английского алфавита (н/р: "a-z")
#     :return: возвращает строку из всех букв этого диапазона.
#     """
#     ascii_l = string.ascii_letters
#     return ascii_l[ascii_l.index(span_let[0]):ascii_l.index(span_let[-1]) + 1]

################

# a = [input() for x in range(4)]
# print(a)
# b = [x.split() for x in a]
# print(b)

#################

# def random_secure_string(len_pass: int = 10) -> str:
#     """
#     Генерация случайных паролей. Необходим импорт string и secrets.
#     :param len_pass: длина пароля
#     :return: пароль в виде строки
#     """
#     import string
#     import secrets
#     try:
#         # securestr = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(len_pass)))
#         # return securestr
#
#         # alphabet = string.ascii_letters + string.digits
#         password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(len_pass))
#         return password
#     except TypeError:
#         return "Password length must be a number!"

###################

# СПИСОК1 + СПИСОК2 = СПИСОК1.extend(СПИСОК2) !!! Можно использовать такую замену методу для return в функциях ,
# т.к и append() и extend() ничего не возвращают!
# a = [1,2,3]
# b = [4,5,6]
# print(a+b) #-> [1, 2, 3, 4, 5, 6]
# a = [1,2]
# b = a + [3] # -> [1, 2, 3]

####################

# def modify_list(l: list):
#     """
#     Изменить список через функцию (которая ничего не возвращает) можно через полный срез [:]
#     :param l: список
#     :return: ничего, меняется сам входящий список
#     """
#     l[:]= [x // 2 for x in l if x % 2 == 0]

# При этом срез необходим ТОЛЬКО в функции!!!
# a = [1,2,3,4,5,6]
# #a= list(filter(lambda x: x%2==0,a))
# a = [x // 2 for x in a if x % 2 == 0]
# print(a)

####################

#
# from pytube import YouTube
#
# link = YouTube("https://www.youtube.com/watch?v=RaXV7Loe9Qw")
# link.streams.filter(only_audio=True).order_by('abr').first().download()

####################

# def get_century(year: int) -> int:
#     """
#     Перевод года в век
#     :param year: год
#     :return: век
#     """
#     return (year - 1) // 100 + 1

###################

#dct = dict(a=2, b=3, c=10) -> {'a': 2, 'b': 3, 'c': 10}

###################

# def hamming_distance(string_1: str, string_2: str) -> int:
#     """
#     Вычисляет "расстояние Хэмминга" между 2мя строками.
#     :param string_1: строка
#     :param string_2: строка
#     :return: число (int)
#     """
#     if len(string_1) == len(string_2):
#         return sum(ch1 != ch2 for ch1, ch2 in zip(string_1, string_2))
#     else:
#         raise ValueError("Length of the args must be the same")

###################

# Интересное поведение оператора and :

# a = 20
# b = 5
# print(b and a) # -> 20
# print(a and b) # -> 5
# Всегда будет выводиться последний элемент!
###################

# def lambda_inner_func(y):
#     """
#     lambda-выражение как альтернатива вложеной функции
#     :param y: что-нибудь
#     :return: что-нибудь
#     """
#     return lambda x: x + y
#
# print(lambda_inner_func([2,3])([4,5]))   # -> [4, 5, 2, 3]
# print(lambda_inner_func([7,8])([10,20])) # -> [10, 20, 7, 8]

####################

# from typing import Union, Any
#
# def update_dictionary(dct: dict, k: Union[int, str, tuple], val: Any):
#     """
#     Принцип EAFP
#     :param dct: словарь
#     :param k: ключ
#     :param val: значение
#     :return: None
#     """
#     try:
#         dct[k].append(val)
#     except KeyError:
#         try:
#             dct[k * 2].append(val)
#         except KeyError:
#             dct[k * 2] = [val]

##################

# Создали кастомный класс словаря:
# md = MyDict()
# md['somekey'].append(1)
# print(md)
# print(md.__doc__)

###################

# a1, b1, a2, b2 = (int(input()) for x in range(4))
# def inters(a1, b1, a2, b2):
#     """
#     Пересечения двух "отрезков"
#     :param a1: начало 1
#     :param b1: конец 1
#     :param a2: начало 2
#     :param b2: конец 2
#     :return: отрезок пересечения или строку
#     """
#     # создать 2 списка и сравнить их:
#     # l_1, l_2 = [x for x in range(a1, b1 + 1)], [x for x in range(a2, b2 + 1)]
#     # res = [x for x in l_1 for y in l_2 if x == y]
#     # использовать только range() :
#     #res = [x for x in range(a1,b1+1) if x in range(a2,b2+1)]
#     #return 'Пустое множество' if not res else ((res[0],res[-1]) if len(res)>1 else res[0])
#
#     # ИЛИ испольовать set, что намного быстрее списков! :
#     #res = set(range(a1, b1 + 1)) & set(range(a2, b2 + 1))
#     #res = set(range(a1, b1 + 1)).intersection(range(a2, b2 + 1))
#     return ('Пустое множество' if not (res := set(range(a1, b1 + 1)).intersection(range(a2, b2 + 1)))
#             else ((min(res), max(res)) if len(res) > 1 else min(res)))

##################

# Лёгкий способ создать словарь:
# a = [1,2,3]
# b = [4,5,6]
# dct = dict(zip(a,b))

####################

# Немного об отлове ошибок:

# import sys
# try:
#     sys.exit()
#     print("Программа ещё работает")
# except BaseException as e:
#     print(f"Сработала ошибка {type(e)}")
# finally:
#     print("finaly сработала")
# Сработала ошибка <class 'SystemExit'>
# finaly сработала

# "Выход из программы" - считается тоже ошибкой (SystemExit), только уже родитель не Excepion (как для практически
# всех ошибок),а BaseException (тут ещё KeyboardInterrupt и GeneratorExit). Смотри древо наследования классов ошикок!

###################


