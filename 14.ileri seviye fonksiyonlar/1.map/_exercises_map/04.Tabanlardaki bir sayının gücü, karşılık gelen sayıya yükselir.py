"""
-------------------------------------------------------------------tw:@tek_elo

Tabanlardaki bir sayının gücü, karşılık gelen sayıya yükselir

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Base numbers abd index: ")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("\nPower of said number in bases raised to the corresponding number in the index:")
print(result)
