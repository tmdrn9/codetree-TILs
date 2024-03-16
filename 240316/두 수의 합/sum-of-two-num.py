import itertools
n,k=map(int,input().split())
li=list(map(int,input().split()))
# n=5
# k=6
cnt=0
# li=[3, 3, 3, 3, 3]
for i in range(n):
    temp=li.pop(i)
    if k-temp in li:
        cnt+=1
    li.append(temp)

print(cnt)