import sys
read = sys.stdin
n = int(read.readline())
country_cities = {}
for i in range(n):
    line = read.readline().strip().split()
    country_cities[line[0]] = set(line[1:])
m = int(read.readline())
country = []
for i in range(m):
    line = read.readline().strip()
    for k in country_cities.keys():
        if line in country_cities[k]:
            print(k)
            break

# второй вариант наоборот
n = int(input())
d = {}
for j in range(n):
    x = input().split()
    for i in range(1, len(x)):
        d[x[i]] = x[0]
m = int(input())
for i in range(m):
    print(d[input()])
