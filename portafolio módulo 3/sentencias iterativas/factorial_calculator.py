n = int(input("Número para factorial: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)
