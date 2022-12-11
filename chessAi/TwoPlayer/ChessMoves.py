class LegalMoves:
    def __init__(self):
       pass

    @classmethod
    def calculate_LegalMoves(self,piece,nextMove,count):
        self.piece = piece
        self.nextMove = nextMove
        self.count = count
        name = self.piece.name
        if name == "Rook": return self.legalMovesForRook()
        elif name == "Bishop": return self.legalMovesForBishop()
        elif name == "King": return self.legalMovesForKing()
        elif name == "Queen": return self.legalMovesForQueen()
        elif name == "Knight": return self.legalMovesForKnight()
        elif name == "Pawn": return self.legalMovesForPawn()
        else: raise KeyError(f'No Moves Match for {name} Piece')

    @classmethod
    def legalMovesForRook(self):
        if( ((self.piece.currPoint[1] != self.nextMove[1] ) and (self.piece.currPoint[0] == self.nextMove[0] )) or ((self.piece.currPoint[0] != self.nextMove[0] ) and (self.piece.currPoint[1] == self.nextMove[1] )) ):
            return True
        return False

    @classmethod
    def legalMovesForBishop(self):
        deltaX = abs(self.piece.currPoint[1] - self.nextMove[1])
        deltaY = abs(self.piece.currPoint[0] - self.nextMove[0])
        if deltaX == deltaY : return True
        return False

    @classmethod
    def legalMovesForKnight(self):
        deltaX = abs(self.piece.currPoint[1] - self.nextMove[1])
        deltaY = abs(self.piece.currPoint[0] - self.nextMove[0])
        if (deltaX == 1 and deltaY == 2) or (deltaX == 2 and deltaY == 1): return True
        return False

    @classmethod
    def legalMovesForQueen(self):
        return (self.legalMovesForRook()) or (self.legalMovesForBishop())

    @classmethod
    def legalMovesForKing(self):
        deltaX = abs(self.piece.currPoint[1] - self.nextMove[1])
        deltaY = abs(self.piece.currPoint[0] - self.nextMove[0])
        if( ((deltaX == 1) and ((deltaY == 0) or (deltaY == 1)) ) or ((deltaX == 0) and (deltaY == 1)) ): return True
        return False

    @classmethod
    def legalMovesForPawn(self):
        deltaY = abs(self.piece.currPoint[0] - self.nextMove[0])
        if self.count == 0 and ((deltaY == 1) or (deltaY == 2)): return True
        elif self.count != 0 and deltaY == 1: return True
        return False