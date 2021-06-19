def linear(a=0.3, b=2):
    def result(x):
        return a * x + b
    return result


print(linear(0.1, 9)(10))
tax = linear(0.1, 7)
print(tax(10))
