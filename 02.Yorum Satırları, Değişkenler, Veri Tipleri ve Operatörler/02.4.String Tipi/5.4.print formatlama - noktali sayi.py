print('-----------------------------------------')
print('Sayı tiplerinde .f kullanılarak rakam\n'
      'biçimlendirmesi yapılabilir\n'
      '.f  sıfırdan sonra 1 rakam\n'
      '.2f sıfırdan sonra 2 rakam\n'
      '.3f sıfırdan sonra 3 rakam\n'
      'yürütüleceğini gösterir')
print('-----------------------------------------')
print("{:.1f} {:.2f} {:.3f}".format(3.14,8.015,9.0123))
print()

print(f"{3.14:.1f} {8.015:.2f} {9.0123:.3f}")
print()

a=3.14
b=8.015
c=9.0123
print(f"{a:.1f} {b:.2f} {c:.3f}")