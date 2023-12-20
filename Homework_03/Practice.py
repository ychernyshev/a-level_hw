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


# 05 Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
while True:
    nominal_currency = [10, 20, 50]
    limit = 10
    limits_table = {}

    nominal = input('Enter a sum: ')
    int_nominal = int(nominal)
    f_hundred = 500
    t_hundred = 200
    o_hundred = 100

    if not nominal.isnumeric():
        print('You need enter a number')
    elif nominal == '0':
        print('You need to enter a sum that is more than 0')
    elif int_nominal > 800:
        print('Sorry, but the ATM will not dispense more than 800₴ at a time')
    else:
        if int_nominal >= 500:
            remainder = int_nominal % 500
            max_nominal = int_nominal - remainder

            print(remainder)
            print(max_nominal)

            # twenty = 0
            # ten = 0

        #     if (max_nominal // 50) > 10:
        #         temporary_list = [int(str(max_nominal // 50)[1])]
        #         remainder += temporary_list[0] * 50
        #         max_nominal -= remainder
        #
        #     if max_nominal:
        #         if max_nominal // 50 > 10:
        #             print('50 > 10')
        #         else:
        #             print(f'{max_nominal // 50} x {nominal_currency[2]}₴')
        #
        #     if not remainder % 10:
        #         if remainder // 10 > 10:
        #             temporary_list = [int(str(remainder // 10)[1])]
        #             remainder -= temporary_list[0] * 10
        #             print(f'{temporary_list[0]} x {nominal_currency[0]}₴')
        #         else:
        #             print(f'{remainder // 10} x {nominal_currency[0]}₴')
        #
        #     if 100 < remainder < 200:
        #         if not remainder % 20:
        #             if remainder // 20 > 10:
        #                 print('20 > 20')
        #             else:
        #                 print(f'{remainder // 20} x {nominal_currency[1]}₴')
        # small = int_nominal % 100
        # hundred = int_nominal - small
        # if hundred:
        #     pass
            # while limit > 0:
            #     print(f'{hundred // 10} x {nominal_currency[0]}₴')
            #
            #     limit -= 1
            #     break
        # if small

