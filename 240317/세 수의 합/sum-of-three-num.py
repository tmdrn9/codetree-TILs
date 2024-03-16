import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))

cnt=0
d=dict()
for i,a in enumerate(li):
    if a in d:
        d[a]+=1
    else:
        d[a]=1

for i in range(n):
    d[li[i]]-=1
    for j in range(i):
        diff=k-li[i]-li[j]
        if diff in d:
            cnt+=d[diff]

print(cnt)