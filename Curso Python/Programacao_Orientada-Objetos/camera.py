class Camera:

    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        print(f'A {self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando == False:
            print(f'A {self.nome} está filmando e NÂO pode fotografar ')
        

    def parar_filmar(self):
        if not self.filmando:
            print(f'A {self.nome} NÃO ESTA FILMANDO')

        else:
            print('Parando de filmar...')
            self.filmando = False
        

can1 = Camera('Sony')
can1.filmar()
can1.fotografar()
can1.parar_filmar()
can1.fotografar()