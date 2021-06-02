def rd(x, y=0):
    """ A classical mathematical rounding by Vo
print( rd(0.49), rd(0.51), rd(0.5), rd(1.5), rd(2.5), rd(0.15,1)) # 0 1 1 2 3 0.2  """

    m = int('1'+'0'*y)     # multiplier - how many positions to the right
    q = x * m              # shift to the right by multiplier
    c = int(q)             # new number
    i = int((q-c) * 10)    # indicator number on the right
    if i >= 5:
        c += 1
    return c / m
