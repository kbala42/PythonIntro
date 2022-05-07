'''
-------------------------------------------------------------------tw:@tek_elo
    format_map metodu format metodu gibi çalışır. dic yapısıyla haritalanır
-------------------------------------------------------------------------------
'''

koordinatlar = {'x': 5, 'y': 3, 'z' : 0}
print( 'x = {x}, y = {y}, z = {z}'.format_map(koordinatlar))
print()

print('Alt sınıflarla haritalama')
class Koordinat(dict):
    def __missing__(self, key):
      return key

print('({x})'.format_map(Koordinat(x = '5')))
print('({x}, {y})'.format_map(Koordinat(x = '5')))
print('({x}, {y}, {z})'.format_map(Koordinat(x = '5')))
print('({x}, {y}, {z})'.format_map(Koordinat(x = '5', z = '-5')))



