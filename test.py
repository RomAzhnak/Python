# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# if __name__ == '__main__':


import collections


def print_hi(name):
    print(f'Hi, {name}')


print(hash('a') & 7)

d = collections.deque()
for i in range(3, 33):
    d.append('e%d' % i)  # добавить e3 - e32
print(d)
print(d[0])

print_hi('Rom')
