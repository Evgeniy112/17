array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0

# СОРТИРОВКА ПУЗЫРЬКОМ
# for i in range(len(array)):  # проходим по всему массиву
#     idx_max = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] > array[idx_max]:
#             idx_max = j
#     if i != idx_max:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_max] = array[idx_max], array[i]

# Сортировка пузырьком
# for i in range(len(array)):
#     print("i= ", i)
#     for j in range(len(array)-i-1):
#         count += 1
#         print("j= ", j)
#         if array[j] > array[j+1]:
#             array[j],array[j+1] = array[j+1],array[j]
#             print("array", j, "=", array)

# Сортировка вставками
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     print('x=', x, "i=", i, 'array=', array, 'idx=', idx)
#     while idx > 0 and array[idx-1] > x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x

#Сортировка слиянием
# def merge_sort(L):  # "разделяй"
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # "властвуй"
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result
# print(merge_sort(array))
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)
import random

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

qsort_random(array)