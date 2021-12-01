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
################
#               Из римских цифр в арабские и наоборот:
# import roman
# def roman_to_int(num_r:str) -> int:
#     return roman.fromRoman(num_r)

###################

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
# Лучше всего писать так:
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
# import collections
# import itertools

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

# datac_obj.x = 33 --> dataclasses.FrozenInstanceError: cannot assign to field 'x'


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

# разделение для лучшей читаемости
# print(3_000_000) -> 3000000

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

# pp = [[i * j for j in a] for i in b]
# result = zip(b,pp)

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

# ИЛИ: блок if здесь уже не нужен ! т.к используется zip() !
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

# dct = dict(a=2, b=3, c=10) -> {'a': 2, 'b': 3, 'c': 10}

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

# import collections.abc
#
# a = [[1,3,[2,4],50],1078,[5,6,7,[8,9,[10,101]]],9]
#
# def flatten(lst: list):
#     """
#     Рекурсия
#     :param lst: вложеный список
#     :return: одномерный список
#     """
#     for item in lst:
#         try:
#             yield from flatten(item)
#         except TypeError:
#             yield item
#
#
# def genflat(lst: list):
#     """
#     Циклом в одномерный список
#     :param lst: вложеный список
#     :return: одномерный список
#     """
#     lst = list(lst)
#     while lst:
#         while lst and isinstance(lst[0], collections.abc.Sequence):
#             lst[0:1] = lst[0]
#         if lst:
#             yield lst.pop(0)


# from copy import deepcopy
#
# def flatten_gen(lst):
#     """
#     Циклом в одномерный список, приоритетный способ.
#     :param lst:
#     :return:
#     """
#     lst = deepcopy(lst)
#     while lst:
#         sublist = lst.pop(0)
#         if isinstance(sublist, list):
#             nested_list = sublist + lst
#         else:
#             yield sublist

##################

# Использование для проверки isinstance( , int) и .__class__ == int и type() == list это по сути одно и тоже

# nan/NaN/Nan является ЧИСЛОМ с плавающей запятой (type(nan) -> <class 'float'>)!
# и float('nan') НЕ ВЫЗОВЕТ ОШИБКИ ValueError !!!
# x = float('nan')

######################

# def matrix_snail(n: int):
#     """
#     Выводит матрицу размером n x n значениями по спирали.
#     :param n: целое число
#     :return: влож.список
#     """
#     par_lst = [[0] * n for i in range(n)]   # или [[None] * n for i in range(n)]
#     x, y, x_2, y_2 = 0, 0, 1, 0
#     for v in range(n ** 2):
#         par_lst[y][x] = v + 1
#         test = x + x_2 if x_2 else y + y_2
#         if test == n or par_lst[y + y_2][x + x_2] != 0:  # test < 0
#             x_2, y_2 = -y_2, x_2
#         x += x_2
#         y += y_2
#     for _ in range(n):
#         print(*par_lst[_])

#####################

# Ключ True преобразовывается в 1 и заменяет его значение своим :
# dct = {1:'PRESS F','1':'won',True:'yahoo'}
# for k,v in dct.items():  #1 yahoo
#     print(k, v)          #1 won

#####################

# import csv
#
# with open('123.txt', 'r') as infile, open('forEXP.csv', 'w') as outfile:
#     stripped = (line.strip() for line in infile)
#     lines = (line.split(",") for line in stripped if line)  # чтобы использовать запятую (,) в тексте и не
#     # получить лишний "элемент" необходимо заключать его в двойные кавычки (н/р "9,2" или текст в разных строках)
#     writer = csv.writer(outfile)  # у этого метода есть quoting (смотри доки)
#     writer.writerows(lines)

########################
# Получение инфы о системе:
# print(platform.system()) # название ОС
# print(platform.platform()) # версия ОС
# print(platform.processor()) # проц
# print(platform.python_version())

# print(*sorted([int(input()) for i in range(int(input()))],reverse=True)[:2],sep='_')
# print([int(input()) for i in range(int(input()), int(input()))])

###################

# def reverse_letters(str_in: str) -> str:
#     """
#     Делает реверс только букв в строке.
#     :param str_in: строка
#     :return: новая строка
#     """
#     result = [ch for ch in str_in[::-1] if ch.isalpha()]
#     for i, v in enumerate(str_in):
#         ##if not v.isalpha(): result.insert(i, v)
#         if not v.isalpha():
#             result.insert(i, v)
#     return ''.join(result)

###################

