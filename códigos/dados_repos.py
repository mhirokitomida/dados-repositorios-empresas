# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:36:03 2023

@author: mauricio.tomida
"""

import requests
import pandas as pd
import numpy as np

class DadosRepositorios:

    def __init__(self, owner, token):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.headers = {'Authorization':'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}

    def lista_repositorios(self):
        repos_list = []
        page_num = 1

        while True: 
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_pag = response.json()
                if len(repos_pag)==0:
                    break
                repos_list.append(repos_pag)
            except:
                repos_list.append(None)
            
            page_num += 1
        
        return repos_list
    
    def nomes_repos(self, repos_list):
        repo_names=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass

        return repo_names
    
    def nomes_linguagens(self, repos_list):
        repo_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages
    
    def repo_sizes(self, repos_list):
        repo_sizes=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_sizes.append(repo['size'])
                except:
                    pass

        return repo_sizes
    
    def repo_watchers_count(self, repos_list):
        repo_watchers_count=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_watchers_count.append(repo['watchers_count'])
                except:
                    pass

        return repo_watchers_count
    
    
    def repo_forks_count(self, repos_list):
        repo_forks_count=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_forks_count.append(repo['forks_count'])
                except:
                    pass

        return repo_forks_count
    
    def repo_visibility(self, repos_list):
        repo_visibility=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_visibility.append(repo['visibility'])
                except:
                    pass

        return repo_visibility
    
    def repo_forks(self, repos_list):
        repo_forks=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_forks.append(repo['forks'])
                except:
                    pass

        return repo_forks
    
    def repo_watchers(self, repos_list):
        repo_watchers=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_watchers.append(repo['watchers'])
                except:
                    pass

        return repo_watchers
    
    def cria_df_repos(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)
        size = self.repo_sizes(repositorios)
        watchers_count = self.repo_watchers_count(repositorios)
        forks_count = self.repo_forks_count(repositorios)
        visibility = self.repo_visibility(repositorios)
        forks = self.repo_forks(repositorios)
        watchers = self.repo_watchers(repositorios)
        
        dados = pd.DataFrame()
        dados['owner'] = np.repeat(self.owner, len(nomes))
        dados['repository_name'] = nomes
        dados['language'] = linguagens
        dados['size'] = size
        dados['watchers_count'] = watchers_count
        dados['forks_count'] = forks_count
        dados['visibility'] = visibility
        dados['forks'] = forks
        dados['watchers'] = watchers

        return dados  