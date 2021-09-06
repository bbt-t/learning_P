from myclasses import *

# def speedtest():
#     import speedtest
#     """
#     Тест скорости интернета
#     :return: upload/download в мбит/с
#     """
#     my_speed = speedtest.Speedtest()
#     speed_dl = my_speed.download()/(2**20)
#     speed_upl = my_speed.upload()/ (2**20)
#     return f"Скорость скачивания {speed_dl: 1.1f} мбит/с' Скорость отдачи {speed_upl: 1.1f} мбит/с'))"

############

# def user_lat_rand(num: int) -> list:
#     """
#     Рандомные (случайные) буквы
#     :param num: сколько букв
#     :return: список
#     """
#     from random import choice
#     from string import ascii_letters
#
#     return list("".join(choice(ascii_letters) for x in range(num)))

# def nn(num):
#     """
#     Выводит список рандомных чисел
#     :param num: сколько чисел вывести
#     :return: список из рандомных чисел
#     """
#     return list("".join(random.choice(string.digits) for x in range(a)))
#
#     Рандомный список: return list("".join(random.choice(string.digits) for x in range(a)))

####################

# while True:
#     try:
#         user_choice = input("Do you have display random letter? YES/NO ")
#         if user_choice == "y" :
#             user_numb = int(input("How many letters do you need? : "))
#
#             print(user_lat_rand(user_numb))
#
#             numb_gen = user_lat_rand(user_numb)
#
#             numb_gen_1 = tuple(numb_gen for s in range(user_numb))
#             print(numb_gen_1)
#
#             break
#         elif user_choice == "n" :
#             print("Oh...ok...see u late!")
#             break
#         else:
#             print("Try again!")
#
#     except():
#         print("Error! Try again!")


# def adic(a):
#     b = min(a), a.index(min(a))
#     c = max(a), a.index(max(a))
#     cb = b,c
#     return  list(cb)
# numb = [1,2,3,4,5]
# print(adic(numb))


#dict_1 = {a: a for a in range(user_num)}                        #простой генератор словаря

# Самостоялка перед множествами
#
#
# user_num = int(input("Enter 6: "))
# if user_num == 6 :
#
#     list_1 = nn(user_num)
#     list_2 = nn(user_num)
#     list_3 = []
#
#     print("First list: ", list_1)
#     print("Second list: ", list_2)
#
#     list_4 = list_2[::1]
#
#
#     for i,v in enumerate(list_1):
#         if i %2==0:
#             list_3.insert(i,v)
#
#         else:
#             list_3.append(list_4[i])
#
#     print("YAHOOO! ", list_3)
#     list_3 = list(map(int,list_3))
#     print("FINAL! ",list_3)

# Уборать повторения из списка
# n = [1,33,2,2,3,1,88,5,4,1,77,7,]
# n = list(set(n))
# print(n)

# a = {1,2,3}
# b = {3,8,7}
# a.update(b)
# print(a)
# print(a.isdisjoint(b))

# Преобразует ввод в список или просто показывает число:

# n = list(input("Enter: "))
# count = 0
# a = []
# while count < len(n): (не обязательно! смотри ниже!)
#
#     for digits in n :
#         count += 1
#         a.append(digits)
#         print(digits, end=" ")
# print(a)

# Самостоятельные задания множества№2
# import sys
# while True:
#     try:
#         a = set(input("Enter 1: "))
#         b = set(input("Enter 2: "))
#
#         a_1 = set()
#         b_1 = set()
#
#         for value in a:
#             a_1.add(int(value))
#
#         for value in b:
#             b_1.add(int(value))
#
#         print(a_1)
#         print(b_1)
#         print(a_1 & b_1)
#
#         sys.exit()
#     except(ValueError):
#         print("Ошибочка! вводи только числа!")

# Самостоялка множества №1
# a = set(range(1,31))
#
# b = set()
# count_1 = 0
# count_2 = 0
#
# for digits in a:
#
#     if digits > 10 and count_1 < 5 :
#         count_1 += 1
#         b.add(digits)
#
#     elif count_2 < 10 and digits in range(10, 31):
#         count_2 += 1
#         b.add(digits)
# print(len(b))

