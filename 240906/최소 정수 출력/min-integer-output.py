import heapq
pq=[]
n=int(input())

for _ in range(n):
    m=int(input())
    if m==0:
        if len(pq)==0:
            print(0)
        else: 
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq,m)