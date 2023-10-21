# Задача 1
# Дан массив целых чисел nums и целое число target. Необходимо вернуть индексы двух чисел таких, чтобы их сумма равна target.
# Имеется ровно одно решение.
# Один и тот же элемент нельзя использовать дважды.
# Результат можно вернуть в любом порядке.

#Сложность алгоритма O(n)
#Идея алгоритма: x+y = target ,
# если target - y = x и разница в виде ключа есть в словаре,
# то при сложении y + dict[x] = target.
# поиск по ключу в словаре реализуется за O(1)
# самый плохой исход по сложности работы алгоритма,если мы пройдемся
# по всему списку  за O(n)

from typing import List


def solve(nums: List[int], target: int) -> List[int]:
    difference_dict = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in difference_dict:
            return [difference_dict[difference], i]
        difference_dict[num] = i
    return list()

#пример
print(solve([3, 3], target=7))

