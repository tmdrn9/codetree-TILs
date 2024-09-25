from collections import deque
import heapq 

dxs,dys=[0,1,0,-1],[1,0,-1,0]
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


n,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
r,c=map(lambda x:int(x)-1,input().split())

for i in range(k):
    q=deque([])
    pq=[]
    max_n=grid[r][c]
    q.append([r,c])
    visited=[[0]*n for _ in range(n)]

    while q:
        nr,nc=q.popleft()
        for dx,dy in zip(dxs,dys):
            newr,newc=nr+dx,nc+dy
            if in_range(newr,newc) and visited[newr][newc]==0 and grid[newr][newc]<max_n:
                visited[newr][newc]=1
                q.append([newr,newc])
                heapq.heappush(pq,(-grid[newr][newc],newr,newc))
    if pq==[]:
        break
    _,r,c=heapq.heappop(pq)
print(r+1,c+1)