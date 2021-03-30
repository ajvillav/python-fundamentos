class Fabric:
    def __init__(self, marc, cil, model, color, tun=None, door=None):
        self.marc = marc
        self.cil = cil
        self.model = model
        self.color = color
        self.tun = tun
        self.door = door

    def __str__(self):
        return f"""marca  {self.marc}
cilindraje  {self.cil}
model  {self.model}
color  {self.color}
tuning  {self.tun}
door  {self.door}"""

a = Fabric('Camaro','5000', '2021', 'red')
print(a.__str__())

