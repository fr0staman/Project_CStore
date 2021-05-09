class Tovar:
    def __init__(self, tova, pric, numb):
        self.tovar = tova
        self.price: int = pric
        self.number: int = numb

    def GetName(self):
        return self.tovar

    def GetPrice(self):
        return self.price

    def GetNumber(self):
        return self.number
