import os

carrinho = []

while True:
    print('Selecione uma Opção: \n[i]nserir [a]pagar [l]ista | ENTER para Sair.')
    option = input()

    if option == "i":
        os.system('cls')
        item = input('Digite o que você deseja adicionar na lista: ')
        carrinho.append(item)
    
    elif option == 'a':
        os.system('cls')
        for x, nome in enumerate(carrinho):
            print(x, nome)
        indice_str = int(input('Digite o índice(número inteiro) onde se encontra seu item: '))

        try:
            indice = int(indice_str)
            del carrinho[indice]
        except IndexError:
            print('O Índece não existe na lista')
        except ValueError:
            print('Por favor digite um número inteiro.')
        except:
            print('Não foi possível apagar o índece.')
            
    elif option == 'l':
        os.system('cls')

        if len(carrinho) == 0:
            print('A lista está vázia, adicione algo a ela.')

        for x, nome in enumerate(carrinho):
            print(x, nome)       
    else:
        break