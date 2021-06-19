s = input()
s1 = s[::-1]
i = s.find('h')
j = len(s) - s1.find('h')
s1 = s[:j-1] + s[i+1:j] + s[j:]
print(s1)