# Самостоялка №3
# a = input("Введи текст: ")
# dict_let = ["a","e","i","u","o","а","е","ё","и","о","ю","я","у"]
# b = []
# for letters in a:
#     if letters.lower() in dict_let:
#         b.append(letters)
# print("".join(b))
# Самостоялка №4
# a = set(range(51))
# b = set()
# for diggers in a:
#     if (diggers/3).is_integer() == True and (diggers/4).is_integer() == False :
#         b.add(diggers)
#
#     elif (diggers / 3).is_integer() == False and (diggers / 4).is_integer() == True:
#         b.add(diggers)
# print(b)
# САМОСТОЯТЕЛЬНАЯ № 6

# user_numb = int(input("Enter number: "))
# user_list = []
# for number in range(1,user_numb+1):
#     if user_numb > 0 :
#         user_list.append(number)
#
# #list(reversed(user_list)) #СОЗДАЁМ!!! если использовать метод .sort() НЕ возвращает результат соритировки (NONE)!

# result = dict(zip(user_list, list(reversed(user_list)))) #создаём словарь из 2х списков с помощью zip!(ключи, значения)
#
# print(result)


# def user_card_secure(user_card):
#     if user_card.isalnum() == True:
#     number_card = user_card[len(user_card) - 4:].rjust(len(user_card), '*')
#     return number_card
#

# Самостоялка №2
# user_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#
# def sort_number(a):
#     for number in a:
#         if number %2 == 0:
#             a.remove(number)
#     return a
#
# print(sort_number(user_list))

# #РЕКУРСИЯ ,работает только до "глубины вызова" = 1000!
# def func(a,b):
#     if a == b :
#         return f"{a}"
#     elif a > b :
#         return f"{a}, {func(a-1,b)}"
#     else: #a < b
#         return f"{a}, {func(a+1,b)}"
#
# print(func(1,998))#работает только до "глубины вызова" < 1000!

# a,b,*c = [True,2,'Hello',3,10,55]
# print(a,b,c)
# s = [4,10]
# print(*s)

# def is_cat_here(*args):
#     if str(args).lower().find("cat") > 0:
#         return True
#     else:
#         return False
#
# a = 'privet'
# b = 'paka baka caT 123124ka'
# c = 'wvwvw qdqcq'
# print(is_cat_here(a,b,c))


#                                                     # NONLOCAL
# def akama():
#     a = "one"
#
#     def akama_2():
#         nonlocal a
#         a = "two"
#         print(a)
#     akama_2()
#     print(a)
# akama()

#                                     #СОЗДАНИЕ КЛАССА ИМЯ КЛАССА ЗАПИСЫВАЕТСЯ КАЖДОЕ СЛОВО С БОЛЬШОЙ БУКВЫ!!!
# class MyFirstClass:
#     is_a_car = True #ОБЩЕЕ ДЛЯ ВСЕХ!
#     number_def = 4
#     def __init__(self,name,color,year):
#         self.name = name
#         self.coloor = color
#         self.year = year
#
# object_my_Class = MyFirstClass(name="Ohhh",color='red',year=1990)
# print(object_my_Class.name)
#
# object_my_Class_1 = MyFirstClass(name="UUUHHH",color='yellow',year=2000)
# print(object_my_Class_1.year)
#
# print(object_my_Class.is_a_car, object_my_Class_1.is_a_car)
#
# a = MyFirstClass.number_def *3                #МОЖНО ОБРАЩАТЬСЯ НАПРЯМУЮ К КЛАССУ (Н/Р 4*3 = 12)
# print(a)
#
# #Пример
# class BlogPost:
#     def __init__(self,name,txt,likes):
#         self.user_name = name
#         self.text = txt
#         self.number_likes = likes
#
# proba = BlogPost(name="Baba",txt="говорит",likes=22)
#
# print(proba.text)
#
#                                         #СОЗДАНИЕ МЕТОДА
#
# class MyNewClassForCar:
#
#     def __init__(self,name,color,year):
#         self.name = name
#         self.coloor = color
#         self.year = year
#
#     def drive(self):
#         print(self.name +" GoGo!")
#
# mazda = MyNewClassForCar("maZzda","Red",2010)
# mazda.drive()


