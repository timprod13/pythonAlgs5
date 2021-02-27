"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
import timeit
import random


def my_list_append():
    for i in range(1000):
        my_list.append(i)


# хоть эта функция и использует команду insert, работает она как и в deque - добавляет в начало списка элемент
def my_list_appendleft():
    for i in range(1000):
        my_list.insert(0, i)


def my_list_pop():
    for i in range(len(my_list)):
        my_list.pop()


def my_list_popleft():
    for i in range(len(my_list)):
        my_list.pop(0)


def my_list_extend():
    for i in range(1000):
        my_list.extend([i, i, i])


def my_list_random_access():
    for i in range(1000):
        random_var = random.choice(my_list)


def my_deque_append():
    for i in range(1000):
        my_deque.append(i)


def my_deque_appendleft():
    for i in range(1000):
        my_deque.appendleft(i)


def my_deque_pop():
    for i in range(len(my_deque)):
        my_deque.pop()


def my_deque_popleft():
    for i in range(len(my_deque)):
        my_deque.popleft()


def my_deque_extend():
    for i in range(1000):
        my_deque.extend([i, i, i])


def my_deque_extendleft():
    for i in range(1000):
        my_deque.extendleft([i, i, i])


def my_deque_random_access():
    for i in range(1000):
        random_var = random.choice(my_deque)


def delimiter():
    print("********************************************")


my_list = [i for i in range(100000)]
my_deque = deque(i for i in range(100000))
delimiter()
print(
    f'my_list_popleft()  {timeit.timeit("my_list_popleft()", setup="from __main__ import my_list_popleft", number=10000)}\n'
    f'my_deque_popleft() {timeit.timeit("my_deque_popleft()", setup="from __main__ import my_deque_popleft", number=10000)}')
delimiter()
print(
    f'my_list_append()  {timeit.timeit("my_list_append()", setup="from __main__ import my_list_append", number=10000)}\n'
    f'my_deque_append() {timeit.timeit("my_deque_append()", setup="from __main__ import my_deque_append", number=10000)}')
delimiter()
print(
    f'my_list_pop()  {timeit.timeit("my_list_pop()", setup="from __main__ import my_list_pop", number=10000)}\n'
    f'my_deque_pop() {timeit.timeit("my_deque_pop()", setup="from __main__ import my_deque_pop", number=10000)}')
delimiter()
print(
    f'my_list_appendleft()  {timeit.timeit("my_list_appendleft()", setup="from __main__ import my_list_appendleft", number=100)}\n'
    f'my_deque_appendleft() {timeit.timeit("my_deque_appendleft()", setup="from __main__ import my_deque_appendleft", number=100)}')
delimiter()
print(
    f'my_list_extend()  {timeit.timeit("my_list_extend()", setup="from __main__ import my_list_extend", number=10000)}\n'
    f'my_deque_extend() {timeit.timeit("my_deque_extend()", setup="from __main__ import my_deque_extend", number=10000)}')
delimiter()
print(
    f'my_list_extend()      {timeit.timeit("my_list_extend()", setup="from __main__ import my_list_extend", number=10000)}\n'
    f'my_deque_extendleft() {timeit.timeit("my_deque_extendleft()", setup="from __main__ import my_deque_extendleft", number=10000)}')
delimiter()
print(
    f'my_list_random_access()  {timeit.timeit("my_list_random_access()", setup="from __main__ import my_list_random_access", number=10)}\n'
    f'my_deque_random_access() {timeit.timeit("my_deque_random_access()", setup="from __main__ import my_deque_random_access", number=10)}')
delimiter()

''' Вывод результатов тестирования:
********************************************
my_list_popleft()  1.7680911
my_deque_popleft() 0.0091950999999999
********************************************
my_list_append()  0.9203954000000001
my_deque_append() 0.6252911999999999
********************************************
my_list_pop()  0.6867019000000005
my_deque_pop() 0.6808188999999993
********************************************
my_list_appendleft()  2.4885852
my_deque_appendleft() 0.0069704999999995465
********************************************
my_list_extend()  2.063256299999999
my_deque_extend() 1.5861517000000003
********************************************
my_list_extend()      2.0201762
my_deque_extendleft() 1.5302912000000006
********************************************
my_list_random_access()  0.007502000000000564
my_deque_random_access() 161.2760793
********************************************
'''
# Deque сконструирован специально для быстрой вставки или удаления с обоих концов, поэтому и время, затрачиваемое на
# одни и те же операции при работе с началом и концом списка практически равны. Список же не способен на такую
# быструю работу с началом списка, так как он для этого не предназначен (например, у list.pop (0) временная сложность
# O (n) ). По остальным тестам при работе с концами списка и дэка (очереди, колоды) время отработки практически
# идентичное, хотя дек и быстрее. Насколько я понимаю, при малых объёмах принимаемых значений производительность у
# списка довольно высока (например, у list.append) и связано это с тем, что список использует "под капотом" realloc
# (фрагментация и перемещение из-за этого данных). Но, как и было сказано в уроке, со случайным доступом к элементу у
# дэка большие проблемы
