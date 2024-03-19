from sortedcontainers import SortedDict

n=int(input())
d=SortedDict()
for i in range(n):
    c=input()
    if c in d:
        d[c]+=1
    else:
        d[c]=1
total=sum(d.values())
# print(total)
for i in d:
    print(f'{i} {((d[i]/total)*100):.4f}')