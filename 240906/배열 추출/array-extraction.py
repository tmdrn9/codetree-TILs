import heapq
n=int(input())
pq=[]

for _ in range(n):
    i=int(input())
    if i !=0:
        heapq.heappush(pq, -i)
    else:
        if len(pq)==0:
            print(0)
        else:
            print(-(heapq.heappop(pq)))