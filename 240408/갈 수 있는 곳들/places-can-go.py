n,k=map(int,input().split())
#동남서북
DR,DC=[0,1,0,-1],[1,0,-1,0]
graph=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

q=[]
for _ in range(k):
    r,c=map(int,input().split())
    q.append((r-1,c-1))
    visited[r-1][c-1]=1

def in_range(r,c):
    return 0<=r<n and 0<=c<n 

def bfs():
    while q:
        rr,cc=q.pop(0)
        for dr,dc in zip(DR,DC):
            nr,nc=rr+dr,cc+dc
            if in_range(nr,nc) and graph[nr][nc]==0 and visited[nr][nc]==0:
                q.append((nr,nc))
                visited[nr][nc]=1


bfs()
print(sum(sum(visited,[])))