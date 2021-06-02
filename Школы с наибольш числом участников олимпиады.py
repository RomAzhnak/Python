lst = [0]*100
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lst[int(line.split()[2])] += 1
out = [i for i in range(1, 100) if lst[i] == max(lst)]
print(*out)
