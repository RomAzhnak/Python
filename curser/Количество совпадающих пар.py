from math import factorial
lst = list(map(int, input().split()))
numb = 0
tmplst = []
for now in lst:
    if now not in tmplst:
        i = lst.count(now)
        if i > 1:
#            numb += int(factorial(i) / (factorial(i - 2) * 2))
            numb += i * (i - 1) / 2 #сокращаем предыдущую формулу с факториалами
            tmplst.append(now)
print(numb)

# второй вариант Быстрый
lst = list(map(int, input().split()))
n, i = 0, len(lst) - 1
while i:
    n += lst.count(lst.pop())
    i -= 1
print(n)

# третий вариант
for i in range(len(a)):
    n += a[i+1:].count(a[i])
