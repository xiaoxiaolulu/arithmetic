"""
能够计算两个数的最大公约数
"""


def calculate_GCD(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print(calculate_GCD(60, 24))


"""
计算LCM， 能够计算出两个数的最小公倍数
"""


def calculate_LCM(x, y):

    if x > y:
        z = x

    else:
        z = y

    while(True):
        if ((z % x == 0 ) and (z % y == 0)):
            LCM = z
            break
        z += 1
    return LCM

print(calculate_LCM(4, 60))
