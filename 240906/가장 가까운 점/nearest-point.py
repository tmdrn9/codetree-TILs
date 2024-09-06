import heapq

pq=[]
n,m=map(int,input().split())

for _ in range(n):
    x,y=map(int,input().split())
    heapq.heappush(pq,(abs(x)+abs(y),x,y))

for _ in range(m):
    _, tempx,tempy=heapq.heappop(pq)
    heapq.heappush(pq,(abs(tempx)+abs(tempy),tempx+2,tempy+2))

_,close_x,close_y=heapq.heappop(pq)
print(close_x,close_y)