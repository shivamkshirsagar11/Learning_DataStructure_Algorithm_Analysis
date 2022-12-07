class ChessPieces:
    def __init__(self,symbol,name,team,currPoint,isDead=False,nextMove=None):
        self.symbol = symbol
        self.name = name
        self.team = team
        self.currPoint = currPoint
    def __str__(self):
        return str(self.symbol)