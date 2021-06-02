bank = {}


def transaction(name, summa, sign=1):
    bank[name] = bank.get(name, 0) + summa * sign


with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split()
        if line[0] == 'DEPOSIT':
            transaction(line[1], int(line[2]))
#           bank[line[1]] = bank.get(line[1], 0) + int(line[2])
        elif line[0] == "WITHDRAW":
            transaction(line[1], int(line[2]), -1)
#            bank[line[1]] = bank.get(line[1], 0) - int(line[2])
        elif line[0] == "BALANCE":
            print(bank.get(line[1], 'ERROR'))
        elif line[0] == 'TRANSFER':
            transaction(line[1], int(line[3]), -1)
            transaction(line[2], int(line[3]))
#            bank[line[1]] = bank.get(line[1], 0) - int(line[3])
#            bank[line[2]] = bank.get(line[2], 0) + int(line[3])
        elif line[0] == 'INCOME':
            for key in bank:
                if bank[key] > 0:
                    bank[key] = int(bank[key] * (1 + int(line[1])/100))

# второй вариант без IF ELSE
bank = dict()


def deposit(name_and_sum, sign=1):
    name, summ = name_and_sum.split()
    bank[name] = bank.get(name, 0) + int(summ) * sign


def withdraw(name_and_sum):
    deposit(name_and_sum, sign=-1)


def balance(name):
    print(bank.get(name, 'ERROR'))


def transfer(name_and_sum):
    withdraw(' '.join(name_and_sum.split()[::2]))
    deposit(' '.join(name_and_sum.split()[1:]))


def income(prs):
    for name, summ in bank.items():
        bank[name] = int(summ * (1 + int(prs) / 100 * (summ > 0)))


commands = dict(DEPOSIT=deposit, WITHDRAW=withdraw, BALANCE=balance,
                TRANSFER=transfer, INCOME=income)

with open('input.txt', encoding='utf8') as inf:
    for line in inf:
        command, name_and_sum = line.strip().split(' ', 1)
        action = commands.get(command)
        action(name_and_sum)
