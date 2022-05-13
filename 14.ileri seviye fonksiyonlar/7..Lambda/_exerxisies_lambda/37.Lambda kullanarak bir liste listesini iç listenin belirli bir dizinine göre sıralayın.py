"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak bir liste listesini iç listenin belirli bir dizinine 
göre sıralayın

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
print ("Original list:")
print(students)
index_no = 0
print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
print(index_on_inner_list(students, index_no))
index_no = 2
print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
print(index_on_inner_list(students, index_no))

