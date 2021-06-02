employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]
for name, number in zip(employee_names, employee_numbers):
    print(name, number)

employee = [[2, 9, 18, 28], ["Дима", "Марина", "Андрей", "Никита"]]
for name in zip(*employee):
    print(*name)
