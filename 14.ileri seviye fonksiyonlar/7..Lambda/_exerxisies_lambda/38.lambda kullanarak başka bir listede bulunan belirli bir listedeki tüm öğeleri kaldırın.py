"""
-------------------------------------------------------------------tw:@tek_elo

lambda kullanarak başka bir listede bulunan belirli bir listedeki 
tüm öğeleri kaldırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]
print("Original lists:")
print("list1:", list1)
print("list2:", list2)
print("\nRemove all elements from 'list1' present in 'list2:")
print(index_on_inner_list(list1, list2))
