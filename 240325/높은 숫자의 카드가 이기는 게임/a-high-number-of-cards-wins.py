import heapq

n=int(input())
total={i for i in range(1,2*n)}
answer=0

b=[int(input()) for _ in range(n)]
a=list(total-set(b))

heapq.heapify(b)
heapq.heapify(a)

temp=heapq.heappop(b)
while len(a)>0:
    aa=heapq.heappop(a)
    if aa>temp:
        answer+=1
        temp=heapq.heappop(b)

print(answer)