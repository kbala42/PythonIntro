list1=[i for i in range(5)]
print((list1))

list2=[i for i in range(11,20)]
print((list2))

list3=[i for i in range(10,100,10)]
print((list3))

list4=[i+5 for i in range(10,100,10)]
print((list4))

list5=[i*2 for i in range(10,100,10)]
print((list5))

list6=[[1,2,3],[4,5,6],[7,8,9]]
list7=[j for i in list6 for j in i]
print(list7)

list8=[i for i in range(1,20) if i%2==0]
print(list8)