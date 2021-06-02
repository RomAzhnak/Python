def merge(a, b):
    i, j, c = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
