"""
四个参数进行求和汇总，如果两个值是一样，汇总结果为888
"""


def BB_SUM(a, b, c, d):

    if a == b or a == c or a == d or b == c or b == d or c == d:
        BB_SUM = 888
    else:
        BB_SUM = a + b + c + d
    return BB_SUM

print(BB_SUM(1, 2, 2, 4))