# def reverse_letters(user_str: str, letter_counter=-1) -> str:
#     rev_let: list = [elem for elem in user_str if elem.isalpha()][::-1]
#     res_string: str = ''
#     for i in range(len(user_str)):
#         if user_str[i].isalpha():
#             res_string += rev_let[(letter_counter := letter_counter + 1)]
#         else:
#             res_string += user_str[i]
#     return res_string

#####################

# def bubble_sort(nums: list):
#     """
#     Сорторовка списка 'пузырьком'
#     :param nums: сортируемый список
#     :return: отсортированый список
#     """
#     # через рекурсию:
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#             bubble_sort(nums)
# через цикл while:
# cycle = True
# while cycle:
#     cycle = False
#     for i in range(len(nums) - 1):
#         if nums[i] > nums[i + 1]:
#             nums[i], nums[i + 1] = nums[i + 1], nums[i]
#             cycle = True

########################

# import roman # из/в римские - арабские: (ну или ниже 3 функции)
# print(roman.toRoman(int(input())))

# def to_roman(number: int) -> str:
#     """
#     Из из арабских в римские
#     :param number: число
#     :return: римское  число
#     """
#     thous, century, ten, one = (
#         ("", "M", "MM", "MMM", "MMMM"),
#         ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
#         ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
#         ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
#     )
#     return f"{thous[number // 1000]}{century[number // 100 % 10]}{ten[number // 10 % 10]}{one[number % 10]}"
#
# def to_roman(number: int) -> str:
#     result: str = ''
#     for arab, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
#                            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')):
#         result += number // arab * roman
#         number %= arab
#     return result

# def to_roman(num: int) -> str:
#     arab_to_roman = {
#         "1": ('I', 'X', 'C', 'M'),
#         "2": ('II', 'XX', 'CC', 'MM'),
#         "3": ('III', 'XXX', 'CCC', 'MMM'),
#         "4": ('IV', 'XL', 'CD'),
#         "5": ('V', 'L', 'D'),
#         '6': ('VI', 'LX', 'DC'),
#         "7": ('VII', 'LXX', 'DCC'),
#         "8": ('VIII', 'LXXX', 'DCCC'),
#         "9": ('IX', 'XC', 'CM'),
#         "0": ('', '', '')
#     }
#     roman_num = ''
#     for i, letter in enumerate(str(num)[::-1]):
#         roman_num += arab_to_roman[letter][i]
#     return roman_num[::-1]

#########################

# from itertools import compress,chain,combinations_with_replacement,filterfalse
#
# a = ['a','b','c','d']
# b = [[11,50,101],[10,20]]
# c = [1,2,3,4,5]
#
# print(list(compress(a,b)))
# print(list(chain.from_iterable(b)))
# print(list(combinations_with_replacement(a,3)))
# print(list(filterfalse(lambda x: x<5, [1,4,6,1,4])))

#####################################

# ПАРАМЕТРИЧЕСКИЙ ПОЛИМОРФИЗМ (множественная диспетчеризация / перегрузка):

# Создание нескольких функций с ОДИНАКОВЫМ ИМЕНЕМ , но разными типами аргументов. Во время вызова функции будет выбрана
# та её версия , которая подходит под тип передаваемого агрумента. Это "удобно" использовать если не знаем
# какого типа аргумент будет передан!
# Это работает только для 1го (первого) передаваемого агрумента!

# from functools import singledispatch
# @singledispatch
# def custom_r(value):
#     """
#     декоратор из functools
#     :param value:
#     :return:
#     """
#     raise TypeError
#
# @custom_r.register(int)
# def _(x): # или не узказывать агруемт (int) в декораторе и добавить аннотацию типа в саму функцию def _(x: int):
#     """
#     Имя функции не имеет знаничения!
#     :param x:
#     :return:
#     """
#     print('INT', x)
#
# @custom_r.register(float)
# @custom_r.register(str)
# def _(x):
#     """
#     Если одна функцию должна обрабатывать несколько типов
#     :param x:
#     :return:
#     """
#     print(f"{type(x).__name__.upper()}:", x)
#
# custom_r(1.2)
# п.с: также есть декоратор (singledispatchmethod) для методов класса!

##########################

# Получить "голый" URL сайта из ссылки:
# from urllib.parse import urlparse
# o = urlparse('http://www.cwi.nl/%7Eguido/Python.html')
# print(o.netloc)

# ИЛИ:
# import re
# re.findall("([\w-]+?\.[\w\-\.]+).*", url)[0]

