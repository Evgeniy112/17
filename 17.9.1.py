import element as element

L = list(map(int, input('Введите через пробел последовательность чисел от 0 до 99: ').split()))


def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


sort_L = merge_sort(L)
print('Отсортированный массив:', sort_L)
print('Количество элементов в  массиве:', len(sort_L))

element = int(input('Введите число от 0 до 99: '))


def binary_search(L, element, left, right):
    print(left, right) # Это чтобы лучше понимать что происходит. Перед сдачей УДАЛИТЬ!!!!!!!
    if left > right:  # если левая граница превысила правую,
        return f"{element} отсутствует в списке"  # значит элемент отсутствует

    if element > right or element < left:
        return f"{element} отсутствует в списке"

    middle = (right + left) // 2  # находим середину
    if L[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < L[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(L, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(L, element, middle + 1, right)


# запускаем алгоритм на левой и правой границе
indx_element = binary_search(sort_L, element, sort_L[0], sort_L[-1])
if indx_element == f"{element} отсутствует в списке":
    print(f"{element} отсутствует в списке")
    if element > sort_L[-1]:
        print(f"Число слева = {sort_L[-1]}")
    elif element < sort_L[0]:
        print(f"Число справа = {sort_L[0]}")
    else:
        list_x = sort_L.append(element)) # Добавляем элемент в список
        sort_x = merge_sort(list_x) # Сортируем полученный список
        indx_x = binary_search(sort_x, element, sort_x[0], sort_x[-1]) # Выполняем поиск

elif sort_L[indx_element] == sort_L[0]:
    print(f"Индекс числа {indx_element}")
    print(f" Число справа = {sort_L[indx_element + 1]}")
elif sort_L[indx_element] == sort_L[-1]:
    print(f"Индекс числа {indx_element}")
    print(f" Число слева = {sort_L[indx_element - 1]}")
else:
    print(f"Индекс числа {indx_element}")
    print(f" Число слева = {sort_L[indx_element - 1]} , число справа = {sort_L[indx_element + 1]} ")
