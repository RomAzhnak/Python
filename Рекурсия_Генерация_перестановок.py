def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    for digit in '0', '1':
        gen_bin(m-1, prefix + digit)


def generate_numbers(n, m, prefix=None):
    """Генерирует все числа (с лидирующими нулями)
    в N-ричной системе счисления (N <= 10)
    длины M"""
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


# для произвольной системы
generate_numbers(3, 3)

# для двоичной системы
# gen_bin(3)
