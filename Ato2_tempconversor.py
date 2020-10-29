x = int(input())
temp = input("Deseja converter para Celsius [C] ou Fahrenheit [F]? \n")

if temp == 'F'or temp=='f':
    fah = ((x * 9) / 5) + 32
    print(f"Está fazendo {fah:.2f} °F")
elif temp == 'C' or temp=='c':
    cel = ((x - 32) * 5) /9
    print(f"Está fazendo {cel:.2f} °C")
