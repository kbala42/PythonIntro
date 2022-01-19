def asalMi(x):
    sayac=2
    if (x==1):
        return False
    elif (x==2):
        return True
    else:

        while (sayac<x):
            if(x%sayac==0):
                sayac+=1
                return False

            return True

asalSayilar=list(filter(asalMi,range(1,100)))
print(asalSayilar)