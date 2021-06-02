numYear, numPart = map(int, input().split())
setStrikes = set()
for i in range(numPart):
    first, step = map(int, input().split())
    setStrikes |= set(i for i in range(first, numYear+1, step))  # set(range(first, numYear+1, step))
setStrikes -= set(range(6, numYear+1, 7))
setStrikes -= set(range(7, numYear+1, 7))
print(len(setStrikes))
