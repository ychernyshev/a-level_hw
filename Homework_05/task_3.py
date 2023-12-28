# Написати функцію переведення розмірів жіночої білизни з міжнародної у решту.
# Всередині функції потрібно просто звертатися до правильно складеного словника.
def women_sizes(size):
    international_sizes = {
        'XXS': {
            'UA': 42, 'GE': 36, 'USA': 8, 'FR': 38, 'GB': 24,
        },
        'XS': {
            'UA': 44, 'GE': 38, 'USA': 10, 'FR': 40, 'GB': 26,
        },
        'S': {
            'UA': 46, 'GE': 40, 'USA': 12, 'FR': 42, 'GB': 28,
        },
        'M': {
            'UA': 48, 'GE': 42, 'USA': 14, 'FR': 44, 'GB': 30,
        },
        'L': {
            'UA': 50, 'GE': 44, 'USA': 16, 'FR': 46, 'GB': 32,
        },
        'XL': {
            'UA': 52, 'GE': 46, 'USA': 18, 'FR': 48, 'GB': 34,
        },
        'XXL': {
            'UA': 54, 'GE': 48, 'USA': 20, 'FR': 50, 'GB': 36,
        },
        'XXXL': {
            'UA': 56, 'GE': 50, 'USA': 22, 'FR': 52, 'GB': 38,
        },
    }
    result = ''
    kv = []

    for isize, sizes in international_sizes.items():
        if size == isize:
            for key, value in sizes.items():
                kv.append(f'{key}: {value}')

    result += ' | '.join(kv)

    return print(' =' * 22, '\n', result, '\n', '= ' * 22)


while True:
    women_sizes(input('Enter the international size: ').upper())
