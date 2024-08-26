import sys

#Obtendo a entrada do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha a operação: ")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Escolha entre as opções 1, 2, 3 e 4: ")

def soma (n1,n2):
    resultado = n1 + n2
    return resultado

def subtracao (n1,n2):
    resultado = n1 - n2
    return resultado

def multiplicacao (n1,n2):
    resultado = n1 * n2
    return resultado

def divisao (n1,n2):
    if n2 == 0:
        return "Erro: Divisão por 0"
    resultado = n1 / n2
    return resultado

if escolha == '1':
    total = soma(n1,n2)
    print (n1, "+", n2, '=', total)
    sys.exit()

if escolha == '2':
    total = subtracao(n1,n2)
    print (n1, "-", n2, '=', total)
    sys.exit()

if escolha == "3":
    total = multiplicacao(n1,n2)
    print (n1, "*", n2, '=', total)
    sys.exit()

if escolha == "4":
    total = divisao(n1,n2)
    print (n1, "/", n2, '=', total)
    sys.exit()

print("Escolha inválida!")