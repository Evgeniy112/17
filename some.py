def binary_search(lst, search_item):
    low = 0 #Начало списка
    high = len(lst) - 1
    search_res = False

    while low <= high and not search_res:
        middle = (low + high) // 2
        guess = lst[middle]
        if guess == search_item:
            search_res = True
            return search_res
        elif guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return middle

lst = [1, 2, 3, 4, 5, 7, 8]
value = 6
result = binary_search(lst, value)
print(result)

# L = list(map(int, input('Введите через пробел последовательность чисел от 0 до 99: ').split()))
#
#
#
# while True:
#     try:
#         element = int(input('Введите число от 0 до 100: '))
#         if element < 0 or element > 100:
#             raise Exception
#         break
#     except ValueError:
#         print('Нужно ввести число!')
#     except Exception:
#         print('Неправильный диапазон!')
#
#
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