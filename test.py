# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# if __name__ == '__main__':

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
