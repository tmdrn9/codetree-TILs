n = int(input())

# Write your code here!
dp=[0]*1001
dp[2]=1
dp[3]=1
dp[4]=1

for i in range(5,n+1):
    dp[i]=dp[i-2]+dp[i-3]
    
print(dp[n]%10007)