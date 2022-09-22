def isValidCo_Ordinates(matrix,x,y):
    if (x < len(matrix)) and (x > -1) and (y < len(matrix)) and (y > -1) and matrix[x][y]: return True
    else: False

def solveMaze(matrix,x,y,curr_path,curr_move):
    # print(matrix)
    # print(curr_path,curr_move)
    # print(curr_move,end="->")
    curr_path.append(curr_move)
    if(not isValidCo_Ordinates(matrix,x,y)):
        curr_path.pop()
        return "inf"
    if(x == len(matrix)-1 and y == len(matrix)-1):
        # print('currr',curr_path[1:])
        # return curr_path
        return curr_move
    else:
        tx = matrix[x][y]
        matrix[x][y] = 0
        down= solveMaze(matrix,x+1,y,curr_path,'D')
        up= solveMaze(matrix,x-1,y,curr_path,'U')
        left= solveMaze(matrix,x,y-1,curr_path,'L')
        right= solveMaze(matrix,x,y+1,curr_path,'R')
        matrix[x][y] = tx
        temp = min(down,up,left,right)
        # print(down,up,left,right,temp)
        # print(curr_move,temp)
        if len(down) < len(temp) and down != "inf": temp = down
        if len(up) < len(temp) and up != "inf": temp = up
        if len(left) < len(temp) and left != "inf": temp = left
        if len(right) < len(temp) and right != "inf": temp = right

        if(temp != ["infD"]) and (temp != ["infU"]) and (temp != ["infL"]) and (temp != ["infR"]):
            curr_path.append(temp)
        return curr_move+temp

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
    ans = solveMaze(matrix,0,0,[],'')
    # print()
    print(ans if ans[len(ans)-3:] != "inf" else "No solution found")
    print(ans)
    # for i in ans:
    #     print(i)