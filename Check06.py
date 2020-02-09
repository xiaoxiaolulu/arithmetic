"""
计算球的体积
"""
import math

raw = int(input("您好，请输入想计算的球体半经"))
pi = math.pi
v = (4/3) * pi * raw ** 3
print(f"结果为{v}")
