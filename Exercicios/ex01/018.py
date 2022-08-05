import random
nome1 = input("Digite o nome de um aluno: ")
nome2 = input("Digite o nome de um aluno: ")
nome3 = input("Digite o nome de um aluno: ")
nome4 = input("Digite o nome de um aluno: ")
list = [nome1, nome2, nome3, nome4]
random.shuffle(list)
print("A ordem da apresentação é: ")
print(list)