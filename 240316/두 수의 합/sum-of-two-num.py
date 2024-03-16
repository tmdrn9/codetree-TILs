import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))

d=dict()
cnt=0
for i in li:
    dif=k-i
    if dif in d:
        cnt+=d[dif]

    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(cnt)