# 01 Кожен пише суму списку за допомогою for та while
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
# 04 Банкомат видає суму максимально можливими купюрами
# while True:
#     nominal_currency = [50, 100, 200, 500, 1000]
#
#     nominal = input('Enter a sum: ')
#
#     reminder = int(nominal) % 1000
#     main_nominal = int(nominal) - reminder
#     hundreds = reminder % 500
#     small = hundreds % 100
#     print(hundreds)
#     fi_hundred = reminder - hundreds
#     on_hundred = hundreds % 200 - small
#     if hundreds == 400:
#         tw_hundred = hundreds / 2
#     elif 400 < hundreds < 500:
#         tw_hundred = (hundreds - small) / 2
#     else:
#         tw_hundred = hundreds - on_hundred - small
#     # print(tw_hundred)
#
#     if not nominal.isnumeric():
#         print('You need enter a number')
#     elif nominal == '0':
#         print('You need to enter a sum that is more than 0')
#     elif small and small < 50 or small > 50:
#         print(f'Your sum is {nominal}₴. The ATM will not issue an amount below or more than 50₴')
#     else:
#         if main_nominal >= 1000:
#             print(f'{int(main_nominal) // nominal_currency[4]} x {nominal_currency[4]}₴')
#
#         if fi_hundred:
#             print(f'1 x {nominal_currency[3]}₴')
#
#         if tw_hundred == 200:
#             print(f'{hundreds // 200} x {nominal_currency[2]}₴')
#
#         if on_hundred == 100:
#             print(f'{on_hundred // 100} x {nominal_currency[1]}₴')
#
#         if small and small == 50:
#             print(f'{small // 50} x {nominal_currency[0]}₴')

# 03 Написати програму, яка виводить сама себе
# prog = [
#     "with open('program.txt', 'a') as file:",
#     "file.writelines(prog)"
# ]
# with open('program.txt', 'w') as file:
#     file.writelines(prog)


# 04 Написати програму, яка виводить саму себе задом наперед
with open('program.txt', 'r') as file:
    content = file.read()
    print(content[::-1])

# 05 Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
# while True:
#     nominal_currency = [10, 20, 50]
#     user_nominal = int(input('Enter a sum: '))
#
#     if not str(user_nominal).isnumeric():
#         print('You need enter a number')
#     elif user_nominal == 0:
#         print('You need to enter a sum that is more than 0')
#     elif user_nominal > 800:
#         print('Sorry, but the ATM will not dispense more than 800₴ at a time')
#     else:
#         if user_nominal <= 100:
#             print(f'{user_nominal // 10} x 10₴')
#
#         if 100 < user_nominal <= 200:
#             temp = user_nominal - 100
#             twenty = user_nominal - temp
#             print(f'{temp // 10} x 10₴')
#             print(f'{twenty // 20} x 20₴')
#
#         if 200 < user_nominal <= 300:
#             ten = user_nominal - 200
#             twenty = user_nominal - ten
#             print(f'{ten // 10} x 10₴')
#             print(f'{twenty // 20} x 20₴')
#
#         if 300 < user_nominal <= 400:
#             ten = user_nominal - 300
#             twenty = user_nominal - ten - 100
#             fifty = user_nominal - ten - twenty
#             print(f'{ten // 10} x 10₴')
#             print(f'{twenty // 20} x 20₴')
#             print(f'{fifty // 50} x 50₴')
#
#         if 400 < user_nominal <= 500:
#             ten = user_nominal - 400
#             twenty = user_nominal - ten - 200
#             fifty = user_nominal - ten - twenty
#             print(f'{ten // 10} x 10')
#             print(f'{twenty // 20} x 20')
#             print(f'{fifty // 50} x 50')
#
#         if 500 < user_nominal <= 600:
#             ten = user_nominal - 500
#             twenty = user_nominal - ten - 300
#             fifty = user_nominal - ten - twenty
#             print(f'{ten // 10} x 10')
#             print(f'{twenty // 20} x 20')
#             print(f'{fifty // 50} x 50')
#
#         if 600 < user_nominal <= 700:
#             ten = user_nominal - 600
#             twenty = user_nominal - ten - 400
#             fifty = user_nominal - ten - twenty
#             print(f'{ten // 10} x 10')
#             print(f'{twenty // 20} x 20')
#             print(f'{fifty // 50} x 50')
#
#         if 700 < user_nominal <= 800:
#             ten = user_nominal - 700
#             twenty = user_nominal - ten - 500
#             fifty = user_nominal - ten - twenty
#             print(f'{ten // 10} x 10')
#             print(f'{twenty // 20} x 20')
#             print(f'{fifty // 50} x 50')

