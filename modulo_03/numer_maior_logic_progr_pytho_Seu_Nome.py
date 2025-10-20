'''
COMPARANDO NÚMEROS COM IF-ELIF-ELSE
Este programa decide qual de dois números é o maior.
Peça ao usuário para digitar 2 números inteiros e mostre:
- Qual número é o maior
- Ou se são iguais  

'''

print("\n--- Comparador de Números ---")

# 1. PEDIR OS NÚMEROS AO UTILIZADOR
try:
    numero_a = int(input("Digite o primeiro número inteiro: "))
    numero_b = int(input("Digite o segundo número inteiro: "))
except ValueError:
    print("\nERRO: Por favor, digite apenas números inteiros válidos.")
    exit()

print("\n--- Resultado da Comparação ---")

# 2. USAR ESTRUTURAS CONDICIONAIS (if, elif, else)

# PRIMEIRA CONDIÇÃO: Verificamos se 'numero_a' é MAIOR que 'numero_b'
# Se a condição for VERDADEIRA, o código DENTRO deste bloco 'if' é executado.
if numero_a > numero_b:
    # f-string: {numero_a} e {numero_b} mostram os valores digitados.
    print(f"O primeiro número ({numero_a}) é o MAIOR.")

# SEGUNDA CONDIÇÃO: Se a primeira for FALSA, testamos esta (elif = senão se)
# Verificamos se 'numero_b' é MAIOR que 'numero_a'
elif numero_b > numero_a:
    print(f"O segundo número ({numero_b}) é o MAIOR.")

# ÚLTIMO CASO: Se NENHUMA das condições acima for VERDADEIRA, este bloco 'else' é executado.
# Isso significa que os números são IGUAIS.
else:
    print("Os dois números são IGUAIS.")

print("\n-----------------------------------")