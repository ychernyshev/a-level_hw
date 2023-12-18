import random


'''
Ввести два цілі числа, знайти більше з них та вивести його, якщо вони рівні, 
вивести будь яке.
'''
while True:
    user_numbers = []
    for item in range(2):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)

    if user_numbers[0] == user_numbers[1]:
        print(random.choice(user_numbers))
    elif user_numbers[0] > user_numbers[1]:
        print(user_numbers[0])
    else:
        print(user_numbers[1])

'''
Ввести два цілі числа, знайти більше з них та вивести його, якщо вони рівні, 
вивести окреме повідомлення, що вони рівні.
'''
while True:
    user_numbers = []
    for item in range(2):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)

    if user_numbers[0] == user_numbers[1]:
        print('Numbers are equal')
    elif user_numbers[0] > user_numbers[1]:
        print(user_numbers[0])
    else:
        print(user_numbers[1])

'''
Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, 
ігнорувати рівність. Надрукувати результати за допомогою конкатенації.
'''
while True:
    user_numbers = []
    the_biggest_number = 0
    an_average_number = 0
    for item in range(3):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)

    for item in user_numbers:
        if the_biggest_number < item:
            the_biggest_number = item

    the_smallest_number = user_numbers[0]

    for item in range(len(user_numbers)):
        if user_numbers[item] < the_smallest_number:
            the_smallest_number = user_numbers[item]

    for item in user_numbers:
        if item == the_biggest_number:
            user_numbers.remove(item)

        if item == the_smallest_number:
            user_numbers.remove(item)

    an_average_number = int(user_numbers[0])

    print(str(the_biggest_number) + ', ' + str(an_average_number) + ', ' + str(the_smallest_number))

'''
Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, 
ігнорувати рівність. Надрукувати результати за допомогою метода format
'''
while True:
    user_numbers = []
    the_biggest_number = 0
    an_average_number = 0
    for item in range(3):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)

    for item in user_numbers:
        if the_biggest_number < item:
            the_biggest_number = item

    the_smallest_number = user_numbers[0]

    for item in range(len(user_numbers)):
        if user_numbers[item] < the_smallest_number:
            the_smallest_number = user_numbers[item]

    for item in user_numbers:
        if item == the_biggest_number:
            user_numbers.remove(item)

        if item == the_smallest_number:
            user_numbers.remove(item)

    an_average_number = int(user_numbers[0])

    print('{0}, {1}, {2}'.format(the_biggest_number, an_average_number, the_smallest_number))

'''
Ввести три цілі числа, знайти серед них найбільше, найменше й середнє, 
опрацювати всі варианти рівності. Надрукувати результати за допомогою префіксу f.
'''
while True:
    user_numbers = []
    entering_count = {}
    the_biggest_number = 0
    an_average_number = 0

    for item in range(3):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)

    for item in user_numbers:
        if item in entering_count:
            entering_count[item] += 1
        else:
            entering_count[item] = 1

    if user_numbers[0] != user_numbers[1] != user_numbers[2]:
        for item in user_numbers:
            if the_biggest_number < item:
                the_biggest_number = item

        the_smallest_number = user_numbers[0]

        for item in range(len(user_numbers)):
            if user_numbers[item] < the_smallest_number:
                the_smallest_number = user_numbers[item]

        for item in user_numbers:
            if item == the_biggest_number:
                user_numbers.remove(item)

            if item == the_smallest_number:
                user_numbers.remove(item)

        an_average_number = int(user_numbers[0])

        print(f'{the_biggest_number}, {an_average_number}, {the_smallest_number}')
    else:
        print(False)

'''
Ввести два числа - роки хлопчика та дівчинки. 
Якщо обом більше 18-ти, то їм можна до 
клубу, якщо їм більше 60 - то їм краще порадити санаторій, якщо їм менше 18 - то можна 
порадити їм піццерію. 
Якщо роки змішані, пропорнувати те, що на менші роки. 
Пропозиції друкувати через префікс.
'''
while True:
    user_numbers = []
    entering_count = {}
    the_biggest_number = 0
    an_average_number = 0

    for item in range(2):
        user_string = int(input('Enter a number: '))
        user_numbers.append(user_string)
    if user_numbers[0] > 18 and user_numbers[1] > 18:
        print('> 18? - можна до клубу')
    elif user_numbers[0] > 55 and user_numbers[1] > 18:
        print('> 55? - краще санаторій')
    elif user_numbers[0] < user_numbers[1] or user_numbers[1] < user_numbers[0]:
        print('One of user is > 18? - можна до клубу')
    else:
        print('<18? Йдіть у піцерію')
