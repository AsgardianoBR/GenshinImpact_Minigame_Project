def soma(num1,num2):
    soma = num1 + num2
    
    return soma
    

def subtracao (num1, num2):
    sub = num1 - num2
    return sub

def multiplicacao (num1, num2):
    mult = num1 * num2
    return mult

def divisao (num1, num2):
    div = num1 / num2
    return div

def main():
    while True:
        num1 = float(input())
        num2 = float(input())

        print("(1) Soma")
        print("(2) Subtração")
        print("(3) Multiplicação")
        print("(4) Divisão")
    
        op = int(input("Qual operação você deseja?\n"))

        if op == 1:
            print(f'{soma(num1, num2):.2f}')
            
        elif op == 2:
            print(f'{subtracao(num1,num2):.2f}')
            
        elif op == 3:
            print(f'{multiplicacao(num1,num2):.2f}')
            
        elif op == 4:
            print(f'{divisao(num1, num2):.2f}')
            
        
        else:
            print("Operação inválida. Tente novamente.")
            
        print("Deseja continuar? [s] / [n]")
        cond = input()
        if cond == 'n':
            break
    
if __name__ == "__main__":
    main()