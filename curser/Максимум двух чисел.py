a = int(input())
b = int(input())
c = (a + b) // 2 + 2
a1 = a + 1
b1 = b + 1
m = ((a1 // c) * (b % c) + (a % c) * (b1 // c))
num = a + b * ((a1 // c) + (b1 // c)) - m
print(num)
