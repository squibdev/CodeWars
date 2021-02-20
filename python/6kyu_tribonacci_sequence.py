def tribonacci(signature, n):
    a, b, c = signature
    if n <= 3:
        out = []
        for _ in range(n):
            out.append(signature[_])
        return out
    else:
        for _ in range(n - 3):
            a, b, c = b, c, a+b+c
            signature.append(c)
    return signature

print(tribonacci([0,1,1], 30))