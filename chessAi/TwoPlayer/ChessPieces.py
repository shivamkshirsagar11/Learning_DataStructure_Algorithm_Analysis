class ChessPieces:
    def __init__(self,symbol,name,team,currPoint,isDead=False):
        self.symbol = symbol
        self.name = name
        self.team = team
        self.currPoint = currPoint
        self.isDead = isDead
    def __str__(self):
        return str(self.symbol)