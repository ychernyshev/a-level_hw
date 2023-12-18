# Кожен пише суму списку за допомогою for та while
# _list = [6, 2, 3, 4]
# temp = 0
# sum = 0
#
# while temp < len(_list):
#     sum += _list[temp]
#
#     temp += 1
#
# print(sum)
#
#
# sum = 0
# for item in _list:
#     sum += item
#
# print(sum)


# ===========
# Банкомат видає суму максимально можливими купюрами
while True:
    nominal_currency = [20, 50, 100, 200, 500, 1000]
    on_hundred, tw_hundred = 0, 0

    nominal = input('Enter a sum: ')

    if nominal.isnumeric():
        reminder = int(nominal) % 1000
        main_nominal = int(nominal) - reminder

        if main_nominal >= 1000:
            print(f'{int(main_nominal) // nominal_currency[5]} x {nominal_currency[5]}$')

        hundreds = reminder % 500
        fi_hundred = reminder - hundreds

        if fi_hundred:
            print(f'1 x {nominal_currency[4]}$')

        on_hundred = hundreds % 200
        tw_hundred = hundreds - on_hundred

        if tw_hundred:
            print(f'{hundreds // 200} x {nominal_currency[3]}$')

        if on_hundred:
            print(f'{on_hundred // 100} x {nominal_currency[2]}$')
    else:
        print('You need enter a number')


# Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
# _list = []
# temp = 0
# i = 0
#
# while i < 5:
#     temp = input('Enter the denomination of the bills: ')
#     if temp.isnumeric():
#         _list.append(int(temp))
#     else:
#         print('You need enter a number')
#         i -= 1
#
#     i += 1
#
# _list.sort()
#
# result = _list[0]
#
#
# for item in result:
#     print(item, end=' ')
