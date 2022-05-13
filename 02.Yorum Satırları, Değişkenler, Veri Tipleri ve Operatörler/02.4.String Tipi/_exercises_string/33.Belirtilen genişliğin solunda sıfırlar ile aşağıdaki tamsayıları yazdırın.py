"""
-------------------------------------------------------------------tw:@tek_elo

Belirtilen genişliğin solunda sıfırlar ile aşağıdaki tamsayıları yazdırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y));
print()

