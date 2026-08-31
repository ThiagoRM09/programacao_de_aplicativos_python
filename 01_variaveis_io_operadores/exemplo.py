nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
altura = float(input("Qual a sua altura: "))
aprovado = bool(input("Digite True para aprovado ou False para reprovado: "))

print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade}")
print(f"Sua altura é: {altura}")
print(f"Você está aprovado: {aprovado}")

print(type(nome))
print(type(idade))
print(type(aprovado))
print(type(altura))

numero1 = 10
numero2 = 3

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
potencia = numero1 ** numero2
resto = numero1 % numero2

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(potencia)
print(resto)