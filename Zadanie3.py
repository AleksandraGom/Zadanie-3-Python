n = int(input("Podaj liczbę wyrazów:"))

fib = [0, 1]

for i in range(n-2):
    fib.append(fib[i] + fib[(i+1)])
print("Elementy ciągu Fibonacciego:",fib)
