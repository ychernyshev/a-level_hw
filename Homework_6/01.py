# Знайомимось з zip функцією, пробуємо написати свій власний zip
def main_zip(first_list, second_list):
    f_list = []
    s_list = []
    result = []

    f_temp = list(reversed(first_list))
    s_temp = list(reversed(second_list))

    if len(first_list) > len(second_list):
        shortly_list_len = len(first_list) - (len(first_list) - len(second_list))
        first_list = first_list[:shortly_list_len]
    elif len(first_list) < len(second_list):
        shortly_list_len = len(second_list) - (len(second_list) - len(first_list))
        second_list = second_list[:shortly_list_len]
        i = 1
        for elem1 in first_list:
            for elem2 in second_list:
                t1 = first_list[i-1:i]
                t2 = second_list[i-1:i]
                result.append((t1, t2))
                i += 1
            break

    print(result)


main_zip([1, 2, 3, 4], ['go', 'one', 5, 400, True, 'lambda'])
