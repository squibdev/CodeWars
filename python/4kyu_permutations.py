def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            print("i, c", i, c)
            for s in permutations(string[:i] + string[i + 1:]):
                print('s', s)
                print('perm', permutations(string[:i] + string[i+1:]))
                result.add(c + s)

    r = list(result)
    r.sort()
    return r

print(permutations('aabb'))