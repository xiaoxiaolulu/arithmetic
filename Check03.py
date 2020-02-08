"""
提取扩展名
"""

filename_with_extension = input("请输入文件名: ")

name_list = filename_with_extension.split('.')
print(f"提取的扩展名为 -> {name_list[-1]}")
