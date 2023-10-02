# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:44:03 2023

@author: mauricio.tomida
"""

import os
from cria_token_criptografada import CriptografadorDeToken
from dados_repos import DadosRepositorios
from manipula_repos import ManipulaRepositorios

#####################################################################
############### Criar e armazenar token criptografado ###############
#####################################################################

# =============================================================================
# # Cria token criptografado
# criptografador = CriptografadorDeToken()
# token = str(input("Insira o token que deseja criptografar: "))
# caminho_para_salvar = input("Insira o nome do token criptografado: ")
# criptografador.criptografar_e_salvar_token(token, caminho_para_salvar)
# =============================================================================

#####################################################################

# Carrega Token criptografado de um arquivo e descriptografa
criptografador = CriptografadorDeToken()
caminho_para_carregar = input("Insira o caminho do token criptografado que deseja descriptografar: ")
token = criptografador.carregar_e_descriptografar_token(caminho_para_carregar)

# Carrega Token direto 
#descomente a linha 34 e comente as linhas 28, 29, 30, caso prefira essa opção
#token = str(input("Insira seu token: ")) 

# instanciando um objeto
username = input("Insira o seu username do github: ")
novo_repo = ManipulaRepositorios(username, token)
# Criando o repositório
nome_repo = 'dados-repositorios-empresas'
description = "Dados dos repositórios de algumas empresas",
novo_repo.cria_repo(nome_repo, description)
nome_pasta = 'dados' # opcional, pasta dentro do repositório

# path para criar os .csv
path = "dados"
existe_path = os.path.exists(path)
if not existe_path:
    os.makedirs(path)

# Busca lista de repositórios, salva localmente e faz upload para github
lista_repositorios = ['amzn', 'netflix', 'spotify', 'apple', 'microsoft', 'facebook', 'youtube', 'nasa', 'NVIDIA']
for repo in lista_repositorios:
    print(f'\nCriando o dataframe da empresa {repo}...')
    # Cria dataframes e visualiza o head
    nome_repo_empresa = f'df_{repo}_rep'
    globals()[nome_repo_empresa] = DadosRepositorios(repo, token).cria_df_repos()
    globals()[nome_repo_empresa].head()
    print(f'Dataframe de {repo} criado!')
    
    # Salvando localmente
    print(f'Salvando dados de {repo} como .csv...')
    diretorio_repo = f'{path}/dados_{repo}.csv'
    globals()[nome_repo_empresa].to_csv(diretorio_repo)
    print(f'Dados de {repo} salvo como .csv!')
    
    # Faz upload para github
    print(f'Salvando dados_{repo}.csv no github no repositório {nome_repo} do usuário {username}...')
    novo_repo.add_arquivo(nome_repo = nome_repo, nome_arquivo = f'dados_{repo}.csv', caminho_arquivo= diretorio_repo, nome_pasta = nome_pasta) # nome_pasta é opcional 