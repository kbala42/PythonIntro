"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir sözlük listesini sıralamak için program

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

