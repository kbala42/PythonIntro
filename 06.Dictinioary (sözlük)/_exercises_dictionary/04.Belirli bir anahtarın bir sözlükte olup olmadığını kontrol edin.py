"""
-------------------------------------------------------------------tw:@tek_elo

Belirli bir anahtarın bir sözlükte zaten var olup olmadığını kontrol edin

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""

print('''
          Çözüm 1
      ''')
      
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def anahtarVarmi(x):
  if x in d:
      print('Anahtar sözlükte var')
  else:
      print('Anahtar sözlükte yok')
anahtarVarmi(5)
anahtarVarmi(9)

print('''
          Çözüm 2
      ''')
def key_in_dict(d, key):
  return (key in d) 
students = {
  'Theodore': 19,
  'Roxanne': 22,
  'Mathew': 21,
  'Betty': 20
}
print("\nOriginal dictionary elements:")
print(students)
print(key_in_dict(students, 'Roxanne'))
print(key_in_dict(students, 'Gina'))

print('''
          Çözüm 3
      ''')

x=d[5]
#x=d[9]
try:
    print (x)
except KeyError:
    print ("No such a key")

