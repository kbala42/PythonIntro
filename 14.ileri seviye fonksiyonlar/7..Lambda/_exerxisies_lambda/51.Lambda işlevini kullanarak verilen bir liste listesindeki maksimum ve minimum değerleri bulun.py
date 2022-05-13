"""
-------------------------------------------------------------------tw:@tek_elo

51.Lambda işlevini kullanarak verilen bir liste listesindeki maksimum ve minimum değerleri bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def max_min_list_tuples(class_students):
    return_max = max(class_students,key=lambda item:item[1])[1]
    return_min = min(class_students,key=lambda item:item[1])[1]
    return return_max, return_min
    
class_students = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("Original list with tuples:")
print(class_students)
print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(class_students))