# ИЛИ:
# from itertools import takewhile
# def get_domain(url: str):
#     """
#     Убрать лишнее из URL - адреса
#     :param url: ссылка (url)
#     :return: очишенная ссылка
#     """
#     for _ in ('https://', 'http://', 'ftp://', 'www.'): url = url.removeprefix(_)
#     return ''.join(takewhile(lambda x: x != '/', url))
#
# print(get_domain("https://www.xakep.ru/page"))

################################

# # Бесконечное число:
#
# import math
# a = math.inf
# print(type(a)) # -> float
#
# import itertools
# a = itertools.count(1)
# print(type(a)) # -> интератор с int - значениями

##############################

# str_in,f_str = [[input() for x in range(int(input()))] for _ in range(2)]
# # for item in string_in:
# #     if all(x.lower() in item.lower() for x in f_str):
# #         print(item)
# print(*(i for i in str_in if all(x.lower() in i.lower() for x in f_str)), sep='\n')

########################

# def is_triangle(lst: list) -> bool:
#     """
#     Проверяет, существует ли треугольник или нет
#     :param lst: 3 стороны
#     :return: да/нет
#     """
#     a, b, c = lst
#     return (a + b > c) and (a + c > b) and (b + c > a)
# или (приоритетней)
# def is_triangle(lst: list) -> bool:
#     lst = lst[:]
#     return lst.pop(lst.index(max(lst))) <= sum(lst)

###########################

# Особенности математических операций:
# a = 10
# b = 5
# print(a//b * a / b) #-> 4.0
# print((a//b * a) / b) #-> 4.0
#
# print((a * b // a) * b)

#################

# a = 10
# b = a/2
# import sys
# try:
#     for _ in range(3):
#         if _ > 1:
#             print('TRY')
#             sys.exit() # а break НЕ вызывает ошибку SystemExit (родитель BaseException)!!!
# except BaseException as e:
#     print('EXPT', type(e))
# else:
#     print('ELS') # Вызывается только если не возникло никаких ошибок!
# finally:
#     print('FNLY') # Вызывается всегда!

####################

# data = ''
# while (str_in := input()):
#     if '#' in str_in:
#         str_in = str_in[:str_in.index('#')].rstrip()
#     data += str_in+'\n'
# print(data[1:])

###################

# data = ''
# i = -1
# for _ in range(n):
#     str_in = inp[(i:=i+1)]
#     if '#' in str_in:
#         str_in = str_in[:str_in.index('#')].rstrip()
#     data += str_in+'\n'
# print(f'\n{data[1:]}')

#########################

# from itertools import combinations
# def two_sum(lst: list, n: int):
# Не норм решение:
#     return [lst.index(i) for i in next(x for x in combinations(lst, 2) if sum(x) == n)]
# Норм решение:
#     return [i for i,v in enumerate(lst) if n - v in lst]

##########################

# Примеры создания различных списков
# import itertools
# import more_itertools
# a = [1,2,3]
# b = [4,5,6]

# print(list(itertools.product(a,b))) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
# print(list(zip(a,b)))               # [(1, 4), (2, 5), (3, 6)]
# print(list(itertools.chain(a,b)))   # [1, 2, 3, 4, 5, 6]


# Яракий пример проблемы float-вычислений :
# print(round(2.85,1)) # 2.9
# print(round(2.65,1)) # 2.6
# Что противоречит правилу округления функцией round() float-числа до "ближайшего чётного" если дроб.часть >=0.5!

###########################

# my_list = [('a', 1), ('c', 2), ('e', 3)]
#
# transposed_list = zip(*my_list)
# print(list(transposed_list)) # -> [('a', 'c', 'e'), (1, 2, 3)]
#
# # В принипе zip(*my_list) и more_itertools.unzip(my_list) одно итоже!
#
# letters, numbers = more_itertools.unzip(my_list) # -> 2 map object
# print(list(letters)) # -> ['a', 'c', 'e']
# print(list(numbers)) # -> [1, 2, 3]

################################

# a = 'aab'
# b = 'aba'

# def is_one_away(string_1: str, string_2: str) -> bool:
#     """
#     Сравнивает две строки (Степик)
#     :param string_1: строка
#     :param string_2: строка
#     :return: True, если они отличаются на одну букву, False в противном случае.
#     """
#     return sum(s != f for s, f in zip(string_1, string_2)) == 1

###################

# Интересное поведение пустого вложенного списка:

# a = [[]]*3
# a[1].append(1)
# print(a) # -> [[1], [1], [1]]

#####################

