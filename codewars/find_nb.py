def find_nb(m):
    n = 1
    floors = 0
    fig = 0
    while fig < m:
        fig += (n - 1) ** 3
        n += 1
        floors += 1
        if fig == m:
            return floors - 1
    else:
        return -1