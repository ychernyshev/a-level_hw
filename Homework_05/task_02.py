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
reversed_students = dict(reversed(list(student.items())))

temp_original = set()
temp_reversed = set()
result = None

for value in student.values():
    # temp_original.add(value)
    temp_original = value
    # print(temp_original)
for item in reversed_students.values():
    temp_reversed = item
    # print(temp_reversed)

print(temp_reversed)
print(temp_original)
result = temp_original.intersection(temp_reversed)
print(result)
# result = temp_original.intersection(temp_reversed)

# for item in range(len(student)):
#     print(item)


# print(result)

