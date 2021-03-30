class Auto:
    tuneado = False
    def __init__(self, puertas=None, color=None):
        self.pertas = puertas
        self.color = color
        if puertas is not None and color is not None:
            print(f'Se ha creado un auto con {puertas} puertas y color {color}.')
        else:
            print('Se ha creado un auto.')
    def tunear(self):
        self.tuneado = True
    def confirmar(self):
        if self.tuneado == True:
            print('Se ha tuneado el auto.')
        else:
            print('No se ha tuneado el auto.')
    def __del__(self):
        print('Se eliminó el auto', self.color)

a = Auto(5,'negro')
a.confirmar()
a.tunear()
a.confirmar()

b = Auto(3,'amarillo')