def main(n):
    a = -0.70
    b = 0.85
    c = 0
    for i in range(2, n+1):
        c = a**3 + b + 1
        a = b
        b = c
    return c

print('%.2e' % main(4))
