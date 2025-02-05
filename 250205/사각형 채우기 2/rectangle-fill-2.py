n = int(input())

# Write your code here!
dp=[0]*1001
dp[0]=dp[1]=1
dp[2]=3
#3 5/4 
for i in range(3,n):
    dp[i]= dp[i-1]*dp[i-2]-1

print(dp[n]/10007)
