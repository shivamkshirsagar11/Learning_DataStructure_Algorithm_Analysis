from ChessPieces import ChessPieces as Piece
from ChessMoves import LegalMoves as Move
class ChessBoard:
    try:
        def __init__(self,team,teamArr,error=""):
            self.board,self.names = self.makeBoard()
            self.team = team
            self.error = error
            self.whiteDead = []
            self.blackDead = []
        
        def makeBoard(self):#initialize board of chess with original placing and teams
            board = [['-' for i in range(8)] for i in range(8)]
            white = {0:"♖",1:"♘",2:"♗",3:"♕",4:"♔",5:"♗",6:"♘",7:"♖"}
            black = {0:"♜",1:"♞",2:"♝",3:"♛",4:"♚",5:"♝",6:"♞",7:"♜"}
            names = {0:"Rook",1:"Knight",2:"Bishop",3:"Queen",4:"King",5:"Bishop",6:"Knight",7:"Rook"}
            for i in range(8):
                for j in range(8):
                    if( i == 0 ):
                        board[i][j] = Piece(white[j],names[j],False,(i,j))
                    elif( i == 7 ):
                        board[i][j] = Piece(black[j],names[j],True,(i,j))
                    elif( i == 1):
                        board[i][j] = Piece("♙","Pawn",False,(i,j))
                    elif( i == 6):
                        board[i][j] = Piece("♟","Pawn",True,(i,j))
            return board,names
        
        def printBoard(self):
            print("--------White--------")
            for i in range(8):
                for j in range(8):
                    if(j == 0):
                        print(f'{i}',end="  ")
                        print(self.board[i][j],end=" ")
                    else: print(self.board[i][j],end=" ")
                print()
            print("   0 1 2 3 4 5 6 7")
            print("--------Black--------")
        
        def isSafe(self,x,y):
            if(x > -1) and (x < 8) and (y > -1) and (y < 8):
                return True
            return False
        def makeMove(self,curr,next,count):
            if (self.isSafe(next[0],next[1])):
                currentPiece = self.board[curr[0]][curr[1]]
                currentPiece.currPoint = (curr[0],curr[1])
                if(currentPiece.team != self.team):
                    self.error = "Cannot move opposite team piece"
                else:
                    if(Move.calculate_LegalMoves(currentPiece,next,count)):
                        if (self.board[next[0]][next[1]] == '-'):
                            self.board[curr[0]][curr[1]] = '-'
                            self.board[next[0]][next[1]] = currentPiece
                        else:
                            nextPiece = self.board[next[0]][next[1]]
                            if(nextPiece.team == self.team):
                                self.error = "Cannot move to Occupied space"
                            else:
                                nextPiece.isDead = True
                                if(self.teamArr[nextPiece.team] == "White"):
                                    self.whiteDead.append(nextPiece)
                                else:
                                    self.blackDead.append(nextPiece)
                                self.board[next[0]][next[1]] = currentPiece
                        
                        self.board[next[0]][next[1]] = currentPiece
                    else:
                        self.error = f'Illegal Move of {currentPiece.name} from {curr} to {next}'
                # now check for every piece legal moves
                # now check for if any piece of opposite team dies
                    
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    print()
    team = {0:False,1:True}
    teamName = {False:"White",True:"Black"}
    chess = ChessBoard(team[0],teamName)
    count = 0
    blocked = False
    while(True):
        if((not blocked)):
            print(f'{teamName[chess.team]}\'s Turn...')
            chess.printBoard()
            print()
            if(chess.error != ""):
                print(chess.error)
                chess.error = ""
                error = True
        command = input("#:Exit, ?:Dead pieces, !:Make Move: ")
        if( command == '#'): break
        elif( command == '?'):
            print(f'White\'s Dead Pieces: {chess.whiteDead}')
            print(f'Black\'s Dead Pieces: {chess.blackDead}')
            blocked = True
        elif(command == '!'):
            blocked = False
            curr = [int(x) for x in input("enter co-ordinate of piece to move: ").split()]
            next = [int(x) for x in input("enter co-ordinate to move piece: ").split()]
            chess.makeMove(curr,next,count)
            if( chess.error == ""):
                count = count + 1
                chess.team = not chess.team
        else:
            print("Choose Apropriate Command")
