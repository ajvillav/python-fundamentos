class fabric:
    def __init__(self, marca=None, cil=None, col=None):
        self.marca = marca
        self.cil = cil
        self.col = col
        print(f'Se ha creado un {marca} de {self.cil} HP y color {col}')

    def __str__(self):
        return f'{self.marca},{self.cil}'

class list:
    def __init__(self,lista=[]):
        self.lista = lista
    def ad(self, x):
        self.lista.append(x)
    def run(self):
        for i in self.lista:
            print(i)
    def dele(self):
        print('Se ha eliminado el ultimo auto de la lista.')
        self.lista.pop()


a = fabric('Camaro', 5600, 'red')
b = fabric('Mustang', 5000, 'white')
c = fabric('Mercedes', 2600, 'white')

l = list([a,b,c])
l.ad(fabric('BMW', 4800, 'black'))
l.run()

l.dele()
l.run()


