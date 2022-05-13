"""
-------------------------------------------------------------------tw:@tek_elo

nth öğesini lambda kullanarak verilen bir liste listesinden çıkarın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def extract_nth_element(test_list, n):
    result = list(map (lambda x:(x[n]), test_list))
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
print ("Original list:")
print(students)
n = 0
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))
n = 2
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))

