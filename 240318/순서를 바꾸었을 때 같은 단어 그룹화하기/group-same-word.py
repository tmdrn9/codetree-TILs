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
    answer.append(sorted(d.items()))

print(answer)