"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir sayı listesinin pozitif ve negatif sayılarının toplamını 
lambda işlevini kullanarak hesaplayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:",nums)

total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))

print("Sum of the positive numbers: ",sum(total_negative_nums))
print("Sum of the negative numbers: ",sum(total_positive_nums))

