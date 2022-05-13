"""
-------------------------------------------------------------------tw:@tek_elo

Lambda işlevini kullanarak verilen listenin her sayısını belirli bir sayıyla çarpın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

