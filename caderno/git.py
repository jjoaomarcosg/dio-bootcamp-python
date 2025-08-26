'''
SISTEMAS DE CONTROLE DE VERSÃO
- Controlam as versões de um arquivo ao longo do tempo.
. Registra o histórico de atualizações de um arquivo;
. Gerencia quais foram as alterações, a data, autor, etc.;
. Organização, controle e segurança.

'''

'''
TIPOS DE SISTEMAS DE CONTROLE DE VERSÃO 
- Dentre os Sistemas de Controle de Versão (VCS), temos:

.VCS Centralizado (CVCS)
ex: CVS, Subversion.

.VCS Distribuído (DVCS) ou Sistema de Controle Distribuído
ex: Git, Mercurial.

- Ele clona o repositório completo, o que inclui o historico de versões
. Cada clone é como um backup;
. Possibilita um fluxo de trabalho flexível;
. Possibilidade de trabalhar sem conexão á rede.
'''

'''
Git 
- É um sistema de controle de versão distribuído
'''

'''
Branch
- É uma ramificação do seu projeto 
. É um ponteiro móvel para um commit no histórico do repositório;
. Quando você cria uma nova branch a partir de outra existente, a nova se inicia 
apontando para o mesmo commit da Branch que estava quando foi criada 

DICA:
- Pensa no seu código como uma árvore.
- O tronco principal é a branch main (ou master) → nela fica a versão oficial do projeto.
- Uma branch é como um galho que você cria a partir do tronco para trabalhar em algo separado,
sem mexer direto no código principal.

'''