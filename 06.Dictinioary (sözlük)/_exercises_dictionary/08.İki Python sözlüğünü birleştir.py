"""
-------------------------------------------------------------------tw:@tek_elo

İki Python sözlüğünü birleştir

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

def merge_dictionaries(*dicts):
  result = dict()
  for d in dicts:
    result.update(d)
  return result
students1 = {
  'Theodore': 10,
  'Mathew': 11,
}
students2 = {
  'Roxanne': 9
}
print("Original dictionaries:")
print(students1)
print(students2)
print("\nMerge dictionaries:")
print(merge_dictionaries(students1, students2))

