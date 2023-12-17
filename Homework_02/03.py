# Ви маєте три числа, вони вводяться з консолі. Перше число називається fizz, друге називається buzz. До третього необхідно дорахувати від одиниці. Дивлячись на поточне число, якщо воно кратне fizz – треба виводити F замість числа. Якщо число кратне buzz – треба виводити B замість числа. Якщо число кратне і fizz, і buzz, треба виводити FB. Якщо воно не кратне нічому, виводимо число. І так - поки не буде досягнуто третього введеного числа.
#
# Приклад умови та результату: Введено числа 2, 5, 18 Висновок має бути таким:
#
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

while True:
    fizz = int(input('\n\nEnter the Fizz number: '))
    buzz = int(input('Enter the Buzz number: '))
    random_number = int(input('Enter a random number: '))

    for item in range(1, random_number + 1):
        if not item % fizz and not item % buzz:
            print('FB', end=' ')
        elif not item % fizz:
            print('F', end=' ')
        elif not item % buzz:
            print('B', end=' ')
        else:
            print(item, end=' ')
