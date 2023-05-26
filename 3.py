import math


def main(a, x, m, n):
    q = 0
    w = 0
    for c in range(1, n + 1):
        for k in range(1, a + 1):
            for j in range(1, m + 1):
                q += (49*(j**3) + c + (math.cos(k))**5)
    for c in range(1, a + 1):
        w += (math.floor(x))**6 + (math.ceil(c))**2
    return w - q

print('%.2e' % main(5,0.51,7,6))
