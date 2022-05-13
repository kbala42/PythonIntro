"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir liste listesini uzunluk ve değere göre sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nSort the list of lists by length and value:")
print(sort_sublists(list1))
