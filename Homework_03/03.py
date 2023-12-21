# Написати fizzbuzz для 20 комплектів по три числа, які записані в файл. Читайте із файлу перший рядок з трьома числами, беріть із нього числа, рахуйте для них fizzbuzz, виводите, продовжуйте з наступним рядком і так до кінця файлу
# string_of_numbers = open('fizzbuzz_numbers.txt', 'r')
#
# for item in string_of_numbers:
#     the_string_for_num = ''
#     temp = ''
#
#     the_list_for_num_in_str = item.split(' ')
#     temp = the_list_for_num_in_str[2]
#     temp2 = temp.split('\n')
#     the_list_for_num_in_str.insert(2, temp2[0])
#     the_list_for_num_in_str.remove(the_list_for_num_in_str[3])
#
#     the_list_for_num_in_int = list(map(int, the_list_for_num_in_str))
#     print(' ')
#     for num in range(1, the_list_for_num_in_int[2] + 1):
#         if not num % the_list_for_num_in_int[0] and not num % the_list_for_num_in_int[1]:
#             print('FB', end=' ')
#         elif not num % the_list_for_num_in_int[0]:
#             print('F', end=' ')
#         elif not num % the_list_for_num_in_int[1]:
#             print('B', end=' ')
#         else:
#             print(num, end=' ')

# Переробити другу задачу так, щоб результат писався в інший файл. Додаємо list comprehension, map та інші свіжеотримані знання до виконання завдання.
string_of_numbers = open('fizzbuzz_numbers.txt', 'r')
write_fb_string = open('fizzbuzz_strings.txt', 'w')

for item in string_of_numbers:
    the_string_for_num = ''
    temp = ''

    the_list_for_num_in_str = item.split(' ')
    temp = the_list_for_num_in_str[2]
    temp2 = temp.split('\n')
    the_list_for_num_in_str.insert(2, temp2[0])
    the_list_for_num_in_str.remove(the_list_for_num_in_str[3])

    the_list_for_num_in_int = list(map(int, the_list_for_num_in_str))
    print(' ')
    for num in range(1, the_list_for_num_in_int[2] + 1):
        if not num % the_list_for_num_in_int[0] and not num % the_list_for_num_in_int[1]:
            write_fb_string.write(' FB ')
        elif not num % the_list_for_num_in_int[0]:
            write_fb_string.write(' F ')
        elif not num % the_list_for_num_in_int[1]:
            write_fb_string.write(' B ')
        else:
            write_fb_string.write(' ' + str(num) + ' ')
    write_fb_string.write('\n')
