#calcular a tabuada com laço de repetição

num = int(input("Digite um número para calcular a tabuada: "))
print("Tabuada de", num,":")
for i in range(1, 11):
    print(num, 'X', i, '=', (num * i))