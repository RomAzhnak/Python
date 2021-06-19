s = input()
i = 0
j = 0
s1 = len(s)
while i < s1:
    if i % 3 == 0:
        s = s[:i-j] + s[i-j+1:]
        j += 1
    i += 1
print(s)


s = 'ну3жн6о 3уд3ал3ит3ь 3ка3жд3ый3 т3ре3ти3й 3си3мв3ол3 с3тр3ок3и'
s = list(s)
del s[2::3]
print(''.join(s))

string = input()
string = ''.join([string[i] for i in range(len(string)) if i % 3 != 0])
print(string)
