"""
-------------------------------------------------------------------tw:@tek_elo

Belirtilen genişliğin sağında '' ile aşağıdaki tam sayıları yazdırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x));
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y));
print()
