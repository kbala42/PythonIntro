import random
sonuc={random.randint(1,400) for i in range(10)}
kazananlar=map(lambda talihli:" seçilen numara:"+str(talihli)+"\n",sonuc)
print(kazananlar)
print(*kazananlar)