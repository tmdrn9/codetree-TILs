from sortedcontainers import SortedDict
n=int(input())
d=SortedDict()
for i in range(n):
    c=input()
    if c in d:
        d[c]+=1
    else:
        d[c]=1

for i in d.items():
    print(i[0],i[1])