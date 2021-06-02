a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0
if a1 >= a2 and b1 >= b2 and c1 >= c2:
    s1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
if a1 >= a2 and b1 >= c2 and c1 >= b2:
    s2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
if a1 >= b2 and b1 >= a2 and c1 >= c2:
    s3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
if a1 >= b2 and b1 >= c2 and c1 >= a2:
    s4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
if a1 >= c2 and b1 >= a2 and c1 >= b2:
    s5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
if a1 >= c2 and b1 >= b2 and c1 >= a2:
    s6 = (a1 // c2) * (b1 // b2) * (c1 // a2)
if s2 > s1:
    s1 = s2
if s3 > s1:
    s1 = s3
if s4 > s1:
    s1 = s4
if s5 > s1:
    s1 = s5
if s6 > s1:
    s1 = s6
print(s1)
