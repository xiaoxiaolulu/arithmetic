"""
有四个数字 1 2 3 4能组成多少个互不相同且重复的三位数
"""
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print(i, j, k)

num = ["1", "2", "3", "4", "5"]
counter = 0

for i in num:
    for j in num:
        for k in num:
            if len(set(i + j + k)) == 3:
                """利用for循环与set去重"""
                print(i, j, k)
            counter += 1
print(counter)
