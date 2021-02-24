def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

def two_sum_v1(numbers, target):
    i = 0
    out = []
    for n in numbers:
        m = target - n
        if m in numbers:
            j = numbers.index(m)
            out.append(i)
            if i == j:
                out.pop()
            else:
                out.append(j)
                break
        i += 1
    return out
            