# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)
# p(0)
def p(n):
    if n == 0: # терминальный случай
        print(0)
    elif n < -100: # терминальный случай
        pass
    elif n > 100: # терминальный случай
        pass
    else:
        p(n-1) # Рекурсивная функция
               # проходит от аргумента до терминального случая
               # и возвращает все значения от терминального случая до аргумента
        print(n)

p(5)