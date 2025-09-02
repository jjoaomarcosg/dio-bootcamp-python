'''
# DOMINANDO STRINGS E FATIAMENTO

# ETAPA 1 - Conhecendo métodos úteis da classe string
# ETAPA 2 - Interpolação de variáveis
# ETAPA 3 - Fatiamento de string
# ETAPA 4 -  String múltiplas linhas 

--------------------------- ETAPA 1 ------------------------------

- MAIÚSCULA, MINÚSCULA E TÍTULO

curso = 'pYtHon'

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python


- ELIMINANDO ESPAÇOS EM BRANCO

curso = '   Python '

print(curso.strip())
>>> 'Python'

print(curso.lstrip())
>>> 'Python '

print(curso.rstrip())
>>> '    Python'


- JUNÇÕES E CENTRALIZAÇÃO

curso = 'Python'

print(curso.center(10, '#'))
>>> '##Python##'

print('.'.join(curso))
>>> 'P.y.t.h.o.n'


'''