# from string import ascii_lowercase,ascii_uppercase,digits
# def is_password_good(passoword):
#     return len(passoword) >= 8 and all(ch in ascii_uppercase or ch in ascii_lowercase or ch in digits for ch in passoword)
#

# def is_password_good(passoword):
#     return len(passoword) >= 8 and sum((any(filter(x,passoword)) for x in (str.isupper, str.islower,str.isnumeric))) == 3
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
# print(is_password_good('12314124124141'))

########################

# nums = [0, 1, 0, 3, 12]

# def move_zeroes(lst: list):
#     """
#     Нули вправо.
#     :param lst: список
#     :return: изменяется переданный список
#     """
#     # lst[:] = [x for x in lst if x > 0] + [0] * lst.count(0)
#     for _ in range(lst.count(0)):
#         lst.append(lst.pop(lst.index(0)))
# move_zeroes(a)
# print(a)

###########################

# класс-декоратор может несолько раз вызвать функцию
# from functools import wraps

# class Example_d:
#     __slots__ = ("count_method",)
#     def __init__(self, count_method=1):
#         self.count_method = count_method
#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args):
#             for _ in range(self.count_method):
#                 func(*args)
#         return wrapper
# или
# import functools
# def repeater(repeat=1):
#     """Повторение выполнения кода"""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for i in range(repeat):
#                 print(f'{i+1}: ', end='')
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return decorator

##########################

# a = []
# a.append('ab') # -> ['ab']
# a.extend('cde') # -> ['c', 'd', 'e']

#####################

# from typing import NewType
# from beartype import beartype
# MatrixType = list[list[int]]
# MatrixType = NewType('MatrixType', list[list[int]])

#########################

# import dis
#
# def func(a,b):
#     c = a+b
#     print(c)
#
# dis.dis(func)

######################

# def rev_func(inp):
#     res: list = []
#     for i, v in enumerate(inp, 1):
#         if ''.join(let for let in 'anton' if x in v ) == 'anton':
#             res.extend((str(i), " "))
#     return ''.join(res)

# def increment_string(string_in: str):
#     n: list = [v for v in string_in[::-1] if v.isnumeric() and v != '0']
#     try:
#         return f"{string_in[:-(len(n))]}{int(''.join(n[::-1])) + 1}"
#     except:
#         return f"{string_in}1"
#
# print(increment_string('f0o999'))

#############################

# Поиск слова "anton" в последовательности:

# import re
# inp:list = [input() for x in range(int(input()))]
# for i, v in enumerate(inp, 1):
#     if re.search(r'.*a.*n.*t.*o.*n', v): # Поиск последовательности (anton) в строке н/р: "a1n1t1o1n1"
#         print(i, end=' ')

#########################

# from itertools import takewhile

# def same_length(n: int) -> bool:
#     """
#     В переданном числе за каждой последовательностью единиц следует последовательность нулей той же длины.
#     :param n: число
#     :return: BOOL
#     """
#     n: str = str(n)
#     while n and 'stop' not in n:
#         n = n[(units:=len(list(takewhile(lambda x: x == '1', n)))):]
#         n = n[zeros:] if units == (zeros:=len(list(takewhile(lambda x: x == '0', n)))) else 'stop'
#     return not n
#
# print(same_length(101010110))

######################

# def dup_count(inp_str: str) -> int:
#     return sum({let: inp_str.lower().count(let) > 1 for let in inp_str}.values())
# или
# count_items: dict = {}
# for let in inp_str:
#     if let not in count_items and (n := inp_str.count(let) > 1):
#         count_items[let] = n
# return len(count_items)
# или
# count_items: list = []
# for items in n:
#     if n.count(items) > 2:
#         count_items.append(n.count(items))
# return len(count_items)
# или
# def dup_count(string: str) -> int:
#     sort_el: list = sorted(string.lower())
#     return len({sort_el[i] for i in range(len(sort_el) - 1) if sort_el[i] == sort_el[i + 1]})
# print(dup_count('abcde'))

#######################

# Редактируем видео с помощью бибилотеки moviepy
# н/р взять аудиодорожку из видео:
# import  moviepy.editor
# video = moviepy.editor.VideoFileClip("имя.mov")
# audio = video.audio
# audio.write_audiofile('имя.mp3')

#########################

# # Выводим "красивые" таблицы прямо в терминал  с помощью библиотеки prettytable :
# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.field_names: list = ["имена","столбцов"]
#
# table.add_row(['записываем','строки'])
# table.add_row(['записываем','другие_строки'])
# table.add_row(['записываем','ещё_строки'])
#
# # ровняем по выбранному краю:
# table.align = 'r'
# # можно указать соритровку:
# table.sortby = 'столбцов'
#
# print(table)
# # Смотри ещё больше функций в документации!

