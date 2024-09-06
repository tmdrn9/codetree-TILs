import heapq

n=int(input())
pq=[]

for _ in range(n):
    a=list(input().split())
    if len(a)==2:
        i=int(a[1])
        heapq.heappush(pq,(-i,i))
    else:
        if a[0]=='pop':
            _,maxn=heapq.heappop(pq)
            print(maxn)
        elif a[0]=='size':
            print(len(pq))
        elif a[0]=='empty':
            temp= 1 if len(pq)==0 else 0
            print(temp)
        else:
            print(pq[0][1])