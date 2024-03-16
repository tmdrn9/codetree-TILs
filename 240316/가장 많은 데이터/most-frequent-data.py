n=int(input())
d=dict()
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
ds=sorted(d,key=lambda x:x[1])
print(d[ds[0]])