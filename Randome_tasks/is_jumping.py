# An implementation of the is_jumping function that takes a number and returns the string "JUMPING"
# if each digit in the number is greater or less than the next digit of the number by 1.
# If not, returns the string "NOT JUMPING"
def is_jumping(number: int) -> str:
    numbers_to_list = []
    jumping_test_table_results = []
    first_index, second_index, i = 0, 1, 0

    if number >= 0:
        for item in str(number):
            numbers_to_list.append(item)
        numbers_to_list = list(reversed(numbers_to_list))

    while i < len(numbers_to_list) - 1:
        if int(numbers_to_list[first_index]) - int(numbers_to_list[second_index]) == 1 or int(numbers_to_list[second_index]) - int(numbers_to_list[first_index]) == 1:
            jumping_test_table_results.append(0)
        else:
            jumping_test_table_results.append(1)

        first_index += 1
        second_index += 1
        i += 1

    if 1 in jumping_test_table_results:
        print('NOT JUMPING')
    else:
        print('JUMPING')


is_jumping(235)
