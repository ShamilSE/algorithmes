def ft_max(n1, n2):
    return n1 if n1 > n2 else n2


def factorize_number(x):
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


factorize_number(10)
