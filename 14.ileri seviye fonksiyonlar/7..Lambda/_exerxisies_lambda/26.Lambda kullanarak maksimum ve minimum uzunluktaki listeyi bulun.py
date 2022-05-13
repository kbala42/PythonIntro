"""
-------------------------------------------------------------------tw:@tek_elo

Lambda kullanarak maksimum ve minimum uzunluktaki listeyi bulun

-------------------------------------------------------------------------------
res: www.w3resource.com/python-exercises/string/
"""
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nList with maximum length of lists:")
print(max_length_list(list1))
print("\nList with minimum length of lists:")
print(min_length_list(list1))

