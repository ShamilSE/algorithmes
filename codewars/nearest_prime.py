def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def solve(n):
    lower = n
    upper = n

    lowerPrime = None
    upperPrime = None

    found = False

    while not found:
        if is_prime(lower):
            found = True
            lowerPrime = lower
        elif is_prime(upper):
            found = True
            upperPrime = upper
        else:
            lower -= 1
            upper += 1

    if lowerPrime:
        return lowerPrime
    elif upperPrime:
        return upperPrime