#####################################

# from typing import Union
# lst: list = [-1, 2, 3, 4]
#
# def add_one(lst: Union[int,str]) -> list:
#   """
#   В списка (который являются одним числом) необходимо добавить (к этому числу) 1
#   :param lst: принимает список из цифр (не только из цифр)
#   :return: возвращает список из цифр
#   """
#   res: str = str(int(''.join(map(str, lst))) + 1)
#   return [int(x) for x in res] if res.isnumeric() else [-int(res[1])] + [int(x) for x in res[2:]]
#
# print(add_one(lst))

######################################

# def harry(matrix_inp: List[List[int]]):
#     """
#     Гарри — почтальон. У него есть почтовый участок размером n * m (матричный / 2D-список).
#     Каждый слот в 2D-списке представляет количество писем в этом месте.Гарри может идти только вправо и вниз.
#     Он начинает обход в (0, 0) и заканчивает в (n-1, m-1). n представляет высоту, а m — длину матрицы.
#     Письма Гарри может брать только там, где находится.
#     :param matrix_inp: двумерный список из чисел
#     :return: сумма елементов, в соответствии с заданием
#     """
#     if not sum(matrix_inp, []):
#         return -1
#     max_value: tuple = max([(i, sum(item)) for i, item in enumerate(matrix_inp)][::-1], key=lambda x: x[1])
#     return sum((x[0] for x in matrix_inp[:max_value[0]]), max_value[1])
#
#
# print(harry([[]]))
# print(harry([
#   [1, 2, 3, 4, 5],
#   [6, 7, 8, 9, 10],
#   [11, 12, 13, 14, 15]
# ]))
# print(harry([[5, 2],
#              [5, 2]]))

# from itertools import accumulate

# from typing import TypeAlias
# mytype: TypeAlias = list[int] #вместо NewType

# MatrixType: TypeAlias = list[list[int]]
#
# def harry(mtrx_inp: MatrixType) -> int:
#     if not sum(mtrx_inp, []):
#         return -1
#     mtrx_inp: list = mtrx_inp[:]
#     mtrx_inp[0] = list(accumulate(mtrx_inp[0]))
#     for y in range(1, m := len(mtrx_inp)):
#         mtrx_inp[y][0] += mtrx_inp[y - 1][0]
#         for x in range(1, n := len(mtrx_inp[0])):
#             mtrx_inp[y][x] = max(mtrx_inp[y - 1][x], mtrx_inp[y][x - 1]) + mtrx_inp[y][x]
#     return mtrx_inp[m - 1][n - 1]

##################################

# import re
# email = 'yas.dasc@12312@yaco'
# if not re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email):
#     print('NO!')
# else:
#     print('OK!')

#################################

# print('123' '456')

################################

# import math
# def persist1(num: int):
#     while num > 9:
#         num: int = math.prod(map(int, str(num)))
#     return num
# print(persist(999))

########################

# a = 123_567_234
#
# print(f"{a:,}")

################################

# from string import punctuation as pu
#
# def gen_hashtag(str_inp: str):
#     res = f"#{''.join(x for x in str_inp if x not in pu).title().replace(' ', '')}"
#     if len(res) > 140:
#         raise ValueError
#     return res
#
# print(gen_hashtag("python is't a community"))

######################################

# def find_outlier(lst: list):
#     res_l: list = [x % 2 for x in lst]
#     return lst[res_l.index(0)] if sum(res_l)-1 else lst[res_l.index(1)]
#
#
# print(find_outlier([2, 4, 0, 4, 11, 36])) #-> 11
# print(find_outlier([160, 3, 19, 11, -21])) #-> 160
# print(find_outlier([-1, 1, 3, 3, 2, -11, -21])) #-> 2

###################################

# a, *b, c = 'No bees', 'no honey'
# print(b) # -> []

#################################

# def check_var_name(check_str: str):
#     #from string import ascii_letters, digits
#     from keyword import kwlist as kw
#     #a_char: str = ascii_letters + digits + '_'
#     #return check_str not in kw and all(let in a_char for let in check_str)
#
#     return not any((check_str in kw, check_str[0].isnumeric())) and check_str.replace('_', '').isalnum()
#
# print(check_var_name('0wrong'))

#################################
# import itertools
# from pprint import pprint
# from copy import deepcopy


