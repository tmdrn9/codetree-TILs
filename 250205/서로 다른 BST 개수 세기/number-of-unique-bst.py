n = int(input())

# Write your code here!
dp=[0]*20
dp[1]=1
dp[2]=2
dp[3]=5
#4
for i in range(4,n+1):
    temp=0
    for j in range(n):
        temp+= dp[i]*dp[n-i-1]
    dp[i]=temp
print(dp[n])