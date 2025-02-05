n = int(input())

# Write your code here!
dp=[0]*20
dp[0]=1
dp[1]=1

#4
for i in range(4,n+1):
    temp=0
    for j in range(i):
        temp+= dp[j]*dp[n-j-1]
    dp[i]=temp
print(dp[n])