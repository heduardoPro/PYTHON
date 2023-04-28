#Empacotamento e Desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Eduardo',
}

a, b = pessoa.values()
a, b = pessoa.items()
#(a1, a2), (b1, b2) = pessoa.items()
#print(a1, a2, b1, b2)
#print(a, b)

#for chave, valor in pessoa.items():
#    print(chave, valor)

dados_pessoais = {
    'altura': 1.80,
    'idade': 20,
}

pessoa_completa = {**pessoa, **dados_pessoais} #Desempacotamento dos Dicionários
print(pessoa_completa)

#args & Kwargs
#kwargs (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, 3, nome='Maria', outro='Valéria')
print()

mostro_argumentos_nomeados(**pessoa_completa)