# нужно {'name':'John','top_note':5}
# РЕКУРСИЯ
# def show(txt):
#     if len(txt) == 0:
#         print("|")
#     else:
#         print("|",txt[-1],end="",sep="")
#         show(txt[:-1])
#
# show("Privet Python!")

# def name():
#     s=8
#     for number in [3,5,10]:
#         yield number
#         print(s)
#         s = s*10
# g = name()
# print(next(g))


# n = {"a":1,"b":2,"c":3}
# iter_n = list(iter(n.items()))
# print(iter_n)

# Как сделать свой итератор (iter-класс):
# class custom_range:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start < self.end:
#             number = self.start
#             self.start+=1
#             return number
#         raise StopIteration
#
# first_range = custom_range(1,20)
#
# for number in first_range:
#     print(number)

# Пример беспонечной последовательности целых чисел:
# def get_inf_square_gen():
#     """
#     Бесконечный генератор целых чисел
#     :return: целое число
#     """
#     numb = 1
#     while True:
#         yield pow(numb,2) #или numb**2
#         numb+=1
# inf_square_generator = get_inf_square_gen()
# print(next(inf_square_generator))

#################

# БЕСКОНЕЧНЫЙ ПЕРЕБОР:
# def even_gen():
#     """
#     Бесконечный генератор из заданной последовательности
#     :return: значение из последотельности
#     """
#     gen_list = ['even', 'odd', 'second']
#     while True:
#         for value in gen_list:
#             yield value

# infinity_gen = even_gen()
#
# print(next(infinity_gen))
# print(next(infinity_gen))

####################
# Чтение из файла:
# n = 10
# a = ~n+1
# print(n)
# print(a)
# b = (input("Введи текст: \n"))
# a = open("D:\\123.txt", "a")
# a.write(b)
# a.close()
# c = open("D:\\123.txt")
# print(c.read())
# c.close()

# ВЫВОД ПОСТОЧНО
# a = open("D:\\123.txt")
# #b = a.readlines()
# #a.close()
# for l in a:
#     print(l,end="")
#
# a.close()

# a = open("D:\\123.txt").readlines()
# b = "".join(open("D:\\123.txt").readlines())
#
# print(b)

# Контекстный менеджер with:

# with open("D:\\123.txt") as fm:
#     for l in fm:
#         print(l,end="")


# with open("D:\\123.txt") as text_user:
#     text_in_list = []
#     for t in text_user:
#         text_in_list.append(t.strip("\n"))
#     print(text_in_list)


# with open("D:\\12343.txt", "a+") as sfile:
#     sfile.seek(0,2)
#     sfile.write("\nPrivet!")

# with open('D:\\12355.txt','bw') as test_file:
#     test_file.write(bytes([1,2,3]))
#
# with open('D:\\12355.txt','br') as test_file:
#     for number in test_file:
#         print(number)

###############

# import os
# import random
# from datetime import date
# date_1 = date(2020,3,8)
#
# print(date_1)
# date_2 = date(2020,4,10)
# print(date_2)
#
# print((date_2-date_1).days)

# date_1 = input("Введи число через пробел: ")
#
# def input_time(date_user):
#     date_user = list(map(int,date_user.split(" ")))
#     return f"Введенная дата : {date(date_user[0],date_user[1],date_user[2])}"
#
# print(input_time(date_1))


# для итерации по нескольким спискам используем ZIP!:
# a = [1,2,3,4,5]
# b = ['c','d','f']
# for list_1,list_2 in zip(a,b):
#     print(list_1,list_2)


# dict_1 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# # for value in dict_1['k1'][0]['nest_key'][1]:
# #     print(value)
# или просто через [0] индекс в конце:
# print(dict_1['k1'][0]['nest_key'][1][0])
# dict_2 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# # for value in dict_2['k1'][2]['k2'][1]['tough'][2]:
# #     print(value)
# или просто через [0] индекс в конце:
# print(dict_2['k1'][2]['k2'][1]['tough'][2][0])

