# Press Shift+F10 to execute it or replace it with your code.

# TESTE DE API

# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste: API Pet Store


# 1 - imports - bibliotecas
import json
import sys

import pytest

import csv

import requests
from requests import HTTPError

import sys
import time

import _json

import pytest

url = 'https://petstore.swagger.io/v2/user'

# 2 -  class - classe


# 3 - definitions - definições = métodos e funções

#### post

def testar_incluir_usuario():
    # configura

    status_code_esperado = 200  # comunicação
    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '1001'  # id do usuário

    # executa

    headers = {'Content-Type': 'application/json'}
    resposta_post = requests.post(url='https://petstore.swagger.io/v2/user',
                                  data=open('json/usuario1.json', 'rb'),
                                  headers=headers
                                  )
    json_body = resposta_post.json()

    print(f'\n \n Resposta: ', resposta_post)  # responde body
    print(f'\n \n Resposta json: ', resposta_post.json())  # responde body

    # valida

    assert resposta_post.status_code == status_code_esperado

    assert json_body['code'] == code_esperado
    assert json_body['type'] == type_esperado
    assert json_body['message'] == mensagem_esperada

    print(
        '\n TESTE 1  - Dados esperados : \n - status code (comunication): {}  \n - code (functional): {}  \n - type:   {} \n - message (id):  {} \n '.format(
            status_code_esperado, code_esperado, type_esperado, mensagem_esperada))

    print(
        '\n TESTE 2 - body  - Dados obtidos API : \n - status code (comunication): {}  \n - code (functional):: {}  \n - type:   {} \n - message (id) :  {} \n '.format(
            resposta_post.status_code, json_body['code'], json_body['type'], json_body['message']))


#### get

def testar_consultar_usuario():
    # Configura

    username = "T_user_name"

    id_esperado = 1001
    username_esperado = 'T_user_name_test'
    firstName_esperado = 'T_first_name'
    lastName_esperado = 'T_last_name'
    email_esperado = 'T_email'
    password_esperado = 'T_password'
    phone_esperado = 'T_phone'
    userStatus_esperado = 1
    status_code_esperado = 200  # comunication
    # status_code_esperado = 404 #comunication

    #### #Executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.get('https://petstore.swagger.io/v2/user/T_user_name_test',
                            headers=headers)
    json_body = resposta.json()

    print(f'\n\n Resposta: ', resposta)  # responde body
    print(f'\n Resposta json: ', resposta.json())  # responde body

    # valida

    assert resposta.status_code == status_code_esperado

    assert json_body['id'] == int(id_esperado)
    assert json_body['username'] == username_esperado
    assert json_body['firstName'] == firstName_esperado
    assert json_body['lastName'] == lastName_esperado
    assert json_body['email'] == email_esperado
    assert json_body['password'] == password_esperado
    assert json_body['phone'] == phone_esperado
    assert json_body['userStatus'] == userStatus_esperado

    status_code_esperado = 200  # comunication
    # status_code_esperado = 404  # comunication #DEFEITO 404 IDENTIFICADO NA API

    print(
        '\n Dados esperados: \n - Status code (comunication): {}  \n - Id esperado (functional): {}  \n - Username esperado: {} \n - First Name esperado: {} \n - Last Name esperado: {}  \n - Email esperado:{}  \n - Password esperado: {} \n - Phone esperado: {} \n - User Status esperado: {}  \n'.format(
            status_code_esperado, id_esperado, username_esperado, firstName_esperado, lastName_esperado, email_esperado,
            password_esperado, phone_esperado, userStatus_esperado))

    print(
        '\n Dados retorno JSON: \n - status code (comunication): {}  \n - id_esperado (functional): {}  \n - Username esperado: {} \n - firstName esperado: {} \n - lastName_esperado: {}  \n - email_esperado:{}  \n - password_esperado: {} \n - phone_esperado: {} \n - userStatus_esperado: {}  \n'.format(
            resposta.status_code, json_body['id'], json_body['username'], json_body['firstName'], json_body['lastName'],
            json_body['email'], json_body['password'], json_body['phone'], json_body['userStatus']))


