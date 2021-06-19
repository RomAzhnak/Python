l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
if hc < h1 or hc < h2:
    print('NO')
elif (l1 + l2 <= lc and w1 <= wc and w2 <= wc) or\
        (l1 + w1 <= lc and l2 <= wc and w2 <= wc) or\
        (l1 + w2 <= lc and l2 <= wc and w1 <= wc) or\
        (l2 + w1 <= lc and l1 <= wc and w2 <= wc) or\
        (l2 + w2 <= lc and l1 <= wc and w1 <= wc) or\
        (w1 + w2 <= lc and l1 <= wc and l2 <= wc) or\
        (l1 + l2 <= wc and w1 <= lc and w2 <= lc) or\
        (l1 + w2 <= wc and l2 <= lc and w1 <= lc) or\
        (l1 + w2 <= wc and l2 <= lc and w1 <= lc) or\
        (l2 + w1 <= wc and l1 <= lc and w2 <= lc) or\
        (l2 + w2 <= wc and l1 <= lc and w1 <= lc) or\
        (w1 + w2 <= wc and l1 <= lc and l2 <= lc) or\
        h1 + h2 <= hc and l1 <= lc and w1 <= wc and l2 <= lc and w2 <= wc or\
        h1 + h2 <= hc and l1 <= lc and w1 <= wc and w2 <= lc and l2 <= wc or\
        h1 + h2 <= hc and w1 <= lc and l1 <= wc and l2 <= lc and w2 <= wc or\
        h1 + h2 <= hc and w1 <= lc and l1 <= wc and w2 <= lc and l2 <= wc:
    print('YES')
else:
    print('NO')
