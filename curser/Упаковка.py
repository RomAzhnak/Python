l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
l3, w3, h3 = int(input()), int(input()), int(input())
if l1 > w1:
    l1, w1 = w1, l1
if l2 > w2:
    l2, w2 = w2, l2
if l3 > w3:
    l3, w3 = w3, l3
ll3 = l2
if l1 > l2:
    ll3 = l1
    l1, w1, h1, l2, w2, h2 = l2, w2, h2, l1, w1, h1
if h1 > h2:
    hh1 = h1
    hh2 = h1
else:
    hh1 = h2
    hh2 = h2
ll1 = l2
if l2 < w1:
    ww1 = w1 + w2
else:
    ww1 = l1 + w2
ll2 = l1 + l2
if w1 > w2:
    ww2 = w1
    ww3 = w1
else:
    ww2 = w2
    ww3 = w2
if ll2 > ww2:
    ll2, ww2 = ww2, ll2
hh3 = h1 + h2
if ll1 <= l3 and ww1 <= w3 and hh1 <= h3:
    print("YES")
elif ll2 <= l3 and ww2 <= w3 and hh2 <= h3:
    print("YES")
elif ll3 <= l3 and ww3 <= w3 and hh3 <= h3:
    print("YES")
else:
    print("NO")
