# Створити структуру даних для студентів з імен та прізвищ, можна випадкових.
# Придумати структуру даних, щоб вказувати, у якій групі навчається студент
# (Групи Python, FrontEnd, FullStack, Java).
# Студент може навчатися у кількох групах. Потім вивести:
#   - студентів, які навчаються у двох та більше групах
#   - студентів, які не навчаються на фронтенді
#   - студентів, які вивчають Python або Java
student = {
    'Alex': {
        'Python', 'FullStack',
    },
    'Bill': {
        'FrontEnd', 'FullStack',
    },
    'Bob': {
        'Java',
    },
}
count_of_groups = 0
persona_groups_number = {}

for key, value in student.items():
    persona_groups_number[key] = len(value)

print(f'List of students who are in more than 2 groups:', end=' ')
for key, value in persona_groups_number.items():
    if value >= 2:
        print(f'{key}', end=' ')

print(f'\nStudent/s who is/are not in FrontEnd group:', end=' ')
for key, value in student.items():
    if not 'FrontEnd' in value:
        print(f'{key}', end=' ')

print(f'\nStudents who learn Python or Java:', end=' ')
for key, value in student.items():
    if 'Python' in value:
        print(f'{key}(Python)', end=' ')
    if 'Java' in value:
        print(f'{key}(Java)', end=' ')