n,k=map(int,input().split())
li=list(map(int,input().split()))
d=dict()
answer=[]
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
d=sorted(d.items(),reverse=True)
d=sorted(d, key=lambda x: x[1],reverse=True)
for j in d[:k]:
    answer.append(str(j[0]))
print(' '.join(answer))