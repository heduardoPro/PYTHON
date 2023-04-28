# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
lista = [1, 2, 1, 2, 1, 1, 0]
s1 = set(lista)
lista2 = list(s1)
print(lista2)

# Métodos úteis:
# add, update, clear, discard

s2 = set()
s2.add('Pedro')
s2.add(1)

print(s2)

s2.update(('Olá Mundo', 1, 2, 3))
print(s2)

s2.discard('Pedro')
print(s2)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s3 = {1, 2, 3}
s4 = {4, 2, 6}

s5 = s3 | s4
s5 = s3 & s4
s5 = s3 ^ s4
s5 = s3 - s4 #Itens presentes apenas no set da esquerda
print(s5)


#EXEMPLOS DE USO DO SETS
