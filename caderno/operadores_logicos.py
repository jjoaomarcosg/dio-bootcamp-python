# OPERADORES LÓGICOS

''' 
OQUE SÃO ? 
- São operadores utilizados em conjunto com os operadores
de comparação, para montar uma expressão lógica. 
Quando um operador de comparação é utilizado, o resultado retornado é
um booleano, dessa forma podemos combinar operadores de comparação
com os operadores lógicos, exemplo:

op_comparacao + op_logico + op_comparacao... N ...

'''

saldo = 1000
saque = 2000
limite = 100

# # saldo >= saque # True
# # saldo <= limite # False

# Operador E
saldo >= saque and saque <= limite #false
# Aqui todas as condições precisam ser verdadeiras
# para retornar True
# Se apenas um for falso, ja retorna False

#-----------------------------------------

# Operador OU
saldo >= saque or saque <= limite
# Aqui precisa ter somente uma condição verdadeira 
# para retornar True
# Se apenas um for verdadeiro, ja retorna True

#-----------------------------------------

# Operador de Negação / inverso da verdade 
contatos_emergencia = []

not 1000 > 1500 #True
# Primeiro avalia a condição, tendo o resultado, o "not" contraria isso.

not contatos_emergencia # True
# Pq lista vazia em Python é false

not 'saque 1500;' # False
# Pq String é True, ela tem valor.

not '' # True
# String vazia é false, pois não tem valor.

#-----------------------------------------

# Parênteses
saldo_1 = 1000
saque_1 = 250
limite = 200
conta_especial = True

saldo_1 >= saque and saque_1 <= limite or conta_especial and saldo_1 >= saque_1
#>>> True

(saldo_1 >= saque and saque_1 <= limite) or (conta_especial and saldo_1 >= saque_1)
#>>> True