#                                     #1 способ жестко привязанный к поиску именно 007
# list_game = [1,2,4,0,0,7,5] #True
# list_game_1 = [1,0,2,4,0,5,7] #True
#
# def spy_game(list_from_game: list) -> bool:
#     """
#     способ №1 , жестко привязанный к поиску именно 007
#     :param list_from_game: список
#     :return: BOOL
#     """
#     list_str = str(list_from_game).replace(",","").replace(" ","")
#     if list_str.find("007") > 0:
#         return True
# print(spy_game(list_game))
#
#
# def spy_game_1(list_from_game: list) -> bool:
#     """
#     2й способ (между 0 0 7 могут быть другие цифры)
#     :param list_from_game:
#     :return: BOOL
#     """
#     code = [0,0,7,"x"]
#     for num in list_from_game:
#         if num == code[0]:
#             code.pop(0)
#     return len(code) == 1
# print(spy_game_1(list_game))

#############

# import pickle
#
# honda = ('cbr','yellow',2010,((1,'Ivan'),(2,'Nik')))
#
# with open('D:\\honda.pickle','r+b') as honda_test_write:
#     pickle.dump(honda,honda_test_write)
#
# with open('D:\\honda.pickle','rb') as honda_in_file_pickle:
#     exp_from_file = pickle.load(honda_in_file_pickle)
#
# print(exp_from_file)

#import shelve

# with shelve.open('D:\\shelvwrit_test') as test_of_shelve_module:
#     test_of_shelve_module['opel'] = 'Germany'
#     test_of_shelve_module['bugatti'] = 'Italy'
#     test_of_shelve_module['reno'] = 'France'
#     test_of_shelve_module['avito'] = 'England'
#
#     print(test_of_shelve_module['reno'])


#
#
# a = [1,2,2,10,7]
# a = list(set(a))
# print(a)

###################

# ПЕРЕМНОЖИТЬ ВСЕ ЭЛЕМЕНТЫ СПИСКА можно ЧЕРЕЗ math.prod() !
# import math
# print(math.prod(a))

##############

# ОЧЕНЬ ВАЖНО ЗНАТЬ И ИСПОЛЬЗОВАТЬ!!!!!!!!!!!!!!!

# sequence = '2 3 1 5 9 22 3 5'
# sequence_list = list(map(int,sequence.split(" ")))
# print(sequence_list)

# перебор значений списка по условиям:
# list_test = list(x for x in sequence_list if x%2!=0)
# list_test_2 = list(x for x in sequence_list if x%2==0)

# first_number = list_test[len(list_test_2)]  #первое значение в более длинном списке
#
# print(first_number)

#################

# def is_divisible(num):
#     return num % sum(map(int,str(num))) == 0
# print(is_divisible(75))

#################

# СОЗДАНИЕ КЛАССА:
# class Person:
#     ### Общие атрибуты (поля)
#     some_num = 10
#
#     ###
#     ### КОНСТРУКТОР. Необходим чтобы нельзя было создать обьект этого класса в некорректном(не валидном) состоянии!
#     # Н/р: нельзя создать обьект класса не указав name,surname,birth
#     #Вызывается при создании обьекта класса (human_1 = Person()) ему сразу автоматом присваиваются эти атрибуты !
#
#     def __init__(self, name, surname, place_of_birth, birth):
#         # "self" - это ссылка на то, из чего вызывается метод
#         self.name = name #определение аргумента при вызове
#         self.surname = surname
#         self.place_of_birth = place_of_birth
#         self.birth = birth
#         print(f"Создали обьект класса {self}")
#     #Защита от перезаписи
#     @property
#     def name(self):
#         return self.name
#     ###
#     ### Методы:
#     def get_age(self, year):
#         print(f"Ему {year - self.birth} лет")
#
#     def info(self):
#         print(f"Фамалия: {self.surname}, Имя: {self.name}")
#
# ##### Без конструктора:
# # human_1 = Person() ==> вывод "Создали обьект класса <__main__.Person object at 0x000001B4112A6FD0>"
# # human_1.name = "Vasya"
# # human_1.surname = "Musk"
# # human_1.place_of_birth = "Africa"
# # human_1.birth = 1980
# #
# # human_2 = Person()
# # human_2.name = 'Sergey'
# # human_2.surname = 'Vegan'
# # human_2.place_of_birth = 'RF'
# # human_2.birth = 2000
# #
# # human_2.info()
# # #Person.info(human_1) #то же самое что и выше, но КРАЙНЕ редко используется!!!
# # human_1.get_age(2020)
# #####
#
# #####НАПРЯМУЮ к общим атрибутам класса (даже без создания обьекта класса) можно обратиться только так!
# # print(Person.some_num)
#
# ##### С конструктором:
#
# human_1 = Person("Vasya","Musk","Africe",1980)
#
# print(human_1.some_num) #=> 10
# #Поменять значение ОБЩЕГО атрибуса через human_1 НЕ ПОЛУЧИТСЯ!
#
# #НО! если это сделать,то у обьекта human_1 повится новый атрибут с тем же названием, ОН ПЕРЕКРОЕТ общий атрибут
# #класса (some_num) т.е будет ПРИОРИТЕТНЕЙ для этого обьекта!!!
# human_1.some_num = 123
# print(human_1.some_num) #===> 123 !!! атрибут обьекта приоритетней чем общий атрибут класса с тем же именем(10)
#
# print(Person.some_num) # => 10
#
# #Через вызов самого класса и метода ПОЛУЧИТСЯ!
# Person.some_num = 123
# print(human_1.some_num) #=> 123
# from pprint import pp

