import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))
d=dict()
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
cnt=0
for i in d.keys():
    dif=k-i
    if dif in li:
        cnt+=d[dif]
print(int(cnt/2))