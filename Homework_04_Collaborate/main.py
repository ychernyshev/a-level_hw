import math


# Задача 1. Курьер
# Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, которая по заданным
# параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

def courier(flat, floor, flats_on_floor):
    entrance_has = floor * flats_on_floor

    entranse_number = 0
    if not flat % entrance_has:
        entranse_number += flat // entrance_has
    elif flat % entrance_has:
        entranse_number += flat // entrance_has + 1

    floor_number = flat // flats_on_floor

    temp = entranse_number - 1
    current_entranse_flats_numbers = temp * (flats_on_floor * floor)
    current_floor = math.ceil((flat - current_entranse_flats_numbers) / flats_on_floor)

    print(f'You need an entranse №{entranse_number}, {current_floor} floor, apartment №{flat}')


courier(13, 4, 3)


# Задача 2. Бриллиант
# Входным данным является целое число. Необходимо:
# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли. Для числа
# 1 он выглядит как одна взездочка, для числа три он выглядит как звезда, потом три звезды, потом опять одна, для пятерки - звезда,
# три, пять, три, одна...
# * *
# ***
# * *****
# *** ***
# * *
# def brilliant(number):
#     if number % 2 and number > 0:
#         for item in range(1, number, 2):
#             string = '*' * item
#             print(string.center(number))
#         for item in range(number, 0, -2):
#             string = '*' * item
#             print(string.center(number))
#     else:
#         print('Number must be positive')

# brilliant(15)


# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:
# 2 4 5;3 2
# 3 2 1;2 0
# 6 5 2 1 2;3 1
# .....
#
# Цифры до точки с запятой надо суммировать, потом делить на их количество. В первой строке сумма будет 11, разделить на их
# количество, т.е. на 3, получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три, ровно два и в остатке
# ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке. Вот так:
# 2 4 5;3 23 2 1;2 06 5 2 1 2;3 1.....
#
# 2+4+5/3 = 3, в остатке 1
# 3+2+1/3 = 2, в остатке 0
# 6+5+2+1+2/5 = 3, в остатке 1
# Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True, если строка не верна, вывести
# результат с пометкой False

# Version A
# filename = 'text.txt'
# with open(filename, 'r') as file:
#     for item in file:
#         string = item
#         temporary_r_lst = []
#         temporary_l_lst = []
#
#         r_numbers_lst = []
#         l_numbers_lst = []
#
#         temp_str = ''
#         l_integer = 0
#
#         temp_list = item.split(';')
#
#         for item in temp_list[0]:
#             if item != ' ':
#                 temporary_l_lst.append(item)
#
#         for item in temp_list[1]:
#             if item != '\n' and item != 'n' and item != ' ':
#                 temporary_r_lst.append(item)
#
#         r_numbers_lst = list(map(int, temporary_r_lst))
#         r_numbers_lst_to_float = str(r_numbers_lst[0]) + '.' + str(r_numbers_lst[1])
#
#         l_numbers_lst = list(map(int, temporary_l_lst))
#
#         for item in l_numbers_lst:
#             l_integer += item
#
#         l_res = l_integer / len(l_numbers_lst)
#
#         temp_list = []
#
#         for item in temporary_l_lst:
#             temp_list.append(item)
#
#         for item in temporary_r_lst:
#             temp_list.append(item)
#
#         temp_list.insert(-2, ';')
#
#         string_full = ''
#
#         for item in temp_list:
#             string_full += item + ' '
#
#         if l_res == float(r_numbers_lst_to_float):
#             print(f'{string_full} {True}')
#         else:
#             print(f'{string_full} {False}')


# Version B
filename = 'team_work/text.txt'
with open(filename, 'r') as file:
    for item in file:
        string = item
        temporary_r_lst = []
        temporary_l_lst = []

        r_numbers_lst = []
        l_numbers_lst = []

        temp_str = ''
        l_integer = 0

        temp_list = item.split(';')

        for item in temp_list[0]:
            if item != ' ':
                temporary_l_lst.append(item)

        for item in temp_list[1]:
            if item != '\n' and item != 'n' and item != ' ':
                temporary_r_lst.append(item)

        r_numbers_lst = list(map(int, temporary_r_lst))

        l_numbers_lst = list(map(int, temporary_l_lst))

        for item in l_numbers_lst:
            l_integer += item

        l_res_integer = l_integer // len(l_numbers_lst)
        l_res_remainder = l_integer % len(l_numbers_lst)

        temp_list = []

        for item in temporary_l_lst:
            temp_list.append(item)

        for item in temporary_r_lst:
            temp_list.append(item)

        temp_list.insert(-2, ';')

        string_full = ''

        for item in temp_list:
            string_full += item + ' '

        if l_res_integer == r_numbers_lst[0] and l_res_remainder == r_numbers_lst[1]:
            print(f'{string_full} {True}')
        else:
            print(f'{string_full} {False}')
