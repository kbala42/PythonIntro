"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak belirli bir tamsayı ve karakter dizisi listesini sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def sort_mixed_list(mixed_list):
    mixed_list.sort(key=lambda e: (isinstance(e, str), e))
    return mixed_list
mixed_list = [19,'red',12,'green','blue', 10,'white','green',1]
print("Original list:")
print(mixed_list)
print("\nSort the said  mixed list of integers and strings:")
print(sort_mixed_list(mixed_list))

