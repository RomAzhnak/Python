"""a = list(map(int, input().split()))
x = int(input())
num = 1
differ = 0
if len(a) == 0:
    num = 1
elif x - a[len(a) // 2] > 0:
    for i in range(len(a) // 2, 0, -1):
        if a[i - 1] >= x:
            num = i + 1
            break
        elif i - 1 == 0:
            num = i
else:
    for i in range(len(a) // 2, len(a)):
        if a[i] < x:
            num = i + 1
            break
        elif i == len(a) - 1:
            num = len(a) + 1
print(num)"""

h_list = list(map(int, input().split()))
x = int(input())
left_pos = -1
right_pos = len(h_list)
while right_pos - left_pos > 1:
    mid = (left_pos + right_pos) // 2
    if h_list[mid] >= x:
        left_pos = mid
    else:
        right_pos = mid
print(right_pos + 1)
