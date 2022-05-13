"""
-------------------------------------------------------------------tw:@tek_elo

Harita işlevini kullanarak belirli bir liste sözlüğünü sözlük listesine ayırın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print("Original dictionary of lists:")
print(marks)
print("\nSplit said dictionary of lists into list of dictionaries:")
print(list_of_dicts(marks))

