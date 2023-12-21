filename = 'text.txt'
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
        r_numbers_lst_to_float = str(r_numbers_lst[0]) + '.' + str(r_numbers_lst[1])

        l_numbers_lst = list(map(int, temporary_l_lst))

        for item in l_numbers_lst:
            l_integer += item

        l_res = l_integer / len(l_numbers_lst)

        temp_list = []

        for item in temporary_l_lst:
            temp_list.append(item)

        for item in temporary_r_lst:
            temp_list.append(item)

        temp_list.insert(-2, ';')

        string_full = ''

        for item in temp_list:
            string_full += item + ' '

        if l_res == float(r_numbers_lst_to_float):
            print(f'{string_full} {True}')
        else:
            print(f'{string_full} {False}')
