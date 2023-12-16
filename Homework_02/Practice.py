# Перевірити, чи є введене число парним.
# number = int(input('Checking if the number is even or odd. Enter a number: '))
# if number % 2:
#      print('Number is Odd.')
# else:
#     print('Number is Even')


# Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10
# while True:
#     number = int(input('Checking if the number is odd . Enter a number: '))
#     if number % 2 and not number % 3 and not number % 5:
#         print('Number is Odd.')
#     else:
#         print('Bad number')

# Ввести число, вивести усі його дільники
delivers = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
}


# def delivers(last_number):
#     if last_number[0] == 2:
#         print(2)
#     elif last_number[0] == 4:
#         print(2, 4)
#     elif last_number[0] == 6:
#         print(2, 4, 6)
#     elif last_number[0] == 8:
#         print(2, 4, 8)


def filling_the_list_with_numbers(number):
    for item in number:
        input_number.append(int(item))


def the_first_number_from_the_list_numbers(input_number):
    first_number = input_number[:1]
    return int(''.join(str(i) for i in first_number))


def the_last_number_from_the_list_numbers(input_number):
    last_number = input_number[1:]
    return int(''.join(str(i) for i in last_number))


while True:
    input_number = []

    number = input('Enter a number: ')
    int_number = int(number)

    if len(number) == 1:
        filling_the_list_with_numbers(number)
        print(delivers.get(int_number))
    elif len(number) == 2:
        filling_the_list_with_numbers(number)
        if the_last_number_from_the_list_numbers(input_number) == 2:
            print(the_first_number_from_the_list_numbers(input_number))
        if the_last_number_from_the_list_numbers(input_number) == 4:
            print(f'{delivers.get(2)}, {delivers.get(4)}')
        if the_last_number_from_the_list_numbers(input_number) == 6:
            print(f'{delivers.get(2)}, {delivers.get(4)}, {delivers.get(6)}')
        if the_last_number_from_the_list_numbers(input_number) == 8:
            print(f'{delivers.get(2)}, {delivers.get(4)}, {delivers.get(8)}')

        # dividers = []2



        # delivers(the_last_number_from_the_list_numbers())
