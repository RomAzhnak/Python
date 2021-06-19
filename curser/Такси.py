distance = list(map(int, input().split()))
price = list(map(int, input().split()))
distance.sort()
price.sort(reverse=True)
s = list(map(lambda x, y: x*y, distance, price))
print(sum(s))

# в функциональном стиле
print(
    sum(
        map(
            lambda x1, y1: x1*y1,
            sorted(
                map(
                    int, input().split()
                    ),
                reverse=True
                ),
            sorted(
                map(
                    int, input().split()
                    )
                )
            )
        )
    )
