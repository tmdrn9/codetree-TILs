import heapq

n=int(input())
pq=list(map(int,input().split()))
answer=0
# for i in li:
#     heapq.heappush(pq,i)
heapq.heapify(pq)
while len(pq)>1:
    a,b=heapq.heappop(pq),heapq.heappop(pq)
    temp=a+b
    answer+=temp
    heapq.heappush(pq,temp)
print(answer)