# from Scripts import today

#
# Vasya = MyFerstClassHuman("Vasya",1989,190,"yellow","Moscow")
# Petya = MyFerstClassHuman("Petya",1995,175,"red","Zade")
# Pykamyka = MyFerstClassHuman.dfltcolor("Myka",1999,170,"Taun")
# Testimperson = MyFerstClassHuman.dflth("Vasya",1989,"yellow","Moscow")
# Vasya.sity
# print(Pykamyka.color_hair)
# print(Testimperson.height)
#
#
# dude = BankAccount(1337,"Linda","Abramovich",3000)
# print(dude.getbalance())
# dude.add(2000)
# print(dude.getbalance())
# dude.withdraw(5000)
# print(dude.getbalance())

# namenewclass = Shape()
# namenewclass_1 = Rect()
# tets = DomZ("ecwce")
# #tets = DomZ.allsome("ecwce")
# tets.display()
# print(tets.__doc__())
#
# import re
#
# a = "Hello my Friend! How are u?"
#
# print(re.sub("How are u", "Who u are", a))
# print(re.findall("my",a))
# print(re.split("How", a))
#
# test_class_init_2 = TestchClass(name='Ivanin',age=23)
#
# print(test_class_init_2.name)
#
# print(((lambda x,y: x + y )(1,2)))
#
# ppp = DomZ("Vkvw","11")
# print(DomZ.__name__)
# print(ppp.__class__.__name__)
# print(type(ppp))


# # Для ускорения математических вычислений в '100 раз' с помощью njit :
# from numba import njit
#
# import math
# from time import perf_counter
#
# @njit(fastmath = True)
# def pryme_test(num):
#     if num == 2:
#         return True
#     if num <= 1 or not num %2:
#         return False
#     for div in range(3,int(math.sqrt(num)) + 1,2):
#         if not num %div:
#             return False
#     return True

# @njit(fastmath = True)
# def run_prog(N):
#     for i in range(N):
#         pryme_test(i)
#
#N = 10000000
#start = perf_counter()
#run_prog(N)
#end = perf_counter()
#print(end - start)

#########################

# ad = int(input())
# n = 2
# while ad % n != 0:
#     n+=1
# print(n)

# a = {'hello': 'world','im':'FINE!'}
#
# print(a.get('123','default_value'))

# filename = 'foobar.txt'
# a,b = filename.rpartition('.')
# print(a,b,sep="\n")

# import hashlib
# print(hashlib.md5('ivan'.encode('utf-8')).hexdigest(), hashlib.md5('iva n'.encode('utf-8')).hexdigest(),sep="\n")

# a = TestchClass(11,"Vanusha")
# print(a.age)
#
# m_t = MyTime()
# print(m_t.ep)
#
# my_game = Game()
# print(my_game.flip)

# import datetime
# import time
# print(datetime.date.isoformat(datetime.date.today()))
# print(time.strftime("%I:%M %p"))

# string_exapm = 'abcd'
# print(string_exapm:=string_exapm.upper())
# print(string_exapm)