# from contextlib import suppress
#
#
# def num_grid(matrx: list) -> list:
#     """
#     Ненавижу матрицы! Следующую задачу ПЛЗ без них...
#     :param matrx: двумарный список
#     :return: бум
#     """
#     SUP = suppress(TypeError)
#     matrx: list = deepcopy(matrx)
#     for item in matrx:
#         for i, val in enumerate(item):
#             if val != '#':
#                 item[i] = 0
#
#     def inner_func(index: int, i: int, v: int):
#         if 0 <= i + index <= 4:
#             with SUP: matrx[i + index][v] += 1
#             if v + 1 <= 4:
#                 with SUP: matrx[i + index][v + 1] += 1
#             if v - 1 >= 0:
#                 with suppress(TypeError): matrx[i + index][v - 1] += 1
#
#     for i, item in enumerate(matrx):
#         for v, t in enumerate(item):
#             if t == '#':
#                 if v + 1 < 5 and v - 1 >= 0:
#                     with SUP: matrx[i][v - 1] += 1
#                     with SUP: matrx[i][v + 1] += 1
#                 inner_func(-1, i, v)
#                 inner_func(1, i, v)
#     pprint(matrx)
# #
# num_grid([
#   [0, 0, 0, '#', '#'],  # [«1», «1», «2», «#», «#»] ok!
#   [0, '#', 0, 0, 0],  # [«1», «#», «3», «3», «2»] ok!
#   [0, 0, '#', 0, 0],  # [«2», «4», «#», «2», «0»] OK!
#   [0, '#', '#', 0, 0],  # [«1», «#», «#», «2», «0»] ok!
#   [0, 0, 0, 0, 0]   # [«1», «2», «2», «1», «0»] WRONG!
# ])

# num_grid([
#   ['-', '-', '-', '#', '#'],  # [«1», «1», «2», «#», «#»] ok!
#   ['-', '#', '-', '-', '-'],  # [«1», «#», «3», «3», «2»] ok!
#   ['-', '-', '#', '-', '-'],  # [«2», «4», «#», «2», «0»] OK!
#   ['-', '#', '#', '-', '-'],  # [«1», «#», «#», «2», «0»] ok!
#   ['-', '-', '-', '-', '-']   # [«1», «2», «2», «1», «0»] WRONG!
# ])


# def inner_func(index: int, i: int, v: int):
#     if 0 <= i + index <= 4:
#         if isinstance(matrx[i + index][v], int): matrx[i + index][v] += 1
#         if v + 1 <= 4 and isinstance(matrx[i + index][v + 1], int):
#             matrx[i + index][v + 1] += 1
#         if v - 1 >= 0 and isinstance(matrx[i + index][v - 1], int):
#             matrx[i + index][v - 1] += 1
#
#
# for i, item in enumerate(matrx):
#     for v, t in enumerate(item):
#         if t == '#':
#             if v + 1 <= 4 and v - 1 >= 0:
#                 if isinstance(matrx[i][v - 1], int): matrx[i][v - 1] += 1
#                 if isinstance(matrx[i][v + 1], int): matrx[i][v + 1] += 1
#             inner_func(-1, i, v)
#             inner_func(1, i, v)
#
# return matrx

##########################

# import re
#
# a = 'abc'
# b = 'd'
# result = [x.start() for x in re.finditer(b, a)]

#########################

# import requests
#
# r = requests.get('https://ubima.ru')
#
# with open('ubima.html', 'w') as f:
#     f.write(r.text)

##########################

# from datetime import datetime
# from collections import deque
#
#
# def reverse(num: int):
#     res = deque(str(num))
#     res.reverse()
#     if num < 0:
#         res.rotate()
#     return int(''.join(res))
#
#
# def reverse2(num: int):
#     return int(''.join(reversed(str(num)))) if num > 0 else -int(''.join(reversed(str(num)[1:])))
# #
# def reverse1(num):
#     """
#     САМОЕ МЕДЛЕННОЕ РЕШЕНИЕ!
#     :param num:
#     :return:
#     """
#     r = 0
#     sign = num // abs(num)
#     num = abs(num)
#     while num != 0:
#         r *= 10
#         r += num % 10
#         num //= 10
#     return r * sign
#
#
# stat = datetime.now()
#
# print(reverse(10*10**2000))
# end = datetime.now()
# res = end - stat
# print(f"Дека {res}")
# stat = datetime.now()
# print(reverse1(10*10**2000))
# end = datetime.now()
# res = end - stat
# print(f"Числом {res}")
# stat = datetime.now()
# print(reverse2(10*10**2000))
# end = datetime.now()
# res = end - stat
# print(f"Однострочник {res}")

