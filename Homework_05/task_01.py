# Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів).
# Знайти найуспішнішого і самого слабенького за середнім балом.
students = {
    'Artur Burned': [1, 2, 3, 4],
    'Piter Peasantsmile': [30, 1, 1, 1],
    'Nikola Background': [2, 3, 5, 6],
}
sum_evaluation = {}
sum_evaluation_list = []
max_evaluation = 0

for key, value in students.items():
    evaluations = 0
    middle_evaluations = {}
    for item in value:
        evaluations += item

    middle_evaluations[key] = evaluations

    for k, v in middle_evaluations.items():
        sum_evaluation[k] = v
        sum_evaluation_list.append(v)

min_evaluation = sum_evaluation_list[0]

for key, value in sum_evaluation.items():
    if max_evaluation < value:
        max_evaluation = value

for item in range(len(sum_evaluation_list)):
    if sum_evaluation_list[item] < min_evaluation:
        min_evaluation = sum_evaluation_list[item]

for key, value in sum_evaluation.items():
    if min_evaluation == value:
        print(f'{key}: low evaluation ({min_evaluation})')
    if max_evaluation == value:
        print(f'{key}: high evaluation ({max_evaluation})')
