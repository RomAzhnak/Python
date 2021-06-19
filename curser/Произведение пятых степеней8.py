from functools import reduce
from itertools import repeat
from operator import mul

print(
    reduce(mul,
           map(pow,
               map(int,
                   input().split()
                   ),
               repeat(5)
               )
           )
)
print(reduce(mul, map(int, input().split()))**5)
