from collections import deque

dxs,dys=[0,1,0,-1],[1,0,-1,0]
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
visited=[list(map(lambda x: 1 if x==0 else 0,grid[i])) for i in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

q=deque([])
q.append((0,0))
visited[0][0]=1
while q:
    x,y=q.popleft()
    for dx,dy in zip(dxs,dys):
        newx,newy=x+dx,y+dy
        if in_range(newx,newy) and visited[newx][newy]==0:
            visited[newx][newy]=1
            q.append((newx,newy))

answer= 1 if visited[-1][-1] else 0
print(answer)