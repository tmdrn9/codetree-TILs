import math,heapq

n,m=map(int,input().split())
edges=[(-1,-1,-1)]
graph=[[] for _ in range(n+1)]
dist=[math.inf]*(n+1)
for _ in range(m):
    edges.append(tuple(map(int,input().split())))

for i in range(1,m+1):
    x,y,z=edges[i]
    graph[y].append((x,z))
pq=[]
dist[n]=0
heapq.heappush(pq,(0,n))
while pq:
    min_dist,min_index=heapq.heappop(pq)
    if dist[min_index]!=min_dist:
        continue
    
    for y,z in graph[min_index]:
        new_dist=dist[min_index]+z
        if dist[y]>new_dist:
            dist[y]=new_dist
            heapq.heappush(pq,(new_dist,y))

max_dist=-1
for i in dist[1:]:
    max_dist=max(max_dist,i)
print(max_dist)