valor = ''

def adicao(num1, num2):
    soma = num1 + num2
    print(soma)

def subracao(num1, num2):
    sub = num1 - num2
    print(sub)

def multiplicacao(num1, num2):
    mult = num1 * num2
    print(mult)
    
def divisao(num1, num2):
    if num1 or num2 == 0:
        print("Não foi possível realizar a divisão por 0")
    else: 
        div = num1 / num2
        print(div)
        
def calculadora(num1, num2, operacao):
    if operacao in ["adicao", "adição", "+"]:
        resultado = num1 + num2
    elif operacao in ["subtracao" , "subtração", "-"]:
        resultado = num1 - num2
    elif operacao in ["multiplicacao" , "multiplicação", "*"]:
        resultado = num1 * num2
    elif operacao in ["divisao", "divisão", "/"]:
        if num1 or num2 != 0: 
            resultado = num1 / num2
        else:
            print("Não foi possível realizar a divisão por 0")
    else:
        resultado = "Operação inválida."
    
    return resultado

saida = "N"
while saida.upper() != "S":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (adição, subtração, multiplicação, divisão ou seus símbolos +, -, *, /): ")
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Erro: Insira valores válidos.")
        continue
    saida = input("Deseja sair? Digite S para sair ou N para continuar: ")