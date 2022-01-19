def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
sayi=int(input("Fibonacci sayısı hesaplanacak sayıyı giriniz"))
print(fibonacci(sayi))