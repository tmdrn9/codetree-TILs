n = int(input())

# Write your code here!
dp=[0]*20
dp[1]=1
dp[2]=2
dp[3]=5
#4
for i in range(4,n+1):
    dp[i]= dp[i-1]*2+(i-2)*(sum(dp[:i-1]))

print(dp[n])