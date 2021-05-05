class Order:
    def __init__(self, coun, datin):
        self.count = coun
        self.date = datin

    def GetCoun(self):
        return self.count

    def GetDatin(self):
        return self.date