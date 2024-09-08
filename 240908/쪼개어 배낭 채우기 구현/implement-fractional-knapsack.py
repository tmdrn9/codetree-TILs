import heapq
n,m=map(int,input().split())
jewelry=[]
ans=0
for _ in range(n):
    w,v=map(int,input().split())
    vv=v/w
    heapq.heappush(jewelry,(-vv,w,v))

for _ in range(n):
    vv,w,v=heapq.heappop(jewelry)
    if w<=m:
        ans+=v
        m-=w
    else:
        ans+=-vv*m
        m=0
    if m==0:
        break
print(f'{round(ans,3):.3f}')