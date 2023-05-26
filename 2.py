import math


def main(x):
    if x < 146:
        return math.ceil(x**7)
    elif 146 <= x < 240:
        return x**2/91
    elif 240 <= x < 313:
        return (x**2-x**3-x)**6-(x**3-0.08-58*x**2)**5-(82*(x**2)-8-x)**3
    else:
        return 52*(x**3+81)**3

print('%.2e' % main(260))
