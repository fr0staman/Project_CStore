class Order:
    def __init__(self, coun, datin):
        self.count:int = coun
        self.date = datin

    def GetCoun(self):
        return self.count

    def GetDatin(self):
        return self.date