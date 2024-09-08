n,m,k=map(int,input().split())
ans=-1

li=[0]*(n+1)
for _ in range(m):
    t=int(input())
    li[t]+=1
    if max(li)==k:
        ans=li.index(k)

print(ans)