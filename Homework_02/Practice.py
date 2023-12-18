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
# while True:
#     number = int(input('\nEnter the number: '))
#     if not number:
#         print('You can\'t divide by 0')
#     elif number == 1:
#         print(1)
#     else:
#         for item in range(2, number + 1):
#             if not number % item:
#                 print(item, end=' ')


# Ввести число, вивести його розряди та їх множники.
digits = {
    0: '10^2',
    1: '10^1',
    2: '10^0',
}

while True:
    user_string = input('\n\nEnter the number: ')
    number = int(user_string)
    print('-'*32)

    # Divisors of numbers
    print('Divisors: ', end=' ')
    if not number:
        print('You can\'t divide by 0')
    elif number == 1:
        print(1)
    else:
        for item in range(2, number + 1):
            if not number % item:
                print(item, end=' ')

    print('')
    # Digits of numbers
    print('Digits:   ', end=' ')
    list_of_numbers = []
    for item in user_string:
        list_of_numbers.append(item)

    number_id = 0
    if len(list_of_numbers) == 1 and number == 0:
        pass
    elif len(list_of_numbers) == 1:
        digits_id = 2
        while number_id < len(list_of_numbers):
            temp = list_of_numbers[number_id]
            print(f'{temp}*{digits.get(digits_id)}')

            number_id += 1
            digits_id += 1
    elif len(list_of_numbers) == 2:
        digits_id = 1
        while number_id < len(list_of_numbers):
            temp = list_of_numbers[number_id]
            print(f'{temp}*{digits.get(digits_id)}', end=' + ')

            number_id += 1
            digits_id += 1
    elif len(list_of_numbers) == 3:
        digits_id = 0
        while number_id < len(list_of_numbers):
            temp = list_of_numbers[number_id]
            print(f'{temp}*{digits.get(digits_id)}', end=' + ')

            number_id += 1
            digits_id += 1
