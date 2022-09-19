def isValidCo_Ordinates(matrix,x,y):
    if (x < len(matrix)) and (x > -1) and (y < len(matrix)) and (y > -1) and matrix[x][y]: return True
    else: False

def solveMaze(matrix,x,y,curr_path,curr_move):
    # print(matrix)
    # print(curr_path)
    curr_path.append(curr_move)
    if(not isValidCo_Ordinates(matrix,x,y)):
        curr_path.pop()
        return ["inf"+curr_move]
    if(x == len(matrix)-1 and y == len(matrix)-1):
        curr_path.append(curr_move)
        return curr_path
    else:
        for i in range(x,len(matrix)):
            for j in range(y,len(matrix)):
                tx = matrix[i][j]
                matrix[i][j] = 0
                down = solveMaze(matrix,i+1,j,curr_path,'D')
                up = solveMaze(matrix,i-1,j,curr_path,'U')
                left = solveMaze(matrix,i,j-1,curr_path,'L')
                right = solveMaze(matrix,i,j+1,curr_path,'R')
                matrix[i][j] = tx
                temp = min(down,up,left,right)
                # print(down,up,left,right)
                if(temp != ["infD"]) and (temp != ["infU"]) and (temp != ["infL"]) and (temp != ["infR"]):
                    curr_path.extend(temp)
                return curr_path

if __name__ == '__main__':
    matrix = []
    print("enter # to stop")
    while(True):
        x = input("row wise element: ")
        if(x == '#'): break
        x = x.split()
        temp = []
        for i in x:
            temp.append(int(i))
        matrix.append(temp)
    print(solveMaze(matrix,0,0,[],'D'))