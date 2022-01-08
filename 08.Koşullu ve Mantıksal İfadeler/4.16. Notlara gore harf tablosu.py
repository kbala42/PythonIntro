vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))

notYuzde =  vize1 * 0.3 + vize2 * 0.3 + final * 0.4

if (notYuzde >= 90):
    print("AA")
elif (notYuzde >= 85):
    print("BA")
elif (notYuzde >= 80):
    print("BB")
elif (notYuzde >= 75):
    print("CB")
elif (notYuzde >= 70):
    print("CC")
elif (notYuzde >= 65):
    print("DC")
elif (notYuzde >= 60):
    print("DD")
elif (notYuzde >= 55):
    print("FD")
else:
    print("FF")