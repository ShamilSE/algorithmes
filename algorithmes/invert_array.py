def invert_array(a, s):
    """
    inverts list, example:
    [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    :param a: list
    :param s: list size
    :return: reversed list
    """
    for k in range(s):
        a[k], a[s - 1 - k] = a[s - 1 - k], a[k]
        return a

def test_invert_array():
    a1 = [1, 2, 3, 4, 5]
    print(a1)
    r = invert_array(a1, len(a1))
    print(a1)
    if r == [5, 4, 3, 2, 1]:
        print('test1 passed')
    else:
        print('test1 did not passed')

    a2 = [10, 0, 56, 70, 0]
    print(a2)
    r = invert_array(a2, len(a2))
    print(a2)
    if r == [0, 70, 56, 0, 10]:
        print('test2 passed')
    else:
        print('test2 did not passed')


test_invert_array()