def testar_consultar_usuario_fail():
    # Configura
    status_code_400 = 400  # comunication - Invalid user supplied
    status_code_404 = 404  # comunication - User not found

    code_esperado_404 = 1  # funcional
    type_esperado_404 = 'error'  # error 404
    mensagem_esperada_404 = 'User not found'  # error 404

    #### #Executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.get('https://petstore.swagger.io/v2/user/T_user_name_test_invalid',
                            headers=headers)
    json_body = resposta.json()

    print(f'\n\n Resposta: ', resposta)  # responde body
    print(f'\n Resposta json: ', resposta.json())  # responde body
    print(f'\n Resposta status code: ', resposta.status_code)  # responde body

    # valida
    assert resposta.status_code == status_code_404

    assert json_body['code'] == code_esperado_404
    assert json_body['type'] == type_esperado_404
    assert json_body['message'] == mensagem_esperada_404
    print('\n Dados esperados: \n - Status code (comunication): {}  \n'.format(status_code_404))

    match resposta:
        case "400":
            print("Error 400 - Invalid user supplied ")
        case "404":
            print(
                "\n Dados retorno JSON: \n - status code (comunication): {} \n - code (functional): {} \n - Type: {} \n - Message: {} \n".format(
                    resposta.status_code, json_body['code'], json_body['type'], json_body['message']))
        # case _:
        # print("Erro Desconhecido")
        # sys.exit(1)

def testar_modificar_usuario():
    # configura

    status_code_esperado = 200  # comunicação

    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = '10012'  # id do usuário

    # executa

    headers = {'Content-Type': 'application/json'}
    resposta_put = requests.put(url='https://petstore.swagger.io/v2/user/T_user_name_test',
                                data=open('json/usuario2.json', 'rb'),
                                headers=headers
                                )
    json_body = resposta_put.json()

    print(f'\n \n Resposta: ', resposta_put)  # responde body
    print(f'\n \n Resposta json: ', resposta_put.json())  # responde body

    # valida

    assert resposta_put.status_code == status_code_esperado

    assert json_body['code'] == code_esperado
    assert json_body['type'] == type_esperado
    assert json_body['message'] == mensagem_esperada

    print(
        '\n TESTE 1  - Dados esperados : \n - status code (comunication): {}  \n - code (functional): {}  \n - type:   {} \n - message (id):  {} \n '.format(
            status_code_esperado, code_esperado, type_esperado, mensagem_esperada))

    print(
        '\n TESTE 2 - body  - Dados obtidos API : \n - status code (comunication): {}  \n - code (functional):: {}  \n - type:   {} \n - message (id) :  {} \n '.format(
            resposta_put.status_code, json_body['code'], json_body['type'], json_body['message']))

    # Consulta usuario modificado

    username = "T_user_name"

    id_esperado = 10012
    username_esperado = 'T_user_name_test_2'
    firstName_esperado = 'T_first_name_2'
    lastName_esperado = 'T_last_name_2'
    email_esperado = 'T_email_2'
    password_esperado = 'T_password_2'
    phone_esperado = 'T_phone_2'
    userStatus_esperado = 2

    # status_code_esperado = 404 #comunication

    headers = {'Content-Type': 'application/json'}
    resposta_get = requests.get('https://petstore.swagger.io/v2/user/T_user_name_test_2', headers=headers)
    json_body = resposta_get.json()

    assert resposta_get.status_code == status_code_esperado

    assert json_body['id'] == int(id_esperado)
    assert json_body['username'] == username_esperado
    assert json_body['firstName'] == firstName_esperado
    assert json_body['lastName'] == lastName_esperado
    assert json_body['email'] == email_esperado
    assert json_body['password'] == password_esperado
    assert json_body['phone'] == phone_esperado
    assert json_body['userStatus'] == userStatus_esperado

    status_code_esperado = 200  # comunication
    # status_code_esperado = 404  # comunication #DEFEITO 404 IDENTIFICADO NA API

def testar_consultar_usuario_e_extrair_senha(username):

    # Configura

    id_esperado = 10012
    username_esperado = 'T_user_name_test_2'
    firstName_esperado = 'T_first_name_2'
    lastName_esperado = 'T_last_name_2'
    email_esperado = 'T_email_2'
    password_esperado = 'T_password_2'
    phone_esperado = 'T_phone_2'
    userStatus_esperado = 2

    status_code_esperado = 200  # comunication
    # status_code_esperado = 404 #comunication

    #### #Executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.get(f'{url}/{username}', headers=headers)
    json_body = resposta.json()

    print(f'\n \n Resposta: ', resposta)  # responde body
    print(f'\n \n Resposta json: ', resposta.json())  # responde body
    print(f'\n \n Resposta status code: ', resposta.status_code)  # responde body

    # valida

    assert resposta.status_code == status_code_esperado

    assert json_body['id'] == int(id_esperado)
    assert json_body['username'] == username_esperado
    assert json_body['firstName'] == firstName_esperado
    assert json_body['lastName'] == lastName_esperado
    assert json_body['email'] == email_esperado
    assert json_body['password'] == password_esperado
    assert json_body['phone'] == phone_esperado
    assert json_body['userStatus'] == userStatus_esperado

    return json_body['password']

