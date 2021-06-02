import itertools
import time
take = lambda n, x: list(itertools.islice(x, n))
start = time.time()
a = (i for i in range(1000000))
print(take(5, map(lambda x: x+100, a)))
end = time.time()

print(end - start)
