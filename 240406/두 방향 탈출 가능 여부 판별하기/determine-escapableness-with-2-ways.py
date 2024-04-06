n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
visited[0][0]=True

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
def dfs(x,y):
    dx,dy=[0,1],[1,0]
    for dxx,dyy in zip(dx,dy):
        new_x,new_y=x+dxx,y+dyy
        if in_range(new_x,new_y) and not visited[new_x][new_y] and grid[new_x][new_y]:
            visited[new_x][new_y]=True
            dfs(new_x,new_y)

dfs(0,0)
print(1 if visited[n-1][m-1] else 0)