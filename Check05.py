"""
获取用户输入并显示交互日历
"""


import calendar

year = int(input("请输入年份"))
month = int(input("请输入月份"))
print(calendar.month(year, month))
