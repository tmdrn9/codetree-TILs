from collections import deque

dxs,dys=[0,1,0,-1],[1,0,-1,0]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
q=deque([])

n,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
start=[tuple(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
visited=[[0]*n for _ in range(n)]
result=0
for r,c in start:
    q.append((r,c))
    visited[r][c]=1
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            newx,newy=x+dx,y+dy
            if in_range(newx,newy) and visited[newx][newy]==0 and grid[newx][newy]==0:
                visited[newx][newy]=1
                q.append((newx,newy))
for v in visited:
    for i in v:
        if i==1:
            result+=1

print(result)