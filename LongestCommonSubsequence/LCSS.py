
def LCS(x,y):
    m = len(x)
    n = len(y)
    row=n;col=m
    Memo = [[None for i in range(m+1)]for j in range(n+1)]
    for i in range(0,n+1): 
        for j in range(0,m+1):
            if i==0 or j==0:
                Memo[i][j] = 0
            elif x[j-1] == y[i-1]: 
                Memo[i][j] = 1 + Memo[i-1][j-1]
            else: 
                Memo[i][j] = max(Memo[i-1][j],Memo[i][j-1])
    if(Memo[n][m] == 0): return "no common string found!!!"
    tot=0
    for i in range(0,n+1):
        for j in range(0,m+1):
            if(Memo[i][j] != 0):tot +=1
    
    return "Common Substring Length: "+str(Memo[n][m])+" Subproblems: "+str(tot-1)

def main():
    x = input("X: ")
    y = input("Y: ")
    print(LCS(x,y))
main()