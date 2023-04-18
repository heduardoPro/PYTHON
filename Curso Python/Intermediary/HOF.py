
'''
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
'''

def saudacao(msg):
    return msg

def executa(funcao):
    return funcao()

saudacao_2 = saudacao('Olá Mundo')
var = executa(saudacao_2)
print(var)