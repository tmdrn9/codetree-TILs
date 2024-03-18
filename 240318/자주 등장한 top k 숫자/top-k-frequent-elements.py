n,k=map(int,input().split())
li=map(int,input().split())
d=dict()
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
dd=sorted(d.items(), reverse=True)
dd=sorted(dd,key=lambda item:item[1],reverse=True)
answer=[]
for a in range(k):
    answer.append(str(dd[a][0]))
print(' '.join(answer))