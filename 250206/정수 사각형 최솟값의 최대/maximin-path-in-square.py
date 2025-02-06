n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dp=[[0]*n for _ in range(n)]
dp2=[[0]*n for _ in range(n)]
temp=-1

dp[0][0]=grid[0][0]
for i in range(1,n):
    dp[0][i]=min(dp[0][i-1],grid[0][i])
    dp[i][0]=min(dp[i-1][0],grid[i][0])

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=min(max(dp[i-1][j],dp[i][j-1]),grid[i][j])

print(dp[n-1][n-1])