import heapq
pq=[]

_, m=map(int,input().split())
li=list(map(int,input().split()))
for i in li:
    heapq.heappush(pq,-i)
for _ in range(m):
    temp=heapq.heappop(pq)+1
    heapq.heappush(pq,temp)

print(-(heapq.heappop(pq)))