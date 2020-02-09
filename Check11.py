

def CBB_SUM(a, b, c, d, e):

    CMM = a+b+c+d+e
    if CMM in range(111, 667):
        return 888
    else:
        return CMM

print(CBB_SUM(100, 1, 2, 3, 40))
