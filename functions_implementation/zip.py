# Zip implementation
def list_to_symbol_and_to_tuple(first_argument, second_argument):
    result = []
    i = 1

    for elem1 in first_argument:
        for elem2 in second_argument:
            t1 = None
            for symbol in first_argument[i - 1:i]:
                t1 = symbol

            t2 = None
            for symbol in second_argument[i - 1:i]:
                t2 = symbol

            result.append((t1, t2))
            i += 1
        break

    return result


def uzip(first_argument, second_argument):
    return list_to_symbol_and_to_tuple(first_argument, second_argument)


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = uzip(a, b)

# use the tuple() function to display a readable version of the result:
print(tuple(x))