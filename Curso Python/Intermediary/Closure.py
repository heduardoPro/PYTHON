#Closure e Funções que retornam outras Funções
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar 

s1 = criar_saudacao('bom dia')
s2 = criar_saudacao('boa noite')

print(s1('Henrique'))
print(s2('Henrique'))