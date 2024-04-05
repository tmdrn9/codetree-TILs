import math,heapq

n,m=map(int,input().split())

edges=[(-1,-1,-1)]
graph=[[] for _ in range(n+1)]
dist=[math.inf]*(n+1)
for _ in range(m):
    edges.append(tuple(map(int,input().split())))

for i in range(1,m+1):
    x,y,z=edges[i]
    graph[x].append((y,z)) 
    # #만약 무방향그래프면
    # graph[y].append((x,z)) 

a,b=map(int,input().split())
path=[0]*(n+1)
pq=[]
dist[a]=0
heapq.heappush(pq,(0,a))

while pq:
    min_dist,min_index=heapq.heappop(pq)
    if min_dist!=dist[min_index]:
        continue

    for y,z in graph[min_index]:
        new_dist=dist[min_index]+z
        if new_dist<dist[y]:
            dist[y]=new_dist
            heapq.heappush(pq,(new_dist,y))
            path[y]=min_index
print(dist[b])
now=b
v=[b]
while now!=a:
    now=path[now]
    v.append(now)
for i in v[::-1]:
    print(i,end=' ')