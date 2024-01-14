# Sorted implementation.
alphabet = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
    14: 'n', 15: 'o', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z',
}


def letters_analyzation(reformated_line_to_list, line_to_indexes, sorted_line_to_indexes):
    i = 0
    result = []

    while i < len(reformated_line_to_list):
        temp = line_to_indexes[0]

        for item in range(len(line_to_indexes)):
            if temp > line_to_indexes[item]:
                temp = line_to_indexes[item]

        sorted_line_to_indexes.append(temp)

        line_to_indexes.remove(temp)
        i += 1

    for item in sorted_line_to_indexes:
        for key, value in alphabet.items():
            if item == key:
                result.append(value)

    return result


def usorted(line):
    reformated_line_to_list = []
    line_to_indexes = []
    sorted_line_to_indexes = []
    i = 0
    result = []

    while i < len(reformated_line_to_list):
        temp = line_to_indexes[0]

        for item in range(len(line_to_indexes)):
            if temp > line_to_indexes[item]:
                temp = line_to_indexes[item]

        sorted_line_to_indexes.append(temp)

        line_to_indexes.remove(temp)
        i += 1

    for item in sorted_line_to_indexes:
        for key, value in alphabet.items():
            if item == key:
                result.append(value)

    if type(line) == tuple:
        for item in line:
            reformated_line_to_list.append(item)

    temp = reformated_line_to_list[0]
    if len(reformated_line_to_list) >= 1:
        for item in reformated_line_to_list:
            print(temp)
            if type(item) == str:
                for key, value in alphabet.items():
                    if item == value:
                        line_to_indexes.append(key)
            elif type(item) == int or type(item) == float:
                i = 0
                # for item in reformated_line_to_list:
                if temp > item:
                    temp = item
                    reformated_line_to_list.remove(item)
                # print(temp)
                while i < len(reformated_line_to_list):
                    result.append(temp)
                    i += 1

                return result
        return letters_analyzation(reformated_line_to_list, line_to_indexes, sorted_line_to_indexes)
    else:
        pass


print(usorted(("b", "g", "a", "d", "f", "c", "h", "e")))
print(usorted(("u", "v", "z", "w", "y", "x")))
x = usorted((1, 2, 5, 4, 3))
y = usorted((4, 4, 5, 7, 0))
print(x, y)
