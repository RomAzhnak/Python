numBook = ['']*4
for i in range(4):
    string = input()
    if string.startswith('+7'):
        string = '8' + string[2:]
    numBook[i] = ''.join([s for s in string if s.isdigit()])
    if len(numBook[i]) == 7:
        numBook[i] = '8495'+numBook[i]
for i in range(1, 4):
    print(["NO", 'YES'][numBook[0] == numBook[i]])  # печатать либо [0] либо [1] в ["NO", 'YES']

"""
# второй способ
import sys


def normalize_phone(num):
    if num.startswith('+7'):
        num = '8' + num[2:]
    num = ''.join([x for x in num if x.isdigit()])
    return '8495' + num if len(num) == 7 else num


read = sys.stdin
numf = normalize_phone(read.readline().strip())
# [print(['NO', 'YES'][numf == normalize_phone(line.strip())]) for line in read]
print(*[['NO', 'YES'][numf == normalize_phone(line.strip())] for line in read], sep='\n')
"""