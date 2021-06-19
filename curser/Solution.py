def rec():
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            print(n)
            rec()
        else:
            rec()
            print(n)


if __name__ == '__main__':
    print(__name__)
rec()
