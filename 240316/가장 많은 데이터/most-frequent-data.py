n=int(input())
d=dict()
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
ds=sorted(d.items(), key=lambda item: item[1],reverse=True)
print(ds[0][1])