##########################

# def translator(str_inp: str, CONST: str = 'двуликий') -> str:
#     """
#     8 задача марафона
#     :return: изменённая строка по условию задачи
#     """
#     bin_l: list = [bin(x) for x in bytearray(str_inp.encode('utf-8'))]
#     res: str = ' '.join(''.join(map(lambda x, y: x.upper() if int(y) else x, CONST, bin_l[_])) for _ in range(len(bin_l)))

#     return res
#
# print(translator("Hi"))# "дВулИкий дВУлИкиЙ"
# print(translator("123")) # "двУЛикиЙ двУЛикИй двУЛикИЙ"

###########################

# from itertools import chain

# def valid_bracket(s_inp: str):
#     CONST: tuple = (('(', ')'), ('[', ']'), ('{', '}'), ('<', '>'))

#     res: list = [x for x in s_inp if x in chain.from_iterable(CONST)]
#     if len(res) % 2:
#         return False
#     return all(res.index(x) + 1 == abs(res.index(y) - len(res)) for x, y in CONST if x in res and y in res)
#
# print(valid_bracket("([])"))
#
#
# def is_anagram(word1, word2) :
#     temp: list = list(word1)
#     try:
#         return bool([temp.pop(temp.index(char)) for char in word2])
#     except ValueError:
#         return False
#
# print(is_anagram('anagrama', 'nagaramm'))

###########################

# from itertools import takewhile
#
# def longest_prefix(lst: list) -> str:
#     return lst[0][:sum(takewhile(int, (len(set(x)) == 1 for x in zip(*lst))))]
#
# print(longest_prefix(['flower', 'flow', 'flight']))
# print(longest_prefix(['sol', 'ution']))
# print(longest_prefix(['car', 'cir']) )

##########################

# def can_exit(matrx: list[list]) -> bool:
#     """
#     10я задача
#     :param matrx:
#     :return:
#     """
#     if matrx[-1][-1] != 0:
#         return False
#     i_zero: list = []
#     for j,item in enumerate(matrx):
#         i_zero.append([])
#         for i, val in enumerate(item):
#             if val == 0:
#                 i_zero[j].append(i)
#
#     result: list = [[x for x in i_zero[i] if x in i_zero[i+1]] for i in range(len(i_zero)-1)]
#     return all(num in i_zero[-1] for num in range(result[-1][-1], 7))
#
#
# print(can_exit([
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 1, 0, 1, 1],
#   [1, 0, 0, 0, 0, 1, 1],
#   [1, 1, 1, 1, 0, 0, 1],
#   [1, 1, 1, 1, 1, 0, 0]
# ]))
#
# print(can_exit([
#   [0, 1, 1, 1, 1, 1, 1],
#   [0, 0, 1, 0, 0, 1, 1],
#   [1, 0, 0, 1, 0, 1, 1],
#   [1, 1, 0, 1, 0, 0, 1],
#   [1, 1, 0, 0, 1, 1, 0]
# ]))
#
# print(can_exit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 1, 1, 1, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 1]
# ]))
#
# print(can_exit([
#   [0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0],
#   [1, 1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1, 0],
#   [1, 1, 1, 1, 1, 1, 0]
# ]))

############################

# Тип функции завит от конкретного значения аргумента: (@overload)


# from typing import Final, overload, Literal, Union, IO, Text, Any

# @overload
# def open(path: Union[str, bytes], mode: Literal['r','w','a','x','r+','w+','a+','x+'],) -> IO[Text]:
#     """
#     Говорит что если на вход передаются такие модификаторы открытия файла ('r','w','a','x','r+','w+','a+','x+'), то
#     будет выход (IO) текст
#     """
#     pass
#
# @overload
# def open(path: Union[str, bytes], mode: Literal['rb','wb','ab','xb','r+b','w+b','a+b','x+b'],) -> IO[bytes]:
#     """
#     а если такие, то на выходе будут уже байты:
#     :param path:
#     :param mode:
#     :return:
#     """
#     pass
#
# @overload
# def open(path: Union[str, bytes], mode: str) -> IO[Any]:
#     pass

###############################

# def unique_char(s: str) -> int:
#     for i, val in enumerate(s):
#         if s.count(val) == 1:
#             return i
#     else:
#         return -1
#
#
# def unique_char1(string):
#     counter = 0
#     try:
#         while string.count(string[counter]) - 1:
#             counter += 1
#         else:
#             return counter
#     except:
#         return -1
#
#
# print(unique_char('python'))
# print(unique_char('pythonTop'))
# print(unique_char('aabb'))