# up = str_exp("tt")
# print(up)
# print(str(up))
# print(len(up))
#
# x = 'abc'
# y = 'abc'
# xy = ['abc','abc']
# print(id(x), id(y), id(xy[0]), sep="\n")
#
# some_list_ = ["Andr", "Olya", "Opel"]
# immap = filter(lambda x:x.startswith("O"), some_list_)
# print(tuple(immap))
#


# def abcsd(x:int)->str :
#     return f"{x} is fine!"
# import sys
# foo = [1,2,3]
#
# print(sys.getrefcount(foo))

###############

# ЗАМЫКАНИЯ:

# def exp_z():
#     inp_list = []
#     def list_c(exp_z):
#         inp_list.append(exp_z)
#         return inp_list
#
#     return list_c
#
# for_exp = exp_z()
# print(for_exp(12))
# print(for_exp(11))
# Узнать значения в замыкании:
# get_result = for_exp.__closure__[0].cell_contents

# def pow_(base=1):
#     return lambda base: base*3
# abcsds = pow_()
# fasga = pow_()
# print(abcsds(2))
# print(fasga(10)+10)
#
#
# def names():
#     all_names = []
#
#     def inner(name:str) -> list:
#         all_names.append(name)
#         return all_names
#
#     return inner
#
# students = names()
# print(students("Vasya"))
# print(students("Petya"))
# print(students("Igor"))
#
# print("OK!" if "Igor" in students.__closure__[0].cell_contents else "NO!")

###############

# def calc(imp_expression):
#     a = "+-/*"
#     if not any(imp_exp in imp_expression for imp_exp in a):
#         raise ValueError(f'Выражение должно содержать оператор из ({a})')
#     elif ',' in imp_expression:
#         raise ValueError ("Выражение не должно содержать запятые!")
#     else:
#         try:
#             return eval(imp_expression)
#         except:
#             return f"{imp_expression} не корректно!"

#############

# Уменьшение вложенности списка:

# v_list = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[13,14,15]]
#
# g_list = [x for row in v_list for x in row]
# s_list = [x for row in g_list[:4] for x in row]
# print(s_list)

#####################

# Пример использования модуля datetime:

# def log_message(message, when=None): #ОЧЕНЬ! важно указывать параметр по умолчанию именно NONE !!!
#     when = (datetime.datetime.now()).strftime('%m/%d/%y %H:%M:%S')
#
#     print(f'{when} : {message}')
#
# log_message('Priv!')

# from itertools import zip_longest
# names = ('Ed','Paris','Emilia')
# list_let = [len(n) for n in names]
# print(*[f"{count}: {name}" for name,count in zip_longest(list_let, names)])

# def format_numbers(phone_number: str) -> str:
#     result = ['7', '(', '0', '0', '0', ')', '0', '0', '0', '-', '0', '0', '-', '0', '0']
#     phone_number = filter(str.isdecimal, phone_number)
#     n = 0
#     while n != len(result):
#         if result[n].isdecimal():
#             result.pop(n)
#             result.insert(n, next(phone_number))
#             n += 1
#         else:
#             n += 1
#     return f"+7{''.join(result[1:])}"

####################

# Тестирование кода:
# for _ in phone_number:
#     assert format_numbers(_) == "+7(909)101-10-10"
#     print(f"{_} --> OK!")
# print("FINISH!")

# def foo(x,y):
#     """
#     Отлавливаем произошедшую ошибку
#     :param x: pass
#     :param y: pass
#     :return: вывод ошибки (если она произошла)
#     """
#     try:
#         return x//y
#     except (TypeError, ZeroDivisionError) as e:
#         print(f"ERROR! {e}")
#         print(type(e))

####################

# while True:
#     command = input("Введите команду: ")
#     if command == 'help':
#         print(HELP)
#     elif command == 'show':
#         print(tasks)
#     elif command == 'add':
#         date_for_task = input("Введите дату: ")
#         task = input("Введите название задачи: ")
#         if tasks[date_for_task] in tasks:
#             tasks[date_for_task].append(task)
#         else:
#             tasks[date_for_task] = []
#             tasks[date_for_task].append(task)
#         print(f"Задача {task} добавлена на {date_for_task}")

#################

#                       Создание копии файла в реверсе:

# with open("D:\\dataset_24465_4.txt","r") as text_1 , open("D:\\dataset_exp.txt","w") as text_2:
#     text_inp = [x.strip() for x in text_1]
#     for _ in text_inp[::-1]:
#         text_2.write(_+"\n")

