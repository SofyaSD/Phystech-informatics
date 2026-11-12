#!/usrbin/python3
def factor(n):
    if n <= 1:
        return []

    factors = []
    d = 2
    while d*d <= n:
        while n%d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input())
print(factor(n))
