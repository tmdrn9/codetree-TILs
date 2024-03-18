n=int(input())
li=[]
d=dict()
for i in range(n):
    li.append(list(map(int,input().split())))
for j in li:
    if (j[0] in d and d[j[0]]<j[1]):
        continue
    else:
        d[j[0]]=j[1]
print(sum(d.values()))