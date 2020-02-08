"""
Decorator
"""


def my_decorator(msg="not hello"):

    def decorated(func):
        def wrapper(*args, **kwargs):
            print("劳资python贼溜")
            func(*args, **kwargs)
            print(f"this msg is {msg}")
            print("杀鸡焉用牛刀, 点尼玛币的狗蛋改造！")

        return wrapper
    return decorated


@my_decorator(msg="hello 狗蛋")
def print_my_name(name):
    print(f"{name}以前瞧不上劳资， 现在开始就聘用不起劳资了")


print_my_name("名字贼溜")
