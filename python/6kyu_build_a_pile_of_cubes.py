def find_nb(m):
    res = 0
    n = 1
    while res < m:
        res += n ** 3
        n+=1
    n -= 1
    if res != m:
        return -1
    else:
        return n