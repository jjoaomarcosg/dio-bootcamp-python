'''
# ESTRUTURAS DE REPETIÇÃO

# ETAPA 1 - O que são estruturas de repetição ?
# ETAPA 2 - Comando for e a função built-in range
# ETAPA 3 - Comando while

#--------------------------- ETAPA 1 ------------------------------

# O QUE SÃO ESTRUTURAS DE REPETIÇÃO ?

- São estruturas utilizadas para repetir um trecho de código um
determinado número de vezes. Esse número pode ser conhecido 
previamente ou determinado através de uma expressão lógica.


#--------------------------- ETAPA 2 ------------------------------

# COMANDO for 

- O comando FOR é usado para percorrer um objeto iterável. Faz
sentido usar FOR quando sabermos o número exato de vezes que
nosso bloco de código deve ser executado, ou quando
queremos percorrer um objeto iterável.

- Iterar é o ato de percorrer uma sequência, item por item, 
do começo ao fim.

# FUNÇÃO RANGE

- Range pe uma função built-in do Python, ela é usada para 
produzir uma sequência de números inteiros a partir de um 
início (inclusivo) para um fim (exclusivo). Se usarmos range (i,j)
será produzido:

i, i+1, i+2, i+3, ..., j-1.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

# RANGE

# range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
>>> [0, 1, 2, 3]


#--------------------------- ETAPA 3 ------------------------------

# COMANDO while

- O comando while é usado para repetir um bloco de código
varias vezes. Faz sentido usar while quando não sabemos o
número exato de vezes que nosso bloco de código deve ser 
executado.

'''