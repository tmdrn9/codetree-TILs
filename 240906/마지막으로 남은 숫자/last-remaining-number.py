import heapq

pq=[]
n=int(input())
li=list(map(int,input().split()))

for i in li:
    heapq.heappush(pq,-i)

while True:
    if len(pq)<2:
        break
    a,b=-heapq.heappop(pq),-heapq.heappop(pq)
    cha=abs(a-b)
    if cha!=0:
        heapq.heappush(pq,-cha)

if len(pq)==1:
    print(-pq[0])
else:
    print(-1)