##############################

# ещё одно поле в таблице пользователей - варифакация да-нет и проверять её при использовании функций бота,
# давить 3 кнопки : сегодня завтра указать дату

#print(datetime.datetime.now().hour)
# time_zone = pytz.timezone('Europe/Moscow')
# time_now = time_zone.localize(datetime.datetime.now())
# #print(time_now.date())

# timezone = 'Europe/Moscow'
# NYC = zoneinfo.ZoneInfo(timezone)
# datetime(2020, 1, 1, tzinfo=NYC)

#######################################

# симулировать 4 бросока кубика и записать сумму 3 самых больших
# бросков. Так нужно будет сделать для каждой характеристики.


# from secrets import choice
# from math import floor
#
# class DndCharacter:
#     """
#     =======================
#     Create Character object
#     =======================
#
#     Cимуляция 4х бросоков кубика -> запись суммы 3х самых больших бросков для каждой характеристики при
#     создании объекта класса (персонажа).
#
#     """
#     def __new__(cls):
#         self = object.__new__(cls)
#
#         def _creation_values() -> int:
#             return sum(sorted((choice(range(1,6)) for _ in range(4)))[1:])
#
#         self._charisma = _creation_values()
#         self._wisdom = _creation_values()
#         self._constitution = _creation_values()
#         self._dexterity = _creation_values()
#         self._strength = _creation_values()
#         self._intelligence = _creation_values()
#         self._health = 10 + floor(self._constitution / 2)
#
#         return self
#
#     @property
#     def charisma(self):
#         return self._charisma
#
#     @property
#     def wisdom(self):
#         return self._wisdom
#
#     @property
#     def constitution(self):
#         return self._constitution
#
#     @property
#     def dexterity(self):
#         return self._dexterity
#
#     @property
#     def strength(self):
#         return self._strength
#
#     @property
#     def intelligence(self):
#         return self._intelligence
#
#     @property
#     def health(self):
#         return self._health
#
# a = DndCharacter()

#####################################

# loop = asyncio.get_event_loop()
#
# async def my_func():
#     delay = 20
#     # твоя логика с отправкой сообщений тут
#     print('qwdqwfqfq')
#     when_to_call = loop.time() + delay  # delay -- промежуток времени в секундах.
#     loop.call_at(when_to_call, my_callback)
#
# def my_callback():
#     asyncio.ensure_future(my_func())

# import asyncio
# import time
# from datetime import datetime, date, time, timedelta
# async def at_minute_start():
#     while True:
#         now = datetime.now().minute
#         # after_minute = now.second + now.microsecond / 1_000_000
#         if now == 45:
#             print('qcqce')
#             await asyncio.sleep(10)
#         else:
#             await asyncio.sleep(10)

# loop = asyncio.get_event_loop()
# loop.create_task(at_minute_start())
# loop.run_forever()

######################################################

# import hmac
# import pickle
# pkl_key = 'secret-key'
# msg = pickle.dumps(a_obj, protocol=5)
# digest: bytes = hmac.digest(pkl_key.encode(), msg, 'sha256')
#
#
# try:
#     with open('data_todo.pickle', 'wb') as f:
#         for items in (digest, b'delimiter', msg):
#             f.write(items)
#
# except pickle.PicklingError:
#     print('Ошибка сериализации (записи)')
# try:
#     with open('data_todo.pickle', 'rb') as f:
#         dig, new_data = f.read().split(b'delimiter')
#         # Безопасное сравнение подписей.
#         dig_1: bytes = hmac.digest(pkl_key.encode(), msg, 'sha256')
#         if hmac.compare_digest(dig_1, dig):
#             raise pickle.UnpicklingError
#         read_obj = pickle.loads(new_data)
#
# except pickle.UnpicklingError:
#     print('Ошибка десериализации (чтения)')
#
# print(read_obj.i)
#print(hash_out == hash_inp)

###################################

# try:
#     try:
#         raise  Exception('a')
#     except Exception as e_a:
#         print('e_a')
#         print(e_a)
#         raise Exception('b') from e_a
# except Exception as e_b:
#     print('e_b')
#     print(e_b)
#     #print_exception(e_b)

####################################

# def num_armstrong(num):
#     """
#     Проверка на 'число Aрмстронга'
#     :param num:
#     :return:
#     """
#     if len(val := str(num)) == 1:
#         return True
#     return sum(int(x) for x in map(lambda x: int(x) ** len(val), val)) == num
#
# print(num_armstrong(153))

#####################################

