def array_search(a, s:int, x:int):
    """
    Searches x in a
    :param a: array
    :param s: array size
    :param x: element should find
    :return:
        index of element
        if several elements equal to x, return with lower index
    """
    for k in range(s):
        if a[k] == x:
            return k
    return -1


def test_array_search():
    a1 = [1, 2, 3, 4, 5]
    r = array_search(a1, len(a1), 8)
    if r == -1:
        print('test1 passed')
    else:
        print('test1 did not passed')

    a2 = [-1, -2, -3, -4, -5]
    r2 = array_search(a2, len(a2), -2)
    if r2 == 1:
        print('test2 passed')
    else:
        print('test2 did not passed')

    a3 = [10, 10, -4, 0, 10]
    r3 = array_search(a3, len(a3), 10)
    if r3 == 0:
        print('test3 passed')
    else:
        print('test3 did not passed')


test_array_search()