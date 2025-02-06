n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
dx,dy=[-1,0,1,0],[0,1,0,-1] #상좌하우
dp=[[1]*n for _ in range(n)]

cells=[]
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))
cells.sort()

result=0
for _,i,j in cells:
    for dxx,dyy in zip(dx,dy):
        ni,nj=i+dxx,j+dyy
        if 0<=ni<n and 0<=nj<n and grid[i][j]<grid[ni][nj]:
            dp[ni][nj]=max(dp[ni][nj],dp[i][j]+1)


# print(max(max(dp)))
ans=0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)