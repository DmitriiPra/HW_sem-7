"""
Задача 36: 
Напишите функцию вывода таблицы умножения 
print_operation_table(operation, num_rows=6, num_columns=6)
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов
таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
(подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два 
аргумента, как, например, у операции умножения.

Пример:
Ввод: `print_operation_table(lambda x, y: x * y) ` 
Вывод:
1  2   3   4   5   6
2  4   6   8   10  12
3  6   9   12  15  18
4  8   12  16  20  24
5  10  15  20  25  30
6  12  18  24  30  36


"""

# def operation(sp):
#     return "\t".join(map(str, sp))

# def print_operation_table(operation, num_rows, num_columns):
#     for i in range(1, num_rows + 1):
#         spisok = []
#         for j in range(1, num_columns + 1):
#             spisok.append(i * j)
#         print(operation(spisok))
# print_operation_table(operation, num_rows=6, num_columns=6)


def operation(sp):
    return "\t".join(map(str, sp))


def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        print(operation(map(lambda j: i * j, range(1, num_columns + 1))))


print("Для построения таблицы умножения, определяемой по формуле:")
print("`print_operation_table(lambda x, y: x * y)`")
num_columns = int(input("Введите значение Х: "))
num_rows = int(input("Введите значение Y: "))

print_operation_table(operation, num_columns, num_rows)
