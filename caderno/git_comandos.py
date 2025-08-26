"""
Git - Comandos básicos para primeiro contato

Configuração inicial:
---------------------
git config --global user.name "Seu Nome"
    -> Define seu nome de usuário global no Git (usado nos commits).

git config --global user.email "seuemail@email.com"
    -> Define seu email global no Git (usado nos commits).


Ciclo básico do Git:
--------------------
git init
    -> Inicia um repositório Git dentro da pasta atual.

git status
    -> Mostra o estado atual dos arquivos (se foram modificados, adicionados ou não rastreados).

git add <arquivo>
    -> Adiciona o arquivo especificado para a "staging area" (preparação para commit).

git add .
    -> Adiciona TODOS os arquivos modificados/novos para a staging area.

git commit -m "mensagem"
    -> Salva no histórico do Git os arquivos que estão na staging area, com uma mensagem descritiva.

git log
    -> Mostra o histórico completo de commits.

git log --oneline
    -> Mostra o histórico de commits de forma resumida (um commit por linha).


Integração com GitHub:
----------------------
git remote add origin <url>
    -> Conecta seu repositório local com um repositório remoto no GitHub.

git branch -M main
    -> Renomeia a branch atual para "main" (padrão usado hoje em vez de "master").

git push -u origin main
    -> Envia os commits locais para o repositório remoto (GitHub), criando o vínculo inicial.

git push
    -> Envia commits locais para o repositório remoto já configurado.

git pull
    -> Baixa as mudanças do repositório remoto e atualiza sua branch local.


Branches (ramificações):
------------------------
git branch <nome-da-branch>
    -> Cria uma nova branch (linha de desenvolvimento paralela).

git checkout <nome-da-branch>
    -> Troca para a branch especificada.

git merge <nome-da-branch>
    -> Mescla a branch especificada dentro da branch atual.
"""
