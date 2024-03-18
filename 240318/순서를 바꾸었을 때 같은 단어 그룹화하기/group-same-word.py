n=int(input())
li=[]
for i in range(n):
    li.append(list(input()))
answer=[]
for i in range(n):
    d=dict()
    for j in li[i]:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    answer.append(tuple(sorted(d.items())))
group=set(answer)
cnt=0
for i in group:
    temp=answer.count(i)
    if cnt<=temp:
        cnt=temp
print(cnt)