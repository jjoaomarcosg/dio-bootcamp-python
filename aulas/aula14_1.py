#--------------------------- ETAPA 2 ------------------------------

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

# EXEMPLO UTILIZANDO UM ITERÁVEL
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:        
    print() # adiciona uma quebra de linha 
    print('Fim')



# EXEMPLO UTILIZANDO BUILT-IN RANGE
for numero in range(0, 11):
    print(numero, end=' ')

print()
# exibindo a tabuada de 5
for numero in range(0, 51, 5):
    print(numero, end=' ')