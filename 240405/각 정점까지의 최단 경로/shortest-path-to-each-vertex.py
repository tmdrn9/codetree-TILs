import math,heapq

n,m=map(int,input().split())
k=int(input())

graph=[[] for _ in range(n+1)]
dist=[math.inf]*(n+1)
pq=[]

edges=[(-1,-1,-1)]
for _ in range(m):
    edges.append(tuple(map(int,input().split())))

for i in range(1,m+1):
    x,y,z=edges[i]
    graph[x].append((y,z))

dist[k]=0
heapq.heappush(pq,(0,k))

while pq:
    min_dist,min_index=heapq.heappop(pq)

    if min_dist!=dist[min_index]:
        continue

    for y,z in graph[min_index]:
        new_dist=dist[min_index]+z
        if dist[y]>new_dist:
            dist[y]=new_dist
            heapq.heappush(pq,(new_dist,y))

for i in range(1,n+1):
    if dist[i]==math.inf:
        print(-1)
    else:
        print(dist[i])