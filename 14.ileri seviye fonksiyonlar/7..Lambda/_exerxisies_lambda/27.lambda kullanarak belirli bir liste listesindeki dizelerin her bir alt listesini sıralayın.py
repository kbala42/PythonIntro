"""
-------------------------------------------------------------------tw:@tek_elo

lambda kullanarak belirli bir liste listesindeki dizelerin her bir alt listesini sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
print("\nOriginal list:")
print(color1)  
print("\nAfter sorting each sublist of the said list of lists:")
print(sort_sublists(color1))

