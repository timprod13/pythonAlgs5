"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
import timeit


# решил все операции записать в одну функцию, надеюсь, что это не ошибка
def my_dict_func():
    my_dict = {}
    for i in range(100):
        my_dict[i] = i * 2
    for i in range(len(my_dict)):
        my_dict.get(i)
    for i in range(len(my_dict)):
        my_dict.pop(i)
    my_dict.values()


def my_ordered_dict_func():
    my_ordered_dict = OrderedDict()
    for i in range(100):
        my_ordered_dict[i] = i * 2
    for i in range(100):
        my_ordered_dict.get(i)
    for i in range(100):
        my_ordered_dict.pop(i)
    my_ordered_dict.values()


my_dict_func()
my_ordered_dict_func()
print(
    f'my_dict_func()         {timeit.timeit("my_dict_func()", setup="from __main__ import my_dict_func", number=10000)}\n'
    f'my_ordered_dict_func() {timeit.timeit("my_ordered_dict_func()", setup="from __main__ import my_ordered_dict_func", number=10000)}')

''' Вывод результатов тестирования:
my_dict_func()         0.1962216
my_ordered_dict_func() 0.3487477
'''

# Изначально стоит сказать, что как минимум наличием одной команды OrderedDict превосходит обычный словарь -
# move_to_end, которая позволяет переместить указанный ключ и значение в конец словаря (либо в начало). По выврду
# можно увидеть, что при одних и тех же операциях OrderedDict медленее почти в 2 раза, потому что внутри OrderedDict
# содержится список кортежей, что хорошо в операциях переупорядочения, но из-за этого скорость по сравнению с
# обычными словарями низка
