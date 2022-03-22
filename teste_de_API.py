#TESTE DE API


# Press Shift+F10 to execute it or replace it with your code.

# 1 - imports - bibliotecas

import pytest

import csv

import requests
from requests import HTTPError

# 2 -  class - classe


# 3 - definitions - definições = métodos e funções

teste_dados_novos_usuarios = [
    ('1', 'Juca', 'Pirama', 'juca@iterasys.com.br'),       #usuário 1
    ('2', 'Agatha', 'Christie', 'agatha@iterasys.com.br')  #usuário 2
]

teste_dados_usuarios_atuais = [
    ('1', 'george.bluth@reqres.in','George', 'Bluth',  'https://reqres.in/img/faces/1-image.jpg', 'https://reqres.in/#support-heading', 'To keep ReqRes free, contributions towards server costs are appreciated!'), #usuário 1
    ('2', 'janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg', 'https://reqres.in/#support-heading', 'To keep ReqRes free, contributions towards server costs are appreciated!') #usuário 2
]

# CRUD em aplicações

#CREATE          - Post     Incluir / Publicar
#REACH/RESEARCH  - Get      Consultar / Pagar
# UPDATE         - Put      Atualizar
#DELETE          - Delete   Excluir


# main

@pytest.mark.parametrize('id, email, nome, sobrenome, avatar, url, text', teste_dados_usuarios_atuais)

def testar_dados_usuarios(id, email, nome, sobrenome, avatar, url, text): # função que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        email_obtido = jsonResponse['data']['email']
        avatar_obtido = jsonResponse['data']['avatar']
        url_obtido = jsonResponse['support']['url']
        text_obtido = jsonResponse['support']['text']

        #print(f'Id : {id_obtido} - Nome : {nome_obtido} - Sobre nome :  {sobrenome_obtido} - Email : {email_obtido} - Avatar : {avatar_obtido}  - URL : {url_obtido} - Texto : {text_obtido}')

        #print(f' \n Id: {id_obtido} \n  - Nome:  {nome_obtido} \n  - Sobre nome:  {sobrenome_obtido} \n  - Email:   {email_obtido} \n  - Avatar:  {avatar_obtido}  \n  - URL:   {url_obtido} \n - Texto:   {text_obtido} \n ')

        print('\n Id: {} \n  - Nome:  {} \n  - Sobre nome:  {} \n  - Email:   {} \n  - Avatar:  {}  \n  - URL:   {} \n - Texto:   {} \n'.format(id_obtido, nome_obtido, sobrenome_obtido, email_obtido, avatar_obtido, url_obtido, text_obtido))

        assert id_obtido == int(id)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert email_obtido == email
        assert avatar_obtido == avatar
        assert url_obtido == url
        assert text_obtido == text

    except HTTPError as http_fail: # para o ISTQB, descobriu rodando é falha
        print(f'Ocorre um erro de HTTP : {http_fail}')
    except Exception as fail: # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada ocorreu : {fail}')

    # Leitor Arquivo CSV

def ler_dados_csv():
    teste_dados_csv = []
    nome_arquivo = 'usuario.csv'

    try:
        with open(nome_arquivo, newline='') as csvfile:  # abre o arquvio csv er atribui um novo nome 'csvfile'
            dados = csv.reader(csvfile, delimiter=',')  # faz a leitura dos dados e define o delimitador no arquivo csv, ','
            next(dados)  # pula uma linha no arquivo dados para poder ler apenas os dados de usuarios no arquivo CSV
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado : {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')

@pytest.mark.parametrize('id, email, nome, sobrenome, avatar', ler_dados_csv())
def testar_dados_usuarios_csv(id, email, nome, sobrenome, avatar):  # função que testa algo
    try:
        response = requests.get(f'https://reqres.in/api/users/{id}')
        jsonResponse = response.json()
        id_obtido = jsonResponse['data']['id']
        email_obtido = jsonResponse['data']['email']
        nome_obtido = jsonResponse['data']['first_name']
        sobrenome_obtido = jsonResponse['data']['last_name']
        avatar_obtido = jsonResponse['data']['avatar']

        # print(f'Id : {id_obtido} - Nome : {nome_obtido} - Sobre nome :  {sobrenome_obtido} - Email : {email_obtido} - Avatar : {avatar_obtido}  - URL : {url_obtido} - Texto : {text_obtido}')

        # print(f' \n Id: {id_obtido} \n  - Nome:  {nome_obtido} \n  - Sobre nome:  {sobrenome_obtido} \n  - Email:   {email_obtido} \n  - Avatar:  {avatar_obtido}  \n  - URL:   {url_obtido} \n - Texto:   {text_obtido} \n ')

        assert id_obtido == int(id)
        assert email_obtido == email
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome
        assert avatar_obtido == avatar

    except HTTPError as http_fail:  # para o ISTQB, descobriu rodando é falha
        print(f'Ocorre um erro de HTTP : {http_fail}')
    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada ocorreu : {fail}')

    print('\n TESTE 1  - Dados obtidos API \n - Id: {} \n  - Email:   {} \n - Nome:  {} \n  - Sobre nome:  {} \n  - Avatar:  {}  \n'.format(
                id_obtido, email_obtido, nome_obtido, sobrenome_obtido, avatar_obtido))

    print('\n TESTE 2 -  Dados obtidos CSV \n - Id: {} \n  - Email:   {} \n - Nome:  {} \n  - Sobre nome:  {} \n  - Avatar:  {}  \n'.format(
                id, email, nome, sobrenome, avatar))
#função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users