def testar_login(username, password):
    # configura

    status_code_esperado = 200  # comunicação / funcional
    #code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = 'logged in user session:'  # mensagem de resposta

    # Executa

    # resposta = requests.get('https://petstore.swagger.io/v2/user/login?username=T_user_name_test_2&password=T_password_2',

    headers = {'Content-Type': 'application/json'}
    resposta=requests.get(f'{url}/login?username={username}&password={password}',
                          headers=headers)
    json_body = resposta.json()

    print(f'\n \n Resposta: ', resposta)  # responde body
    print(f'\n \n Resposta json: ', resposta.json())  # responde body

    # valida

    assert resposta.status_code == status_code_esperado
    assert json_body['code'] == status_code_esperado
    assert json_body['type'] == type_esperado
    assert mensagem_esperada in json_body['message']

    token = json_body['message'].rpartition(':')[2]

    print(
        '\n TESTE 1  - Dados esperados : \n - status code (comunication): {}  \n - code (functional): {}  \n - type:   {} \n - message (id):  {} \n '.format(
            status_code_esperado, status_code_esperado, type_esperado, mensagem_esperada))

    print(
        '\n TESTE 2 - body  - Dados obtidos API : \n - status code (comunication): {}  \n - code (functional):: {}  \n - type:   {} \n - message (id) :  {} \n '.format(
            resposta.status_code, json_body['code'], json_body['type'], json_body['message']))

    return token

#### put

def testar_extrair_senha_realizar_login():

    # configura

    username = "T_user_name_test_2"

    # Executa

    password = testar_consultar_usuario_e_extrair_senha(username)
    token = testar_login(username, password)

    print(f' token login:  {token}')


def testar_deletar_usuario():
    # configura

    status_code_esperado = 200  # comunicação
    code_esperado = 200  # funcional
    type_esperado = 'unknown'  # fixo como desconhecido
    mensagem_esperada = 'T_user_name_test_2'  # id do usuário

    status_code_esperado_erro_400 = 400  # comunication
    status_code_esperado_erro_404 = 404  # comunication

    #### Executa

    headers = {'Content-Type': 'application/json'}
    resposta = requests.delete('https://petstore.swagger.io/v2/user/T_user_name_test_2', headers=headers)
    json_body = resposta.json()

    print(f'\n \n Resposta: ', resposta)  # responde body
    print(f'\n \n Resposta json: ', resposta.json())  # responde body

    # valida 200

    assert resposta.status_code == status_code_esperado
    assert json_body['code'] == code_esperado
    assert json_body['type'] == type_esperado
    assert json_body['message'] == mensagem_esperada


def testar_deletar_usuario_fail():
    # configura

    status_code_esperado_erro_404 = 404  # comunication

    # valida 404

    headers = {'Content-Type': 'application/json'}
    resposta = requests.delete('https://petstore.swagger.io/v2/user/T_user_name_test_invalid', headers=headers)
    incorrect_json = resposta.json()

    # print(f'\n Resposta: ', resposta)  # responde body
    # print(f'\n Resposta json: ', resposta.json())  # responde body
    # print(f'\n Resposta json statu code: ', resposta.status_code) # responde body
    # print(f'\n Resposta json statu code: ', incorrect_json)# responde bodyjson_body

    try:
        a_json = json.loads(incorrect_json)
        print(a_json)
    except json.decoder.JSONDecodeError:
        print("String could not be converted to JSON")

    match resposta:
        case "400":
            print("Error 400 - Invalid username supplied ")
        case "404":
            assert resposta.status_code == status_code_esperado_erro_404
            print(
                "\n User not found : \n Dados retorno JSON: \n - status code (comunication): {}".format(
                    resposta.status_code))


        # case _:
        # print("Erro Desconhecido")
        # sys.exit(1)

    # status_code_esperado = 404  # comunication #DEFEITO 404 IDENTIFICADO NA API

# status_code_esperado = 404  # comunication #DEFEITO 404 IDENTIFICADO NA API

# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users


# função que faz algo --> Fora do meu computador
# API que vamos usar para fazer o teste:
# https://reqres.in/api/users
