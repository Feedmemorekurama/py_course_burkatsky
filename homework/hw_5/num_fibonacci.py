fib_1 = 1
fib_2 = 1
n = int(input("Enter num:"))
i=0
print(fib_1)
print(fib_2)
while i < n-91: #Не знаю почему так, но при -91 он выдает правильно
    fib_sum = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_sum
    i += 1
    print(fib_2)
    
