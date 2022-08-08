frase  = "Curso em Vídeo Python"
### Análise
len(frase) # len serve para informar quantos caracteres tem a frase, contando com os espaços.
frase.count('o') # count serve para contar quantas letras especificadas tem na frase.
frase.find("especificação") # find serve para indicar onde esta posicionado a especifição.

### Transformação
frase.replace("Python","QUalquer coisa") # O replace serve pra trocar uma plavra determinada por outra.
frase.upper() # coloca todas as letras em maiusculas.
frase.lower() # coloca todas as letras em minusculas.
frase.capitalize() # deixa a primeira letra da frase maiuscula e as outras minusculas.
frase.title() # coloca a primeira letra de cada palavra em maiuscula.
frase.strip() # remove os espaçços das bordas.

### Junção
'-'.join(frase)