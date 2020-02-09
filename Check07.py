"""
输入数字进行判断是否与666与888间隔小于88
"""


def near_target_value(n):

    result = (abs(666-n) <= 888 or (abs(888 - n) <= 888))
    return result
