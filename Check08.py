""""
能够print出一个列表 A与列表B不同
"""

list_1 = ["L2", "L3", 'a', 'ss']
list_2 = ["L2", "L3"]
change_list_1_to_set = set(list_1)
change_list_2_to_set = set(list_2)

print(change_list_1_to_set.difference(change_list_2_to_set))
