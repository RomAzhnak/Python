n = int(input())
clicks = list(map(int, input().split()))[:n]
k = int(input())
seqClick = list(map(int, input().split()))[:k]
counts = [0 for _ in range(n+1)]
for i in seqClick:
    counts[i] += 1
for i in range(n):
    if clicks[i] >= counts[i+1]:
        print('NO')
    else:
        print('YES')
