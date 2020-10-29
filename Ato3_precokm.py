km = float(input())

if km > 200:
    preco = 0.45 * km
    print("O valor da passagem é: {:.2f}".format(preco))
else:
    preco = 0.50 * km
    print("O valor da passagem é: {:.2f}".format(preco))