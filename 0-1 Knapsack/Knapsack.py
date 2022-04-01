import Object as o

def Knapsack(obj,n,c):
    Memo = [[None for x in range(c + 1)] for x in range(n + 1)]
    for i in range(n+1): 
        for j in range(c+1): 
            if i == 0 or j == 0:
                Memo[i][j] = 0
            elif obj[i-1].weight <= j:
                Memo[i][j] = max(obj[i-1].profit+Memo[i-1][j-obj[i-1].weight],Memo[i-1][j])
            else: 
                Memo[i][j] = Memo[i-1][j]
    # print(Memo)
    return "Maximum profit in Given Product is: "+str(Memo[n][c])

def main():
    objArray = o.MakeObjects()
    n = len(objArray)
    W = 50
    print(Knapsack(objArray,n,W))
    return
main()