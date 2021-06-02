synonyms = {}
for i in range(int(input())):
    line = input().split()
    synonyms[line[0]], synonyms[line[1]] = line[1], line[0]
print(synonyms[input()])
