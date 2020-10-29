numeros = list()
while True:
    num = int(input())
    if num not in numeros:
        numeros.append(num)
    else:
        print("número duplicado. Tente novamente.")
    x = input("Deseja continuar? [S/N]")
    if x == 'N' or x == 'n':
        break
numeros.sort()
print(numeros)