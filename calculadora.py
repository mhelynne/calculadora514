def soma(a, b):
	print("A soma é: ", a+b)

def subtrai(a, b):
	print("A diferença é: ", a-b)

def multiplica(a, b):
	print("A produto é: ", a*b)

def divide(a, b):
	if b == 0:
		print("Não é possível dividir por zero")
	else:
		print("A divisão é: ", a/b)

#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)