import random
matriz = []

#Criando a matriz -------------------------------------
for a in range(4):
    linha=[]
    for b in range(4):
        numero_aleatorio = random.randint(1, 99)
        linha.append(numero_aleatorio)
    matriz.append(linha)

print('-- Matriz --')
for i in matriz:
    for elemento in i:
        print(f'{elemento}  ', end='')
    print('')
print()

#Maior valor da terceira coluna -------------------------------------
valor = 0
for a in range(4):
    if matriz[a][2] > valor:
        valor = matriz[a][2]
print(f'O maior valor da 3° coluna é: {valor}')

#Maior valor da terceira coluna -------------------------------------
soma = 0

for a in range(4):
    soma += matriz[a][a]    
print(f'A soma da diagonal principal é: {soma}')






#Triângulo inferior




#Triângulo superior
