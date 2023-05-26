import math


def main(y):
    a = y + (1 + 59*(y**3) + 37*(y**2))**7
    b = (52*(y**2))**5 + 5*y
    c = a/b
    q = math.sqrt(math.log2(0.02-50*y)**3 + (1 + (y**2))**4)
    f = c - q
    return f

print('%.2e' % main(-0.09))
