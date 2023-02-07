import re 

def questao1():
    texto = '''Lorem ipsum dolor sit amet 123.456.789-10, consectetur adipisicing elit. Sunt libero itaque quam et ipsa 111222333-44 odio mollitia suscipit dolor dolores iure ea voluptates 12332112332 commodi quis quasi, expedita dolorem fuga, sit ducimus.'''
    regexp = re.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}?\d{11}?')
    cpfs = re.findall(regexp, texto)
    print(cpfs)

def questao2():
    texto = '''3. Escreva um programa para retornar
todos os CEPs de um texto. Formatos possíveis de CEP: 59.084-030, 59084030,
59084-030.'''

    new_texto = re.findall('[0-9]{2}\.?[0-9]{3}\-[0-9]+|\d{8}', texto)
    print(new_texto)

def questao3():
    
    texto = '''3. Escreva @ um ## programa para retornar um texto $ sem caracteres especiaisenúmero.'''
    new_texto = re.findall('\W', texto)
    print(new_texto)

def questao6():
    texto = '6.Escreva 666, um programa para retornar -88 todos os números de um texto.'
    numeros = re.findall('[-+]?\d+', texto)
    print(numeros)

def questao7():
    texto = '7. Escreva um programa para retornar todas as palavras que começam e terminam com vogais' 
    vogais = re.findall('(^a|e|i|o|u)[a-z]+a|e|i|o|u$', texto)
    print(vogais)

#questao2()
#questao3()
#questao6()
questao7()