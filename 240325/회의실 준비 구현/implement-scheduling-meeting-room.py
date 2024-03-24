import heapq
n=int(input())
pq=[]
for _ in range(n):
    s,e=map(int,input().split())
    heapq.heappush(pq,(e,s))
start=pq[0][1]
cnt=0
for k in range(n):
    i=heapq.heappop(pq)
    if start<=i[1]:
        cnt+=1
        start=i[0]
    else:
        continue
print(cnt)