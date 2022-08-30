import math
def isPossible(game):
    for i in range(len(game)):
        for j in range(len(game[0])):
            if i == 0 and j == 0 and j<len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j+1] == 'O') or (game[i][j] == 'O' and game[i+1][j] == 'O'):
                    return True
            elif i == 0 and j==len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j-1] == 'O') or (game[i][j] == 'O' and game[i+1][j] == 'O'):
                    return True
            elif i == 0 and j<len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j-1] == 'O') or (game[i][j] == 'O' and game[i][j+1] == 'O')or (game[i][j] == 'O' and game[i+1][j] == 'O'):
                    return True
            
            elif i == len(game)-1 and j<len(game[0])-1 and j == i:
                if (game[i][j] == 'O' and game[i][j+1] == 'O') or (game[i][j] == 'O' and game[i-1][j] == 'O'):
                    return True
            elif i == len(game)-1 and j==len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j-1] == 'O') or (game[i][j] == 'O' and game[i-1][j] == 'O'):
                    return True
            elif i == len(game)-1 and j<len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j-1] == 'O') or (game[i][j] == 'O' and game[i][j+1] == 'O')or (game[i][j] == 'O' and game[i-1][j] == 'O'):
                    return True
            
            elif i < len(game)-1 and j < len(game[0])-1:
                if (game[i][j] == 'O' and game[i][j-1] == 'O') or (game[i][j] == 'O' and game[i][j+1] == 'O')or (game[i][j] == 'O' and game[i-1][j] == 'O') or (game[i][j] == 'O' and game[i+1][j] == 'O'):
                    return True
    return False
                
def maxGames(game):
    max = -math.inf
    for i in range(len(game)):
        for j in range(len(game[0])):
            if game[i][j]== 'X':continue
            store = game[i][j]
            if(isPossible(game)):
                game[i][j] = 'X'
                temp = 1 + maxGames(game)
                if temp > max:
                    max = temp
                game[i][j] = store
            else:
                max = 0
                break
    return max
                
if __name__ == "__main__":
    # grid = [['O','O','X'],
    #         ['X','O','O'],
    #         ['O','O','X']]
    grid = [['O','O'],
            ['X','X'],
            ['X','X']]
    # print(isPossible(grid))
    print(maxGames(grid))
    