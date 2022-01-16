liste1=[1,2,3,4,5,6,7]
liste2=["python","java","c","c++","c#","pascal","cobol"]
liste3=[]
for i in range(len(liste1)):
    liste3.append((liste1[i],liste2[i]))
print(liste3)