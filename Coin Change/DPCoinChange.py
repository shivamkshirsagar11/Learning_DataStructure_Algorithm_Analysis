import math

def CoinChange(coin,n,amount):
    Memo = [[None for x in range(amount + 1)] for x in range(n + 1)]
    for i in range(n+1): 
        for j in range(amount+1): 
            if i == 0 and j == 0: 
                Memo[i][j] = 0
            elif i == 0: 
                Memo[i][j] = math.inf
            elif j == 0: 
                 Memo[i][j] = 0
            elif coin[i-1] <= j:
                Memo[i][j] = min(1 + Memo[i][j-coin[i-1]],Memo[i-1][j])
            else: 
                Memo[i][j] = Memo[i-1][j]
    # print(Memo)
    if(Memo[n][amount] == 0 or Memo[n][amount] == math.inf): return "Cannot form Given Amount with Given coins of denomination"
    return "Amount with Minimum coins: "+str(Memo[n][amount])

def main():
    # coinArray = [1,2,5,10,20,50,100,200,500,2000]
    coinArray = [1,3,4]
    n = len(coinArray)
    Amount = 7
    print(CoinChange(coinArray,n,Amount))
    return
main()