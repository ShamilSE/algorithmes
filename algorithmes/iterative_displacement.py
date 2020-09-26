def iterative_displacement(a, s):
    tmp = a[0]
    for k in range(0, s - 1):
        a[k] = a[k + 1]
    a[s - 1] = tmp
    return a


print(iterative_displacement([0, 1, 2, 3, 4], 5))


def reversed_iterative_displacement(a, s: int):
    tmp = a[s - 1]
    for k in range(s - 1, -1, -1):
        a[k] = a[k - 1]
    a[0] = tmp
    return a


print(reversed_iterative_displacement([0, 1, 2, 3, 4], 5))
