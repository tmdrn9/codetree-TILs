import math
n,m=map(int,input().split())
edges=[[-1,-1,-1]]
for _ in range(m):
    edges.append(list(map(int,input().split())))
dist=[math.inf]*(n+1)
visited=[False]*(n+1)
dist[1]=0
graph=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,m+1):
    x,y,z=edges[i]
    graph[x][y]=z

for i in range(1,n+1):
    min_index=-1
    for j in range(1,n+1):
        if visited[j]==True:
            continue
        if min_index==-1 or dist[min_index]>dist[j]:
            min_index=j
    visited[min_index]=True        
    for j in range(1,n+1):
        if graph[min_index][j]==0:
            continue
        dist[j]=min(dist[j],dist[min_index]+graph[min_index][j])

for i in range(2,n+1):
    if dist[i]==math.inf:
        print(-1)
    else:
        print(dist[i])