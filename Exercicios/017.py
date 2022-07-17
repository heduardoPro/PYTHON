import random
nome1 = input("Digite o nome de um aluno: ")
nome2 = input("Digite o nome de um aluno: ")
nome3 = input("Digite o nome de um aluno: ")
nome4 = input("Digite o nome de um aluno: ")
list = [nome1, nome2, nome3, nome4]

escolhido = random.choice(list)
print("O aluno escolhido foi: {}".format(escolhido))