###########################

# from collections import OrderedDict, defaultdict, deque
# a = {"a":1,"b":2,"c":3,"d":4}
# a = OrderedDict(a)
# a.move_to_end("b")
# print(a)

# a = deque([1,2,3],maxlen=3)
# a.appendleft(5)
# print(a)
# print(len(a))
# a.pop()
# print(a)

########

# a = [19, 46, -2097, 134]

# # def ends_add_to_10(lst: list) -> int:
# #     #return sum(x // 10 for x in (int(x[0]) + int(x[-1]) for x in map(str, map(abs, lst))) if x == 10)
# #     #return sum(x // 10 for x in (eval(f'{v[0]}+{v[-1]}') for v in map(str, map(abs, lst))) if x == 10)
# #     return sum(int(str(abs(v))[0]) + int(str(abs(v))[-1]) == 10 for v in lst)

# Моямодификация функции выше:
#     return sum(eval(f"{x[0]} + {x[-1]}") == 10 for x in map(str, map(abs, a)))

# # print(ends_add_to_10(a))
########

# a = 'hello world tt Privet pipkA m'
#
# def revers_str(string: str) -> str:
#     """
#     Функция размещает буквы тексте в алфавитном порядке.
#     :param string: любая строка (желательно без цифр).
#     :return: новая отсортированая строка с сохранением пробелов 'hello world -> dehll loorw'
#     """
#     if not isinstance(string, str):
#         raise TypeError('Argument must be a string')
#
#     string_sort: list = sorted(string.replace(" ", ""))
#     for _ in (i for i, x in enumerate(string) if x.isspace()):
#         string_sort.insert(_, " ")
#     return ''.join(string_sort)

########
# def is_prime_number(num: int) -> bool:
#     """
#     Проверка входящего числа на принадлежность к простому.
#     :param num: целочисленное неотрицательное (int)
#     :return: True если число простое
#     """
#     result: list = []
#     for _ in range(num):
#         if _ % 2 != 0:
#             result.append(num % _ == 0)
#     return sum(result) == 1
#
# print(is_prime_number(2))
#####


#                       При обращении к несузествующему ключу вернётся None а не ошибка!
# some_dict = {'a':1,'b':2,'c':3}
# print(some_dict.get('v'))

#                                   Найти вхождения строки в строку:
# for_find_str, find_str = [input() for i in range(2)]
# result_find = [for_find_str.startswith(find_str, i) for i in range(len(for_find_str))]
# print(sum(result_find))

#                           Узнать самый частый элемент в последовательности:
# lst = [1, 3, 3, 3, 2, 5, 6, 6, 7, 7, 7, 7, 7, 8, 9]
#
# max_item = max(lst, key=lst.count)
# print(max_item)

#####
#                                     Время выполнения кода:
# from datetime import timedelta, datetime
# import time
#start_time = time.monotonic()
#sort_by_count(my_arr_a,my_arr_b)
#end_time = time.monotonic()
#print(f"не моя версия {timedelta(seconds=end_time - start_time)}")

# start_time = time.monotonic()
# my_sort_count(my_arr_a,my_arr_b)
# end_time = time.monotonic()
# print(f"моя версия {timedelta(seconds=end_time - start_time)}")

# start_time = datetime.now()
# sort_by_count(my_arr_a,my_arr_b)
# end_time = datetime.now()
# print(f"выполнено {end_time-start_time}")
# start_time = datetime.now()
# my_sort_count(my_arr_a,my_arr_b)
# end_time = datetime.now()
# print(f"мой выполнено {end_time-start_time}")

#####

# #                             Создание словаря с помощью ZIP :
# set_exp = {7,8,9}
# list_exp = [1,2,5]
# dict_exp = dict(zip(set_exp,list_exp))
# print(dict_exp)

# import logging
#
# logger = logging.getLogger()
# print(logger)
#
# def main(name):
#     logger.warning(f"Enter in the main() func: name = {name}")

# Массивы:
from array import *

def arra_exmp(n):
    n.append(4.7)

names = array('i', [
    36739,
    2,
    3,
    4,
])

if __name__ == '__main__':
