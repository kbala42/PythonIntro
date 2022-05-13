"""
-------------------------------------------------------------------tw:@tek_elo

Lambda ile tamsayı listesinden kare ve küp listeleri oluşturun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

