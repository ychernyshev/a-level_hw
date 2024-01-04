# Знайомимось з zip функцією, пробуємо написати свій власний zip
def list_to_symbol_and_to_tuple(first_list, second_list):
    result = []
    i = 1

    for elem1 in first_list:
        for elem2 in second_list:
            t1 = None
            for symbol in first_list[i - 1:i]:
                t1 = symbol

            t2 = None
            for symbol in second_list[i - 1:i]:
                t2 = symbol

            result.append((t1, t2))
            i += 1
        break

    return result


def mine_zip(first_list, second_list):
    f_list = []
    s_list = []

    f_temp = list(reversed(first_list))
    s_temp = list(reversed(second_list))

    if len(first_list) > len(second_list):
        shortly_list_len = len(first_list) - (len(first_list) - len(second_list))
        first_list = first_list[:shortly_list_len]

        return list_to_symbol_and_to_tuple(first_list, second_list)
    elif len(first_list) < len(second_list):
        shortly_list_len = len(second_list) - (len(second_list) - len(first_list))
        second_list = second_list[:shortly_list_len]

        return list_to_symbol_and_to_tuple(first_list, second_list)


print(mine_zip(['go', 'one', 5, 400, True, 'lambda'], [1, 2, 3, 4]))
