from ChessPieces import ChessPieces as Piece
class ChessBoard:
    try:
        def __init__(self,team,error=""):
            self.board,self.names = self.makeBoard()
            self.team = team
            self.error = error
        
        def makeBoard(self):#initialize board of chess with original placing and teams
            board = [['-' for i in range(8)] for i in range(8)]
            white = {0:"♖",1:"♘",2:"♗",3:"♕",4:"♔",5:"♗",6:"♘",7:"♖"}
            black = {0:"♜",1:"♞",2:"♝",3:"♛",4:"♚",5:"♝",6:"♞",7:"♜"}
            names = {0:"Rook",1:"Knight",2:"Bishop",3:"Queen",4:"King",5:"Bishop",6:"Knight",7:"Rook"}
            for i in range(8):
                for j in range(8):
                    if( i == 0 ):
                        board[i][j] = Piece(white[j],names[j],0,(i,j))
                    elif( i == 7 ):
                        board[i][j] = Piece(black[j],names[j],1,(i,j))
                    elif( i == 1):
                        board[i][j] = Piece("♙","Pawn",0,(i,j))
                    elif( i == 6):
                        board[i][j] = Piece("♟","Pawn",1,(i,j))
            return board,names
        
        def printBoard(self):
            # print(f'   {0}:{self.names[0]}, {1}:{self.names[1]}, {2}:{self.names[2]}, {3}:{self.names[3]}, {4}:{self.names[4]}, {5}:{self.names[5]}, {6}:{self.names[6]}, {7}:{self.names[7]}')
            print("   0 1 2 3 4 5 6 7")
            for i in range(8):
                for j in range(8):
                    if(j == 0):
                        print(f'{i}',end="  ")
                        print(self.board[i][j],end=" ")
                    else: print(self.board[i][j],end=" ")
                print()
        
        def isSafe(self,x,y):
            if(x > -1) and (x < 8) and (y > -1) and (y < 8):
                return True
            return False
        def makeMove(self,curr,next):
            if (self.isSafe(next[0],next[1])):
                currentPiece = self.board[curr[0]][curr[1]]
                currentPiece.currPoint = (curr[0],curr[1])
                currentPiece.nextMove = (next[0],next[1])
                if(currentPiece.team != self.team):
                    self.error = "Cannot move opposite team piece"
                # now check for every piece legal moves
                # now check for if any piece of opposite team dies
                else:pass
                    
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    print()
    x = int(input("Which team do you want to choose: 0:white, 1:black "))
    if( x not in [0,1]): raise Exception("Choice must be from 0:white, 1:black")
    chess = ChessBoard(x)
    print("# for exit")
    print()
    chess.printBoard()
    print()
    while(True):
        if(chess.error is not ""):
            print(chess.error)
            chess.error = ""
        curr = [int(x) for x in input("enter co-ordinate of piece to move: ").split()]
        if( curr == '#'): break
        next = [int(x) for x in input("enter co-ordinate to move piece:").split()]
        chess.makeMove(curr,next)
