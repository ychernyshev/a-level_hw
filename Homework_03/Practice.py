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
# for item in int(_list):
#     if temp < item:
#         temp = item
#
#
# print(temp)

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