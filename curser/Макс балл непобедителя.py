maxmark = [[0, 0] for _ in range(12)]  # [максимальный балл, второй максимум]
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        clas, mark = list(map(int, line.split()[2:]))
        if mark > maxmark[clas][0] and mark != maxmark[clas][1]:
            maxmark[clas][0] = mark
            maxmark[clas].sort()
print(maxmark[9][0], maxmark[10][0], maxmark[11][0])
