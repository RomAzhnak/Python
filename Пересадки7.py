route = list(map(int, input().split()))
route1 = sorted(route[:2])
route2 = sorted(route[2:])
route1 = {i for i in range(route1[0], route1[1]+1)}
route2 = {i for i in range(route2[0], route2[1]+1)}
print(len(route1 & route2))
