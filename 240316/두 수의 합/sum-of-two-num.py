import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))

cnt=0
for i,a in enumerate(li):
    temp=li.pop(i)
    if k-a in li:
        cnt+=1
    li.append(temp)

print(int(cnt/2))