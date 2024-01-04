# 1. Написати 2 функції. Перша функція прийматиме рядок та приводитиме його до нижнього регістру.
# Друга функція прийматиме рядок та приводитиме його до верхнього регістру.
# Головна програма має застосовувати обидві функції до списку рядків за допомогою map,
# для кожного з рядків, та друкувати результат.
from collections import OrderedDict


def lower_string(str_):
    return str_.lower()


def upper_string(str_):
    return str_.upper()


def main(str_):
    to_lower_str = list(map(lower_string, str_))
    to_upper_str = list(map(upper_string, str_))
    lower_str = ''
    upper_str = ''

    for item in to_lower_str:
        lower_str += item

    for item in to_upper_str:
        upper_str += item

    return print(f'Upper: {upper_str}; Lower: {lower_str}')

# Uncomment for calling the function
# main('str')


# 2. Написати функцію, яка буде підносити число у квадрат. Написати другу, яка буде перевіряти, чи є число простим.
# Потрібно видрукувати в головній програмі квадрати усіх простих чисел зі списку від 0 до 50 за допомогою map
def squaring_the_number(number):
    return number ** 2


def prime_number_testing(number):
    # Prime number testing.
    # Series of 0 or 1 numbers are filling the number_checking_table following the conditions below
    number_checking_table = []

    if not number > 1:
        number_checking_table.append(1)
    else:
        number_checking_table.append(0)

    if number % 1 and number % number:
        number_checking_table.append(1)
    else:
        number_checking_table.append(0)

    if not number % 2:
        number_checking_table.append(1)
    else:
        number_checking_table.append(0)

    if not number % 3 and number != 3 or not number % 5 and number != 5:
        number_checking_table.append(1)
    else:
        number_checking_table.append(0)

    return number_checking_table


def is_simple_number(squaring_the_number, number):
    # A prime number has every testing result as 0. If one of the testing results is 1, it`s not a prime number
    if number == 0:
        n = number
    else:
        number_checking_table = prime_number_testing(number)

        if 1 in number_checking_table:
            n = number
        else:
            map_number = [number]
            one_number_list = list(map(squaring_the_number, map_number))

            for item in one_number_list:
                print(item, end=' ')


list_of_numbers_as_str = []
list_of_numbers_as_int = []

for number in range(0, 51):
    list_of_numbers_as_str.append(str(number))

list_of_numbers_as_int = list(map(int, list_of_numbers_as_str))

# Uncomment for calling the function
for number in list_of_numbers_as_int:
    is_simple_number(squaring_the_number, number)


# 4. Візьміть файл, в якому є багато англійських слів у рядках.
# Порахуйте частоту зустрічі кожного слова та видрукуйте відсортовано.
def count_of_words_in_the_text_file():
    with open('lorem.txt', 'r') as file:
        words_archive = []
        count_of_words = {}

        for item in file:
            word_list = item.split()
            for word in word_list:
                words_archive.append(word)
        for word in words_archive:
            if word in count_of_words:
                count_of_words[word] += 1
            else:
                count_of_words[word] = 1
        count_of_words_sorted = dict(sorted(count_of_words.items(), key=lambda value_item: value_item[1]))
        ordered_dict = OrderedDict(reversed(list(count_of_words_sorted.items())))
        for key, value in ordered_dict.items():
            print(f'{key}: {value}')


# Uncomment for calling the function
# count_of_words_in_the_text_file()
