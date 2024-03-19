from sortedcontainers import SortedDict

n=int(input())
li=list(map(int,input().split()))
d=SortedDict()

for i,c in enumerate(li):
    if c in d:
        continue
    else:
        d[c]=i+1
for i in d.items():
    print(i[0],i[1])